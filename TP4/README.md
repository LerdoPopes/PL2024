PL2024

Título: TPC4 De PL

Autor: Pedro Afonso Moreira Lopes, A100759

Explicação da resolução do exercício:

Para este exercício, temos que criar um um analisador léxico para instruções SELECT..FROM de SQL. O analisador é capaz de reconhecer diferentes partes de uma instrução SQL, como os comandos SELECT, FROM e WHERE, identificadores de tabelas e colunas, operadores, números e outros caracteres. Para este fim, foram utilizadas expressões regulares (Regex) para a leitura e adição dos elementos textuais necessários para a resolução do exercício numa lista.

Estando todos os elementos necessários nessa lista, depois é feita uma travessia por essa lista, somando sempre que possível as sequências de números ao contador total e devolvendo o valor da soma também, tal como o exercício pediu.

A lista vai conter os seguintes elementos:

    SELECT: Correspondente à palavra-chave "select".
    FROM: Correspondente à palavra-chave "from".
    WHERE: Correspondente à palavra-chave "where".
    FIELD: Correspondente nomes de tabelas, nomes de colunas, etc.
    COMMA: Correspondente a uma vírgula.
    OPERATOR: Correspondente ao operador.
    NUM: Correspondente a números, incluindo números inteiros e decimais.

Com esta lista feita, utilizando a função **re.finditer()**, o script determina o token correspondente com base no grupo correspondido na expressão regular e, com isto, o script todos os tuplos criados ao longo da sua execução.

Este código é executado através da inserção de um input no stdin.

