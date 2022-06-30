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
class Battleship:
    def __init__(self,controller,size,location):
        self.controller=controller
        self.size = size
        self.location = location
        self.sunk = False
        if self.controller == "player":
          locations=self.location.split()
          i=0
          for counter in locations:
              locations[i]=int(locations[i])
              i=i+1
          self.location=[]
          for counter in range(0,self.size*2,+2):
              self.location.append([locations[counter],locations[counter+1]])

    def hit(self,fired_position):
        if fired_position in self.location:
            self.location.remove(fired_position)
            if self.location == []:
              self.sunk = True
            print(f"Hit at {fired_position}")
            return True
        else:
            return False   
def ai_mode1():
  global hit_crd
  global c_fire
  global computer_fired
  global ai_attempts
  global c_grid
  global second_hit
  global technique_to_hit
  
  c_fire=[hit_crd[0],hit_crd[1]+1]
  if c_fire not in c_grid:
    ai_attempts=2
    ai_mode2()
  else:  
    print(f"Computer fired at {c_fire}")
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    if player_ship1.hit(c_fire):
      second_hit=True
      technique_to_hit=1
    elif player_ship2.hit(c_fire):
      second_hit=True
      technique_to_hit=1
    elif player_ship3.hit(c_fire):
      second_hit=True
      technique_to_hit=1
    elif player_ship4.hit(c_fire):
      second_hit=True
      technique_to_hit=1
    elif player_ship5.hit(c_fire):
     second_hit=True
    technique_to_hit=1
def ai_mode2():
  global hit_crd
  global c_fire
  global computer_fired
  global ai_attempts
  global c_grid
  global second_hit
  global technique_to_hit
  c_fire=[hit_crd[0],hit_crd[1]-1]
  if c_fire not in c_grid:
    ai_attempts=3
    ai_mode3()
  else:  
    print(f"Computer fired at {c_fire}")
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    if player_ship1.hit(c_fire):
      second_hit=True
      technique_to_hit=2
    elif player_ship2.hit(c_fire):
      second_hit=True
      technique_to_hit=2
    elif player_ship3.hit(c_fire):
      second_hit=True
      technique_to_hit=2
    elif player_ship4.hit(c_fire):
      second_hit=True
      technique_to_hit=2
    elif player_ship5.hit(c_fire):
     second_hit=True
     technique_to_hit=2
def ai_mode3():
  global hit_crd
  global c_fire
  global computer_fired
  global ai_attempts
  global c_grid
  global second_hit
  global technique_to_hit
  c_fire=[hit_crd[0]+1,hit_crd[1]]
  if c_fire not in c_grid:
    ai_attempts=4
    ai_mode4()
  else:  
    print(f"Computer fired at {c_fire}")
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    if player_ship1.hit(c_fire):
      second_hit=True
      technique_to_hit=3
    elif player_ship2.hit(c_fire):
      second_hit=True
      technique_to_hit=3
    elif player_ship3.hit(c_fire):
      second_hit=True
      technique_to_hit=3
    elif player_ship4.hit(c_fire):
      second_hit=True
      technique_to_hit=3
    elif player_ship5.hit(c_fire):
     second_hit=True
     technique_to_hit=3
def ai_mode4():
  global hit_crd
  global c_fire
  global computer_fired
  global ai_attempts
  global c_grid
  global second_hit
  global technique_to_hit
  c_fire=[hit_crd[0]-1,hit_crd[1]]
  if c_fire not in c_grid:
    ai_attempts=0
    c_fire=random.choice(c_grid)
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    print(f"Computer fires at {c_fire}")
  else:  
    print(f"Computer fired at {c_fire}")
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    if player_ship1.hit(c_fire):
      second_hit=True
      technique_to_hit=4
    elif player_ship2.hit(c_fire):
      second_hit=True
      technique_to_hit=4
    elif player_ship3.hit(c_fire):
      second_hit=True
      technique_to_hit=4
    elif player_ship4.hit(c_fire):
      second_hit=True
      technique_to_hit=4
    elif player_ship5.hit(c_fire):
     second_hit=True
     technique_to_hit=4
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
for xx in range(1, 11):
  for yy in range(1, 9):
   combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
for yy in range(1,11):
  for xx in range(1,9):
   combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])
for xx in range(1, 11):
  for yy in range(1, 7):
    combi5.append([[xx, yy], [xx, yy + 1], [xx, yy + 2], [xx, yy + 3],[xx, yy + 4]])
for yy in range(1, 11):
  for xx in range(1, 7):
    combi5.append([[xx, yy], [xx + 1, yy], [xx + 2, yy], [xx + 3, yy],[xx + 4, yy]])
