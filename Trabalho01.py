#Victor Gabriel Castão da Cruz

#Lendo valor
N = int(input())

#Calculando dias
dias = int(N/86400)
N = N % 86400

#Calculando horas
horas = int(N/3600)
N = N % 3600

#Calculando minutos
minutos = int(N/60)
N = N % 60

#Calculando segundos
segundos = N

#Imprimindo resposta
print(dias, "dia(s),", horas, "hora(s),", minutos, "minuto(s) e", segundos, "segundo(s).")
