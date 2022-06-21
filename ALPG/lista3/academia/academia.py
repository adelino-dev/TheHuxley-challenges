################ Recebendo dados ######################
dados = []
entrada = input()
num = 1

while entrada != "SAIR" and num<100:
    dados.append(entrada)
    entrada = input()
    num += 1

################ Recebendo Senhas ######################

senhas = []
entrada = input()

while entrada != "-1":
    senhas.append(entrada)
    entrada = input()

########## Analisando permissões de acesso ###############

for senha in senhas:
    if senha in dados:
        i = dados.index(senha)
        nome = dados[i-1]
        situacao = dados[i+1]

        if situacao == "P":
            print(nome + ", seja bem-vindo(a)!")
        else:
            print("Não está esquecendo de algo, " + nome + "? Procure a recepção!")
    
    else:
        print("Seja bem-vindo(a)! Procure a recepção")
