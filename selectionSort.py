def selectionSort(selectionSortArr, size):
    for step in range(size):
        minIdx = step

        for idxStep in range(step + 1, size):
            if selectionSortArr[idxStep] < selectionSortArr[minIdx]:
                minIdx = idxStep

        (selectionSortArr[step], selectionSortArr[minIdx]) = (selectionSortArr[minIdx], selectionSortArr[step])

inputData = []
for element in range(5):
    if len(inputData) == 0:
        userInput = input("Bitte geben Sie eine Zahl ein: ")
    else:
        userInput = input("Bitte geben Sie eine weitere Zahl ein: ")

    inputData.append(userInput)

size = len(inputData)       

selectionSort(inputData, size)

print("Sortierte Eingabe nach Selection sort: ")
print(inputData)

