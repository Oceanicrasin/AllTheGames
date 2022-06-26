import random
xs=[1,2,3,4,5]
ys=[1,2,3,4,5]
grid=[]
hit=[]
hits = 0
miss = 0
i=0
ii=0
for x in xs:
  for y in ys:
    h=[x,y]
    grid.append(h)
#grid.pop(0)
c_grid=grid    
selected=True
while selected:
  choice1=random.choice(grid)
  choice2=random.choice(grid)
  choice3=random.choice(grid)
  choice4=random.choice(grid)
  choice5=random.choice(grid)
  c_Choices=[ choice1, choice2, choice3, choice4, choice5]
  for counter in c_Choices:
    for counter1 in c_Choices:
      if counter != counter1:
        i=i+1
  if i>24:
    selected=False
    pChoice1=input("Enter the coordinates of your first ship seperated by a space: ")
    pChoice2=input("Enter the coordinates of your second ship seperated by a space: ")
    pChoice3=input("Enter the coordinates of your third ship seperate by a space: ")
    pChoice4=input("Enter the coordinates of your fourth ship seperated by a space: ")
    pChoice5=input("Enter the coordinates of your fifth ship seperated by a space: ")
    def ships(whichone):
      whichone=whichone.split()
      j=0
      for counter in whichone:
        whichone[j]=int(whichone[j])
        j=j+1
      return whichone  
    pChoice1=ships(pChoice1)
    pChoice2=ships(pChoice2)
    pChoice3=ships(pChoice3)
    pChoice4=ships(pChoice4)
    pChoice5=ships(pChoice5)
    p_Choices=[pChoice1,pChoice2,pChoice3,pChoice4,pChoice5
    ]
print(p_Choices)     
continuing=True
while continuing:
  ii=ii+1
  print("Round",ii)
  crd=input("Enter coordinate to bomb seperated by a space: ")
  crd=ships(crd)
  hit.append(crd)
  #grid.remove(crd)
  for counter in hit:
    print(counter)
  if crd in c_Choices:
    print("HIT at ",crd)
    hits=hits+1
    c_Choices.remove(crd)
  else:
    print("miss")
    miss=miss+1
  print(f"You have hit {hits} times and missed {miss} times")  
  if not c_Choices:
    print("Congrats you win, it took you ",ii,"Attempts")
    continuing=False
  c_fire=random.choice(c_grid)
  c_grid.remove(c_fire)
  print(f"Computer fires at {c_fire}")
  if c_fire in p_Choices:
    print("Hit")
    p_Choices.remove(c_fire)
  else:
    print("Computer misses")
  if not p_Choices:
    print(f"Computer wins after {ii} attempts")
    continuing=False
  
  
    
  