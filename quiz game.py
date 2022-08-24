print("Seja bem-vindo ao nosso joguinho!")
playing = input("Pronto para jogar? [sim ou não?] ")
print(playing)

if playing != "sim":
    quit()

print("Então bora lá!") 

pergunta1 = input("Qual a cor do cavalo branco de napoleão? ")
if pergunta1 == "branco":
    print("Boa garoto(a)!")
else:
    print("Bzzzz! Errado :(")