import random

print("--------------------BEM-VINDO AO JOGO DE MONTY-HALL--------------------- \n")

def requisitos():
    print("OBS: TENHA EM MENTE QUE, O NÚMERO DE PRÊMIOS NÃO PODE SER MAIOR QUE O NÚMERO DE PORTAS, NEM QUE O NÚMERO DE PORTAS ABERTAS. DEVE EXISTIR AO MENOS 1 PRÊMIO, 1 PORTA ABERTA E 3 PORTAS TOTAIS \n")
    print("A SOMA DO NÚMERO DE PORTAS ABERTAS COM O NÚMERO DE PRÊMIOS, DEVE SER NO MÍNIMO 1 UNIDADE MENOR QUE AS PORTAS TOTAIS. A ESCOLHA DA SUA PORTE NÃO DEVE SER UM NÚMERO EXCEDENTE AO DE PORTAS TOTAIS!\n")
    print("ADEMAIS, O NÚMERO DE PORTAS ABERTAS NÃO PODE SER MAIOR QUE O NÚMERO TOTAL DE PORTAS. \n")
    print("POR FIM, O NÚMERO DE PORTAS ABERTAS DEVE SER MENOR, NO MÍNIMO, EM 2 UNIDADES QUE O NÚMERO DE PORTAS TOTAIS. \n ")
requisitos()
#verificando se as regras batem
while True:
    portas_total = int(input("Digite o número total de portas: "))

    portas_abertas = int(input("Digite o número total de portas abertas: "))

    premios_total = int(input("Digite o número total de prêmios: "))

    escolha = int(input("Digite a porta que você quer escolher: "))
    if portas_total > premios_total and portas_total >= (portas_abertas+2) and portas_total > (premios_total + portas_abertas) and premios_total > 0 and portas_abertas > 0 and portas_total >=3 and escolha>0 and escolha <portas_total:
        break
    else:
        print(" \nERRO. \n")
        requisitos()

#lista de portas total
lista_portas_total = []

for i in range(1,portas_total+1):
    lista_portas_total.append(i)

#lista das portas premiadas 


lista_portas_premiadas = [0]
for i in range(0,premios_total):
    y = 1
    x = random.randint(1,portas_total)
    
    
    #verificando se o valor escolhido aleatoriamente, não se repete na lista
    while y <= len(lista_portas_premiadas):
        teste = True
        while teste == True:
            if lista_portas_premiadas[y-1] == x:
                x = random.randint(1,portas_total)
                y = 1
            else:
                teste = False
        
        y+=1
    
    lista_portas_premiadas.append(x)
lista_portas_premiadas.remove(0)

#lista das portas abertas


lista_portas_abertas = [0]
for i in range(0,portas_abertas):
    k = random.randint(1,portas_total)

    #verificando se as portas abertas são diferentes da escolhida 
    
    while True:
        if k != escolha:
            break
        else:
            k = random.randint(1,portas_total)
    #verificando se as portas abertas são diferentes da(s) premiada(s)
    
    
    auxiliar_interna = 1
    
    while auxiliar_interna<= len(lista_portas_abertas):
        auxiliar = 1
        while auxiliar <= len(lista_portas_premiadas):
            teste_aux = True
            while teste_aux == True:
                if lista_portas_premiadas[auxiliar-1] == k or escolha == k or lista_portas_abertas[auxiliar_interna -1] == k:
                    k = random.randint(1,portas_total)
                    auxiliar = 1
                    auxiliar_interna = 1
                else:
                    teste_aux = False
            auxiliar +=1
    
        auxiliar_interna +=1

    
    lista_portas_abertas.append(k)
    
lista_portas_abertas.remove(0)


#mostrando ao usuário as portas totais e as portas que serão abertas:

print("----------------------------------------------")
print(f"As portas totais são: {lista_portas_total} ")
print("----------------------------------------------")
print(f"A(s) porta(s) que foi/foram aberta(s) são/é:  {lista_portas_abertas} ")


