#Victor Gabriel Castão da Cruz
#11911ECP004

#Verificação Módulo/Script
if __name__ == "__main__":

    #Ordenação de uma lista em ordem decrescente de habilidade
    def ordem(lista):

        #Tamanho lista
        tamanho = len(lista)

        #Utilizando o selection sort
        for i in range(tamanho):
            maior = -1
            indice = i

            #Achar o maior elemento
            for j in range(i, tamanho):
                if lista[j][1] > maior:
                    maior = lista[j][1]
                    indice = j
            #Colocar elemento na posição certa
            lista[i], lista[indice] = lista[indice], lista[i]

        #Retornar lista ordenada
        return lista

    #Função para ordenar um time em ordem alfabética
    def ordem2(lista):

        #Tamanho do time
        tamanho = len(lista)

        #Utilizando selection sort
        for i in range(tamanho):
            menor = lista[i]
            indice = i

            #Encontrar "menor" nome (em relação a ordem lexicográfica)
            for j in range(i, tamanho):
                if lista[j] < menor:
                    menor = lista[j]
                    indice = j

            #Colocar na posição correta
            lista[i], lista[indice] = lista[indice], lista[i]

        #Retornar time ordenado
        return lista

    #Função que imprimirá os resultados
    def imprimir(lista, times):

        #Agrupar um time de cada vez
        for i in range(times):

            #Lista de nomes
            lst = []
            
            print("Time", i+1)

            #Adicionar jogadores ao time em questão, que serão os elementos i, i+times, i+2*times ...
            for j in range(i, len(lista), times):
                lst.append(lista[j][0])

            #Ordenar
            lst = ordem2(lst)

            #Imprimir nomes do time
            for nome in lst:
                print(nome)

            #Pular linha
            print()

        #Retorno vazio
        return
        
    #Leitura parâmetros
    parametros = input()
    parametros = parametros.split()
    jogadores = int(parametros[0])
    times = int(parametros[1])

    #Lista dos jogadores
    nomes = []
    for i in range(jogadores):
        leitura = input()
        leitura = leitura.split()
        leitura[1] = int(leitura[1])
        nomes.append(leitura)

    #Ordenar por habilidade
    nomes = ordem(nomes)

    #Imprimir resultado
    imprimir(nomes, times)
