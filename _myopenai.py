import os
import openai
from openai import OpenAI

def my_chat_completion(client: OpenAI, model: str = "gpt-3.5-turbo",
                           seed: int = 1, temperature: float = 1.0,
                           prompt_system: str = "You are a helpful assistant.",
                           prompt_user: str = "Hello",
                           *args, **kwargs) -> dict:

    completion = client.chat.completions.create(
        model=model,
        seed=seed,  # For reproducibility
        temperature=temperature,
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user}
        ],
        *args, **kwargs
    )
    return completion

def printChatCompletion(cc: openai.types.chat.chat_completion.ChatCompletion):
    print(cc.choices[0].message.content)
    