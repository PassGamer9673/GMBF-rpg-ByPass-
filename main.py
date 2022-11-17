
#Variáveis
vida = 10
moeda = 0
madeira = 0
pedra = 0
ferro = 0

#Repetição
while vida > 0:
  
  #Comandos para jogar
  print (" ")
  print ("Comandos de jogo:")
  print (" ")
  print ("!MatarGoblin -> -2 vida +16 Moeda")
  print ("!MatarGnomo -> -1 vida +6 moeda")
  print ("!CortarArvore -> +10 madeira")
  print ("!MinerarPedra -> +5 pedra")
  print ("!MinerarFerro +5 ferro")
  print ("!Comprar2Vida -> -5 moeda +2 vida")
  print (" ")
  print ("Você tem:")
  print (f"Vida: {vida}")
  print (f"Moeda: {moeda}")
  print (f"Madeira: {madeira}")
  print (f"Pedra {pedra}")
  print (f"Ferro {ferro} ")
  print (" ")
      
  #Programação
  entrada = input()
  if entrada == "!MatarGoblin":
    vida -= 2
    moeda += 16
    print (" ")
    print ("Você perdeu 2 vidas e ganhou 16 moedas")
    print (f"Você tem {vida} vida(s) e {moeda} moeda(s) agora")
    print (" ")
    
  if entrada == "!MatarGnomo":
    vida -= 1
    moeda += 6
    print (" ")
    print ("Você perdeu 1 vida e ganhou 6 moedas")
    print (f"Você tem {vida} vida(s) e {moeda} moeda(s)")
    print (" ")
    
  if entrada == "!CortarArvore":
    madeira += 10
    print (" ")
    print ("Você ganhou 10 madeiras")
    print (f"Você tem {madeira} madeira(s)")
    print (" ")

  if entrada == "!MinerarPedra":
    pedra += 10
    print (" ")
    print ("Você ganhou 10 pedras")
    print (f"Você tem {pedra} pedra(s)")
    print (" ")

  if entrada == "!MinerarFerro":
    ferro += 5
    print (" ")
    print ("Você ganhou 5 ferros")
    print (f"Você tem {ferro} ferro(s)")
    print (" ")

  if entrada == "!Comprar2Vida":
    vida += 2
    moeda -=5
    print (" ")
    print ("Você ganhou 2 viadas")
    print (f"Você tem {vida} vida(s)")