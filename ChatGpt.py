import openai
import os

api_key = "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"
if not api_key:
    raise ValueError("A chave da API não foi encontrada. Certifique-se de que a variável de ambiente OPENAI_API_KEY esteja configurada.")
openai.api_key = api_key

def enviar_mensagem(mensagem):

    completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": mensagem},
    ]
    )
print(enviar_mensagem("Ola"))