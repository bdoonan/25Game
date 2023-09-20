import random
import itertools
yourScore = 0
scores=[0]*8
winningCard = [0]*1
winningCardSuit = ""
def main():
    numOfPlayers=11
    global yourScore
    while (numOfPlayers>9 or numOfPlayers<3):
        numOfPlayers=int(input("How many players will be playing? At least 3 are required and 9 is the maximum\n"))
    
    print("New Game\n")
        
    while(yourScore<25) and (scores[0]<25) and (scores[1]<25) and (scores[2]<25) and (scores[3]<25) and (scores[4]<25) and (scores[5]<25) and (scores[6]<25) and (scores[7]<25):
        list2=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        deck=list(itertools.product(list2,['Hearts','Spades','Clubs','Diamonds']))
        Shuffle(deck)
        dealCards(deck,numOfPlayers)
        
    if yourScore == 25:
        print('You win\n')
    else:
        print ("You lose\n")
    playAgain = input('Do you want to play again? Y/N\n')
    yourScore = 0
    for i in range(len(scores)):
        scores[i] = 0
    if playAgain == 'Y':
        main()
def Shuffle(deck):
    random.shuffle(deck)

def dealCards(deck, numOfPlayers):
    listOfHands=[0]*numOfPlayers
    for i in range(numOfPlayers):
        Hand = [0]*5
        for j in range(5):
            Hand[j]=deck[j]
            del deck[j]
            
            
        listOfHands[i]=Hand
    
    trumpCard=deck[0]
    Game(listOfHands, trumpCard)
