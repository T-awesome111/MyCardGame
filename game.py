import random
import time

cards = []
hands = []
scores = []



def playerNumber():
  print()
  players = int(input("Enter how many players there are: "))
  return(players)

def readFile(pFile, pList):
    file = pFile.readlines()
    for item in file:
        item = item.strip("\n")
        item = item.split(",")
        pList.append(item)


def startHand(pCards, pPlayers, temp,pRemaining,pGame):
    cardOne = ""
    cardTwo = ""
    for x in range(0, pPlayers):
        temptwo = []
        numOne = random.randint(0,pRemaining)
        cardOne = pCards[0][numOne]
        del pCards[0][numOne]
        pRemaining = pRemaining -  1

        numTwo = random.randint(0,pRemaining)
        cardTwo = pCards[0][numTwo]
        del pCards[0][numTwo]
        pRemaining = pRemaining - 1

        temptwo.append(cardOne)
        temptwo.append(cardTwo)
        temp.append(temptwo)
    if pGame == "poker":
      temptwo = []
      temp.append(temptwo)
      for item in temp:
        if item != []:
          item.append(False)

def turn(pHand,pPlayer,pCards,pRemaining):
    bust = False
    count = 2
    clear = 0
    print("Clearing screen")
    while clear!= 60:
        print(" ")
        clear+=1
    time.sleep(2)
    print("It is player",(pPlayer + 1),"'s turn")
    time.sleep(0.5)
    print("Other players look away")
    time.sleep(5)
    print("Your cards are",pHand[pPlayer])
    time.sleep(0.5)
    score = checkScore(pHand,pPlayer)
    print("Your current score is:",score)
    time.sleep(0.5)
    choice = input("Do you want to stick(stay with your current cards, s) or twist (get another card, t): ")
    choice = choice.lower()
    while choice != "s" and not(bust):
        drawCard(pHand,pPlayer,pCards,pRemaining)
        pRemaining -= 1
        score = checkScore(pHand,pPlayer)
        print("You drew",pHand[pPlayer][count])
        time.sleep(1)
        print("Now your hand is",pHand[pPlayer]," with a score of",score)
        time.sleep(1)
        count += 1
        if score > 21:
            bust = True
            print("You are bust and out of the game")
        else:
            choice = input("Do you want to stick(stay with your current cards, s) or twist (get another card, t): ")
    return(score)


def checkScore(pHand,pPlayer):
    points = 0

    for item in pHand[pPlayer]:
        if item[0] == "J" or  item[0] == "Q" or item[0] == "K" :
            points += 10
        elif item[0] == "A":
            points += 1
        elif item[0] == "1" and item[1] == "0":
            points += 10
        else:
            points += int(item[0])

    return(points)

def drawCard(pHand,pPlayer,pCards,pRemaining):
    numOne = random.randint(0,pRemaining)
    cardOne = pCards[0][numOne]
    del pCards[0][numOne]
    pHand[pPlayer].append(cardOne)
  
def winner(pScores):
  max = 0
  index = 0
  count = 0
  for item in pScores:
      if item > 21:
          pass
      elif item > max:
          max = item
          index = count
      count +=1
  if max == 0:
      return(3141592)
  else:
      return(index)


def playTwentyOne(pCards,pPlayers,pHands,pScores):
    startHand(pCards, pPlayers, pHands,len(pCards[0])-1,"twentyone")
    count = 0

    while count < pPlayers:
        pScores.append(turn(pHands,count,pCards,len(pCards[0])-1))
        count += 1
        time.sleep(1)
    won = winner(pScores)
    clear = 0
    print("Clearing screen")
    while clear != 60:
        print(" ")
        clear += 1
    print("Gathering the results.....")
    time.sleep(3)
    if won == 3141592:
        print("No one won as everyone was bust")
    else:
        print("The winner was player",won + 1,"with a score of:",pScores[won])

def introduction(pCards,pHands,pScores):
  choice = 0
  while choice != 9: 
    print()
    print()
    pHands = []
    pScores = []
    time.sleep(1)
    print("Welcome, are you ready to play some card games? Here are the options: ")
    time.sleep(1)
    print("1 - twentyone")
    print("2 - poker")
    print("9 - Exit")
    choice = int(input("Enter your choice here: "))
    if choice == 1:
      print("Great choice")
      players = playerNumber()
      playTwentyOne(pCards,players,pHands,pScores)
    elif choice == 2:
      print("Great choice")
      players = playerNumber()
      playPoker(pCards,players,pHands,pScores)
      choice = 9
    else:
      print("Goodbye")

    
  

