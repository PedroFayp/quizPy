print("Bem-vindo ao meu quiz")

playing = input("Você quer jogar? ")

if playing != "sim":
    quit()

print("Ok! Vamos jogar :)")

time.sleep(1.5)

print("ATENÇÃO! Responda em português e utilize acentos")

time.sleep(3)

print("primeira pergunta")
time.sleep(2)

answer = input("O que Significa CPU? ")
if answer == "unidade central de processamento":
    print("Correto!")
else:
    print("Incorreto")

answer = input("O que Significa GPU? ")
if answer == "unidade de processamento de gráficos":
    print("Correto!")
else:
    print("Incorreto")

answer = input("O que Significa RAM? ")
if answer == "memória de acesso aleatório":
    print("Correto!")
else:
    print("Incorreto")

answer = input("")
if answer == "":
    print("Correto!")
else:
    print("Incorreto")