from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .validator import validate_user_data
from .serializer import UserSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


class UserCreateView(APIView):
    permission_classes = [AllowAny]
    
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
    permission_classes = [AllowAny]
    
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

class UserProfileView(APIView):
    def get(self, request, username):
        
        # 01. user 조회
        user = User.objects.get(username=username)
        
        # 02. User 객체 직렬화 (JSON)
        serializer = UserProfileSerializer(user)
        
        return Response(serializer.data)
    
    
# 로그아웃은 refresh token만 blacklist에 등록해주면 된다.
# access token은 등록하면 안됨.
# 유저가 api 콜을 할때마다 access token을 사용한다. 한 유저가 api를 몇천번을 콜하므로.
# access token이 black list에 있는지 체크하려면 시스템에 부담이 될것이다.
# 따라서 access token은 프론트엔드 쪽에서 지워줘야한다.


# 비밀번호 변경
class UserPasswordChangeView(APIView):
    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not request.user.check_password(old_password):
            return Response(
                {'message': '기존 비밀번호가 일치하지 않습니다.'}, 
                status=400
                )
        
        # 알아서 해싱해서 저장해줌. (장고 내장 기능)
        request.user.set_password(new_password)
        request.user.save()
        
        return Response()