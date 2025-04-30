from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify


"""
Decorador que verifica se o usuário tem a permissão necessária para acessar a rota.

Parâmetros:
permissao (str): O nome da permissão exigida para acessar a rota. O usuário deve ter essa permissão 
                ou a permissão 'PoderAdemiro' para acessar.

Retorna:
- A função decorada se o usuário tiver a permissão necessária.
- Resposta de erro 403 (Acesso negado) se o usuário não tiver a permissão.
"""
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



"""
Decorador que verifica se o usuário tem o cargo de 'superadmin' para acessar a rota.

Retorna:
- A função decorada se o usuário for um 'superadmin'.
- Resposta de erro 403 (Acesso negado) se o usuário não for um 'superadmin'.
"""
def superadmin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("role") != "superadmin":
            return jsonify({"error": "Acesso negado"}), 403
        return fn(*args, **kwargs)
    return wrapper