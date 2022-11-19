#Variáveis
vida = 10
moeda = 0
madeira = 0
pedra = 0
ferro = 0
espada = 6
picareta = 8
machado = 8

#Repetição
while vida > 0:
  
  #Comandos para jogar
  print (" ")
  print ("Comandos de jogo:")
  print (" ")
  print ("!MatarGoblin -> -3 espada -2 vida +16 Moeda")
  print ("!MatarGnomo -> -1 espada -1 vida +6 moeda")
  print ("!CortarArvore -> +10 madeira")
  print ("!MinerarPedra -> +5 pedra -1 picareta")
  print ("!MinerarFerro +5 ferro -1 picareta")
  print ("!Comprar2Vida -> -5 moeda +2 vida")
  print ("!RepararPicareta -> -10 moeda + 2 picareta")
  print ("!RepararMachado -> -10 moeda +2 machado")
  print ("!RepararEspada -> -10 moeda +2 machado")
  print ("!VenderMadeira -> -1 madeira +4 moeda")
  print ("!VenderPedra -> -1 pedra +6 moeda ")
  print ("!VenderFerro -> -1 ferro +9 moeda")
  print (" ")
  print ("Você tem:")
  print (f"Vida: {vida}")
  print (f"Moeda: {moeda}")
  print (f"Madeira: {madeira}")
  print (f"Pedra {pedra}")
  print (f"Ferro {ferro} ")
  print (f"Picareta {picareta}")
  print (f"Machado {machado}")
  print (f"Espada {espada}")
  print (" ")
      
  #Programação
  entrada = input()
  if entrada == "!MatarGoblin":
    vida -= 2
    moeda += 16
    espada -= 3
    print (" ")
    print ("Você perdeu 2 vidas e ganhou 16 moedas")
    print (f"Você tem {vida} vida(s) e {moeda} moeda(s) agora")
    print (" ")
    
  if entrada == "!MatarGnomo":
    vida -= 1
    moeda += 6
    espada -= 1
    print (" ")
    print ("Você perdeu 1 vida e ganhou 6 moedas")
    print (f"Você tem {vida} vida(s) e {moeda} moeda(s)")
    print (" ")
    
  if entrada == "!CortarArvore":
    madeira += 10
    machado -= 1
    print (" ")
    print ("Você ganhou 10 madeiras")
    print (f"Você tem {madeira} madeira(s)")
    print (" ")

  if entrada == "!MinerarPedra":
    pedra += 10
    picareta -= 1
    print (" ")
    print ("Você ganhou 10 pedras")
    print (f"Você tem {pedra} pedra(s)")
    print (" ")

  if entrada == "!MinerarFerro":
    ferro += 5
    picareta -= 2
    print (" ")
    print ("Você ganhou 5 ferros")
    print (f"Você tem {ferro} ferro(s)")
    print (" ")

  if entrada == "!Comprar2Vida":
    vida += 2
    moeda -= 5
    print (" ")
    print ("Você ganhou 2 vidas")
    print (f"Você tem {vida} vida(s)")

  if entrada == "!RepararPicareta":
    moeda -= 10
    picareta += 2
    print (" ")
    print ("Você ganhou 2 picaretas")
    print (f"Você tem {picareta} picareta(s)")
    print (" ")

  if entrada == "!RepararMachado":
    moeda -= 10
    machado += 2
    print (" ")
    print ("Você ganhou 2 machados")
    print (f"Você tem {machado} machado(s)")
    print (" ")

  if entrada == "!RepararEspada":
    moeda -= 10
    espada += 2
    print (" ")
    print ("Você ganhou 2 espadas")
    print (f"Você tem {espada} espada(s) ")
    print (" ")

  if entrada == "!VenderMadeira":
    moeda += 4
    madeira -= 1
    print (" ")
    print ("Você ganhou 4 moedas")
    print (f"Você tem {madeira} madeira(s) ")
    print (" ")

  if entrada == "!VenderPedra":
    moeda += 6
    pedra -= 1
    print (" ")
    print ("Você ganhou 6 moedas")
    print (f"Você tem {pedra} pedra(s) ")
    print (" ")

  if entrada == "!VenderFerro":
    moeda += 9
    ferro -= 1
    print (" ")
    print ("Você ganhou 9 moedas")
    print (f"Você tem {pedra} pedra(s) ")
    print (" ")