#cálculo rápido da probabilidade de acertar trocando de porta (fórmula criada e deduzida no meu canal do ytb)
probabilidade = round(((premios_total*(portas_total-1))/(portas_total*(portas_total-portas_abertas-1)))*100,2)
probabilidade_sem_trocar = round((premios_total/portas_total)*100,2)
#perguntando para o usuário se ele vai querer optar pela troca de escolha ou não e verificando se digitou a tecla corretamente



while True:
    pergunta = input("Você deseja trocar de porta [s/n] ").lower()
    if pergunta != "s" and pergunta != "n":
        print("Erro. Digite 's' para sim e 'n' para não")
    if pergunta == "s" or pergunta == "n":
        break

if pergunta == "s":
    
    
    #retirando as portas abertas
    var_aux = 0

    while var_aux < len(lista_portas_total):
        var_tst = 0
        while var_tst < len(lista_portas_abertas):
            if lista_portas_abertas[var_tst] == lista_portas_total[var_aux]:
                lista_portas_total.pop(var_aux)
                var_aux = 0
                
            var_tst +=1
        var_aux +=1
    #removendo a porta que o usuário escolheu
    lista_portas_total.remove(escolha)    
    #verificando se o usuário fez a escolha correta
    p = True
    valida = False
    while p == True:

        escolha_atual = int(input(f"Digite a nova porta escolhida, sabendo que estão disponíveis as portas: {lista_portas_total} "))
        l = 0
        while l < len(lista_portas_total):
            if lista_portas_total[l] == escolha_atual:
                p = False
                valida = True
        
            l+=1
        if not valida:
            print("\nERRO. PORTA INVÁLIDA. TENTE NOVAMENTE\n")
    
    
    #vendo se a nova porta que o usuário escolheu é uma premiada ou não
    ganhou = False
    
    for i in lista_portas_premiadas:
        if i == escolha_atual:
            ganhou = True
            break
        

    if ganhou:
        print(f"PARABÉNS! VOCÊ FOI PRÊMIADO COM A PORTA {escolha_atual}! A(s) porta(s) premiada(s) foi/foram: {lista_portas_premiadas}.")
        print(f"Sabia que a matemática te ajudou nessa? Sempre que você optar pela troca de portas, sua chance será maior. Nesse caso, sua chance é de aproximadamente: {probabilidade}%. ")
        print(f"Se você não tivesse optado pela troca, sua chance seria de aproximadamente: {probabilidade_sem_trocar}%")
    else:
        print(f"Infelizmente, apesar da boa decisão matemática, você não foi premiado. A sua escolha de número {escolha_atual} não era uma porta premiada. As portas premiadas eram: {lista_portas_premiadas} ")
        print(f"Sua chance de ganhar, trocando de porta, era de aproximadamente: {probabilidade}%. Sem trocar, era de aproximadamente: {probabilidade_sem_trocar}%")



# se a pergunta foi não:        
if pergunta == "n":
    ganhou = False
        
    #retirando as portas abertas
    
    var_aux = 0
    while var_aux < len(lista_portas_total):
        var_tst = 0
        while var_tst < len(lista_portas_abertas):
            if lista_portas_abertas[var_tst] == lista_portas_total[var_aux]:
                lista_portas_total.pop(var_aux)
                var_aux = 0
                
            var_tst +=1
        var_aux +=1
    for i in lista_portas_premiadas:
        if i == escolha_atual:
            ganhou = True
            break
    
    if ganhou:
        print(f"PARABÉNS! VOCÊ FOI PRÊMIADO COM A PORTA {escolha}! A(s) porta(s) premiada(s) foi/foram: {lista_portas_premiadas}.")
        print(f"Apesar de não ir para um lado muito matemático, sua sorte lhe ajudou. Sabia que, sempre que você optar pela troca de portas, sua chance será maior? Nesse caso, sua chance é de aproximadamente: {probabilidade}%")
        print(f"Enquanto sem trocar de porta, sua chance é de aproximadamente: {probabilidade_sem_trocar}%")
    else:
        print(f"Infelizmente, você não foi premiado. A sua escolha de número {escolha} não era uma porta premiada. As portas premiadas eram: {lista_portas_premiadas} ")
        print(f"Sua chance de ganhar, trocando de porta, era de aproximadamente: {probabilidade}%. Sem trocar, era de aproximadamente: {probabilidade_sem_trocar}%")


