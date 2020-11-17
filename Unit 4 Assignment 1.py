structure = {'1': ['2', '3'], '2': ['4', '5'], '3': ['4', '5'], '4': ['5'], '5': ['1']}

completePath = []

def main():
    # Code Here
    print('Depth First Search', recursiveDFS(structure, '3', completePath))
    print('Breadth First Search', interativeBFS(structure, '3', completePath))
    print("There are no issues with running the program in PyCharm")


def recursiveDFS(structure, nodeStart, completePath):
    completePath = completePath + [nodeStart]
    print(completePath)

    for node in structure[nodeStart]:
        if not node in completePath:
            completePath = recursiveDFS(structure, node, completePath)
        return completePath


def interativeBFS(structure, nodeStart, completePath):
    x = [nodeStart]

    while x:
        print(x)
        firstNode = x.pop(0)

        if not firstNode in completePath:
            completePath = completePath + [firstNode]
            x = x + structure[firstNode]

    return completePath


main()
