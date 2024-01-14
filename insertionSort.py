def insertionSort(insertionSortArr):
    for step in range(1, len(insertionSortArr)):
        key = insertionSortArr[step]
        j = step -1

        while j >= 0 and key < insertionSortArr[j]:
            insertionSortArr[j + 1] = insertionSortArr[j]
            j = j - 1

            insertionSortArr[j +1 ] = key

inputData = []
for element in range(5):
    if len(inputData) == 0:
        userInput = input("Bitte geben Sie eine Zahl ein: ")
    else:
        userInput = input("Bitte geben Sie eine weitere Zahl ein: ")

    inputData.append(userInput)    

insertionSort(inputData)

print("Sortiertes Eingabe in aufsteigender Reihenfolge: ")
print(inputData)