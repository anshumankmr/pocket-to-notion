"""
Implement Rate Limiting Logic
As a Middleware
"""
from functools import wraps
from .rate_limiter_firebase.rate_limiter_firebase import RateLimiterFirebase
from flask import request

def rate_limiting_logic():
    def _rate_limiting_logic(f):
        @wraps(f)
        def __rate_limiting_logic(*args, **kwargs):
            # print(f"before {f.__name__}")
            rate_limiter = RateLimiterFirebase(request.remote_addr)
            if rate_limiter.check_if_allowed(8):
                result = f(*args, **kwargs)
                # print(f"{f.__name__} result: {result}")
            else:
                print('Whoops!!! Too Many Requests')
                return "Too Many Request", 429
            # print(f"after {f.__name__}")

            return result
        return __rate_limiting_logic
    return _rate_limiting_logic
