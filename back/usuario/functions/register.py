from django.contrib.auth import get_user_model

User = get_user_model()

def RegisterFunction(username, email, password):
    if User.objects.filter(username=username).exists():
        response = {
            "message": "Usuário já existente.",
            "code": 400
        }
        return response
    elif User.objects.filter(email=email).exists():
        response = {
            "message": "Email já está sendo utilizado.",
            "code": 400
        }
        return response
    
    user = User.objects.create(username=username)
    user.email = email
    user.set_password(password)
    user.save()

    response = {
        "message": "Usuario criado com sucesso",
        "user": {
            "username": username,
            "email": email,
            "id": user.id
        },
        "code": 201
    }

    return response