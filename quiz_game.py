import time

print("Bem-vindo ao meu quiz")

playing = input("Você quer jogar? ")

if playing.lower() != "sim":
    quit()

print("Ok! Vamos jogar :)")
pontos = 0

time.sleep(1.5)

print("ATENÇÃO! Responda em português e utilize acentos")

time.sleep(3)

print("primeira pergunta")
time.sleep(2)

answer = input("O que Significa CPU? ")
if answer.lower() == "unidade central de processamento":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto")

time.sleep(1.5)

print("Próxima pergunta")

time.sleep(1.5)

answer = input("O que Significa GPU? ")
if answer.lower() == "unidade de processamento de gráficos":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto")

time.sleep(1.5)

print("Próxima pergunta")

time.sleep(1.5)

answer = input("O que Significa RAM? ")
if answer.lower() == "memória de acesso aleatório":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto")

time.sleep(1.5)

print("Última pergunta")

time.sleep(1.5)

answer = input("O que Significa PSU? ")
if answer.lower() == "unidade de fonte de alimentação":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto")

time.sleep(1.5)

print("Contando os acertos...")

time.sleep(1.5)

print("Você acertou " + str(pontos) + " perguntas corretamente")
print("Você teve um aproveitamento de " + str((pontos / 4) * 100) + "%.")

time.sleep(1)

print("Parabéns! Obrigado por jogar")