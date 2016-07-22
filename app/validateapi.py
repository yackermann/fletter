from functools import wraps
from flask import request, jsonify

class ValidateAPI():
    """Check API requests"""

    def expect_json(self, func):
        """Check request is it json or not"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.headers['Content-Type'] == 'application/json':
                return func(*args, **kwargs)
            else:
                return jsonify({
                    'status' : 'failed',
                    'error'  : 'Unsupported media type!'
                }), 415

        return wrapper