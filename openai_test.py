# https://teamsparta.notion.site/SCC-API-feat-ChatGPT-dd4f1b384f0543b48a0647d9314fb265


from openai import OpenAI
from api_pjt.config import OPENAI_API_KEY 

# 대신 터미널에서 export OPENAI_API_KEY="your_api_key_here" 도 가능
CLIENT = OpenAI(
    api_key=OPENAI_API_KEY,
)


def ask_chatgpt(user_message):
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
    
    return completion.choices[0].message.content
    
system_instructions = """
이제부터 너는 '에이든 카페'의 직원이야.
아래 종류의 음료 카테고리에서 주문을 받고, 주문을 처리하는 대화를 진행해.

1. 아메리카노
2. 카페라떼
3. 프라푸치노
4. 콜드브루
5. 스무디

주문을 받으면, 주문 내용을 확인하고, 주문을 처리하는 대화를 진행해.
주문이 완료되면, 주문 내용을 확인하고, 주문이 완료되었음을 알려줘.
"""

# 처음 인사를 위해
response = ask_chatgpt(system_instructions)
print(f"에이든 카페봇 : {response}\n\n")

while True:
    user_input = input("유저 : ")
    if user_input == "종료":
        break
    response = ask_chatgpt(user_input)
    print(f"에이든 카페봇 : {response}\n\n")