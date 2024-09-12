from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .validator import validate_user_data



class UserCreateView(APIView):
    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response({"message": rlt_message}, status=400)
        
        username = request.data.get('username')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        birth = request.data.get('birth')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        
        # 비밀번호 자동 해싱처리 등 기능 제공
        user = User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            birth=birth,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        
        # JSON 형태
        return Response(
            {
                "message": "User created successfully.",
                "id" : user.pk,
                "username" : user.username,
                "nickname" : user.nickname,
                "email" : user.email,
            }
        )