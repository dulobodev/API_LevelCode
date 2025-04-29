from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

def admin_required(permissao):
    def decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):  # Mude o nome para evitar conflito
            verify_jwt_in_request()
            claims = get_jwt()
            permissions = claims.get("permissions", [])
            if permissao not in permissions and 'PoderAdemiro' not in permissions:
                return jsonify({"error": "Acesso negado"}), 403
            return fn(*args, **kwargs)
        return wrapped  # Retorna 'wrapped' em vez de 'wrapper'
    return decorator


def superadmin_required(fn):
    @wraps(fn)  # Isso preserva o nome da função original
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_info = get_jwt_identity()
        if user_info['role'] != 'superadmin':
            return jsonify({"error": "Acesso negado"}), 403
        return fn(*args, **kwargs)
    return wrapper