import random
import itertools
yourScore = 0
scores=[0]*8
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
    playAgain = ('Do you want to play again? Y/N\n')
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
    while len(YourHand) > 0:
        if yourScore == 25:
            return
        for i in scores:
            if i==25:
                return
        print('Your hand is:')
        HandCount=1
        for i in YourHand:
            print(str(HandCount)+ '.) ' + i[0] + " of " + i[1])
            HandCount+=1
        print()
        CardPlayed = int(input('Which card will you play this round? Answer from 1-' + str(len(YourHand)) + "\n"))
        print()
        card=YourHand[CardPlayed-1]
        winningCard = card
        winningCardSuit = winningCard[1]
        print("Your card played:")
        print(card[0]+" of " + card[1])
        print()
        del YourHand[CardPlayed-1]
        oppCount = 0
        oppList = [0]*len(listOfHands)
        for i in listOfHands:
            randint = random.randrange(0,len(listOfHands[1]))
            Count2 = 0
            for j in i:
                if j[1] == winningCardSuit and winningCardSuit == trumpCard[1]:
                    randint = i.index(j)
                if j[1] == winningCardSuit and j[1] != trumpCard[1]:
                    randint = i.index(j)
            oppList[oppCount]=i[randint]
            print("Opponent card played:")
            if (winningCard[0] == '5' and card[1]==trumpCard[1]):
                winningCard
                

            elif (i[randint][0] == '5' and i[randint][1]==trumpCard[1]):
                winningCard = i[randint]
                

            elif (winningCard[0] == 'Jack' and card[1]==trumpCard[1]):
                winningCard
                
                
            elif (i[randint][0] == 'Jack' and i[randint][1]==trumpCard[1]):
                winningCard = i[randint]
                


            elif (winningCard[0] == 'Ace' and card[1]=='Hearts'):
                winningCard
                

            elif (i[randint][0] == 'Ace' and i[randint][1]=='Hearts'):
                winningCard = i[randint]


            elif (winningCard[0] == 'Ace' and card[1]==trumpCard[1]):
                winningCard = card
                


            elif (i[randint][0] == 'Ace' and i[randint][1]==trumpCard[1]):
                winningCard = i[randint]
                


            elif (winningCard[0] == 'King' and card[1]==trumpCard[1]):
                winningCard
                


            elif (i[randint][0] == 'King' and i[randint][1]==trumpCard[1]):
                winningCard = i[randint]
                


            elif (winningCard[0] == 'Queen' and card[1]==trumpCard[1]):
                winningCard
                


            elif (i[randint][0] == 'Queen' and i[randint][1]==trumpCard[1]):
                winningCard = i[randint]
                
            elif (i[randint][1] == trumpCard[1] and winningCard[1] == trumpCard[1]):
                if (trumpCard[1]=='Spades') or trumpCard[1] == 'Clubs':
                    if int(i[randint][0]) < int(winningCard[0]):
                        winningCard = i[randint]
                else:
                    if int(i[randint][0]) > int(winningCard[0]):
                        winningCard = i[randint]

            elif (i[randint][1] == trumpCard[1] and winningCard[1] != trumpCard[1]):
                winningCard = i[randint]

            elif (i[randint][1] == winningCard[1]):
                if winningCard[0] == 'King':
                    winningCard
                elif i[randint][0] == 'King':
                    winningCard=i[randint]

                elif winningCard[0] == 'Queen':
                    winningCard

                elif i[randint][0] == 'Queen':
                    winningCard=i[randint]

                elif winningCard[0] == 'Jack':
                    winningCard
                elif i[randint][0] == 'Jack':
                    winningCard=i[randint]
            
                else:
                    if (winningCard[1]=='Spades') or winningCard[1] == 'Clubs':
                        if winningCard[0] == 'Ace':
                            winningCard
                        elif i[randint][0] == 'Ace':
                            winningCard=i[randint]
                        elif int(i[randint][0]) < int(winningCard[0]):
                            winningCard = i[randint]
                    else:
                        if winningCard[0] == 'Ace':
                            winningCard=i[randint]
                        elif i[randint][0]=='Ace':
                            winningCard
                        elif int(i[randint][0]) > int(winningCard[0]):
                                winningCard = i[randint]
                
            print(i[randint][0] + " of " +i[randint][1])
            print()
            oppCount+=1
            
            del i[randint]
        if winningCard == card:
            yourScore+=5
        print(winningCard)
        print()
        print("Your score: ", yourScore)
        print()
        print("Other scores: ")
        for i in range(len(oppList)):
            if winningCard == oppList[i]:
                scores[i]+=5
            print(scores[i])
        print()
main()
