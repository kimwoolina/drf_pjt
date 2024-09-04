# https://teamsparta.notion.site/SCC-API-feat-ChatGPT-dd4f1b384f0543b48a0647d9314fb265


from openai import OpenAI
from api_pjt.config import OPENAI_API_KEY 

# 대신 터미널에서 export OPENAI_API_KEY="your_api_key_here" 도 가능
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

system_instructions = """
이제부터 너는 "영어, 한글 번역가"야. 
지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": system_instructions,
        },
        {
            "role": "user",
            "content": "Django가 너무 어려워요. 도와... 아니 살려주세요.",
        },
        {
            "role": "user",
            "content": "Hi My name is Lina.",
        },
    ],
)

print(completion.choices[0].message)