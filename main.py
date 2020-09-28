import random
import matplotlib.pyplot as plt
import numpy as np

# Lab 1 Example 1
# Sum of heads when flipping a coin using for loop
def coinFlipModel1():
    total_flips = 10000
    heads=0
    tails=0
    for i in range(total_flips):
        coin = round(random.random())
        if coin == 0:
            heads = heads+1
        else:
            tails = tails+1
    print("Number of heads: ",heads,".")

# Lab 1 Example 2
# Sum of heads and tails when flipping a coin using an array
def coinFlipModel2():
    total_flips = 10000
    heads = np.zeros((total_flips,1))
    for i in range(total_flips):
        heads[i,:] = round(random.random())
    print("Number of heads: ",sum(sum(heads)))
    print("Number of tails: ",sum(total_flips-sum(heads)))

# Lab 1 Example 3
# Histogram showing random distribution
def coinFlipHist():
    n = 50000
    x = np.zeros((n,1))
    for i in range(n):
        x[i,:] = random.random()
    #bins = np.arange(-1,1,0.1)
    bins = np.arange(-0.95, 0.95, 0.1)
    plt.hist(x,bins)
    plt.show()

# Lab 1 Example 4
# Histogram showing sum of two dice
def sumTwoDice():
    n = 100000
    d1 = np.zeros((n,1))
    d2 = np.zeros((n,1))
    for i in range(n):
        d1[i,:] = random.randint(1,6) # Create array of size 60 to hold rolls for die 1
    for i in range(n):
        d2[i,:] = random.randint(1,6) # Create array of size 60 to hold rolls for die 2
    s = d1+d2 # Create new array that adds the two dice rolls together
    b = range(1,15) ; sb = np.size(b)
    h1, bin_edges = np.histogram(s,bins=b)
    b1 = bin_edges[0:sb-1]
    #
    fig1 = plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Sum of two dice')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Number of occurences')
    fig1.savefig('Sum of two dice.jpg')
    #
    fig2 = plt.figure(2)
    p1 = h1/n
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    fig2.savefig('PMF of sum of two dice.jpg')

# Lab 1 Problem 1
# Generate a probability histogram of the number of rolls required of two dice before a sum of 7 appears
def rollTwoDiceUntil7():
    runs = 1000 # Do 1000 total simulations
    rollsPerRun = 60 # Each with a max of 60 rolls
    rollsTo7 = np.zeros((runs,1)) # Create array to hold number of rolls required to get sum of 7
    for i in range(runs): # loop 1000 times
        got7Yet = False
        for j in range(rollsPerRun):
            newRand1 = random.randint(1,6) # Roll 1-6
            newRand2 = random.randint(1,6) # Roll 1-6
            if (newRand1 + newRand2 == 7) and (got7Yet == False):
                rollsTo7[i] = j
                got7Yet = True
    myBins = range(1,62) # Create range from 1 to 62
    sizeOfBins = np.size(myBins) # Keep track of the size of the bins
    myHistogram, bin_edges = np.histogram(rollsTo7,bins=myBins) # Create array to hold values of histogram and array to hold bin edges
    xAxis = bin_edges[0:sizeOfBins-1] # Create array to display number of rolls it took to get a sum of 7
    #
    fig = plt.figure(1) # Create figure
    probabilities = myHistogram/rollsPerRun # Calculate prograbilities
    plt.stem(xAxis,probabilities) # Create stem graph
    plt.title('Stem plot - Number of rolls of two dice to get sum of 7') # Set title
    plt.xlabel('Sum of two dice') # Set x axis label
    plt.ylabel('Probability') # Set y axis label
    fig.savefig('P1 - PMF of two dice sum of 7.jpg') # Save graph to a file

