import os
from grop import Grop

#Defina a chave da API dietamente no código ou garanta que ela esteja configurada corretamente no ambiente 
os.environ["GROQ_API_KEY"] = "Digite aqui sua chave de API"

client = Grop(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Icializa a lista de mensagens para manter o contexto da conversa
messages = []

while True:
    usuario = input("Digite uma mensagem ou 'sair' para encerrar")

    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    #Adicione a mensagem do usuário à lista de mensagens
    messages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messagens=messages
        model="llama-3.1"
    )

    resposta = chat_completion.choices[0].message.content
    print("Resposta:", resposta)

    #Adiciona a resposta do assistente à lista de mensagens para manter o contexto
    messages.append({"role": "assistant", "content": resposta})