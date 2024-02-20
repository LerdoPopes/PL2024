PL2024

Título: TPC2 De PL

Autor: Pedro Afonso Moreira Lopes, A100759

Explicação da resolução do exercício:

Para este exercício, temos que criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet. Para este fim, foram utilizadas expressões regulares (Regex) para a leitura e substituição dos elementos textuais desejados pelo exercício, como se pode ver na função **conversor**

Foi criada, além dessa função, uma auxiliar **cabecalho** que numera os <hN></hN> na conversão do Cabeçalho, verificando e contando o nº de # atrás da palavra.

Para a conversão de todos os elementos, exceto da Lista Numerada, foram utilizadas expressões regulares, tal como mencionado atrás. Para o caso específico da Lista Numerada, depois de inserir como input "lista", é pedido ao utilizador para inserir a lista numerada com os seus inputs, assumindo que este vai inserir uma lista de forma correta, sendo então feita a conversão quando este finalmente escreve "fim" no seu input.

Para a execução do código, este foi executado como normal e funciona através da inserção de inputs que deseja que sejam transformados em HTML.
