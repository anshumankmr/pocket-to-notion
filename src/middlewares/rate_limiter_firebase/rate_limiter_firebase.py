"""
Rate Limiter Logic
"""
from .token_bucket import TokenBucket
from google.cloud import firestore
from .constants import constants
import time


class NotSupportedAlgorithm(Exception):
    "Raised When an Algorithm is Passed as An Argument"
    pass


class UnableToDecide(Exception):
    """
    Raised When an Exception Occurs While Trying
    To Decide To Do With an Incoming Request
    """
    pass


class RateLimiterFirebase:
    """
    RateLimiterFirebase is the main class 
    for implementing the rate limiting Logic
    """

    def __init__(self, unique_identifier, default_config=None,
                 rate_limiting_type="TOKEN_BUCKET", collection_name="app"):
        self.unique_identifier = unique_identifier
        self.rate_limiting_type = rate_limiting_type
        self.collection_name = collection_name
        self.db = firestore.Client()
        col_ref = self.db.collection(self.collection_name)
        doc_ref = col_ref.document(self.unique_identifier)
        config = default_config if bool(
            default_config) else constants["default_config"]
        doc = doc_ref.get()
        if doc.exists:
            config = doc.to_dict()
        else:
            config["last_refill_time_stamp"] = time.time()
            # utf8_config = self.convert_to_utf8(self.config)
            doc_ref.set(config)  # TO DO ADD LOGIC TO VALIDATE config
        if self.rate_limiting_type != "TOKEN_BUCKET":
            raise NotSupportedAlgorithm("Currently Not Supported")
        else:
            self.rate_limiting_method = TokenBucket(
                config["max_bucket_size"], config["current_bucket_size"],
                config["refill_rate"], config["last_refill_time_stamp"])

    def check_if_allowed(self, token_count):
        try:
            result = self.rate_limiting_method.allow_request(token_count)
            new_config = self.rate_limiting_method.get_current_config()
            doc_ref = self.db.collection(
                self.collection_name).document(self.unique_identifier)
            doc_ref.update(new_config)
            return result
        except UnableToDecide as e:
            print(e)
            return True