playerCorrect = True
c_grid=grid    
ship_creation=True
playerCorrect=True
while ship_creation:
  computer_ship1=Battleship("computer",3,random.choice(combi3))
  computer_ship2=Battleship("computer",3,random.choice(combi3))
  computer_ship3=Battleship("computer",3,random.choice(combi3))
  computer_ship4=Battleship("computer",3,random.choice(combi3))
  computer_ship5=Battleship("computer",5,random.choice(combi5))
  c_Choices=[ computer_ship1.location, computer_ship2.location, computer_ship3.location, computer_ship4.location, computer_ship5.location]
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
          player_ship1=Battleship("player",3,"10 1 10 2 10 3")#input("Enter the three coordinates of your first ship seperated by a space: \n"))
          player_ship2=Battleship("player",3,"2 1 2 2 2 3")#input("Enter the three coordinates of your second ship seperated by a space: \n"))
          player_ship3=Battleship("player",3,"3 1 3 2 3 3")#input("Enter the three coordinates of your third ship seperated by a space: \n"))
          player_ship4=Battleship("player",3,"4 1 4 2 4 3")#input("Enter the three coordinates of your fourth ship seperated by a space: \n"))
          player_ship5=Battleship("player",5,"5 1 5 2 5 3 5 4 5 5")#input("Enter the five coordinates of your fifth ship seperated by a space: \n"))
          p_Choices=[player_ship1.location,player_ship2.location,player_ship3.location,player_ship4.location,player_ship5.location]
          current_locations=[]
          if player_ship1.location in combi3:
            for location in player_ship1.location:
              current_locations.append(location)
            i=i+1  
            if player_ship2.location in combi3:
              for location in player_ship2.location:
                if location in current_locations:
                  i=-10
                  print("Duplicate location")
                  break
              for location in player_ship2.location:
                current_locations.append(location)
              i=i+1
              if player_ship3.location in combi3:
                for location in player_ship3.location:
                  if location in current_locations:
                    i=-10
                    print("Duplicate location")
                    break
                for location in player_ship3.location:
                  current_locations.append(location)
                i=i+1
                if player_ship4.location in combi3:
                  for location in player_ship4.location:
                    if location in current_locations:
                      i=-10
                      print("Duplicate location")
                      break
                  i=i+1
                  if player_ship5.location in combi5:
                    for location in  player_ship5.location:
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
player_ships=5
computer_ships=5 
second_hit=False
technique_to_hit=0
print(c_Choices) 
ai_attempts=0
computer_fleet=[computer_ship1.sunk, computer_ship2.sunk, computer_ship3.sunk, computer_ship4.sunk, computer_ship5.sunk]
player_fleet=[player_ship1.sunk,player_ship2.sunk,player_ship3.sunk,player_ship4.sunk,player_ship5.sunk]
playing=True
ai_mode=False 
number_of_shots=0
hit_crd=[]
while playing:
  ii=ii+1
  print("Round",ii)
  print(f"You have {player_ships} ships left")
  print(f"Computer has {computer_ships} ships left")
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
        elif crd == "4":
          print(f"You have hit {hits} times and missed {miss} times")    
        else:
          break
      crd=crd.split()
      crd=[int(crd[0]),int(crd[1])]
      player_fired.append(crd)
      break
    except:
      print("Mistakes in coordinates place again")
  if computer_ship1.hit(crd):
    hits +=1
  elif computer_ship2.hit(crd):
    hits +=1
  elif computer_ship3.hit(crd):
    hits +=1
  elif computer_ship4.hit(crd):
    hits +=1
  elif computer_ship5.hit(crd):
    hits +=1
  else:
    miss=miss+1
    print("Miss")
  computer_fleet=[computer_ship1.sunk, computer_ship2.sunk, computer_ship3.sunk, computer_ship4.sunk, computer_ship5.sunk]  
  for counter in c_Choices:
    if not counter:
      c_Choices.remove(counter)
  computer_ships=5  
  for counter in computer_fleet:
    if counter:
      computer_ships-=1
  if  computer_ships == 0:    
    print(f"Congrats you win, it took you {ii} Attempts")
    playing=False
    break
  if ai_mode == True:
    if current_player_ships > player_ships:
      number_of_shots=0
      ai_mode=False
    else:  
      if second_hit ==False:  
        if ai_attempts==1:
          ai_mode1()
        elif ai_attempts==2:
          ai_mode2()
        elif ai_attempts==3:
          ai_mode3()
        elif ai_attempts==4:
          ai_mode4() 
      else:
        pass    
  else:  
    hit_crd=[]
    c_fire=[2,1]#random.choice(c_grid)
    computer_fired.append(c_fire)
    c_grid.remove(c_fire)
    print(f"Computer fires at {c_fire}")
    if player_ship1.hit(c_fire):
      current_player_ships=player_ships
      ai_mode=True
      ai_attempts=0
      hit_crd=c_fire
    elif player_ship2.hit(c_fire):
      current_player_ships=player_ships
      ai_mode=True
      ai_attempts=0
      hit_crd=c_fire
    elif player_ship3.hit(c_fire):
      current_player_ships=player_ships
      ai_mode=True
      ai_attempts=0
      hit_crd=c_fire
    elif player_ship4.hit(c_fire):
      current_player_ships=player_ships
      ai_mode=True
      ai_attempts=0
      hit_crd=c_fire
    elif player_ship5.hit(c_fire):
      current_player_ships=player_ships
      ai_mode=True
      ai_attempts=0
      hit_crd=c_fire
    else:
      print("Computer misses")
  player_fleet=[player_ship1.sunk,player_ship2.sunk,player_ship3.sunk,player_ship4.sunk,player_ship5.sunk]  
  player_ships=5   
  for counter in player_fleet:
    if counter:
      player_ships-=1
  if  player_ships == 0: 
    print(f"Computer wins after {ii} attempts")
    playing=False       
  ai_attempts+=1   