# Lab Problem 2
# Generate an unfair six-sided die with the following probabilties [0.1,0.15,0.3,0.25,0.05,0.15]
def unfairSixSidedDie():
    n = 10000 # Perform 10,000 rolls
    rolls = np.zeros((n,1)) # Create array to hold value of each roll
    for i in range(n): # Loop 10,000 times
        newRand = random.randint(1,100) # Random number from 0 to 100
        if newRand <= 10: # 10% chance
            rolls[i,:] = 1 # Roll a 1
        elif newRand <= 25: # 15% chance (25=10+15)
            rolls[i,:] = 2 # Roll a 2
        elif newRand <= 55: # 30% chance (55=10+15+30)
            rolls[i,:] = 3 # Roll a 3
        elif newRand <= 80: # 25% chance (80=10+15+30+25) 
            rolls[i,:] = 4 # Roll a 4
        elif newRand <= 85: # 5% chance (85=10+15+30+25+5) 
            rolls[i,:] = 5 # Roll a 5
        elif newRand <= 100: # 15% chance (100=10+15+30+25+5+15) 
            rolls[i,:] = 6 # Roll a 6
    myBins = range(1,8) # Create range from 1 to 8
    sizeOfBins = np.size(myBins) # Keep track of size of the bins
    myHistogram, bin_edges = np.histogram(rolls,bins=myBins) # Create array to hold values of histogram and array to hold bin edges
    xAxis = bin_edges[0:sizeOfBins-1] # Create array to display occurance of each value
    #
    fig = plt.figure(1) # Create figure
    probabilities = myHistogram/n # Calculate prograbilities
    plt.stem(xAxis,probabilities) # Create stem graph
    plt.title('Stem plot - Probability of each value for unfair six-sided die') # Set title
    plt.xlabel('Die value') # Set x axis label
    plt.ylabel('Probability') # Set y axis label
    fig.savefig('P2 - PMF of unfair die.jpg') # Save graph to a file

# Lab Problem 3
# When 100 coins are tossed find the probability exactly 35 will be heads
def exactly35Heads():
    runs = 100000 # Do 100,000 total simulations
    flipsPerRun = 100 # Each with 100 coin tosses
    got35Heads = 0 # Create int to keep track of how many times there were exactly 35 heads
    for i in range(runs): # loop 100,000 times
        headCount = 0
        for j in range(flipsPerRun): # loop 100 times
            if random.randint(0,1) == 0:
                headCount = headCount+1
        if headCount == 35:
            got35Heads = got35Heads+1
    probability = got35Heads/runs
    print("Probability=",probability," (",got35Heads,"/",runs,")")

# Lab Problem 4
# Determine probability of "4 of a kind" in a 6-card poker draw
def FourOfAKind():
    runs = 100000 # Do 100,000 total simulations
    draws = 6 # Draw 6 cards per round
    gotFourOfAKind = 0
    for i in range(runs): # loop 100,000 times
        deck = np.array(['A','A','A','A', '2','2','2','2', '3','3','3','3', '4','4','4','4', '5','5','5','5', '6','6','6','6', '7','7','7','7', '8','8','8','8', '9','9','9','9', 'T','T','T','T', 'J','J','J','J', 'Q','Q','Q','Q', 'K','K','K','K']) # Create array to represent a deck of 13 different cards and 4 copies in the deck
        hand = [0,0,0,0,0,0,0,0,0,0,0,0,0] # Create array of size 13 initialized to 0 to represent 14 possible cards player could draw
        for j in range(draws):
            newRand = random.randint(0,deck.size-1) # Random number from 0 to last card in deck 
            newCard = deck[newRand] # Get the new card from the deck
            deck = np.delete(deck,[newRand]) # Remove new card from deck
            if newCard == 'A':
                hand[0] = hand[0]+1 # Add ace to player's hand
            elif newCard == '2':
                hand[1] = hand[1]+1 # Add two to player's hand
            elif newCard == '3':
                hand[2] = hand[2]+1 # Add three to player's hand
            elif newCard == '4':
                hand[3] = hand[3]+1 # Add four to player's hand
            elif newCard == '5':
                hand[4] = hand[4]+1 # Add five to player's hand
            elif newCard == '6':
                hand[5] = hand[5]+1 # Add six to player's hand
            elif newCard == '7':
                hand[6] = hand[6]+1 # Add seven to player's hand
            elif newCard == '8':
                hand[7] = hand[7]+1 # Add eight to player's hand
            elif newCard == '9':
                hand[8] = hand[8]+1 # Add nine to player's hand
            elif newCard == 'T':
                hand[9] = hand[9]+1 # Add ten to player's hand
            elif newCard == 'J':
                hand[10] = hand[10]+1 # Add jack to player's hand
            elif newCard == 'Q':
                hand[11] = hand[11]+1 # Add queen to player's hand
            elif newCard == 'K':
                hand[12] = hand[12]+1 # Add king to player's hand
        if np.isin(4,hand):
            gotFourOfAKind = gotFourOfAKind+1
    probability = gotFourOfAKind/runs # Calculate proability of getting four of a kind
    print("Probability=",probability," (",gotFourOfAKind,"/",runs,")")
            

# - - - - - - - - - - - - - -
# Uncomment to run a function
# - - - - - - - - - - - - - -
#coinFlipModel1()
#coinFlipModel2()
#coinFlipHist()
#sumTwoDice()
#rollTwoDiceUntil7()
#unfairSixSidedDie()
#exactly35Heads()
FourOfAKind()