# Academia

## Descrição
O sistema de acesso à academia Corpo Tangente Derivada está obsoleto e tem sido motivo de insatisfação. Acredite se quiser, os clientes dependem de uma antiga caderneta, a qual contém o nome, a senha e a situação da mensalidade. Duda, a dona fitness da academia, decidiu aderir à evolução tecnológica, ela deseja que você crie, urgentemente, uma catraca digital, que seja capaz de receber os dados citados acima para cada cliente e, logo após, ao receber uma senha, liberar o acesso ou não.

## Formato de entrada


Para cada cliente a ser cadastrado, o programa receberá uma estrutura com os campos:

Nome: string com no máximo 50 caracteres.
Senha de acesso: inteiro.
Situação da mensalidade: caractere correspondente a 'P' quando estiver paga, ou 'F', quando estiver devendo.
O programa deverá receber essas entradas até que o nome dado seja “SAIR” ou o limite de 100 clientes seja atingido.

Após encerrado o cadastro, serão recebidas inúmeras senhas, até que o valor lido seja -1.

## Formato de saída

Automaticamente, ao receber uma senha de acesso, o programa deverá:


Caso haja uma senha cadastrada correspondente e a situação da mensalidade seja “P”, imprimir o nome do cliente, acompanhado de uma mensagem de boas-vindas. Ex.: “Maria Foco Total, seja bem-vindo(a)!”

Caso haja uma senha cadastrada correspondente, mas a situação da mensalidade seja diferente de “P”, imprimir o nome do cliente, acompanhado de uma mensagem o direcionando à recepção. Ex.: “Não está esquecendo de algo, Joãozinho Fitness? Procure a recepção!”

Caso não haja uma senha cadastrada, imprimir uma mensagem de boas-vidas que o direcione à recepção. Ex.: “Seja bem-vindo(a)! Procure a recepção!”

## Exemplos de:
_______________________________
### Entrada
    Maria Foco Total
    19875
    P
    SAIR
    19875
    -1

### Saída
    Maria Foco Total, seja bem-vindo(a)!
_______________________________
[Ver no The Huxley](https://thehuxley.com/problem/3628)