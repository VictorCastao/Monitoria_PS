#Victor Gabriel Castão da Cruz - 11911ECP004

#Inicialização da lista
palavras = []

#Popular lista com as palavras presentes nas frases, formatadas para eliminar pontuações e ficarem com todas as letras minúsculas
def separa_palavras(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(".","")
    string = string.replace(",","")
    string = string.replace(":","")
    string = string.replace(";","")
    string = string.replace("!","")
    string = string.replace("?","")
    x = string.split()
    for p in x:
        palavras.append(p)

#Função que identifica a similaridade da palavra buscada com outra. Essa similaridade pode corresponder a uma ocorrência também
def similar(coringa, elemento):
    resp = False
    indice_coringa = 0
    indice_elemento = 0
    #Altero a primeira letra a ser analisada na palavra
    while indice_elemento <= len(elemento)-len(coringa): #Laço vai até o último caractere possível de iniciar as comparações
        indice_coringa = 0
        comum = 0 #Contador de letras iguais
        #Analiso a sequencia de N caracteres, onde N = len(coringa) 
        while indice_coringa < len(coringa):
            if coringa[indice_coringa] == '*' or coringa[indice_coringa] == elemento[indice_elemento+indice_coringa]:
                comum += 1
            indice_coringa += 1
        if comum == len(coringa):
            #Se em algum momento haver semelhança, já retornar resposta
            return True
        indice_elemento += 1
    return resp

#Ler quantidade de frases
linhas = int(input())

#Ler frases e adicionar palavras na lista
for i in range(linhas):
    texto = input()
    separa_palavras(texto)

#Ler quantidade de consultas
consultas = int(input())

#Para cada consulta, verificar ocorrências e similaridades
for j in range(consultas):
    termo_original = input() #Forma a ser impressa
    termo = termo_original.strip().lower() #Formatação para se adequar às funções
    ocorrencias = 0
    similares = 0
    for k in palavras:
        if similar(termo, k):
            if len(k) == len(termo): #Tamanhos iguais configuram ocorrência
                ocorrencias += 1
            else: #Tamanhos diferentes configuram similaridade
                similares += 1

    #Imprimir respostas
    print("Palavra buscada:", termo_original)
    print("Ocorrencia:", ocorrencias)
    print("Palavras similares:", similares)
