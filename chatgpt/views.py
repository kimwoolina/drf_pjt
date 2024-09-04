from rest_framework.views import APIView
from rest_framework.response import Response

from openai import OpenAI
from django.conf import settings 

class TranslateAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        
        CLIENT = OpenAI(api_key=settings.OPEN_API_KEY)
        
        system_instructions = """
        이제부터 너는 "영어, 한글 번역가"야. 
        지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
        프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
        """
        
        completion = CLIENT.chat.completions.create(
    
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        )
        
        chatgpt_response = completion.choices[0].message.content
        
        return Response({"message" : chatgpt_response})