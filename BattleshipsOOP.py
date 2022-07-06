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
    size=2
    validLocation=False
    def __init__(self, controller, location):
        self.location = location
        super().__init__(controller, self.size, self.location)


class Submarine(Ship):
    size=3
    validLocation=False
    def __init__(self, controller, location):
        super().__init__(controller, self.size, location) 

class Cruiser(Ship):
    size=3
    validLocation=False
    def __init__(self, controller, location):
        super().__init__(controller, self.size, location)      

class Battleship(Ship):
    size=4
    def __init__(self, controller, location):
        super().__init__(controller, self.size, location)   

class Carrier(Ship):
    size=5
    def __init__(self, controller, location):
        super().__init__(controller, self.size, location)  
                                      
class Ship_Factory_Tools:
    combi2=[]
    combi3=[]
    combi4=[]
    combi5=[]
    for xx in range(1, 11):
        for yy in range(1, 10):
            combi2.append([[xx, yy], [xx, yy + 1]])
    for yy in range(1,11):
        for xx in range(1,10):
            combi2.append([[xx, yy], [xx + 1, yy]])  

    for xx in range(1, 11):
        for yy in range(1, 9):
            combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
    for yy in range(1,11):
      for xx in range(1,9):
        combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])  

    for xx in range(1, 11):
        for yy in range(1, 8):
            combi4.append([[xx, yy], [xx, yy + 1], [xx, yy + 2],[xx, yy + 3]])
    for yy in range(1,11):
      for xx in range(1,8):
        combi4.append([[xx, yy], [xx + 1, yy], [xx + 2, yy],[xx + 3, yy]])  

    for xx in range(1, 11):
        for yy in range(1, 7):
            combi5.append([[xx, yy], [xx, yy + 1], [xx, yy + 2],[xx, yy + 3],[xx, yy + 4]])
    for yy in range(1,11):
      for xx in range(1,7):
        combi5.append([[xx, yy], [xx + 1, yy], [xx + 2, yy],[xx + 3, yy],[xx + 4, yy]])                

    def check_for_size(location,size):
        if len(location)==size*4-1:
            return True
        else:
            return False
    def convert_to_list(locations,size):
        location=locations.split()
        i=0
        locations=[]
        for counter in location:
            location[i]=int(location[i])
            i=i+1
        for counter in range(0,size*2,+2):
              locations.append([location[counter],location[counter+1]])    
        return locations

    def check_for_valid_location(self,location,size):
        if size ==2:
            if location in self.combi2:
                return True
            else:
                return False    
        elif size ==3:
            if location in self.combi3:
                return True
            else:
                return False 
        elif size ==4:
            if location in self.combi4:
                return True
            else:
                return False   
        elif size ==5:
            if location in self.combi5:
                return True
            else:
                return False   
    def check_for_duplication(fleet_location):
        pass                                      

class Ship_Factory:
    try:
        while True:
            player_destroyer=Destroyer("player",input("Enter the two coordinates for you destroyer seperated by a space: \n")) 
            if Ship_Factory_Tools.check_for_size(player_destroyer.location,player_destroyer.size):
                player_destroyer.location=Ship_Factory_Tools.convert_to_list(player_destroyer.location,player_destroyer.size)
                if Ship_Factory_Tools.check_for_valid_location(Ship_Factory_Tools,player_destroyer.location,player_destroyer.size):
                    break
                else:
                    print("Invalid location")
            else:
                print("Invalid size")
    except:
        print("Invalid input")            
    try:
        while True:
            player_submarine=Submarine("player",input("Enter the three coordinates for your submarine seperated by a space: \n"))
            if Ship_Factory_Tools.check_for_size(player_submarine.location,player_submarine.size):
                player_submarine.location=Ship_Factory_Tools.convert_to_list(player_submarine.location,player_submarine.size)
                if Ship_Factory_Tools.check_for_valid_location(Ship_Factory_Tools,player_submarine.location,player_submarine.size):
                    break
                else:
                    print("Invalid location")
            else:
                print("Invalid size")
    except:
        print("Invalid input")                 
    try:
        while True:
            player_cruiser=Cruiser("player",input("Enter the three coordinates for your cruiser seperated by a space: \n"))
            if Ship_Factory_Tools.check_for_size(player_cruiser.location,player_cruiser.size):
                player_cruiser.location=Ship_Factory_Tools.convert_to_list(player_cruiser.location,player_cruiser.size)
                if Ship_Factory_Tools.check_for_valid_location(Ship_Factory_Tools,player_cruiser.location,player_cruiser.size):
                    break
                else:
                    print("Invalid location")
            else:
                print("Invalid size")
    except:
        print("Invalid input")            
    try:
        while True:
            player_battleship=Battleship("player",input("Enter the four coordinates for your battleship seperated by a space: \n"))
            if Ship_Factory_Tools.check_for_size(player_battleship.location,player_battleship.size):
                player_battleship.location=Ship_Factory_Tools.convert_to_list(player_battleship.location,player_battleship.size)
                if Ship_Factory_Tools.check_for_valid_location(Ship_Factory_Tools,player_battleship.location,player_battleship.size):
                    break
                else:
                    print("Invalid location")
            else:
                print("Invalid size")
    except:
        print("Invalid input")            
    try:
        while True:
            player_carrier=Carrier("player",input("Enter the five coordinates for your carrier seperated by a space: \n"))
            if Ship_Factory_Tools.check_for_size(player_carrier.location,player_carrier.size):
                player_carrier.location=Ship_Factory_Tools.convert_to_list(player_carrier.location,player_carrier.size)
                if Ship_Factory_Tools.check_for_valid_location(Ship_Factory_Tools,player_carrier.location,player_carrier.size):
                    break
                else:
                    print("Invalid location")
            else:
                print("Invalid size")
    except:
        print("Invalid input")            
class Grid:  # Grid class
    grid_locations=[]  
    for x in range(1,11):
        for y in range(1,11):
            grid_locations.append([x,y])     