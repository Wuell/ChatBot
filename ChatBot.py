import openai

apikey = "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"

openai.api_key = apikey

def send_message(mensagem):
    resposta = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": mensagem}
        ]
    )  
    return resposta.choices[0].message

print(send_message("Qual o maior buraco negro conhecido"))