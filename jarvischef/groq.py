from decouple import config
from groq import Groq
API_KEY = config('GROQ_API_KEY')


# def get_groq_client():
#     from groq import Groq
#     from decouple import config

#     API_KEY = config('GROQ_API_KEY')
#     return Groq(api_key=API_KEY)




# def get_chat_response(user_message):
#     try:
#         completion = get_groq_client.chat.completions.create(
#             model="llama3-groq-70b-8192-tool-use-preview",
#             messages=[
#                 {"role": "user", "content": user_message},
#                 {
#                     "role": "assistant",
#                     "content": "I can help you with that. Could you please provide me with the ingredients you have available and any dietary restrictions you might have?"
#                 }
#             ],
#             temperature=0.5,
#             max_tokens=1024,
#             top_p=0.65,
#             stream=False,
#             stop=None,
#         )
#         # Adjust logic based on observed response format
#         # response = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
#         response = "".join(choice['delta']['content'] or "" for choice in completion['choices'])

#         return response
#     except AttributeError as e:
#         return f"Error: {str(e)}"


def get_chat_response(user_message):
    prompt = f"I want to make a {user_message} recipe. Can you help me with that? "
    
    client = Groq(api_key = API_KEY)
    compition = client.chat.completions.create(
                    model="mixtral-8x7b-32768",
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }
                    ],
                    temperature=0.5,
                    top_p=1,
    )
    return(compition.choices[0].message.content)
