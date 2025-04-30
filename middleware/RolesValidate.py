from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt, get_jwt_identity
from flask import jsonify

def admin_required(permissao):
    def decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):  
            verify_jwt_in_request()
            claims = get_jwt()
            permissions = claims.get("permissions", [])
            if permissao not in permissions and 'PoderAdemiro' not in permissions:
                return jsonify({"error": "Acesso negado"}), 403
            return fn(*args, **kwargs)
        return wrapped 
    return decorator


def superadmin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("role") != "superadmin":
            return jsonify({"error": "Acesso negado"}), 403
        return fn(*args, **kwargs)
    return wrapper