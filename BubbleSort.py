def bubbleSort(bubbleSortArr):
    for accessElement in range(len(bubbleSortArr)):
        for compareElement in range(0, len(bubbleSortArr) - accessElement - 1):
            if bubbleSortArr[compareElement] > bubbleSortArr[compareElement + 1 ]:
                temp = bubbleSortArr[compareElement]
                bubbleSortArr[compareElement] = bubbleSortArr[compareElement + 1 ]
                bubbleSortArr[compareElement + 1 ] = temp


inputData = []
for element in range(5):
    if len(inputData) == 0:
        userInput = input("Bitte geben Sie eine Zahl ein: ")
    else:
        userInput = input("Bitte geben Sie eine weitere Zahl ein: ")
    
    inputData.append(userInput)

        

bubbleSort(inputData)

print("Sortierte Eingabe nach bubbleSort: ")
print(inputData)