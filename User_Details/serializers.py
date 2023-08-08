from django.http import JsonResponse
from .models import CustomUser

def get_user_data(request):
    user = CustomUser  # This is incorrect; it should be an instance of CustomUser
    data = {
        "username": user.username,
        "password": user.password,
        "email": user.email,
        "full_name": user.full_name,
        "age": user.age,
        "gender": user.gender
    }
    return JsonResponse(data)