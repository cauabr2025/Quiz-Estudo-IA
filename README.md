🧠 Meu Assistente de Estudos com IA (Llama 3) Versão 1.0

Sabe quando você estuda, estuda, mas parece que o conteúdo não entra na cabeça? Eu decidi resolver isso com Python, acabou o problema rsrsrs.

Tava estudando e criei este projeto para transformar minha rotina de revisão em um aprendizado ativo. Em vez de só ler resumos, eu coloco a IA para me testar e, o melhor: me explicar onde eu errei.

🚀 O que ele faz?

Basicamente, é um professor particular no meu terminal:

1.  Perguntas Infinitas: Eu digito um tema (ex: "Python", "Direito Constitucional", "Inglês") e ele gera um quiz inédito na hora.
2.  Correção Instantânea: Naõ precisa esperar. Errou? O sistema avisa na hora.
3.  Diagnóstico Inteligente: Se eu erro, ele não só mostra a resposta certa, mas gera uma explicação do conceito para eu aprender e não errar mais.

🛠️ O que eu usei?

-   Python (A mágica toda)
-   Groq API (Para acessar o modelo *Llama 3* de graça e super rápido)
-   Dotenv (Para esconder minhas chaves de API com segurança)
-   JSON (Para estruturar os dados que vêm da IA)

💻 Quer testar?
BORA BILL! 
1.  Clone o projeto:
    bash
    git clone [https://github.com/cauabr2025/Quiz-Estudo.git](https://github.com/cauabr2025/Quiz-Estudo.git)
    

2.  Instale o necessário:
    bash
    pip install groq python-dotenv
    

3.  Configure a Chave:
    - Crie um arquivo chamado .env na pasta do projeto.
    - Cole sua chave da Groq lá: GROQ_API_KEY=sua_chave_aqui

4.  Rode:
    bash
    python main.py
    
Feito com teclado mecânico e muita paciêcia por Cauã Bryan.
