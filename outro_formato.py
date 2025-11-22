import os
import json
from pyvis.network import Network

# Base de dados simulada (hospital)
dados = {
    "entidades": [
        {"nome": "Hospital Central", "tipo": "Instituição"},
        {"nome": "Diretor", "tipo": "Pessoa"},
        {"nome": "Médico", "tipo": "Pessoa"},
        {"nome": "Enfermeiro", "tipo": "Pessoa"},
        {"nome": "Paciente", "tipo": "Pessoa"},
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

# Construindo o grafo com PyVis
net = Network(notebook=True, directed=True, cdn_resources="remote")

# Configura opções (fundo preto, arrastar nós, física desativada)
net.set_options(
    """
{
  "nodes": {
    "font": { "size": 18, "color": "white" }
  },
  "edges": {
    "font": { "size": 14, "color": "white" }
  },
  "interaction": { "dragNodes": true },
  "physics": { "enabled": false },
  "layout": { "improvedLayout": true }
}
"""
)

# Fundo preto
net.bgcolor = "#000000"

# 🔹 Configuração de cores dos nós
cores_nos = {"Instituição": "orange", "Pessoa": "deepskyblue"}

# 🔹 Configuração de cores por relação completa
cores_relacoes = {
    "tem diretor": "white",
    "tem médicos": "lightblue",
    "tem enfermeiros": "violet",
    "tem pacientes": "gold",
    "atende": "lime",
    "cuida de": "orange",
    "coordena": "red",
}

# 🔹 Configuração de cores por verbo isolado
cores_verbos = {"tem": "cyan", "coordena": "pink", "cuida": "orange", "atende": "lime"}

# Adiciona nós com cores
for entidade in dados["entidades"]:
    nome = entidade.get("nome", "")
    tipo = entidade.get("tipo", "")
    cor = cores_nos.get(tipo, "gray")
    net.add_node(nome, label=nome, color=cor)

# Adiciona arestas com fonte configurável e cores
for origem, relacao, destino in dados["relacoes"]:
    verbo = relacao.split()[0]  # pega o primeiro termo
    # prioridade: verbo > relação completa
    cor = cores_verbos.get(verbo, cores_relacoes.get(relacao, "gray"))
    net.add_edge(
        origem,
        destino,
        label=relacao,
        font={
            "size": 18,
            "color": "white",
            "face": "arial",
            "strokeWidth": 0,  # remove sombra interna
            "strokeColor": "black",  # cor da sombra se strokeWidth > 0
            "background": None,  # pode ser "black" para fundo atrás do texto
        },
        width=3,
        color=cor,
    )

# Gera o HTML
net.show("grafos_conhecimento_hospital.html")
