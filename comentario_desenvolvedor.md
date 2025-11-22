# 🏥 Relato do Projeto do Grafo Hospitalar

## 📑 Sumário

- [Erros e Dificuldades Encontradas](#-erros-e-dificuldades-encontradas)
- [Acertos e Soluções Aplicadas](#-acertos-e-soluções-aplicadas)
- [Conquistas Alcançadas](#-conquistas-alcançadas)
- [Conclusão](#-conclusão)

---

## ⚠️ Erros e Dificuldades Encontradas
- ❌ **Configuração das arestas**: inicialmente, as cores não apareciam corretamente, pois a lógica só considerava relações completas e ignorava os verbos
- ❌ **Sombra interna nos textos das arestas**: o contorno padrão do PyVis deixava a leitura menos clara
- ❌ **Controle do tamanho das arestas**: a tentativa de usar funções descontinuadas gerou erro, já que não funcionam mais nas versões atuais do PyVis
- ❌ **Espaçamento entre os nós**: mesmo configurando parâmetros, os nós continuavam muito próximos, exigindo ajustes finos nos parâmetros de física

---

## ✅ Acertos e Soluções Aplicadas
- 🎨 **Cores dos nós**: diferenciamos entidades por tipo (Instituição, Diretor, Médico, Enfermeiro, Paciente), tornando o grafo mais intuitivo
- 🌈 **Cores das arestas por relação completa**: cada relação ganhou uma cor própria (`tem diretor`, `coordena`, `atende` etc.)
- 🔠 **Cores por verbo isolado**: além das relações completas, passamos a permitir configuração por verbo (`tem`, `coordena`, `cuida`), dando flexibilidade ao desenvolvedor
- ✨ **Fonte configurável nas arestas**: ajustamos tamanho, cor, tipo de letra, sombra e fundo, eliminando o problema da sombra interna
- 🖤 **Fundo preto e contraste**: o grafo ficou visualmente elegante e legível
- ⚙️ **Configuração de física via JSON**: substituímos funções descontinuadas por parâmetros JSON corretos (`springLength`, `springConstant`), garantindo compatibilidade

---

## 🏆 Conquistas Alcançadas
- 🚀 **Evolução do projeto**: evoluímos de um grafo simples para uma ferramenta interativa e configurável, com visual moderno
- 🛠️ **Flexibilidade de configuração**: o desenvolvedor agora pode personalizar cores, fontes e espaçamento sem alterar a estrutura principal do código
- 📚 **Superação de desafios**: superamos erros técnicos e limitações da biblioteca, transformando cada obstáculo em aprendizado
- 🌍 **Solução robusta**: o projeto se tornou uma solução clara e flexível, que pode ser usada tanto para ensino quanto para gestão hospitalar

---

## ✨ Conclusão
A jornada mostra bem o ciclo de desenvolvimento: começamos com um grafo básico, enfrentamos erros de configuração e limitações técnicas, mas fomos ajustando passo a passo.

O resultado é uma **solução robusta, configurável e visualmente clara** — uma conquista que demonstra evolução e domínio sobre a ferramenta.

---

*Desenvolvido com ❤️ e persistência*
