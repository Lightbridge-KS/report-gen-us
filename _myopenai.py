import openai

def printChatCompletion(cc: openai.types.chat.chat_completion.ChatCompletion):
    print(cc.choices[0].message.content)
    