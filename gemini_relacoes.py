import os
import re
import json
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from pyvis.network import Network

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Texto de entrada
texto = "Albert Einstein nasceu na Alemanha e trabalhou nos EUA."

# Configuração do modelo Gemini via LangChain
llm = ChatGoogleGenerativeAI(
    model="models/gemini-pro-latest",  # ou "models/gemini-flash-latest"
    temperature=0,
    api_key=api_key,
)

# Prompt para extrair entidades e relações
prompt = PromptTemplate(
    input_variables=["texto"],
    template="""
    Extraia entidades (pessoas, lugares, conceitos) e relações do texto abaixo.
    Retorne no formato JSON:
    {{
      "entidades": [...],
      "relacoes": [[origem, relacao, destino], ...]
    }}
    Texto: {texto}
    """,
)

# Criando a cadeia com RunnableSequence
chain = RunnableSequence(prompt | llm)

# Executa a cadeia
resultado = chain.invoke({"texto": texto})
print("Saída do modelo Gemini:\n", resultado.content)

# --- Tratamento do JSON ---
conteudo = resultado.content.strip()
conteudo = conteudo.replace("```json", "").replace("```", "").strip()

# Converte para dicionário Python
dados = json.loads(conteudo)

# Construindo o grafo com PyVis
net = Network(notebook=True, directed=True, cdn_resources="remote")

# Adiciona nós
for entidade in dados["entidades"]:
    if isinstance(entidade, dict):
        nome = entidade.get("nome") or entidade.get("texto") or ""
    else:
        nome = entidade
    net.add_node(nome, label=nome)

# Adiciona arestas
for origem, relacao, destino in dados["relacoes"]:
    net.add_edge(origem, destino, label=relacao)

net.show("grafo_conhecimento_gemini.html")
