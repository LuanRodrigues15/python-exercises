import random as rd

forca_stages = [
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

palavras = ["montanha", "cachorro", "estrela", "relógio", "pintura","oceano", "janela", "computador", "floresta", "livro","rio", "guitarra", "cidade", "telefone", "chuva","deserto", "praia", "foguete", "sonho", "carro","jardim", "pássaro", "ponte", "luz", "vento"]
palavra_escolhida = rd.choice(palavras)
nmr_letras = len(palavra_escolhida)

print(f"A palavra escolhida possui {nmr_letras} letras")
print("_" * nmr_letras)

letras_corretas = []
tentativas = 0
vida = nmr_letras + 2
game_over = False


while not game_over:
    resposta = input("Digite a letra para verificar se existe na palavra: ").lower()
    
    tentativas += 1
    print(f"\n\n{tentativas}º tentativa")
    print(f"Você tem {vida} de Vida")
    
    display = ""
    
    for letra in palavra_escolhida:
        if letra == resposta:
            display += letra
            letras_corretas.append(resposta)
        elif letra in letras_corretas:
            display += letra
        else:
            display += "_"        
            
    print(display)
    
    if resposta not in palavra_escolhida:
        vida -= 1
        if vida == 0:
            game_over = True
            print(f"Que pena! Você perdeu... A palavra escolhida era: {palavra_escolhida}")
    
    if "_" not in display:
        game_over = True
        print("Você ganhou!")
     
    if vida > 6:
        print(forca_stages[6])
    else:
        print(forca_stages[vida])