def playPoker(pCards,pPlayers,pHands,pScores):
  bets = [0 for i in range(0,pPlayers)]
  maxBet = 0
  startHand(pCards, pPlayers, pHands,len(pCards[0])-1,"poker")
  pokerShowHand(pCards,pPlayers,pHands,pScores)
  clear = 0
  while clear != 60:
    print()
    clear += 1
  pokerRound(pHands,pPlayers,maxBet,pCards,bets,1)
  if outOfPlayers(pHands,pPlayers):
    for i in range(0,3):
      drawCard(pHands,pPlayers,pCards,len(pCards[0])-1)
    print()
    print("The communal cards are: ")
    print(str(pHands[-1][0]),str(pHands[-1][1]),str(pHands[-1][2]))
    pokerRound(pHands,pPlayers,maxBet,pCards,bets,2)
    if outOfPlayers(pHands,pPlayers):
      drawCard(pHands,pPlayers,pCards,len(pCards[0])-1)
      print()
      print("The communal cards are: ")
      print(str(pHands[-1][0]),str(pHands[-1][1]),str(pHands[-1][2]),str(pHands[-1][3]))
      pokerRound(pHands,pPlayers,maxBet,pCards,bets,3)
      if outOfPlayers(pHands,pPlayers):
        drawCard(pHands,pPlayers,pCards,len(pCards[0])-1)
        print()
        print("The communal cards are: ")
        print(str(pHands[-1][0]),str(pHands[-1][1]),str(pHands[-1][2]),str(pHands[-1][3]),str(pHands[-1][4]))
        pokerRound(pHands,pPlayers,maxBet,pCards,bets,4)
        if outOfPlayers(pHands,pPlayers):
          count = 1
          for item in pHands:
            if count == len(pHands):
              print("The communal cards are", str(pHands[-1][0]),str(pHands[-1][1]),str(pHands[-1][2]),str(pHands[-1][3]),str(pHands[-1][4]))
            else:
              print("Player "+str(count)+"'s cards are",str(item[0]),str(item[1]))
            count +=1
          print(bets)
        else:
          print("Player",str((foldedWinner(pHands,pPlayers))+1),"wins")
      else:
        print("Player",str((foldedWinner(pHands,pPlayers))+1),"wins")
    else:
      print("Player",str((foldedWinner(pHands,pPlayers))+1),"wins")
  else:
    print("Player",str((foldedWinner(pHands,pPlayers))+1),"wins")
          
  
  

def pokerShowHand(pCards,pPlayers,pHands,pScores):
  count = 0
  clear = 0
  while count < pPlayers:
    clear = 0
    while clear != 60:
      print()
      clear += 1
    time.sleep(0.5)
    print("Player "+str(count + 1)+"'s hand is about to be shown")
    print("All other players please look away")
    time.sleep(2)
    print("Your cards are:",pHands[count][0],pHands[count][1])
    input("Press enter to continue")  
    count += 1
  
  

def pokerRound(pHands,pPlayers,pMax,pCards,pBets,round):
  matched = False
  flag = True
  while not(matched):
    for i in range(0,pPlayers):
      pMax = max(pBets)
      if not(pHands[i][2]):
        if pMax == 0 or pBets[i] != pMax or flag:
          betting(pBets,i,pMax,pHands)
    pMax = max(pBets)
    matched = check(pHands,pPlayers,pCards,pBets,pMax)
    flag = False


def betting(pBets,pPlayer,pMax,pHands):
  valid = True
  betted = False
  
  while (valid and not(betted)):
    if not(pHands[pPlayer][2]):
      bet = 0
      print("It is player "+str(pPlayer + 1)+"'s turn to bet")
      bet = input("Enter your bet amount here(a to call, b to check, c to fold): ")
      if bet == "a" and pBets[pPlayer] < pMax:
        bet = pMax
        pBets[pPlayer] = pMax
        betted = True
      elif bet == "b":
        if pBets[pPlayer] < pMax or pBets[pPlayer] > pMax:
          print("You do not have the same amount betted as is in the pot so you cannot check")
          valid = False
        else:
          bet = pMax
          pBets[pPlayer] = bet
          betted = True
      elif bet == "c":
        betted = True
        pHands[pPlayer][2] = True
      else:
        try:
          int(bet)
        except ValueError:
          valid = False
        else:
          bet = int(bet)
          valid = True
      if valid and not(betted): 
        if (pBets[pPlayer] + bet) >= pMax:
          pBets[pPlayer] = pBets[pPlayer] + bet
          betted = True
        else:
          print("That does not match the pot, try again")
    
def max(pBets):
  tempMax = 0
  for item in pBets:
    if item > tempMax:
      tempMax = item
  return tempMax    
      
def check(pHands,pPlayers,pCards,pBets,pMax):
  matching = False
  count = 0
  players = 0
  for item in range(0,pPlayers):
    if not(pHands[item][2]):
      players += 1
  for item in range(0,pPlayers):
    if not(pHands[item][2]):
      if pBets[item] != pMax:
        matching = False
      else:
        count += 1
        if count == players:
          matching = True
  if matching == False:
    print("Not everyone has the same amount in the pot so the betting will go round again")
  return matching
  
def outOfPlayers(pHands,pPlayers):
  count = 0
  for item in range(0,pPlayers):
    if not(pHands[item][2]):
      count += 1
  if count == 1:
    return False
  else:
    return True

def foldedWinner(pHands,pPlayers):
  index = 0
  for item in range(0,pPlayers):
    if not(pHands[item][2]):
      index = item
  return index