def Game(listOfHands, trumpCard):
    global yourScore
    global scores
    print("The trump card is:", trumpCard)
    YourHand=listOfHands[0]
    del listOfHands[0]
    print("Your hand is:")
    HandCount=1
    for i in YourHand:
        print(str(HandCount)+ '.) ' + i[0] + " of " + i[1])
        HandCount+=1
    print()
    for i in YourHand:
        if (i[0]=='Ace' and i[1]==trumpCard[1]) or trumpCard[0] == 'Ace':
            TopCardResponse = input("Would you like to take the top card? Y/N\n")
            if TopCardResponse=='Y':
                Trade = int(input('Which card would you like to replace? Answer from 1-5 from the top card to the bottom card\n'))
                YourHand[Trade-1]=trumpCard
                print('Your new hand is:')
                for i in YourHand:
                    print(i[0] + " of " + i[1])
                print()
                break
            else:
                break
    Pos=0
    handSize=6
    while len(YourHand) > 0:
        handSize-=1
        print ("New Round")
        if yourScore == 25:
                return
        for i in scores:
                if i==25:
                    return
        global winningCard
        global winningCardSuit
        oppCount = 0
        oppList = [0]*len(listOfHands)
        if Pos==0:
            
            print('Your hand is:')
            HandCount=1
            for i in YourHand:
                print(str(HandCount)+ '.) ' + i[0] + " of " + i[1])
                HandCount+=1
            print()
            print("Major suit: " + trumpCard[1])
            CardPlayed = int(input('Which card will you play this round? Answer from 1-' + str(len(YourHand)) + "\n"))
            print()
            card=YourHand[CardPlayed-1]
            winningCard = card
            winningCardSuit = winningCard[1]
            print("Your card played:")
            print(card[0]+" of " + card[1])
            print()
            del YourHand[CardPlayed-1]
            startInt = 0
            endInt=(len(listOfHands))
            playHand(trumpCard,listOfHands, startInt, endInt, oppCount, oppList, handSize)
            if winningCard == card:
                yourScore+=5
                Pos=0
            print()
            print("Your score: ", yourScore)
            print()
            print("Other scores: ")
            for i in range(len(oppList)):
                if winningCard == oppList[i]:
                    scores[i]+=5
                    Pos=i+1
                print("Player ", i+2, " score: ",scores[i])
            print() 
        else:
            if len(listOfHands[Pos-1])==0:
                randintStart=0
            else:
                randintStart=random.randrange(0,len(listOfHands[Pos-1]))
            card = listOfHands[Pos-1][randintStart]
            oppList[Pos-1] = card
            winningCard = card
            winningCardSuit = winningCard[1]
            print("Player", Pos+1, "card played: "+card[0]+" of " + card[1])
            print()
            del listOfHands[Pos-1][randintStart]
            oppCount = Pos-1
            startInt = Pos
            endInt=(len(listOfHands))
            playHand(trumpCard,listOfHands, startInt, endInt, oppCount, oppList,handSize)
            oppCount=0
            print("Major suit: " + trumpCard[1])
            if card[1] != trumpCard[1]:
                print("Minor suit: " + card[1])
            print ("Current winning card: " + winningCard[0] + " of " + winningCard[1])
            print()
            print('Your hand is:')
            HandCount=1
            for i in YourHand:
                print(str(HandCount)+ '.) ' + i[0] + " of " + i[1])
                HandCount+=1
            print()
            CardPlayed = int(input('Which card will you play this round? Answer from 1-' + str(len(YourHand)) + "\n"))
            yourCard = YourHand[CardPlayed-1]
            for i in YourHand:
                if card[1] == trumpCard[1] and i[1] == trumpCard[1]:
                    while yourCard[1] != i[1]:
                        CardPlayed = int(input('Which card will you play this round? Answer from 1-' + str(len(YourHand)) + ". This card must be a " + trumpCard[1] + "\n"))
                        yourCard = YourHand[CardPlayed-1]
                elif i[1] == card[1]:
                    while yourCard[1] != i[1] and yourCard[1] != trumpCard[1]:
                        CardPlayed = int(input('Which card will you play this round? Answer from 1-' + str(len(YourHand)) + ". This card must be a " + i[1] + " or a " + trumpCard[1] + "\n"))
                        yourCard = YourHand[CardPlayed-1]
            del YourHand[CardPlayed-1]
            print("Your card played: " + yourCard[0] + " of " + yourCard[1])
            if (winningCard[0] == '5' and winningCard[1]==trumpCard[1]):
                winningCard
                
                    
            elif (yourCard[0] == '5' and yourCard[1]==trumpCard[1]):
                winningCard = yourCard
                

            elif (winningCard[0] == 'Jack' and winningCard[1]==trumpCard[1]):
                winningCard
                
                
            elif (yourCard[0] == 'Jack' and yourCard[1]==trumpCard[1]):
                winningCard = yourCard
                


            elif (winningCard[0] == 'Ace' and winningCard[1]=='Hearts'):
                winningCard
                

            elif (yourCard[0] == 'Ace' and yourCard[1]=='Hearts'):
                winningCard = yourCard
                

            elif (winningCard[0] == 'Ace' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (yourCard[0] == 'Ace' and yourCard[1]==trumpCard[1]):
                winningCard = yourCard
                


            elif (winningCard[0] == 'King' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (yourCard[0] == 'King' and yourCard[1]==trumpCard[1]):
                winningCard = yourCard
                


            elif (winningCard[0] == 'Queen' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (yourCard[0] == 'Queen' and yourCard[1]==trumpCard[1]):
                winningCard = yourCard
                
                
            elif (yourCard[1] == trumpCard[1] and winningCard[1] == trumpCard[1]):
                if (trumpCard[1]=='Spades') or trumpCard[1] == 'Clubs':
                    if int(yourCard[0]) < int(winningCard[0]):
                        winningCard = yourCard
                        
                else:
                    if int(yourCard[0]) > int(winningCard[0]):
                        winningCard = yourCard
                        

            elif (yourCard[1] == trumpCard[1] and winningCard[1] != trumpCard[1]):
                winningCard = yourCard
                

            elif (yourCard[1] == winningCard[1]):
                if winningCard[0] == 'King':
                    winningCard
                elif yourCard[0] == 'King':
                    winningCard=yourCard
                    
                elif winningCard[0] == 'Queen':
                    winningCard

                elif yourCard[0] == 'Queen':
                    winningCard=yourCard
                    
                elif winningCard[0] == 'Jack':
                    winningCard
                elif yourCard[0] == 'Jack':
                    winningCard=yourCard
            elif (yourCard[1] != winningCard[1]):
                winningCard
                    
            else:
                    if (winningCard[1]=='Spades') or winningCard[1] == 'Clubs':
                        if winningCard[0] == 'Ace':
                            winningCard
                        elif yourCard[0] == 'Ace':
                            winningCard=yourCard
                            
                        elif int(yourCard[0]) < int(winningCard[0]):
                            winningCard = yourCard
                            
                    else:
                        if winningCard[0] == 'Ace':
                            winningCard=yourCard
                            
                        elif yourCard[0]=='Ace':
                            winningCard
                        elif int(yourCard[0]) > int(winningCard[0]):
                                winningCard = yourCard
            if Pos !=1:
                startInt = 0
                endInt = Pos-1
                playHand(trumpCard,listOfHands, startInt, endInt, oppCount, oppList, handSize)
            if winningCard == yourCard:
                yourScore+=5
                Pos=0
            print()
            print("Your score: ", yourScore)
            print()
            print("Other scores: ")
            for i in range(len(oppList)):
                if winningCard == oppList[i]:
                    scores[i]+=5
                    Pos=i+1
                print("Player ", i+2, " score: ",scores[i])
            print() 

                    
            
            
        
def playHand(trumpCard,listOfHands, startInt, endInt, oppCount, oppList, handSize):
    global winningCard
    global winningCardSuit
    for i in range(startInt,endInt):
            if len(listOfHands[i])==0:
                   randint=0
            else:     
                randint = random.randrange(0,len(listOfHands[i]))
            for j in listOfHands[i]:
                if j[1] == winningCardSuit and winningCardSuit == trumpCard[1]:
                    randint = listOfHands[i].index(j)
                if j[1] == winningCardSuit and j[1] != trumpCard[1]:
                    randint = listOfHands[i].index(j)
            currCard=listOfHands[i][randint]
            del listOfHands[i][randint]
            oppList[oppCount]=currCard
            print("Player", i+2,"card played:", currCard[0] + " of " +currCard[1])
            if (winningCard[0] == '5' and winningCard[1]==trumpCard[1]):
                winningCard
                
                    
            elif (currCard[0] == '5' and currCard[1]==trumpCard[1]):
                winningCard = currCard
                

            elif (winningCard[0] == 'Jack' and winningCard[1]==trumpCard[1]):
                winningCard
                
                
            elif (currCard[0] == 'Jack' and currCard[1]==trumpCard[1]):
                winningCard = currCard
                


            elif (winningCard[0] == 'Ace' and winningCard[1]=='Hearts'):
                winningCard
                

            elif (currCard[0] == 'Ace' and currCard[1]=='Hearts'):
                winningCard = currCard
                

            elif (winningCard[0] == 'Ace' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (currCard[0] == 'Ace' and currCard[1]==trumpCard[1]):
                winningCard = currCard
                


            elif (winningCard[0] == 'King' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (currCard[0] == 'King' and currCard[1]==trumpCard[1]):
                winningCard = currCard
                


            elif (winningCard[0] == 'Queen' and winningCard[1]==trumpCard[1]):
                winningCard
                


            elif (currCard[0] == 'Queen' and currCard[1]==trumpCard[1]):
                winningCard = currCard
                
                
            elif (currCard[1] == trumpCard[1] and winningCard[1] == trumpCard[1]):
                if (trumpCard[1]=='Spades') or trumpCard[1] == 'Clubs':
                    if int(currCard[0]) < int(winningCard[0]):
                        winningCard = currCard
                        
                else:
                    if int(currCard[0]) > int(winningCard[0]):
                        winningCard = currCard
                        

            elif (currCard[1] == trumpCard[1] and winningCard[1] != trumpCard[1]):
                winningCard = currCard
                

            elif (currCard[1] == winningCard[1]):
                if winningCard[0] == 'King':
                    winningCard
                elif currCard[0] == 'King':
                    winningCard=currCard
                    
                elif winningCard[0] == 'Queen':
                    winningCard

                elif currCard[0] == 'Queen':
                    winningCard=currCard
                    
                elif winningCard[0] == 'Jack':
                    winningCard
                elif currCard[0] == 'Jack':
                    winningCard=currCard
            elif (currCard[1] != winningCard[1]):
                winningCard
                    
            else:
                    if (winningCard[1]=='Spades') or winningCard[1] == 'Clubs':
                        if winningCard[0] == 'Ace':
                            winningCard
                        elif currCard[0] == 'Ace':
                            winningCard=currCard
                            
                        elif int(currCard[0]) < int(winningCard[0]):
                            winningCard = currCard
                            
                    else:
                        if winningCard[0] == 'Ace':
                            winningCard=currCard
                            
                        elif currCard[0]=='Ace':
                            winningCard
                        elif int(currCard[0]) > int(winningCard[0]):
                                winningCard = currCard
                                
                
            print()
            oppCount+=1
            

main()
