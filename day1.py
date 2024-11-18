import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def gpt4omini(input):
    completion = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": input,
        }
        ],
        model="gpt-4o-mini",
        )
    print(completion.choices[0].message.content)

import ollama

def llama3(input):
    response = ollama.chat(
        model='llama3.1',
        messages=[
            {
                'role': 'user',
                'content': input,
            },
        ],
    )
    print(response['message']['content'])

# gpt4omini("""
# 아래 예제를 참고해서 영어를 한국어로 번역해줘.
# 1. cat -> 고양이
# 2. bird -> 새
# 3. tiger -> 호랑이
# 4. lion -> 사자
# 5. monkey -> 원숭이
#
# dog ->
# """)

# gpt4omini("""
# 영화 리뷰를 보고 긍정적(positive)인 평가인지 부정적(negative) 평가인지 판별해줘.
# 아래 예제를 참고해서 답변해.
# 1. 감독이 미쳤다. -> positive
# 2. 배우의 연기가 너무 좋았다. -> positive
# 3. 돈주고 보기 아깝다. -> negative
# 4. 보는 내내 졸았다. -> negative
# 5. 내용이 잘 이해되지 않는다. -> negative
#
# The storyline was dull and uninspiring. ->
# """)

# gpt4omini("""
# Convert the following natural language requests into SQL queries:
# 1. "월급이 50000원이 넘는 직원들 조회": SELECT * FROM employees WHERE salary > 50000;
# 2. "재고가 하나도 없는 제품 조회": SELECT * FROM products WHERE stock = 0;
# 3. "수학 점수가 90점을 넘은 학생들의 이름만 조회": SELECT name FROM students WHERE math_score > 90;
# 4. "최근 30일 이내에 들어온 주문 조회": SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
# 5. "고객들이 거주하고 있는 도시와 해당 도시에 거주중인 고객의 수 조회": SELECT city, COUNT(*) FROM customers GROUP BY city;
#
# Request: "Find the average salary of employees in the marketing department."
# SQL Query:
# """)

# gpt4omini("""
# # Simple - 1
# Solve the following problem step-by-step: 23 + 47
#
# Step-by-step solution:
# 1. 각 자리 수 분리. 23 -> 20 + 3, 47 -> 40 + 7
# 2. 십의 자리 합산. 20 + 40 = 60
# 3. 일의 자리 합산. 3 + 7 = 10
# 4. 전체 합산. 60 + 10 = 70
#
# Answer: 70
#
# # Simple - 2
# Solve the following problem step-by-step: 123 - 58
#
# Step-by-step solution:
# 1. 각 자리 수 분리. 123 -> 100 + 20 + 3, 58 -> 50 + 8
# 2. 백의 자리와 십의 자리 합산. 58은 백의 자리가 없으므로 100. 20 - 50 = -30
# 3. 일의 자리 합산. 3 - 8 = -5
# 4. 전체 합산. 100 + (-30) + (-5) = -65
#
# Answer: 65
#
# # Simple 결과 확인
# Solve the following problem step-by-step: 345 + 678 - 123
# """)
