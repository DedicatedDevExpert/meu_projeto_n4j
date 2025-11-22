import os
import json
from pyvis.network import Network

# Base de dados simulada (hospital)
dados = {
    "entidades": [
        {"nome": "Hospital Central", "tipo": "Instituição"},
        {"nome": "Diretor", "tipo": "Diretor"},
        {"nome": "Médico", "tipo": "Médico"},
        {"nome": "Enfermeiro", "tipo": "Enfermeiro"},
        {"nome": "Paciente", "tipo": "Paciente"},
    ],
    "relacoes": [
        ["Hospital Central", "tem diretor", "Diretor"],
        ["Hospital Central", "tem médicos", "Médico"],
        ["Hospital Central", "tem enfermeiros", "Enfermeiro"],
        ["Hospital Central", "tem pacientes", "Paciente"],
        ["Médico", "atende", "Paciente"],
        ["Enfermeiro", "cuida de", "Paciente"],
        ["Diretor", "coordena", "Médico"],
        ["Diretor", "coordena", "Enfermeiro"],
    ],
}

net = Network(notebook=True, directed=True, cdn_resources="remote")

# Configuração visual + física com springLength "springLength": 250,aqui altera a distancia entre nós
net.set_options("""
{
  "nodes": {
    "font": { "size": 18, "color": "white" }
  },
  "edges": {
    "font": { "size": 14, "color": "white" }
  },
  "interaction": { "dragNodes": true },
  "physics": {
    "enabled": true,
    "barnesHut": {
      "springLength": 250,
      "springConstant": 0.05
    }
  },
  "layout": { "improvedLayout": true }
}
""")

net.bgcolor = "#000000"

# Cores por tipo de entidade
cores_nos = {
    "Instituição": "orange",
    "Diretor": "red",
    "Médico": "green",
    "Enfermeiro": "purple",
    "Paciente": "yellow",
}

# Cores por relação completa
cores_relacoes = {
    "tem diretor": "white",
    "tem médicos": "lightblue",
    "tem enfermeiros": "violet",
    "tem pacientes": "gold",
    "atende": "lime",
    "cuida de": "orange",
    "coordena": "red",
}

# Cores por verbo isolado
cores_verbos = {"tem": "cyan", "coordena": "pink", "cuida": "orange", "atende": "lime"}

# Adiciona nós
for entidade in dados["entidades"]:
    nome = entidade["nome"]
    tipo = entidade["tipo"]
    cor = cores_nos.get(tipo, "gray")
    net.add_node(nome, label=nome, color=cor)

# Adiciona arestas
for origem, relacao, destino in dados["relacoes"]:
    verbo = relacao.split()[0]
    cor = cores_verbos.get(verbo, cores_relacoes.get(relacao, "gray"))
    net.add_edge(
        origem,
        destino,
        label=relacao,
        font={
            "size": 16,  # tamanho da letra
            "color": "white",  # cor da letra
            "face": "arial",  # tipo de fonte
            "strokeWidth": 0,  # remove sombra/borda
            "strokeColor": "black",  # cor da sombra (se strokeWidth > 0)
            "background": None,  # ou "black" para fundo atrás do texto
        },
        width=1,
        color=cor,
    )

net.show("grafo_conhecimento_hospital_relacoes.html")
