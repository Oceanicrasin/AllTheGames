from multiprocessing.reduction import duplicate
import random
xs=[1,2,3,4,5,6,7,8,9,10]
ys=[1,2,3,4,5,6,7,8,9,10]
combi3=[]
combi5=[]
grid=[]
player_fired=[]
computer_fired=[]
hits = 0
miss = 0
i=0
ii=0
#grid formation
for x in xs:
  for y in ys:
    grid.append([x,y])
def inlist(my_list, item):
  i=0
  for counter in my_list:
    if item in counter:
      i=i+1
      return True
  return False    
for xx in range(1, 9):
  for yy in range(1, 9):
   combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
   combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])
combi3.append([[xx,8],[10,9],[10,10]])
combi3.append([[9,8],[9,9],[9,10]])
for xx in range(1, 7):
  for yy in range(1, 7):
    combi5.append([[xx, yy], [xx, yy + 1], [xx, yy + 2], [xx, yy + 3],[xx, yy + 4]])
    combi5.append([[xx, yy], [xx + 1, yy], [xx + 2, yy], [xx + 3, yy],[xx + 4, yy]])
for xx in range(7,11):
  combi5.append([[xx,3],[xx,4],[xx,5],[xx,6],[xx,7]])
  combi5.append([[xx,4],[xx,5],[xx,6],[xx,7],[xx,8]])
  combi5.append([[xx,5],[xx,6],[xx,7],[xx,8],[xx,9]])
  combi5.append([[xx,6],[xx,7],[xx,8],[xx,9],[xx,10]])
def ships(whichone,index):
    whichone=whichone.split()
    i=0
    for counter in whichone:
      whichone[i]=int(whichone[i])
      i=i+1
    if index == "three":
      l1=[whichone[0],whichone[1]]
      l2=[whichone[2],whichone[3]]
      l3=[whichone[4],whichone[5]]
      whichone.clear()
      whichone.append(l1)  
      whichone.append(l2)
      whichone.append(l3)
    elif index == "five":
      l1=[whichone[0],whichone[1]]
      l2=[whichone[2],whichone[3]]
      l3=[whichone[4],whichone[5]]
      l4=[whichone[6],whichone[7]]
      l5=[whichone[8],whichone[9]]
      whichone.clear()
      whichone.append(l1)  
      whichone.append(l2)
      whichone.append(l3)
      whichone.append(l4)
      whichone.append(l5)
    return whichone  
playerCorrect = True
c_grid=grid    
ship_creation=True
playerCorrect=True
while ship_creation:
  choice1=random.choice(combi3)
  choice2=random.choice(combi3)
  choice3=random.choice(combi3)
  choice4=random.choice(combi3)
  choice5=random.choice(combi5)
  c_Choices=[ choice1, choice2, choice3, choice4, choice5]
  current_locations=[]
  duplicated=0
  for counter in c_Choices:
    for counter1 in counter:
      current_locations.append(counter1)
  for location1 in current_locations:
    for location2 in current_locations:
      if location1 == location2:
        duplicated=duplicated+1
  if duplicated ==17:
    ship_creation = False      
    while True:
      try:
        while playerCorrect:
          pChoice1=input("Enter the three coordinates of your first ship seperated by a space: \n")
          pChoice2=input("Enter the three coordinates of your second ship seperated by a space: \n")
          pChoice3=input("Enter the three coordinates of your third ship seperated by a space: \n")
          pChoice4=input("Enter the three coordinates of your fourth ship seperated by a space: \n")
          pChoice5=input("Enter the five coordinates of your fifth ship seperated by a space: \n")
          pChoice1=ships(pChoice1,"three")
          pChoice2=ships(pChoice2,"three")
          pChoice3=ships(pChoice3,"three")
          pChoice4=ships(pChoice4,"three")
          pChoice5=ships(pChoice5,"five")
          p_Choices=[pChoice1,pChoice2,pChoice3,pChoice4,pChoice5]
          current_locations=[]
          if pChoice1 in combi3:
            for location in pChoice1:
              current_locations.append(location)
            i=i+1  
            if pChoice2 in combi3:
              for location in pChoice2:
                if location in current_locations:
                  i=-10
                  print("Duplicate location")
                  break
              for location in pChoice2:
                current_locations.append(location)
              i=i+1
              if pChoice3 in combi3:
                for location in pChoice3:
                  if location in current_locations:
                    i=-10
                    print("Duplicate location")
                    break
                for location in pChoice3:
                  current_locations.append(location)
                i=i+1
                if pChoice4 in combi3:
                  for location in pChoice4:
                    if location in current_locations:
                      i=-10
                      print("Duplicate location")
                      break
                  i=i+1
                  if pChoice5 in combi5:
                    for location in pChoice5:
                      if location in current_locations:
                        i=-10
                        print("Duplicate location")
                        break
                    i=i+1
            if i>4: 
              playerCorrect=False
            else:
              print("Mistakes in coordinates place again")
        break
      except:
        print("Mistakes in coordinates place again. It errored")
i=0        
playing=True
while playing:
  ii=ii+1
  print("Round",ii)
  print("Computer has",len(c_Choices),"ships left")
  while True:
    try:
      while True:
        crd=input("Enter coordinate to bomb seperated by a space: ")
        if crd == "1":
          print("All the places you have bombed")
          for counter in player_fired:
            print(counter)
        elif crd == "2":
          print("All the places the computer has bombed")
          for counter in computer_fired:
            print(counter)
        elif crd == "3":
          print("Locations of your remaining ships")
          for counter in p_Choices:
            print(counter)
        else:
          break
      crd=ships(crd,"nein")
      player_fired.append(crd)
      break
    except:
      print("Mistakes in coordinates place again")
  #grid.remove(crd)
  if inlist(c_Choices,crd):
    print("HIT at ",crd)
    hits=hits+1
    h=0
    i=0
    for counter in c_Choices:
      if crd in counter:
        c_Choices[h].remove(crd)
        break
      else:
        h+=1
  else:
    print("miss")
    miss=miss+1
  print(f"You have hit {hits} times and missed {miss} times")
  for counter in c_Choices:
    if not counter:
      c_Choices.remove(counter)
  if not c_Choices:    
    print("Congrats you win, it took you ",ii,"Attempts")
    playing=False
    break
  c_fire=random.choice(c_grid)
  computer_fired.append(c_fire)
  c_grid.remove(c_fire)
  print(f"Computer fires at {c_fire}")
  if inlist(p_Choices,c_fire):
    print("Hit")
    o=0
    for counter in p_Choices:
      if c_fire in counter:
        p_Choices[o].remove(c_fire)
      else:
        o=o+1
  else:
    print("Computer misses")
  if not p_Choices:
    print(f"Computer wins after {ii} attempts")
    playing=False        