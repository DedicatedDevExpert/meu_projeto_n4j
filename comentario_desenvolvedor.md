🏥 Relato do Projeto do Grafo Hospitalar
📑 Sumário
• 	⚠️ Erros e Dificuldades Encontradas
• 	✅ Acertos e Soluções Aplicadas
• 	🏆 Conquistas Alcançadas
• 	✨ Conclusão

⚠️ Erros e Dificuldades Encontradas
• 	❌ Configuração das arestas: inicialmente, as cores não apareciam corretamente, pois a lógica só considerava relações completas e ignorava os verbos.
• 	❌ Sombra interna nos textos das arestas: o contorno padrão do PyVis deixava a leitura menos clara.
• 	❌ Controle do tamanho das arestas: a tentativa de usar  gerou erro (), já que essa função não funciona mais nas versões atuais do PyVis.
• 	❌ Espaçamento entre os nós: mesmo configurando , os nós continuavam muito próximos, exigindo ajustes finos nos parâmetros de física.

✅ Acertos e Soluções Aplicadas
• 	🎨 Cores dos nós: diferenciamos entidades por tipo (, ), tornando o grafo mais intuitivo.
• 	🌈 Cores das arestas por relação completa: cada relação ganhou uma cor própria (, ,  etc.).
• 	🔠 Cores por verbo isolado: além das relações completas, passamos a permitir configuração por verbo (, , ), dando flexibilidade ao desenvolvedor.
• 	✨ Fonte configurável nas arestas: ajustamos tamanho, cor, tipo de letra, sombra e fundo, eliminando o problema da sombra interna.
• 	🖤 Fundo preto e contraste: o grafo ficou visualmente elegante e legível.
• 	⚙️ Configuração de física via : substituímos o uso de  por parâmetros JSON corretos (, ), garantindo compatibilidade.

🏆 Conquistas Alcançadas
• 	🚀 Evoluímos de um grafo simples para uma ferramenta interativa e configurável, com visual moderno.
• 	🛠️ O desenvolvedor agora pode personalizar cores, fontes e espaçamento sem alterar a estrutura principal do código.
• 	📚 Superamos erros técnicos e limitações da biblioteca, transformando cada obstáculo em aprendizado.
• 	🌍 O projeto se tornou uma solução robusta, clara e flexível, que pode ser usada tanto para ensino quanto para gestão hospitalar.

✨ Conclusão
A jornada mostra bem o ciclo de desenvolvimento: começamos com um grafo básico, enfrentamos erros de configuração e limitações técnicas, mas fomos ajustando passo a passo.
O resultado é uma solução robusta, configurável e visualmente clara — uma conquista que demonstra evolução e domínio sobre a ferramenta.
