# PL2024

Título:
TPC1 De PL 

Autor: 
Pedro Afonso Moreira Lopes, A100759

Explicação da resolução do exercício:

Para este exercício, temos que fazer a leitura de um ficheiro CSV sem utilizar o módulo CSV e, de seguida, imprimir aquilo que é pedido pelo enunciado do exercício. Para este fim, foi utilizado o STDIN para o envio do argumento. Além disto, para o parse do ficheiro CSV, é feita a navegação do ficheiro CSV linha a linha e a divisão dos atributos da linha, tal e qual como se encontra aqui em baixo:

    for line in path:
        row = line.rstrip().split(',')

Feito isto, ficamos com acesso aos valores de cada linha, podendo assim fazer os cálculos e distribuições necessárias para a resolução do exercício. Como por exemplo, para as distribuições de atletas, de acordo com as suas idades, é calculado o valor não-fracionário da idade a dividir por 5 e multiplicado outra vez por esse número, de forma a obter o valor absoluto da idade e, assim, podemos armazenar, no dicionário de distribuições criado, cada distribuição para cada intervalo de anos, de acordo com a chave que lhe é correspondida, de acordo com o cálculo anterior.

Finalmente, para as percentagens de atletas aptos e inaptos, foram calculados os números de atletas aptos e inaptos através da verificação do último atributo e, com isto, o número total de atletas e as respetivas percentagens.
Para as modalidades desportivas ordenadas por ordem alfabética, foram armazenados os nomes de todas as modalidades numa lista e, depois disto, esta foi ordenada.

Para a execução do código, como foi utilizado o STDIN para a leitura do CSV, o comando utilizado foi o seguinte:  cat emd.csv | python3 TPC1.py.
