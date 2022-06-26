import random
cards=["1","2","3","4","5","6","7","8","10","11"]
dealer=random.choice(cards)
dealer = [dealer,random.choice(cards)]
print(dealer[0])
player=random.choice(cards)
player = [player,random.choice(cards)]
print(', '.join(player))
pChoice=True
cChoice=True
pTotal=0
cTotal=0
pBust=False
cBust=False
while pChoice==True:
  for counter in player:
    cTotal=cTotal+int(counter)
  choice=input("Do you want to twist or stick: ")
  if choice == "twist":
    player.append(random.choice(cards))
    print(', '.join(player))
    for counter in player:
      pTotal=pTotal+int(counter)
      if pTotal>21:
        print("Player Busts")
        pBust=True
        break
  else:
    pChoice=False       
  if pBust==True:
    break

while cChoice == True and pBust == False:
  for counter in dealer:
    cTotal=cTotal+int(counter)
  option1=random.randint(1,2)
  if option1 == 1 or cTotal<16:
    dealer.append(random.choice(cards))
    for counter in dealer:
      cTotal=cTotal+int(counter)
    if cTotal>21:
      print("Dealer busts")
      cBust=True
      break
  else:
    cChoice=False
if pTotal>15 and pTotal<22 and pBust == False:
  if cTotal>15 and cTotal<22 and cBust == False:
    if cTotal>pTotal:
      print("Dealer wins")
    elif cTotal<pTotal:
      print("Player wins")
    elif cTotal== pTotal:
      print("Draw")
  else:
    print("Player wins")
else:
  print("Dealer wins")

       