#Victor Gabriel Castão da Cruz
#11911ECP004

#Função que analisará as sequências
def analise(matriz, C):

    #Identificar quantidade de linhas e colunas
    linhas = len(matriz)
    colunas = len(matriz[0])

    #Lista que armazenará a quantidade de palitos de tamanho equivalente ao índice da lista
    comprimentos = [0]

    #Laço para deixar a lista com X valores 0, onde X = colunas
    for i in range(linhas):
        comprimentos.append(0)

    #Laço para analisar sequencias. Como a sequência é vertical, percorro todas as linhas de uma coluna para depois alterar a coluna
    for c in range(colunas):

        #Para cada coluna, minha sequência inicial tem tamanho 0
        seq = 0

        #Percorrendo os itens da coluna
        for l in range(linhas):

            #Caso seja 1, incremento no tamanho da minha sequência
            if matriz[l][c] == 1:
                seq += 1

                #Se estiver na última linha, o tamanho da sequência atual deverá ser armazenado
                if l == linhas-1:
                    comprimentos[seq] += 1

            #Caso seja 0, armazeno a sequência encontrada até agora e depois zero seu valor novamente
            else:
                comprimentos[seq] += 1
                seq = 0

            #OBS: Embora sequências de tamanho 0 também sejam armazenadas (pela lógica do código), isso não irá interferir no resultado final

    #Computar os resultados
    resultado = 0

    #Para cada tamanho maior ou igual a 0, somo em resultado a quantidade de sequências desse tamanho
    for index in range(C, linhas+1):
        resultado += comprimentos[index]

    #Retorno o número correto de sequências maiores ou iguais a C
    return resultado

#Os comandos serão executados caso o arquivo seja executado como script
if __name__ == "__main__":

    #Como são vários parâmetros por linha, realizo a leitura como uma string
    var = input()

    #Crio uma lista com os parâmetros
    var = var.split()

    #Variáveis serão os itens da lista convertidos para int
    P = int(var[0])
    N = int(var[1])
    C = int(var[2])

    #Criação da matriz
    mtx =[]

    #Leitura da matriz 
    for i in range(N):

        #Leio uma linha inteira da matriz
        lst = input()

        #Crio lista com os valores
        lst = lst.split()

        #Lista que irá para a matriz
        lista = []
        
        #Percorro a lista lida e adiciono seus valores convertidos para a lista que será adicionada à matriz
        for item in lst:
            lista.append(int(item))

        #Matriz recebe uma linha inteira
        mtx.append(lista)

    #Chamo minha função de análise
    resp = analise(mtx, C)

    #Imprimir resposta
    print(resp)
    
