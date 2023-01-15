import random

drawCounter = 1

def lotto(numbers, draws):
    results = []
    poolOfMachine = [list for list in range(1,numbers+1,1)]
    for drawingNumber in range(1,draws+1,1):
        number = random.choice(poolOfMachine)
        while number in results:
            number = random.choice(poolOfMachine)
        results.append(number)
    results.sort()
    return results

def yourLotto(numbers, draws):
    yourLottoResults = []
    for number in range(1,draws+1,1):
        pickNumber = int(input("Choose a number of your draw: "))
        while pickNumber > numbers or pickNumber in yourLottoResults:
            print("Picked number is out of index or already picked this number.")
            pickNumber = int(input("Choose a number of your draw: ")) 
        yourLottoResults.append(pickNumber)
    yourLottoResults.sort()
    return yourLottoResults

howManyNumbers = int(input("Input numbers in the pool of machine: "))
numberOfDraws = int(input("Input number of draws: "))
while numberOfDraws >= howManyNumbers:
    print("Number of draws must have been less than numbers in the pool.")
    numberOfDraws = int(input("Input number of draws: "))

yourDraws = yourLotto(howManyNumbers,numberOfDraws)
print (yourDraws,"\n\nThe Machine pool is empty, please release the lock.\nAnd let's begin a draw.")
lottoDraws = lotto(howManyNumbers,numberOfDraws)
while yourDraws != lottoDraws:
    print(lottoDraws)
    print ("Oops! You didn't win the lottery. It's a trial number",drawCounter,"\n")
    lottoDraws = lotto(howManyNumbers,numberOfDraws)
    drawCounter+=1
print(lottoDraws)
print("Wow! You won millions of dollars!, You won a lottery after",drawCounter,"trials.")

