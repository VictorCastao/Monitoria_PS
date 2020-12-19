#Victor Gabriel Castão da Cruz
#11911ECP004

#Análise módulo / script
if __name__ == "__main__":

    #Analisar palavras na horizontal
    def busca_horizontal(matriz, linhas, colunas, palavra):
        resultado = 0
        letras = len(palavra)
	
	#Percorrer linhas
        for i in range(linhas):
	    
	    #Comparar até que a posição de início da comparação torne-se inválida (evita chegar ao fim da matriz sem necessidade)
            for j in range(colunas-letras+1):

                comparado = 0

		#Comparar letra a letra
                for k in range(letras):

		    #Colocar .lower() para casos onde a matriz já foi percorrida e alterada para maiúsculo
                    if matriz[i][j+k] == "*" or matriz[i][j+k].lower() == palavra[k]:

                        comparado += 1

		#Palavra encontrada
                if comparado == letras:

                    resultado += 1

		    #Ao encontrar a palavra, aplicar .upper() em sua posição	
                    for l in range(j, j+letras):

                        matriz[i][l] = matriz[i][l].upper()        

	#Retorna ocorrências na horizontal
        return resultado

    #Processo semelhante ao caso da horizontal, entretanto, agora as linhas estão no laço interno e as colunas no externo
    def busca_vertical(matriz, linhas, colunas, palavra):

        resultado = 0
        letras = len(palavra)

        for j in range(colunas):

            for i in range(linhas-letras+1):

                comparado = 0

                for k in range(letras):

                    if matriz[i+k][j] == "*" or matriz[i+k][j].lower() == palavra[k]:

                        comparado += 1

                if comparado == letras:

                    resultado += 1

                    for l in range(i, i+letras):
                        matriz[l][j] = matriz[l][j].upper()        

        return resultado

    #Busca na diagonal (direção inferior direita)
    def busca_inf_dir(matriz, linhas, colunas, palavra):

        resultado = 0
        letras = len(palavra)

	#Percorrer linhas até que a posição da linha seja inviável (letras disponíveis < tamanho da palavra)
        for i in range(linhas-letras+1):

	    #Percorrer colunas até a última posição viável
            for j in range(colunas-letras+1):

                comparado = 0

                for k in range(letras):

                    #Diferente das outras, tanto linha quanto a coluna se movimentam, ambas na mesma quantidade (sentido inferior direito)
                    if matriz[i+k][j+k] == "*" or matriz[i+k][j+k].lower() == palavra[k]:

                        comparado += 1

                if comparado == letras:

                    resultado += 1

                    for l in range(letras):

                        matriz[i+l][j+l] = matriz[i+l][j+l].upper()        

        return resultado

    #Busca na outra diagonal, semelhante ao caso anterior
    def busca_sup_dir(matriz, linhas, colunas, palavra):

        resultado = 0
        letras = len(palavra)

	#Devido ao sentido, as linhas são analisadas inicialmente da posição mais acima possível, indo até o final da matriz
        for i in range(letras-1, linhas):

	    #Colunas percorridas no mesmo sentido dos casos anteriores (esquerda para direita)
            for j in range(colunas-letras+1):

                comparado = 0

                for k in range(letras):

		    #Linhas e colunas são movimentadas, porém, devido ao sentido superior direito, a linha diminui, enquanto a coluna aumenta
                    if matriz[i-k][j+k] == "*" or matriz[i-k][j+k].lower() == palavra[k]:

                        comparado += 1

                if comparado == letras:

                    resultado += 1

                    for l in range(letras):

                        matriz[i-l][j+l] = matriz[i-l][j+l].upper()        

        return resultado
                
    #Desenvolvimento além das funções

    #Leitura linhas e colunas        
    linhas = int(input())
    colunas = int(input())

    #Inicializando matriz
    matriz = []

    #Leitura matriz
    for i in range(linhas):

        leitura = input()
        leitura = leitura.split()
        matriz.append(leitura)


    #Definir quantidade de buscas
    buscas = int(input())

    #Armazenamento das palavras a serem buscadas
    lista_resp = []

    #Para cada palavra, executar as funções de busca e armazenar um par contendo palavra e número de ocorrências em uma lista
    for p in range(buscas):

        palavra = input()

	#Calculando ocorrências totais
        oc = 0
        oc += busca_horizontal(matriz, linhas, colunas, palavra)
        oc += busca_vertical(matriz, linhas, colunas, palavra)
        oc += busca_inf_dir(matriz, linhas, colunas, palavra)
        oc += busca_sup_dir(matriz, linhas, colunas, palavra)

	#Armazenar resultado 
        lst = [palavra, oc]
        lista_resp.append(lst)

    #Imprimir resultado total
    print('-'*40)
    print("Lista de Palavras")
    print('-'*40)

    for valores in lista_resp:

        print("Palavra:", valores[0])
        print("Ocorrencias:", valores[1])
        print('-' * 40)

    for l in range(linhas):

        for c in range(colunas):

            print(matriz[l][c], end='')

            if c < colunas-1:

                print(" ", end='')

        print()

#Fim do código
