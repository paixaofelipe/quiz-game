print("Seja bem-vindo ao nosso joguinho!")
playing = input("Pronto para jogar? [sim ou não?] ")
print(playing)

if playing != "sim": #Pergunta se a pessoa quer jogar
    quit()

print("Então bora lá!") 

pergunta = input("Qual a cor do cavalo branco de napoleão? ")
if pergunta == "branco":
    print("Boa garoto(a)!")
else:
    print("Bzzzz! Errado :(")

pergunta = input("Quanto é 2+2? ")
if pergunta == "4" or "quatro":
    print("Boa garoto(a)! Será que vai acertar a próxima?")
else:
    print("Bzzzz! Errado :(")

pergunta = input("Qual o nome da capital do Brasil? ")
if pergunta == "Brasília":
    print("Boa garoto(a)! Tá avançando...")
else:
    print("Bzzzz! Errado :(")

pergunta = input("Complete: Deus ajuda quem...? ")
if pergunta == "cedo madruga":
    print("Você é demais! Parabéns!")
    print("Você você ganhou um Parabéns!")
else:
    print("Bzzzz! Errado :(")