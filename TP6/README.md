# Gramática Independente de Contexto

## Autor

**Nome:** Pedro Lopes

**Número:** A100759

## Resumo

Este trabalho consiste na implementação de uma gramática livre de contexto para representar expressões aritméticas e lógicas simples. A gramática é definida por um conjunto de terminais, não-terminais e produções, que descrevem como as expressões podem ser formadas. 

### Exemplos de Expressões

```
$ ?a
$ b=a*2/(27-3)
$ !a+b
$ c=(a*b)/(a/b)
```

## Resolução

```
T = {'?', '!', '(', ')', '=', '*', '/', '-', '+', var, num}

N = {Problema, exp, exp2, exp3, sinal, sinal2}

S = Problema

P = {

    Problema -> ? VAR                   LA = {?}
              | ! exp                   LA = {!}
              | VAR '=' exp             LA = {VAR}

    exp ->  termo exp2                  LA = {VAR, NUM, '('}
         | '(' exp ')' exp2             LA = {VAR, NUM, '('}

    exp2  -> '+' exp                    LA = {'+'}
           | '-' exp                    LA = {'-'}
           | '/' exp                    LA = {'/'}
           | '*' exp                    LA = {'*'}    
           | &                          LA = {$, ')'}

    termo -> fator exp3                 LA = {VAR,NUM}

    exp3  -> '+' fator exp3             LA = {'+'}
           | '-' fator exp3             LA = {'-'}
           | '/' fator exp3             LA = {'/'}
           | '*' fator exp3             LA = {'*'}
           | &                          LA = {$}

    fator -> NUM                        LA = {NUM}
           | VAR                        LA = {VAR}
           | &                          LA = {$}

}
```