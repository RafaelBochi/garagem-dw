from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

User = get_user_model()

def LoginFunction(username_or_email, password):
    if username_or_email is not None:
        try:
            user = User.objects.get(
                Q(username=username_or_email) | Q(email=username_or_email)
            )
            user = authenticate(username=user.username, password=password)
        except:
            user = None
    else:
        response = {"message": "Username ou email inválido",
                    "code": 400}
        return response

    if user is not None:
        response = {
            "message": "Usuario logado com sucesso",
            "user": {"username": user.username, "email": user.email, "id": user.id},
            "code": 200
        }
        return response
    else:
        response = {"message": "Credenciais Invalidas", "code": 400}
        return response
