# Calcular dígito


## Descrição
Escreva um programa que verifique se o dígito verificador de uma chave está calculado corretamente. Esta chave é uma string, como o CPF ou CNPJ,  isto é, uma sequência de caracteres numéricos com alguns sinais de pontuação intercalados. No caso específico deste problema, a chave é mais simples porque contém apenas um dígito verificador.

**Descriçãodo problema.** A chave contém 9 dígitos arábicos agrupados em 3 grupos de tamanho 3 e separados por um sinal de ponto-final. O último grupo é separado do dígito verificador por um hífen. O dígito verificador é calculado como o resto da divisão por 10 da soma dos maiores algarismos em cada um dos três grupos. Vejao exemplo.


**Exemplo.** Suponha que a entrada seja dada por '001.290.611-6'


O dígito verificador é obtido como:

1. Maior elemento do grupo '001'= 1

1. Maior elemento do grupo '290'= 9

1. Maior elemento do grupo '611' = 6

1. Somados valores 1,9 e 6 = 16

1. Resto da divisão por 10 do número 16 = 6

**Defina e use uma função chamada** `calcular_digito` **para retornar o caracter do dígito verificador**. A string contendo a chave é passada como parâmetro. A função deve retornar uma string contendo apenas um caracter: a representação do dígito na forma de texto.



## Formato de entrada

A entrada consiste de linhas contendo uma chave ou a _string_ FIM.



## Formato de saída

A saída consiste de um texto com o valor VALIDO quando o dígito na chave estiver apresentado corretamente ou INVALIDO caso contrário.


## Exemplos de:
________________________________________
### Entrada
    001.290.611-6
    101.260.619-0
    FIM

### Saída
    VALIDO
    INVALIDO
________________________________________

[Ver no The Huxley](https://thehuxley.com/problem/2000)