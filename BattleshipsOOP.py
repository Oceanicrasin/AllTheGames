import random
player_fired=[]
computer_fired=[]
hits = 0
miss = 0
i=0
ii=0
class Ship:
    def __init__(self,controller,size,location):
        self.size=size
        self.controller=controller
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
class Destroyer(Ship):
    combi2=[]
    for xx in range(1, 11):
        for yy in range(1, 10):
         combi2.append([[xx, yy], [xx, yy + 1]])
    for yy in range(1,11):
        for xx in range(1,10):
            combi2.append([[xx, yy], [xx + 1, yy]])   
    def __init__(self, controller, location):
        super().__init__(controller, 2, location) 

class Submarine(Ship):
    combi3=[]
    for xx in range(1, 11):
        for yy in range(1, 9):
            combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
    for yy in range(1,11):
      for xx in range(1,9):
        combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])
    def __init__(self, controller, location):
        super().__init__(controller, 3, location) 

class Cruiser(Ship):
    combi3=[]
    for xx in range(1, 11):
        for yy in range(1, 9):
            combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
    for yy in range(1,11):
      for xx in range(1,9):
        combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])
    def __init__(self, controller, location):
        super().__init__(controller, 3, location)       


class Battleship(Ship):
    combi4=[]
    for xx in range(1, 11):
        for yy in range(1, 8):
            combi4.append([[xx, yy], [xx, yy + 1], [xx, yy + 2],[xx, yy + 3]])
    for yy in range(1,11):
      for xx in range(1,8):
        combi4.append([[xx, yy], [xx + 1, yy], [xx + 2, yy],[xx + 3, yy]])
    def __init__(self, controller, location):
        super().__init__(controller, 4, location)        

class Carrier(Ship):
    combi5=[]
    for xx in range(1, 11):
        for yy in range(1, 7):
            combi5.append([[xx, yy], [xx, yy + 1], [xx, yy + 2],[xx, yy + 3],[xx, yy + 4]])
    for yy in range(1,11):
      for xx in range(1,7):
        combi5.append([[xx, yy], [xx + 1, yy], [xx + 2, yy],[xx + 3, yy],[xx + 4, yy]])
    def __init__(self, controller, location):
        super().__init__(controller, 4, location)                          



   
class Grid:  # Grid class
    grid_locations=[]  
    for x in range(1,11):
        for y in range(1,11):
            grid_locations.append([x,y])     
   
g=Destroyer("player","1 2 1 3")
print(g.location)            