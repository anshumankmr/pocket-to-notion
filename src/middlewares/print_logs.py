"""
Implement Rate Limiting Logic
As a Middleware
"""
from functools import wraps
from flask import request


def print_log():
    def _print_log(f):
        @wraps(f)
        def __print_log(*args, **kwargs):
            print(request.get_json())
            result = f(*args, **kwargs)
            return result
        return __print_log
    return _print_log
