from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .validator import validate_user_data
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateView(APIView):
    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response({"message": rlt_message}, status=400)
        
        # user = User.objects.create_user(
        #     username=request.data.get('username'),
        #     password=request.data.get('password'),
        #     nickname=request.data.get('nickname'),
        #     birth=request.data.get('birth'),
        #     first_name=request.data.get('first_name'),
        #     last_name=request.data.get('last_name'),
        #     email=request.data.get('email'),
        # )
        
        # create_user: 비밀번호 자동 해싱처리 등 기능 제공
        user = User.objects.create_user(**request.data)
        
        # JWT token 발급
        refresh = RefreshToken.for_user(user)
        
        serializer = UserSerializer(user)
        response_dict = serializer.data
        response_dict["access"] = str(refresh.access_token)
        response_dict["refresh"] = str(refresh)
        
        return Response(response_dict) 
    
    
    
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            return Response({'error': 'Username and password required'}, status=400)
        
        # authenticate: 두개가 일치하면 해당 유저를 반환해줌
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({'error': '아이디 또는 비밀번호가 틀렸습니다.'}, status=400)
        
        # JWT token
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
            }
        )
        