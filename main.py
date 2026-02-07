import os
from dotenv import load_dotenv #pip
from groq import Groq
load_dotenv()
chave = os.getenv('GROK_API_KEY')

import openai

client = openai.OpenAI(
    api_key=chave,
    base_url="https://api.groq.com/openai/v1"
)
x = input('Eai meu brother, sobre qual materia você quer testar seu conhecimento? ')
y = input('Tem algum assunto em específico? ')
w = input('Tem alguma banca de prova especifica que deseja treinar? ')
while True:
    prompt = (f"Crie 1 questão de {x} sobre {y} para concursos públicos brasileiros do modelo da banca {w}, nível médio. Com alternativas. Sem dizer o gabarito")
    correcao = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=prompt)
    print(correcao.output_text)
    resposta = input('\nMe diga a alternativa ')
    correcao = client.responses.create(
        model="llama-3.3-70b-versatile",
        input= (f'Diga se a resposta {resposta} da pergunta {correcao} estar certo/errado e explique da forma mais simples')
)
    print(correcao.output_text)
    print('\nO que você quer fazer agora?')
    print('1 - Outra pergunta')
    print('2 - Trocar de assunto')
    print('3 - Sair')
    opcao = input('Escolha (1/2/3): ')
    if opcao == '1':
        continue
    elif opcao == '2':
        x = input('Eai meu brother, sobre qual materia você quer testar seu conhecimento? ')
        y = input('Tem algum assunto em específico? ')
        w = input('Tem alguma banca de prova especifica que deseja treinar? ')
        continue
    elif opcao == '3':
        print('\n Bons estudos! Até a proxima')
        break
    else:
        print('Opção invalida, continuando no mesmo assunto')
