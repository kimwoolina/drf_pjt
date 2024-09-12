from .models import User

def validate_user_data(user_data):
    username = user_data.get('username')
    password = user_data.get('password')
    nickname = user_data.get('nickname')
    birth = user_data.get('birth')
    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')
    email = user_data.get('email')
    
    if len(nickname) < 4:
        return "nickname should be at least 4 characters long."
    
    if len(password) < 8:
        return "password should be at least 8 characters long."
    
    if User.objects.filter(username=username).exists():
        return "username already exists."
    
    if User.objects.filter(email=email).exists():
        return "email already exists."
    
    return user_data