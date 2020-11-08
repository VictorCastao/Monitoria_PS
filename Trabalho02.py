#Inicializando variáveis correspondentes ao número de dias e a soma
soma_total = 0
soma_parcial = 0
dias = 0
resposta = 0
n = 0
indicador = False

#Lendo número de dias
n = int(input())

#Obtendo somas de cada dia
while dias < n:

    #Atualizando dia atual
    dias = dias + 1

    #Acessos do dia
    soma_parcial = int(input())

    #Atualizando total de acessos
    soma_total = soma_total + soma_parcial

    #Verificando se a meta foi atingida
    #Caso seja, teremos a resposta
    if soma_total >= 1000000 and indicador == False:
        resposta = dias

        #Evitar atualização da resposta
        indicador = True

#Imprimindo resposta
print(resposta)
