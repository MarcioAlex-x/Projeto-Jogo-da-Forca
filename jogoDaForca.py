palavra = "Python".upper()

letra = input("Digite uma letra").upper()

if letra in palavra:
    print("Você acertou a letra")
else:
    print("Você errou")