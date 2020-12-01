#11911ECP004 - Victor Gabriel Castão da Cruz

#Leitura Variáveis
bornes = int(input())
comandos = int(input())
afetado = int(input())

#Função para criar lista a ser utilizada
def popular_lista():
    #Acrescentar um termo nulo ao início para evitar problemas com indexação iniciada em 0
    #l[0] = 1 pois essa estação já é visitada inicialmente
    l = ['X',1]

    #Adicionar zeros correspondentes às visitas até o momento
    for i in range(bornes-1):
        l.append(0)

    #Retornar lista finalizada
    return l

#Chamar função
lista = popular_lista()

#Marcador de posição
posicao_atual = 1

#Ler comandos e atualizar posição
for i in range(comandos):
    movimento = int(input())
    posicao_atual += movimento

    #Como é um ciclo, a posição 0 é a última estação
    if posicao_atual == 0:
        posicao_atual = bornes

    #Como é um ciclo, ao final das estações, chega-se ao começo novamente
    elif posicao_atual == bornes+1:
        posicao_atual = 1

    #Atualizar número de visitas
    lista[posicao_atual] += 1

#Imprimir visitas feitas à estação em questão
print(lista[afetado])

