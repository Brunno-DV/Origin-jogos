import random

def jogar():
 
  imprime_mensagem_abertura()
  palavra_secreta = carrega_palavra_secreta()

  letras_acertadas = ["_" for letra in palavra_secreta] #Carrega palavra secreta
  print(letras_acertadas)

  enforcou = False
  acertou = False
  erros = 0

  while (not enforcou and not acertou):
    
    chute = pede_chute()

    if (chute in palavra_secreta):
      marca_chute_correto(chute, letras_acertadas, palavra_secreta)
    else:
      erros += 1
    
    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
  
  if (acertou):
    imprime_mensagem_vencedor()
  else:
    imprime_mensagem_perdedor()

  print("Fim do jogo")

def imprime_mensagem_abertura():
  print("************************************")
  print("Olá, bem vindo ao jogo de forca!")
  print("************************************")

def carrega_palavra_secreta():
  arquivo = open(r"C:\Users\engenharia1\OneDrive - GIMI\Área de Trabalho\Alura\Python\Jogos\Advinhacao\palavras.txt", "r")
  palavras = []

  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

  arquivo.close()

  numero = random.randrange(0, len(palavras))

  palavra_secreta = palavras[numero].upper()

  return palavra_secreta

def pede_chute():
  chute = input("Qual a letra? ")
  chute = chute.strip().upper()
  return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
  index = 0
  for letra in palavra_secreta:
    if(chute == letra):
      letras_acertadas[index] = letra
    index += 1

def imprime_mensagem_vencedor():
  print("Você ganhou!")

def imprime_mensagem_perdedor():
  print("Você perdeu")

if(__name__ == "__main__"):
  jogar()