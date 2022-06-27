class Battleship:
    def __init__(self,size,location):
        self.size = size
        self.location = location
        locations=self.location.split()
        i=0
        for counter in locations:
            locations[i]=int(locations[i])
            i=i+1
        self.location=[]
        print(locations)
        for counter in range(0,self.size*2,+2):
            print(counter)
            self.location.append([locations[counter],locations[counter+1]])
       

    def hit(self,fired_position):
        if fired_position in self.location:
            self.location.remove(fired_position)
            print(f"Hit at {fired_position}")
            return True
        else:
            print("Miss") 
            return False   
            

     