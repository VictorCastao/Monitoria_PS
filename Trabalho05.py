#Leitura variáveis
primeiro = int(input())
terceiro = int(input())
quarto = int(input())
sexto = int(input())

#Soma dos 4 valores informados
soma = primeiro + terceiro + quarto + sexto

#Criação de listas necessárias
duplas = []
resultado = []

#Todos os números entre 1° e 3°
for i in range(primeiro+1, terceiro):

    #Caso i seja um número elegível
    if primeiro % 2 != i % 2:

        #Todos os números ente 4° e 6°    
        for j in range(quarto+1, sexto):

            #Caso j seja elegível (pela lógica, i também é)
            if (soma + i + j) % 7 != 0 and (soma + i + j) % 13 != 0 and quarto % 2 != j % 2:

                #Dupla de números possível para escolha
                duplas.append([i,j])

#Função para construir uma lista com todas as listas possíveis
def construir_lista(resultado):
    for i in duplas:
        resultado.append([primeiro, i[0], terceiro, quarto, i[1], sexto])

#Chamar função
construir_lista(resultado)

#Imprimir números definidos inicialmente
print("Primeiro:", "{:02}".format(primeiro))
print("Terceiro:", "{:02}".format(terceiro))
print("Quarto:", "{:02}".format(quarto))
print("Sexto:", "{:02}".format(sexto))

#Imprimir jogos possíveis
print("Lista de apostas:")
for ls in resultado:
    print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5]))
    
