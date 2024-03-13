PL2024

**Título:** TPC5 De PL

**Autor:** Pedro Afonso Moreira Lopes, A100759

## Explicação da resolução do exercício:

Este programa, desenvolvido em Python, simula o comportamento de uma máquina de vendas. Ele permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, adicionar produtos/stock, selecionar produtos para compra e sair do mesmo.

Para a resolução deste exercício, foi utilizada a biblioteca de Python `ply` para realizar a análise léxica, assim interpretando os comandos inseridos pelo utilizador.

Com isto dito, estes foram os passos para a resolução do exercício:

- **Criação do Tokens:** Antes de tudo, definimos primeiro os tokens que vão ser utilizados e tratados num tuplo.

- **Expressões Regulares** Com isso feito, vamos definir funções de tratamento para cada token, aplicando-lhes as expressões regulares necessárias.

- **Tratamento de cada Token com o lexer** Finalmente, vamos chamar o lexer na função principal e verificar o primeiro token capturado pelo utilizador e, dependendo deste, a função principal vai fazer algo. Como por exemplo:

- **LISTAR:** Vai ser feita a listagem de todos os produtos disponíveis. Isto é feito através da leitura do ficheiro JSON.

- **MOEDA** Com este comando, dando-lhe de argumento a quantidade para inserir, separado de vírgulas, este vai carregar o saldo atual.

- **SELECIONAR** Aqui vai ser feita a seleção do artigo para compra, sendo então necessário verificar se o artigo existe e se tem quantidade disponível para venda. Caso não tenha, a compra é rejeitada.

- **ADICIONAR** Este é o comando extra que permite adicionar artigos à máquina, estejam estes já existentes ou não.

- **SAIR** Finalmente, para terminar as transações com a máquina, é utilizado este comando, guardando também o estado da máquina após o seu uso.

## Execução do código

Este código é executado através do seguinte comando:

``` 
python TPC5.py
```

## Exemplo de transações com a máquina

Com isto, segue-se em baixo uma série de transações com a máquina, demonstrando como os comandos e interação Utilizador/Máquina funciona:

``` 
LISTAR
cod       |     nome                     |  quantidade   |     preco    
A1        |     água 0.5L                |     8         |     0.7      
A2        |     Cola                     |     6         |     1.0      
A3        |     Fanta                    |     8         |     1.0      
A4        |     7-Up                     |     5         |     1.0      
A5        |     Guaraná                  |     9         |     1.0      
A6        |     Sumol                    |     7         |     1.0      
A7        |     Bolachas                 |     3         |     0.6      
A8        |     Gomas                    |     3         |     1.3      
A9        |     Cerveja                  |     2         |     1.0      
ADICIONAR Batatas 2 1e30c
Produto Batatas adicionado à máquina!
ADICIONAR Cerveja 2
Produto Cerveja adicionado à máquina!
LISTAR
cod       |     nome                     |  quantidade   |     preco    
A1        |     água 0.5L                |     8         |     0.7      
A2        |     Cola                     |     6         |     1.0      
A3        |     Fanta                    |     8         |     1.0      
A4        |     7-Up                     |     5         |     1.0      
A5        |     Guaraná                  |     9         |     1.0      
A6        |     Sumol                    |     7         |     1.0      
A7        |     Bolachas                 |     3         |     0.6      
A8        |     Gomas                    |     3         |     1.3      
A9        |     Cerveja                  |     4         |     1.0      
A10       |     Batatas                  |     2         |     1.3      
MOEDA 2e,50c
Saldo = 2e50c
SELECIONAR A10
Pode retirar o produto dispensado " Batatas "
Saldo = 1e20c
SELECIONAR A10
Saldo insuficiente para satisfazer o seu pedido
Saldo = 1e20c; Pedido = 1e30c
SELECIONAR A7
Pode retirar o produto dispensado " Bolachas "
Saldo = 0e60c
SELECIONAR A7
Pode retirar o produto dispensado " Bolachas "
Saldo = 0e00c
SELECIONAR A10
Saldo insuficiente para satisfazer o seu pedido
Saldo = 0e00c; Pedido = 1e30c
LISTAR
cod       |     nome                     |  quantidade   |     preco    
A1        |     água 0.5L                |     8         |     0.7      
A2        |     Cola                     |     6         |     1.0      
A3        |     Fanta                    |     8         |     1.0      
A4        |     7-Up                     |     5         |     1.0      
A5        |     Guaraná                  |     9         |     1.0      
A6        |     Sumol                    |     7         |     1.0      
A7        |     Bolachas                 |     1         |     0.6      
A8        |     Gomas                    |     3         |     1.3      
A9        |     Cerveja                  |     4         |     1.0      
A10       |     Batatas                  |     1         |     1.3      
MOEDA 1e,20c,10c
Saldo = 1e30c
SELECIONAR A10
Pode retirar o produto dispensado " Batatas "
Saldo = 0e00c
LISTAR
cod       |     nome                     |  quantidade   |     preco    
A1        |     água 0.5L                |     8         |     0.7      
A2        |     Cola                     |     6         |     1.0      
A3        |     Fanta                    |     8         |     1.0      
A4        |     7-Up                     |     5         |     1.0      
A5        |     Guaraná                  |     9         |     1.0      
A6        |     Sumol                    |     7         |     1.0      
A7        |     Bolachas                 |     1         |     0.6      
A8        |     Gomas                    |     3         |     1.3      
A9        |     Cerveja                  |     4         |     1.0      
A10       |     Batatas                  |     0         |     1.3      
MOEDA 1e
Saldo = 1e00c
SELECIONAR A10
Produto não tem stock!
SELECIONAR A12
Produto não existente em stock!
SAIR
Troco : 1e 
Até à próxima!
```