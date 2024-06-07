import random
KHADKHADEY = {
    1: "Jhandi",
    2: "Burja",
    3: "Ita",
    4: "Pana",
    5: "Hukum",
    6: "Chidi"
}
faceCount = 6
rollCount = 6

def singleDiceRoll(faceCount):
    return random.randint(1,faceCount)

def checkMatch(dict, key1, key2):
    if dict[key1] == dict[key2]:
        return True
    return False

def generateRolls(rollCount, faceCount):
    rollRet = []
    for i in range(rollCount):
        rollRet.append(singleDiceRoll(faceCount))
    
    return rollRet
def findTotalMatchInAList(givenList):
    matchCounts = {}
    listOf = generateRolls(rollCount, faceCount)
    for i in listOf:
        if i in matchCounts:
            matchCounts[i] += 1
        else:
            matchCounts[i] = 1
    return matchCounts
    
    
#Reward
def calculateReward(bets, matchCounts):
    rewards = {}
    for symbol, amount in bets.items():
        face = next(key for key, value in KHADKHADEY.items() if value == symbol)
        if matchCounts.get(face, 0) > 1:
            rewards[symbol] = amount * matchCounts[face]
        else:
            rewards[symbol] = 0
    return rewards

# print(findTotalMatchInAList(generateRolls(rollCount, faceCount)))
def GameManager(playerCount):
    # Generate dice rolls
    rolls = generateRolls(rollCount, faceCount)
    print("Dice Rolls:", [KHADKHADEY[roll] for roll in rolls])
    
    # Find total matches
    matchCounts = findTotalMatchInAList(rolls)
    
    # Convert matches to readable format
    readable_matches = {KHADKHADEY[key]: value for key, value in matchCounts.items()}
    print("Match Counts:", readable_matches)
    
    # Example bets
    bets = {
        "Jhandi": 5,
        "Burja": 10
    }
    
    # Calculate rewards
    rewards = calculateReward(bets, matchCounts)
    print("Rewards:", rewards)

# Example usage with one player
GameManager(1)