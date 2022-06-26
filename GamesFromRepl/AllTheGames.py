import random
import os
while True:
  try:
    print("1. Guess the number game")
    print("2. Rock,paper scissors")
    print("3. Pass the pigs")
    print("4. Darts(not really a game)")
    print("5. Snake eyes")
    print("6. Battleships")
    print("7. 21 game")
    print("8. National lotto")
    print("9. Coin flip")
    print("10.Censored Roulette")
    print("11. Magic 8 ball")
    print("12. Mastermind") 
    print("13. Fizz")
    print("14. Hangman")
    while True:
      try:
        number = int(input("Enter the game number you want: "))
        break
      except:
        print("Invalid data try again")
    if number == 1:
          print("Welcome to guess the number game")
          while True:
            try:         
              first = int(input("Enter the number you want the generator to start at: "))
              last = int(input("Enter the number you want the generator to end at: "))
              number = random.randint(first, last)
              break
            except:
              print("Invalid data enter again")  
          i = 0
          while True:
              i = 1 + i
              print("Guess", i)
              guess = int(input("Enter your guess: "))
              if guess == number:
                  print("correct")
                  break
              if guess > number:
                  print("too high")
              if guess < number:
                  print("too low")       
    elif number == 2:
          print("Welcome to rock paper scissors")
          c_number = 0
          c_score = 0
          p_number = 0
          p_score = 0
          i = 1
          idk = ["rock", "scissors", "paper"]
      
          def rpcLogic():
              global i
              global c_number
              global c_score
              global p_number
              global p_number
              global p_score
              print("Round", i)
              c_choice = random.choice(idk)
              if c_choice == "rock":
                  c_number = 1
              elif c_choice == "scissors":
                  c_number = 2
              elif c_choice == "paper":
                  c_number = 3
              while True:
                try:
                  p_choice = input("Enter your choice: rock paper or scissors: ")
                  break
                except:
                  print("Invalid data enter again")
              if p_choice == "rock":
                  p_number = 1
              elif p_choice == "scissors":
                  p_number = 2
              elif p_choice == "paper":
                  p_number = 3
              if c_choice == p_choice:
                  print("The computer chose", c_choice)
                  print("No one gets a point")
              elif c_number == 1 and p_number == 2:
                  print("The computer chose", c_choice)
                  print("computer gets a point")
                  c_score = c_score + 1
              elif c_number == 3 and p_number == 1:
                  print("The computer chose", c_choice)
                  print("computer gets a point")
                  c_score = c_score + 1
              elif c_number == 2 and p_number == 3:
                  print("The computer chose", c_choice)
                  print("computer gets a point")
                  c_score = c_score + 1
              elif c_number == 2 and p_number == 1:
                  print("The computer chose", c_choice)
                  print("player gets a point")
                  p_score = p_score + 1
              elif c_number == 1 and p_number == 3:
                  print("The computer chose", c_choice)
                  print("player gets a point")
                  p_score = p_score + 1
              elif c_number == 3 and p_number == 2:
                  print("The computer chose", c_choice)
                  print("player gets a point")
                  p_score = p_score + 1
              i = i + 1
      
          pr = input("Do you want to play by rounds or points: ")
          if pr == "rounds" :
            while True:
              try:
                round_count = int(input("Enter how many rounds you want to play: "))
                while i <= round_count:
                  rpcLogic()
                if round_count<1:
                  print("invalid data try again")
                else:
                  break
              except:
                print("Invalid data try again")
          else:
             while True:
              try:
                round_count = int(input("Enter how many points you want to play to: "))
                if round_count<1:
                  print("invalid data try again")
                else:
                  break
              except:
                print("Invalid data try again")       
     #     while p_score < round_count and c_score < round_count:
     #             rpcLogic()
          if p_score == c_score:
              print("Draw")
          elif p_score < c_score:
              print("You lose")
          else:
              print("You win")
    elif number == 3:
      while True:
        try:
          print("Welcome to pass the pigs game")
          score = []
          p_score = []
          i = 0
          continue_turn = True
          side = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          right_side = [1, 2, 3, 4, 5]
          left_side = [6, 7, 8, 9, 10]
          feet = [11, 12, 13, 14]
          razorback = [15, 16, 17, 18]
          snout = [19, 20]
          jowler = [21]
          while True:
            try:
              players = int(input("Enter how many players you have: "))
              if players<2:
                print("Invalid number of players enter again")
              else:
                break
            except:
              print("Invalid data try again")
          for counter in range(players):
              score.append(0)
              p_score.append(0)
          help = ["rightSide", "leftSide", "feet", "back", "snout", "jowler"]
      
          def score_check():
              for counter in p_score:
                  if counter >= 100:
                      return False
                  else:
                      return True
      
          def continu():
              global score
              global p_score
              global continue_turn
              print("Turn score ", score[ii])
              print("Overall score", p_score[ii])
              print("Do you want to continue ")
              while True:
                try:
                  con = int(
                  input("Type 1 to end your turn and bank your score or type 2 to continue your turn: \n"  ))
                  break
                except:
                  print("Invalid data try again")
              if con == 1:
                  continue_turn = False
                  p_score[ii] = p_score[ii] + score[ii]
      
          def singularity(singularity, letter):
              if letter == "a":
                  pig = pigA
              else:
                  pig = pigB
              Trotter = 5
              Razorback = 5
              Snouter = 10
              Jowler = 15
              sider = 0
              all = [Trotter, Razorback, Snouter, Jowler, sider]
              if singularity == "trotter":
                  all.remove(Trotter)
              elif singularity == "razorback":
                  all.remove(Razorback)
              elif singularity == "snouter":
                  all.remove(Snouter)
              elif singularity == "jowler":
                  all.remove(Jowler)
              elif singularity == "sider":
                  all.remove(sider)
              for counter in all:
                  if counter == Trotter:
                      if pig in feet:
                          print("Trotter")
                          return 5
                  if counter == Razorback:
                      if pig in razorback:
                          print("Razorback")
                          return 5
                  if counter == Snouter:
                      if pig in snout:
                          print("Snout")
                          return 10
                  if counter == Jowler:
                      if pig in jowler:
                          print("Jowler")
                          return 15
                  if counter == sider:
                      if pig in right_side or pig in left_side:
                          print("side")
                          return 0
      
          while score_check():
              for counter in range(0, players):
                  score[counter] = 0
              i = i + 1
              ii = -1
              print(f"Round {i}")
              for counter in p_score:
                  if p_score[ii] >= 100:
                      print("Player ", ii + 1, "wins after", i, "rounds")
                  else:
                      print("player", ii + 2, "turn")
                  continue_turn = True
                  ii = ii + 1
                  while continue_turn == True and score_check():
                      input("Press enter to roll")
                      pigA = random.randint(1, 21)
                      pigB = random.randint(1, 21)
                      print(f"You rolled a {pigA}")
                      print(f"You rolled a {pigB}")
                      #Sides and out starts here
                      if pigA in right_side and pigB in right_side:
                          print("sider")
                          score[ii] = score[ii] + 1
                          continu()
                      elif pigA in left_side and pigB in left_side:
                          print("sider")
                          score[ii] = score[ii] + 1
                          continu()
                      elif pigA in right_side and pigB in left_side:
                          print("pig out")
                          print("score:", score[ii])
                          print("overall score:", p_score[ii])
                          continue_turn = False
                          score[ii] = 0
                      elif pigA in left_side and pigB in right_side:
                          print("pig out")
                          print("score:", score[ii])
                          print("overall score:", p_score[ii])
                          continue_turn = False
                          score[ii] = 0
              #ends here
              #singularity starts here
                      elif pigA in side and pigB not in side:
                          score[ii] = score[ii] + singularity("sider", "b")
                          continu()
                      elif pigB in side and pigA not in side:
                          score[ii] = score[ii] + singularity("sider", "a")
                          continu()
                      elif pigA in feet and pigB not in feet:
                          print("Trotter")
                          score[ii] = score[ii] + 5 + singularity("trotter", "b")
                          continu()
                      elif pigA in razorback and pigB not in razorback:
                          print("Razorback")
                          score[ii] = score[ii] + 5 + singularity("razorabck", "b")
                          continu()
                      elif pigA in snout and pigB not in snout:
                          print("Snout")
                          score[ii] = score[ii] + 10 + singularity("snout", "b")
                          continu()
                      elif pigA in jowler and pigB not in jowler:
                          print("Jowler")
                          score[ii] = score[ii] + 15 + singularity("jowler", "b")
                          continu()
              #singularity ends here
              #double starts
                      elif pigA in feet and pigB in feet:
                          print("Double Trotter")
                          score[ii] = score[ii] + 20
                          continu()
                      elif pigA in razorback and pigB in razorback:
                          print("Double Razorback")
                          score[ii] = score[ii] + 20
                          continu()
                      elif pigA in snout and pigB in snout:
                          print("Double snouter")
                          score[ii] = score[ii] + 40
                          continu()
                      elif pigA in jowler and pigB in jowler:
                          print("Double jowler")
                          score[ii] = score[ii] + 60
                          continu()
          break            
        except:
         print("I'm not sure what you did but this code will not error")        
    elif number == 4:
      while True:
        try:
          print("Welcome to darts")
          play_again = True
          players = 1
          ii = 0
      
          def cheeky():
              global ii
              global players
              if ii > players - 1:
                  ii = 0
              return p_score != 0
      
          while play_again:
              ii = 0
              p_score = []
              while True:
                try:
                  players = int(input("Enter how many players you have: "))
                  break
                except:
                  print("Invalid data try again")
              for counter in range(players):
                  p_score.append(501)
              print("New game.Each player starts at 501")
              while cheeky():
                  if ii > players - 1:
                      ii = 0
                  print("Player", ii + 1)
              while True:
                try:
                  score = int(input("Enter your total from the three darts:"))
                  break
                except:
                  print("Invalid data try again")
              if p_score[ii] - score > 1:
                  p_score[ii] = p_score[ii] - score
                  print(p_score[ii])
              elif p_score[ii] - score == 0:
                  p_score[ii] = p_score[ii] - score
                  print("Player ", ii + 1, " wins the game")
                  ask = input("Do you want to play again? ")
                  ii = 0
                  if ask == "no":
                      play_again = False
              else:
                  print(p_score[ii])
                  ii = ii + 1
          break      
        except:
          print("I'm not sure what you did but this code will not error")        
    elif number == 5:
      while True:
        try:
            print("Welcome to snake eyes")
            score = []
            p_score = []
            i = 0
            continue_turn = True
            while True:
               try:
                 players = int(input("Enter how many players you have: "))
                 if players<2:
                   print("Invalid number of players enter again")
                 else:
                   break
               except:
                 print("Invalid data try again")
            for counter in range(players):
                score.append(0)
                p_score.append(0)
        
            def score_check():
                for counter in p_score:
                    if counter >= 10:
                        return False
                    else:
                        return True
        
            def continu():
                global score
                global p_score
                global continue_turn
                print("Turn score ", score[ii])
                print("Banked score", p_score[ii])
                print("Do you want to continue ")
                con = int(
                    input(
                        "Type 1 to end your turn and bank your score or type 2 to continue your turn: "
                    ))
                if con == 1:
                    continue_turn = False
                    p_score[ii] = p_score[ii] + score[ii]
        
            while score_check():
                for counter in range(0, players):
                    score[counter] = 0
                i = i + 1
                ii = -1
                print(f"Round {i}")
                for counter in p_score:
                    if p_score[ii] >= 10:
                        if ii == -1:
                            print(f"Player {players} wins after {i} rounds")
                            exit()
                        else:
                            print("Player ", ii + 1, "wins after", i, "rounds")
                            exit()
                        #break
                    else:
                        print("player", ii + 2, "turn")
                    continue_turn = True
                    ii = ii + 1
                    while continue_turn == True and score_check():
                        input("Press enter to roll")
                        Dice1 = random.randint(1, 6)
                        Dice2 = random.randint(1, 6)
                        print(f"You rolled a {Dice1}")
                        print(f"You rolled a {Dice2}")
                        total = Dice1 + Dice2
                        #Sides and out starts here
                        if Dice1 == 1 and Dice2 == 1:
                            score[ii] = 0
                            p_score[ii] = 0
                            continue_turn = False
                        elif Dice1 == 1 or Dice2 == 1:
                            print("score:", score[ii])
                            print("overall score:", p_score[ii])
                            continue_turn = False
                            score[ii] = 0
        
                        else:
                            score[ii] = score[ii] + total
                            continu()
            break
        except:
         print("I don't know what you did but this code will not error out")
    elif number == 6:
      while True:
        try:
          print("Welcome to battleships")
          xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          ys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          combi3 = []
          combi5 = []
          grid = []
          hit = []
          hits = 0
          miss = 0
          i = 0
          ii = 0
      
          def inlist(my_list, item):
              o = 0
              for counter in my_list:
                  if item in counter:
                      o = o + 1
                      return True
              return False
              o = 0
              for counter in my_list:
                  if item in counter:
                      o = o + 1
                      return counter.remove(item)
              return False
      
          def ships(whichone, index):
              whichone = whichone.split()
              j = 0
              for counter in whichone:
                  whichone[j] = int(whichone[j])
                  j = j + 1
              if index == "three":
                  l1 = [whichone[0], whichone[1]]
                  l2 = [whichone[2], whichone[3]]
                  l3 = [whichone[4], whichone[5]]
                  whichone.clear()
                  whichone.append(l1)
                  whichone.append(l2)
                  whichone.append(l3)
              elif index == "five":
                  l1 = [whichone[0], whichone[1]]
                  l2 = [whichone[2], whichone[3]]
                  l3 = [whichone[4], whichone[5]]
                  l4 = [whichone[6], whichone[7]]
                  l5 = [whichone[8], whichone[9]]
                  whichone.clear()
                  whichone.append(l1)
                  whichone.append(l2)
                  whichone.append(l3)
                  whichone.append(l4)
                  whichone.append(l5)
              return whichone
      
          #grid formation
          for x in xs:
              for y in ys:
                  g = [x, y]
                  grid.append(g)
      
          for xx in range(1, 9):
              for yy in range(1, 9):
                  combi3.append([[xx, yy], [xx, yy + 1], [xx, yy + 2]])
                  combi3.append([[xx, yy], [xx + 1, yy], [xx + 2, yy]])
          for xx in range(1, 6):
              for yy in range(1, 6):
                  combi5.append([[xx, yy], [xx, yy + 1], [xx, yy + 2], [xx, yy + 3],
                                 [xx, yy + 4]])
                  combi5.append([[xx, yy], [xx + 1, yy], [xx + 2, yy], [xx + 3, yy],
                                 [xx + 4, yy]])
      
          #grid.pop(0)
          c_grid = grid
          selected = True
          playerCorrect = True
          while selected:
              choice1 = random.choice(combi3)
              choice2 = random.choice(combi3)
              choice3 = random.choice(combi3)
              choice4 = random.choice(combi3)
              choice5 = random.choice(combi5)
              c_Choices = [choice1, choice2, choice3, choice4, choice5]
              for counter in c_Choices:
                  for counter1 in c_Choices:
                      if counter != counter1:
                          i = i + 1
              if i > 24:
                  selected = False
                  while playerCorrect:
                    while True:
                      try:
                        pChoice1=input( "Enter the three coordinates of your first ship seperated by a space\n" )
                        pChoice2=input( "Enter the three coordinates of your second ship seperated by a space\n")
                        pChoice3=input("Enter the three coordinates of your third ship seperate by a space\n" )
                        pChoice4=input("Enter the three coordinates of your fourth ship seperated by a space\n" )
                        pChoice5=input( "Enter the five coordinates of your fifth ship seperated by a space\n" )
        
                        pChoice1 = ships(pChoice1, "three")
                        pChoice2 = ships(pChoice2, "three")
                        pChoice3 = ships(pChoice3, "three")
                        pChoice4 = ships(pChoice4, "three")
                        pChoice5 = ships(pChoice5, "five")
                        p_Choices = [pChoice1, pChoice2, pChoice3, pChoice4, pChoice5]
                        if pChoice1 in combi3:
                            i = i + 1
                        if pChoice2 in combi3:
                            i = i + 1
                        if pChoice3 in combi3:
                            i = i + 1
                        if pChoice4 in combi3:
                            i = i + 1
                        if pChoice5 in combi5:
                            i = i + 1
                        if i > 4:
                            playerCorrect = False
                        else:
                            print("Mistakes in coordinates place again")
                        break
                      except:
                        print("Invalid data enter again")
          i = 0
          print(p_Choices)
          continuing = True
          while continuing:
              ii = ii + 1
              print("Round", ii)
              print("Computer has", len(c_Choices), "ships left")
              while True:
                try:
                  crd = input("Enter coordinate to bomb seperated by a space: ")
                  crd = ships(crd, "nein")
                  break
                except:
                  print("Invalid data enter again")
              hit.append(crd)
              #grid.remove(crd)
              for counter in hit:
                  print(counter)
              if inlist(c_Choices, crd):
                  print("HIT at ", crd)
                  hits = hits + 1
                  h = 0
                  i = 0
                  for counter in c_Choices:
                      if crd in counter:
                          c_Choices[h].remove(crd)
                          break
                      else:
                          h = h + 1
              else:
                  print("miss")
                  miss = miss + 1
              print(f"You have hit {hits} times and missed {miss} times")
              for counter in c_Choices:
                  if not counter:
                      c_Choices.remove(counter)
              if not c_Choices:
                  print("Congrats you win, it took you ", ii, "Attempts")
                  continuing = False
                  break
              c_fire = random.choice(c_grid)
              c_grid.remove(c_fire)
              print(f"Computer fires at {c_fire}")
              if inlist(p_Choices, c_fire):
                  print("Hit")
                  o = 0
                  for counter in p_Choices:
                      if c_fire in counter:
                          p_Choices[o].remove(c_fire)
                          print("Ships locations left")
                          print(p_Choices)
                      else:
                          o = o + 1
              else:
                  print("Computer misses")
              if not p_Choices:
                  print(f"Computer wins after {ii} attempts")
                  continuing = False
          break      
        except:
          print("I'm not sure what you did but this code will not error") 
    elif number == 7:
          print("Welcome to 21 game")
          total = 0
          while True:
              if total == 17:
                  total = 20
                  print("ai chose 3")
                  print("player loses")
                  break
              if total == 18:
                  total = 20
                  print("ai chose 2")
                  print("player loses")
                  break
              if total == 19:
                  total = 20
                  print("ai chose 1")
                  print("player loses")
                  break
              else:
                  x = random.randint(1, 3)
                  total = total + x
                  print("a.i chose: ", x)
                  print("total + a.i number = ", total)
                  if total > 20:
                      print("game over")
                  if total > 20:
                      print("a.i loses")
                      break
                  else:
                      correct = True
                      while correct == True:
                        while True:
                          try:
                            y = int(input("player input: "))
                            if y <= 3 and y > 0:
                              correct = False
                              break
                            else:
                             print("Input wrong enter a number between 1 and 3")
                          except:
                            print("Invalid data enter again")                          
                      total = total + y
                      d = int(total)
                      print("total = ", total)
                      if total > 20:
                          print("game over")
                      if d > 20:
                          print("player loses")
                          break         
    elif number == 8:
      while True:
        try:
          des1=input("Simulation mode or gameplay: \n")
          if des1=="simulation":
            print("Wait for around 2minutes for results")
            six=0
            fiveB=0
            five=0
            four=0
            three=0
            two=0
            one= 0
            zero=0
            for counter in range(1000000):
              ball1= random.randint(1,60)
              ball2= random.randint(1,60)
              ball3= random.randint(1,60)
              ball4= random.randint(1,60)
              ball5= random.randint(1,60)
              ball6= random.randint(1,60)
              bonus=random.randint(1,7)
        
              lBall1=random.randint(1,60)
              lBall2=random.randint(1,60)
              lBall3=random.randint(1,60)
              lBall4=random.randint(1,60)
              lBall5=random.randint(1,60)
              lBall6=random.randint(1,60)
              lbonus=random.randint(1,7)
              lotto=[lBall1,lBall2,lBall3,lBall4,lBall5,lBall6]
              userGuess=[ball1,ball2,ball3,ball4,ball5,ball6]
              i=0
              for actual in lotto:
                for guess in userGuess:
                  if actual == guess:
                    i=i+1
              if i >=6:
                six= six+1
              elif i ==5:
                if bonus == lbonus:
                  fiveB= fiveB+1
                else:
                  five= five+1
              elif i == 4:
                four= four+1
              elif i == 3:
                three= three+1
              elif i ==2:
                two= two+1
              elif i == 1:
                one= one+1
              else :
                zero= zero+1
            print("Amount of jackpot wins: ", six)       
            print("Number of 5 correct with bonus ball: ", fiveB)
            print("Number of five correct with bonus balls: ", five)
            print("Number of four correct:  ", four)
            print("Number of three correct: ", three)
            print("Number of two correct:   ", two)
            print("Number of one correct:   ",one)
            print("Number of none correct:  ", zero)
                    
        
          else:
            des2=input("Do you want your choices to be random or do you want to decide: \n")
            if des2 == "random":
              ball1= random.randint(1,60)
              ball2= random.randint(1,60)
              ball3= random.randint(1,60)
              ball4= random.randint(1,60)
              ball5= random.randint(1,60)
              ball6= random.randint(1,60)
              bonus=random.randint(1,7)
            else:
              while True:
                try: 
                  isCorrect=True
                  ball1=int(input("Enter a number between 1 and 59: \n"))
                  ball2=int(input("Enter a number between 1 and 59: \n") )
                  ball3=int(input("Enter a number between 1 and 59: \n"))
                  ball4=int(input("Enter a number between 1 and 59: \n"))
                  ball5=int(input("Enter a number between 1 and 59: \n"))
                  ball6=int(input("Enter a number between 1 and 59: \n"))
                  bonus=int(input("Enter a number betwwen 1 and 6 for bonus ball: \n"))
                  userGuess=[ball1,ball2,ball3,ball4,ball5,ball6]
                  if bonus<1 or bonus>6:
                    isCorrect=False
                  for counter in userGuess:
                    if counter<1 or counter>59:
                      isCorrect=False
                  if isCorrect:
                    break
                except:
                  print("Invalid data try again")
              print("Your options were ",userGuess,bonus)
            lBall1=random.randint(1,60)
            lBall2=random.randint(1,60)
            lBall3=random.randint(1,60)
            lBall4=random.randint(1,60)
            lBall5=random.randint(1,60)
            lBall6=random.randint(1,60)
            lbonus=random.randint(1,7)
            lotto=[lBall1,lBall2,lBall3,lBall4,lBall5,lBall6]
            userGuess=[ball1,ball2,ball3,ball4,ball5,ball6]
            i=0
            for actual in lotto:
              for guess in userGuess:
                if actual == guess:
                  i=i+1
            print("Computer chose ",lotto,lbonus)
            if i >=6:
              print("Jackpot")
            elif i ==5:
              if bonus == lbonus:
                print("£1,000,000")
              else:
                print("£1750")
            elif i == 4:
              print("£140")
            elif i == 3:
              print("£30")
            elif i ==2:
              print("Free lucky dip")
            else:
              print("You won nothing")
            input()  
          break      
        except:
          print("I'm not sure what you did but this code will not error")   
    elif number == 9:
      print("Welcome to coin flip")
      correct=0
      wrong=0
      while True:
        try:
          while True:
            rounds=int(input("How many rounds do you want to play: "))
            if rounds<1:
              print("Invalid data try again")
            else:break  
          break
        except:
              print("Invalid data try again")
      for counter in range(rounds):
        options=["tails","heads"]
        CC = random.choice(options)
        PC = input("enter what you predict the coin flip will be \n heads \n tails \n")
        if CC == PC:
         print("you guessed right") 
         correct=correct+1 
        else:
         print("you guessed wrong") 
         wrong=wrong+1
      print(f"You guessed correctly {correct} times")
      print(f"You guessed incorrectly {wrong} times")
    elif number == 10:
      while True:
        try:
          print("Welome to censored roulette")
          everyone=[]
          alive=[]
          dead=[]
          while True:
            try:
              players = int(input("Enter how many players you have: "))
              if players<2:
                print("Invalid number of players enter again")
              else:
                break
            except:
              print("Invalid data try again")
          i=1
          for counter in range(players):
            everyone.append(False)
            alive.append(i)
            i=i+1
          def gameEnd():
            global alive
            global dead
            i=0
            for counter in everyone:
              if counter == False:
                
                i=i+1  
            if i >1:
              return True
            else:
              return False
          while gameEnd():
            for counter in alive:
              if counter == 0:
                alive.remove(counter)
            i=0    
            for counter in alive:
              
              print("Player",counter,"turn")
              while True:
                try:
                  while True:
                    choice=int(input("Enter a number between 1 and 6: "))
                    if choice>6 or choice<1:
                      print("Invalid data input again")
                    else:
                      break
                  break
                except:
                  print("Invalid data try again")
              bullet=random.randint(1,6)
              if bullet == choice:
                print("You died")
                alive[i]=0
                dead.append(counter)
                everyone[i]=True
              else:   
                print("You survived for now")  
              i=i+1  
          for counter in alive:
            if counter == 0:  
               alive.remove(counter)
          break      
        except:
          print("I'm not sure what you did but this code will not error")     
      print("Player",alive[0],"wins")
    elif number == 11:
     while True:
      input("ask a question: ")
      opt = random.randint(1,20)
      if opt == 1:
       print("It is certain.")
      if opt == 2:
       print("It is decidedly so.")
      if opt == 3:
       print("Without a doubt.")
      if opt == 4:
       print("Yes definitely.")
      if opt == 5:
       print("You may rely on it.")
      if opt == 6:
       print(" As I see it, yes")
      if opt == 7:
       print("Most likely.")
      if opt == 8:
       print("Outlook good.")
      if opt == 9:
       print("Yes")
      if opt == 10:
       print("Signs point to yes")
      if opt == 11:
       print("Reply hazy, try again.")
      if opt == 12:
       print("Ask again later.")
      if opt == 13:
       print("Better not tell you now.")
      if opt == 14:
       print("Cannot predict now.")
      if opt == 15:
       print("Concentrate and ask again.")
      if opt == 16:
       print("Don't count on it.")
      if opt == 17:
       print("My reply is no.")
      if opt == 18:
       print("My sources say no.")
      if opt == 19:
       print("Outlook not so good.")
      if opt ==20:
       print("Very doubtful")
      break
    elif number == 12:
      print("Welcome to masterminds")
      guessCount=1
      while True:
        try:
          diff=input("Do you want hard, normal or easy difficulty: \n ")
          if diff == "hard" or diff == "normal" or diff == "easy":
            break
        except:
          print("Invalid data try again")
      if diff == "hard":
        numberSize=5
      else:
        numberSize=4
      numbers=[random.randint(1,9)]
      sNumbers=str(numbers[0])
      for counter in range(numberSize-1):
        number=random.randint(0,9)
        numbers.append(number)
        sNumbers=sNumbers+str(number)
      print(sNumbers)
      correct=False
      while correct == False:
        while True:
          print("Rounds",guessCount)
          try:
            pChoice=input(f"Enter your {numberSize} digit number guess: ")
            pChoiceL=[]
            for counter in pChoice:
              pChoiceL.append(counter)
            if pChoice == sNumbers:
              print("Correct")
              correct=True
            else:
              if diff == "easy":
                positions=[]
                i=0
                ii=0
                for counter in range(4):
                  if int(pChoiceL[i])==numbers[i]:
                    positions.append(i+1)
                    ii=ii+1
                  i=i+1
                print(f"You have {ii} numbers correct")  
                if positions:
                  print("The positons are",positions)
                
              elif diff == "normal" or diff == "hard":  
                i=0
                ii=0
                for counter in range(numberSize):
                  if int(pChoiceL[i])==numbers[i]:
                    ii=ii+1
                  i=i+1
                print(f"You have {ii} numbers correct")  
            guessCount=guessCount+1          
            break
          except:
            print("Invalid data try again")

    elif number == 13:
      print("Welcome to Fizz")
      numbers = int(input("Enter the numbers that you want to play with: \n"))
      multiples=[]
      for counter in range(numbers):
        add=int(input("Enter a number to play with: \n"))
        multiples.append(add)
      incorrect=False
      i=1
      while incorrect == False:
        answer=[]
        while True:
          try:
            userChoice=input("Enter your choice: ")
            if userChoice=="":
              print("Invalid data try again")
            else:
              break
          except:
            print("Invalid data try again")
        for counter in multiples:
          if i%counter == 0:
            answer.append("fizz")
        if not answer:
          answer.append(str(i))
        userSolution=userChoice.split() 
        ii=0
        for counter in userSolution:
          if counter == "fiz" or counter == "Fizz" or counter == "Fiz":
            userSolution[ii]="fizz"
          ii=ii+1  
        if userSolution == answer:
          print("Correct")
          i=i+1
        else:
          print("You failed")
          print(f"You survived {i} rounds")
          break

    elif number == 14:
      print("Welcome to hangman but you die instead")
      guess_word = input("Enter your word to be guessed: \n")
      guess_word_list=[]
      for counter in guess_word:
        guess_word_list.append(counter)
      os.system("clear")
      print(f"The word has {len(guess_word)} letters")
      guesses = []
      correct_guesses=[]
      guessed = False
      lives=6
      guess_number = 1
      while guessed == False and lives>0:
        print(f"Guess {guess_number}")
        try:
          while True:
            guess=input("Enter your letter guess: \n")
            break
        except:
          print("Invalid data")
        guesses.append(guess)
        if guess in guess_word_list:
          print("Correct")
        else:
          print("Incorrect")
          lives -=1
          print(f"You have {lives} lives left")
          
        correct_guesses.append(guess)
        i=0  
        for letter in guess_word_list:
          for correct in correct_guesses:
            if letter == correct:
              i+=1
        if i >=len(guess_word_list):
          guessed=True
        guess_number+=1
  except:
    print("I regret to inform you that your code has an error in it")
    print("Don't worry press enter to go back to the main menu")
    print("Sound like a place I should say Game over")
    print("Let me remind you this message only pops up for run time errors not synatx errors")
    print("Maybe you converted to int on accident or forgot? It's possible that you inputed the wrong thing")
    print("Don't you love how the extra indentations need for this makes the code look like a highway")
    print("Thank you for reading this definitly written by python error")
    print("You moron your code has a fricking error")
    
    input()
