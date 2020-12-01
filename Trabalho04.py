#Ler quantidade de preços a serem fornecidos
dias = int(input())

#Variáveis e lista necessária para armazenar preços
preco_diario = 0
contador = 0
precos = []

#Função que irá verificar se o lucro analisado é mais vantajoso
def verificar_lucro(dc, mdc, dv, mdv, l, ml):
    #Caso inicial
    if dc == 0 and dv == 0:
        return True
    #Lucro maior
    elif l > ml:
        return True
    #Desempate por dia de compra
    elif l == ml and dc < mdc:
        return True
    #Desempate por dia de venda
    elif l == ml and dc == mdc and dv < mdv:
        return True
    #Caso o lucro não seja vantajoso
    else:
        return False

#Leitura do preço das ações
while contador < dias:
    preco_diario = float(input())
    precos.append(preco_diario)
    contador += 1

#Ler intervalo das comparações
intervalo_maximo = int(input())

#Ler dinheiro disponível
dinheiro_disponivel = float(input())

#Variáveis calculadas a cada iteração
dia_compra = 0
dia_venda = 0
quantidade_acoes = 0
lucro = 0.0


#Variáveis definitivas (guarda a melhor opção até aquele momento)
melhor_dia_compra = 0
melhor_dia_venda = 0
melhor_quantidade_acoes = 0
melhor_lucro = 0.0

#Laços aninhados que verificarão as possibilidades de compra e venda
#Percorrer toda a lista
while dia_compra < len(precos):
    #Caso inicial (vender no mesmo dia)
    dia_venda = dia_compra
    
    #Percorrer até o intervalo máximo entre o dia de compra e o dia de venda
    while (dia_venda <= dia_compra + intervalo_maximo) and dia_venda < len(precos):

        #Ações devem ser compradas em partes inteiras
        quantidade_acoes = int(dinheiro_disponivel // precos[dia_compra])

        #Lucro calculado (considerando apenas o dinheiro gasto para compra)
        lucro = (precos[dia_venda] - precos[dia_compra]) * quantidade_acoes

        #Verificar se essa é a melhor opção
        if verificar_lucro(dia_compra, melhor_dia_compra, dia_venda, melhor_dia_venda, lucro, melhor_lucro):

            #Fazer atualizações necessárias
            melhor_dia_compra = dia_compra
            melhor_dia_venda = dia_venda
            melhor_quantidade_acoes = quantidade_acoes
            melhor_lucro = lucro

        #Incremento
        dia_venda += 1

    #Incremento
    dia_compra += 1

#Imprimindo respostas

#Acrescentando 1 devido a contagem se iniciar em 0
print("Dia da compra:", melhor_dia_compra+1)
print("Valor de compra: R$", format(precos[melhor_dia_compra], '.2f'))

#Acrescentando 1 devido a contagem se iniciar em 0
print("Dia da venda:", melhor_dia_venda+1)
print("Valor de venda: R$", format(precos[melhor_dia_venda], '.2f'))
print("Quantidade de acoes compradas:", melhor_quantidade_acoes)
print("Lucro: R$", format(melhor_lucro, '.2f'))
