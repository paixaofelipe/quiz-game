print("Seja bem-vindo ao nosso joguinho!")
playing = input("Pronto para jogar? [sim ou não?] ")
print(playing)

if playing.lower() != "sim": #Pergunta se a pessoa quer jogar
    quit()

print("Então bora lá!")

pontos = 0

pergunta = input("Qual a cor do cavalo branco de napoleão? ") #Primeira Pergunta
if pergunta.lower() == "branco":
    print("Boa garoto(a)!")
    pontos += 1 #Ganha +1 ponto
else:
    print("Bzzzz! Errado :(")

pergunta = input("Quanto é 2+2? ") #Segunda Pergunta
if pergunta.lower() == "4" or pergunta.lower() == "quatro":
    print("Boa garoto(a)! Será que vai acertar a próxima?")
    pontos += 1
else:
    print("Bzzzz! Errado :(")

pergunta = input("Qual o nome da capital do Brasil? (Lembre que é nome de cidade) ") #Terceira Pergunta
if pergunta == "Brasília":
    print("Boa garoto(a)! Tá avançando...")
    pontos += 1
else:
    print("Bzzzz! Errado :(")

pergunta = input("Complete: Deus ajuda quem...? ") #Quarta Pergunta
if pergunta.lower() == "cedo madruga":
    pontos += 1
    print("Você é demais! Parabéns!")
    print("Você ganhou um Parabéns!")
else:
    print("Bzzzz! Errado :(")

print("Você conseguiu acertar " + str(pontos) + " perguntas!")
print("Isso são " + str((pontos / 4) * 100) + "% das perguntas!")