def mergeSort(pList):
  if len(pList) > 1:
    mid = len(pList) // 2   
    left = pList[:mid]   
    right = pList[mid:]    
    mergeSort(left)      
    mergeSort(right)       
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right): 
      if left[i] < right[j]:                
        pList[k] = left[i]                  
        i = i+1
      else:
        pList[k] = right[j]
        j = j+1
      k = k+1

    while i < len(left):
      pList[k] = left[i]
      i = i+1
      k = k+1

    while j < len(right): 
      pList[k] = right[j]
      j = j+1
      k = k+1

def isStraight(pHands):
  dictValues = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"1":10,"J":11,"Q":12,"K":13,"A":14}
  scores = []
  temp = []
  straights = []
  for item in pHands:
    temp = []
    if item == pHands[-1]:
      pass
    else:
      temp = [dictValues[item[0][0]],dictValues[item[1][0]],
              dictValues[pHands[-1][0][0]],dictValues[pHands[-1][1][0]],
              dictValues[pHands[-1][2][0]],dictValues[pHands[-1][3][0]],
              dictValues[pHands[-1][4][0]]]
      scores.append(temp)
  for x in range(0,len(scores)):
    mergeSort(scores[x])
  count = 0
  print(scores)
  for record in scores:
    temp2 = []
    for item in record:
      if item not in temp2:
        temp2.append(item)
    scores[count] = temp2
    count += 1
  count= 0
  for record in scores:
    if len(record) < 5:
      pHands[count].append(False)
    elif len(record) == 5:
      straight = True
      for item in range(0,len(record)):
        if item != len(record)-1:
          if record[item] != record[item+1]:
            straight = False
      pHands[count].append(straight)
    

        

    
  #return pHands

def flush(pHands):
  count = 0
  temp = []
  personalHands = []
  for item in range(0,len(pHands)-1):
    temp = [pHands[item][0],pHands[item][1],pHands[-1][0],pHands[-1][1],pHands[-1][2],pHands[-1][3],pHands[-1][4]]
    personalHands.append(temp)
  count = 0
  for record in personalHands:
    clubs = 0
    diamonds = 0
    spades = 0
    hearts = 0
    for item in record:
      if item[1] == "C":
        clubs += 1
      elif item[1] == "D":
        diamonds += 1
      elif item[1] == "S":
        spades += 1
      elif item[1] == "H":
        hearts += 1 
    if clubs==5 or diamonds == 5 or spades == 5 or hearts == 5:
      pHands[count].append(True)
    else:
      pHands[count].append(False)
    count += 1
  return pHands
      
def ofAKind(pHands):
  
  temp = []
  personalHands = []
  count = 0
  for item in range(0,len(pHands)-1):
    temp = [pHands[item][0],pHands[item][1],pHands[-1][0],pHands[-1][1],pHands[-1][2],pHands[-1][3],pHands[-1][4]]
    personalHands.append(temp)
  for record in personalHands:
    dict = {}
    for item in record:
      if item[0] in dict:
        dict[item[0]] = dict[item[0]] + 1
      else:
        dict[item[0]] = 1
    max = 0
    for item in dict:
      if dict[item] > max:
        max = dict[item]
    pHands[count].append(max)
    count += 1

  return pHands

def higher(pHands):
  dictValues = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"1":10,"J":11,"Q":12,"K":13,"A":14}
  temp = []
  personalHands = []
  count = 0
  for item in range(0,len(pHands)-1):
    temp = [pHands[item][0],pHands[item][1],pHands[-1][0],pHands[-1][1],pHands[-1][2],pHands[-1][3],pHands[-1][4]]
    personalHands.append(temp)
  for record in personalHands:
    max = "2"
    for item in record:
      if dictValues[item[0]] > dictValues[max]:
        max = item[0]
    pHands[count].append(max)
    count += 1
  return pHands

def findHands(pHands):
  pHands = isStraight(pHands)
  pHands = flush(pHands)
  pHands = ofAKind(pHands)
  pHands = higher(pHands)
  return pHands

def bestHand(pHands):
  pHands = findHands(pHands)
  print(pHands)
  values = []
  for x in range(0,len(pHands)-1):
    if pHands[x][2] and pHands[x][3]:
      values.append(7)
    elif pHands[x][2]:
      values.append(6)
    elif pHands[x][3]:
      values.append(5)
    elif pHands[x][4] == 4:
      values.append(4)
    elif pHands[x][4] == 3:
      values.append(3)
    elif pHands[x][4] == 2:
      values.append(2)
    else:
      values.append(1)

  count = 0
  index = []
  max = 0
  for item in values:
    print(max,index,item)
    temp = []
    if item >= max:
      print("e")
      max = item
      temp.append(count)
      temp.append(item)
      index.append(temp)
    count += 1

  return (index)

def winnerPoker(index):
  if len(index) == 1:
    return (index[0][0]+1)
  else:
    compare = index[0][1]
    

file = open("cards.txt", "r")
readFile(file, cards)
file.close()
introduction(cards,hands,scores)
