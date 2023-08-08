from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import CustomUser,StoredData
from .serializers import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import hashlib
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class UserRegistrationView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        full_name = request.data.get('full_name')
        age = request.data.get('age')
        gender = request.data.get('gender')

        if not username or not password or not email or not full_name or not age or not gender:
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        user, created = CustomUser.objects.get_or_create(username=username, email=email, age=age)
        if created:
            user.username = username
            user.password = password
            user.full_name = full_name
            user.age = age
            user.gender = gender
            user.save()

            response_data = {
                'status': 'success',
                'message': 'User registered successfully',
                'username': user.username,
                'password': user.password,
                "email": user.email,
                "full_name": user.full_name,
                "age": user.age,
                "gender": user.gender
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)



class GenerateTokenView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'status': 'error', 'message': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        print(user,"opop")

        if user is None:
            return Response({'status': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        # Set token expiration time (1 hour)
        token_expire_duration = timedelta(seconds=3600)
        token.expires = token.created + token_expire_duration
        token.save()

        response_data = {
            'access_token': token.key,
            'expires_in': 3600,
        }
        return Response({'status': 'success', 'message': 'Token generated successfully', 'data': response_data}, status=status.HTTP_200_OK)

class StoreDataView(APIView):
    def post(self, request, format=None):
        unique_key = request.data.get('key')
        data_value = request.data.get('value')

        if not unique_key or not data_value:
            return Response({'status': 'error', 'message': 'Missing key or value'}, status=status.HTTP_400_BAD_REQUEST)

        stored_data, created = StoredData.objects.get_or_create(key=unique_key)
        stored_data.value = data_value
        stored_data.save()

        return Response({'status': 'success', 'message': 'Data stored successfully.'}, status=status.HTTP_201_CREATED)


class RetrieveDataView(APIView):
    def get(self, request, key, format=None):
        print(key,"yuy")
        dummy_data = {
            "key": key,
            "value": "dummy_data_value",
        }

        return Response({'status': 'success', 'data': dummy_data}, status=status.HTTP_200_OK)

class UpdateDataView(APIView):
    def put(self, request, key, format=None):
        print(f"Attempting to update data with key: {key}")
        try:
            stored_data = StoredData.objects.get(key=key)
        except StoredData.DoesNotExist:
            print(f"Data not found with key: {key}")
            return Response({'status': 'error', 'message': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)

        new_value = request.data.get('value')
        if new_value is None:
            return Response({'status': 'error', 'message': 'Missing value'}, status=status.HTTP_400_BAD_REQUEST)

        stored_data.value = new_value
        stored_data.save()

        return Response({'status': 'success', 'message': 'Data updated successfully.'}, status=status.HTTP_200_OK)


class DeleteDataView(APIView):
    def delete(self, request, key, format=None):
        try:
            print(key,"key")
            data_object = StoredData.objects.get(key=key)
            data_object.delete()
            return Response({'status': 'success', 'message': 'Data deleted successfully.'}, status=status.HTTP_200_OK)
        except StoredData.DoesNotExist:
            return Response({'status': 'error', 'message': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)

