import random
import cardHolder
from time import sleep
#imports libraries and file

romanticDivination = False
horseShoeSpread = False
celticCrossSpread = False
threeCardSpread = False
careerDivination = False
#Checks that all spreads are false when starting program

#list of cards to shuffle deck and pull randomly
def divination():
    for i in range(5):
        random.shuffle(cardHolder.deck)
        #shuffles cards and pulls the top card from the deck

    #creates a newdeck based on the first few cards in the spread and copies the information over    
    newDeck = cardHolder.deck[0:spread].copy()
    sleep(1)
    #for every card and line number in the newdeck get the value of its position
    #based on the position in the new deck if the spread is marked true print this value at that specific position
    for i,card in enumerate(newDeck):
        if careerDivination == True:
            if i == 0:
                print("The first card represents your current job or situation")
            if i == 1:
                print("The second card represents any challenges or obstacles ")
            if i == 2:
                print("The third card represents potential opportunities or new directions")
            if i == 3:
                print("The fourth card represents your strengths and skills")
            if i == 4:
                print("The fifth card represents the likely outcome or next steps.")          
        if threeCardSpread == True:
            if i == 0:
                print("the first card represents your past")
            if i == 1:
                print("the secound card represents your present")
            if i == 2:
                print("the third card represents your future")
        if celticCrossSpread == True:
            if i == 0:
                print("The first card represents your current situation")
            if i == 1:
                print("The second card represents any obstacles or challenges that may be in the way")
            if i == 2:
                print("The third card represents any potential opportunities")
            if i == 3:
                print("The fourth card represents the foundation of the situation")
            if i == 4:
                print("The fifth card represents the past")
            if i == 5:
                print("The sixth card represents the future")
            if i == 6:
                print("The seventh card represents your attitude towards the situation")
            if i == 7:
                print("The eighth card represents other people’s attitudes")
            if i == 8:
                print("The ninth card represents your hopes and fears")
            if i == 9:
                print("The tenth card represents the likely outcome")
        if horseShoeSpread == True:
            if i == 0:
                print('The first card represents the past')
            if i == 1:
                print('The second card represents the present')
            if i == 2:
                print('The third card represents the future ')
            if i == 3:
                print('The fourth card represents your hopes and fears')
            if i == 4:
                print('The fifth card represents external factors that may be affecting the situation')
            if i == 5:
                print('The sixth card represents advice or guidance')
            if i == 6:
                print('The seventh card represents the likely outcome.')
        if romanticDivination == True:
            if i == 0:
                print('The first card represents you')
            if i == 1:
                print('The second card represents the other person in the relationship')
            if i == 2:
                print('The third card represents the relationship itself')
            if i == 3:
                print('The fourth card represents the strengths of the relationship')
            if i == 4:
                print('The fifth card represents the weaknesses of the relationship')
            if i == 5:
                print('The sixth card represents what needs to be done to improve the relationship')
            if i == 6:
                print('The seventh card represents the likely outcome')
        #when printing the card seperate the quotations and wait 4 secounds before going to next card
        print(card, sep = ' ')
        sleep(4)
    #pulls out cards based on the spread

spread = 0
#how many cards will be pulled

Question = input("What would you like to ask the tarot cards ")
#prompt user with a question for the cards
wordCatcher = Question.split()
#split the input words in wordcatcher to be read individually


if 'lover' in wordCatcher or 'partner' in wordCatcher or 'love' in wordCatcher or 'romance' in wordCatcher:
    print('we will do a romantic divination')
    romanticDivination = True
    spread = 7
    divination()
        
elif 'money' in wordCatcher or 'finance' in wordCatcher or 'job' in wordCatcher or 'career' in wordCatcher:
    print('we will do a career divination')
    careerDivination = True
    spread = 5
    divination()
elif 'worried' in wordCatcher or 'troubled' in wordCatcher or 'future' in wordCatcher:
    print('we will do a three card spread')
    threeCardSpread = True
    spread = 3
    divination()
elif  'unsure' in wordCatcher or 'curious' in wordCatcher or 'wonder' in wordCatcher or 'uncertain' in wordCatcher or 'celtic' in wordCatcher:
    print('we will do a celtic cross spread')
    spread = 10
    celticCrossSpread = True
    divination()
else:
    print('we will do a horseshoe spread')
    horseShoeSpread = True
    spread = 7
    divination()
#if one of the specific words are in an if statement run divination function


    
