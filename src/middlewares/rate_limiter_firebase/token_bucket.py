"""
Implements a Simple Token Bucket Logic
as a Proof of Concept for using Rate 
Limiting with Firebase and Python
"""
import time


class TokenBucket:
    """
    An Implementation of the Token Bucket Algorithm
    Based On https://www.youtube.com/watch?v=FU4WlwfS3G0
    """

    def __init__(self, max_bucket_size, current_bucket_size, refill_rate=1, last_refill_time_stamp = time.time()):
        self.max_bucket_size = int(max_bucket_size)
        self.refill_rate = int(refill_rate)
        self.current_bucket_size = int(current_bucket_size)
        self.last_refill_time_stamp = last_refill_time_stamp

    def allow_request(self, tokens):
        print('Before',self.current_bucket_size,tokens, self.max_bucket_size,self.refill_rate,self.last_refill_time_stamp)
        print(self.refill())
        if int(self.current_bucket_size) >= int(tokens):
            self.current_bucket_size =int(self.current_bucket_size) - int(tokens)
            print('After',self.current_bucket_size,tokens, self.max_bucket_size,self.refill_rate,self.last_refill_time_stamp)
            return True

        return False

    def refill(self):
        print('In Refill')
        now = time.time()
        time_passed = now - self.last_refill_time_stamp
        tokens_to_add = int((time_passed * int(self.refill_rate))//(10**3))
        print(tokens_to_add)
        self.current_bucket_size = min(
            int(self.max_bucket_size), int(tokens_to_add)+ int(self.current_bucket_size))
        return {}

    def get_current_config(self):
        return {"max_bucket_size": self.max_bucket_size , "refill_rate": self.refill_rate, "current_bucket_size": self.current_bucket_size, "last_refill_time_stamp": self.last_refill_time_stamp}