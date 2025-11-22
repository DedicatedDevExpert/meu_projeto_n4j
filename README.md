# 🧠 Sistema de Grafos de Conhecimento com Gemini AI

Um projeto Python para extração automática de entidades e relações usando Google Gemini AI, com visualização interativa através de grafos de conhecimento.

## 📋 Visão Geral

Este sistema combina inteligência artificial com visualização de dados para:
- **Extrair automaticamente** entidades e relações de textos usando Gemini AI
- **Visualizar conhecimento** através de grafos interativos
- **Simular cenários** com dados estruturados (exemplo: sistema hospitalar)
- **Gerar visualizações HTML** interativas e personalizáveis

## 🛠️ Tecnologias Utilizadas

### Linguagens
- **Python 3.12+** - Linguagem principal do projeto

### Bibliotecas e Frameworks
- **google-generativeai** - SDK oficial do Google Gemini AI para geração de conteúdo
- **langchain-google-genai** - Integração LangChain com Gemini para processamento de linguagem natural
- **pyvis** - Biblioteca para criação de grafos interativos em HTML
- **python-dotenv** - Gerenciamento seguro de variáveis de ambiente
- **json** - Manipulação de dados estruturados
- **os/re** - Operações do sistema e expressões regulares

### Tecnologias Web
- **HTML5** - Renderização dos grafos interativos
- **JavaScript** - Interatividade dos grafos (via PyVis)
- **CSS3** - Estilização visual dos componentes

## 🚀 Funcionalidades

### 1. Extração Inteligente de Entidades (`gemini_relacoes.py`)
- Utiliza Gemini AI para processar texto em linguagem natural
- Extrai automaticamente entidades e relações de textos simples
- Exemplo: "Albert Einstein nasceu na Alemanha e trabalhou nos EUA"
- Converte resultados para formato JSON estruturado

### 2. Visualização de Dados Simulados (`hospital_relacoes.py`)
- Demonstra estrutura organizacional hospitalar
- Entidades: Hospital Central, Diretor, Médico, Enfermeiro, Paciente
- Relações hierárquicas: "tem diretor", "coordena", "atende", "cuida de"
- Sistema de cores diferenciado por tipo de profissional

### 3. Formatação Alternativa (`outro_formato.py`)
- Mesma estrutura hospitalar com física desabilitada
- Classificação simplificada: Instituição vs Pessoa
- Layout estático para melhor legibilidade

### 4. Exploração de Modelos (`modelos_gemini.py`)
- Lista todos os modelos Gemini disponíveis
- Verifica capacidades de geração de conteúdo
- Ferramenta de diagnóstico e exploração da API

## 📁 Estrutura do Projeto

```
├── 📄 gemini_relacoes.py          # Extração IA de entidades/relações
├── 📄 hospital_relacoes.py        # Simulação sistema hospitalar
├── 📄 outro_formato.py            # Visualização alternativa
├── 📄 modelos_gemini.py           # Exploração modelos Gemini
├── 🌐 grafo_conhecimento_gemini.html           # Saída IA
├── 🌐 grafo_conhecimento_hospital_relacoes.html # Saída hospitalar
├── 🌐 grafos_conhecimento_hospital.html        # Saída alternativa
├── 🔧 .env                        # Configurações API
├── 📦 ambiente/                   # Ambiente virtual Python
└── 📚 lib/                        # Bibliotecas JavaScript/CSS
```

## ⚙️ Configuração e Instalação

### 1. Pré-requisitos
```bash
# Python 3.12 ou superior
# Conta Google Cloud com Gemini AI habilitado
```

### 2. Configuração do Ambiente
```bash
# Ativar ambiente virtual
ambiente\Scripts\activate

# Instalar dependências
pip install google-generativeai langchain-google-genai pyvis python-dotenv
```

### 3. Configuração da API
```bash
# Criar arquivo .env na raiz do projeto
GOOGLE_API_KEY=sua_chave_api_aqui
```

## 🎯 Como Usar

### Extração com IA
```python
# Executar extração automática
python gemini_relacoes.py

# Resultado: grafo_conhecimento_gemini.html
```

### Simulação de Dados
```python
# Gerar grafo hospitalar
python hospital_relacoes.py

# Resultado: grafo_conhecimento_hospital_relacoes.html
```

### Explorar Modelos
```python
# Listar modelos disponíveis
python modelos_gemini.py
```

## 🎨 Características Visuais

- **Fundo escuro** para melhor contraste
- **Sistema de cores** diferenciado por tipo
- **Interatividade** completa (arrastar, zoom, pan)
- **Física configurável** para layout automático
- **Responsividade** para diferentes dispositivos

## 🔍 Casos de Uso

1. **Estruturas Hospitalares** - Mapear hierarquias e relações em instituições de saúde
2. **Extração de Texto** - Processar frases simples para identificar entidades
3. **Visualização Organizacional** - Demonstrar relações entre profissionais
4. **Prototipagem de Grafos** - Base para sistemas mais complexos
5. **Educação** - Demonstrar conceitos de grafos de conhecimento

## 🤝 Contribuição

Este projeto demonstra a integração entre IA generativa e visualização de dados, servindo como base para sistemas mais complexos de extração e representação de conhecimento.

## 📄 Licença

Projeto desenvolvido para fins educacionais e de demonstração tecnológica.

---

*Desenvolvido com ❤️ usando Python e Gemini AI*