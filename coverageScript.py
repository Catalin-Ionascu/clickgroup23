def parseFile(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    numberOfBranches = 0
    IDset = set()

    for line in lines:
        if "Number of branches" in line:
            numberOfBranches = int(line.split()[0])
        elif "ID Branch was hit" in line:
            uniqueID = int(line.split()[0])
            IDset.add(uniqueID)

    return numberOfBranches, len(IDset)

def coveragePrint(path):
    numberOfTotalBranches, numberOfHitBranches = parseFile(path)
    if numberOfTotalBranches != 0:
        coverage = numberOfHitBranches / numberOfTotalBranches * 100
        print(path)
        print(f"Number of branches hit: {numberOfHitBranches}")
        print(f"Coverage: {(int)(coverage)}%")
        print()
    else:
        print(path)
        print("Number of branches hit: 0")
        print("Coverage: 0%")
        print()

path = 'coverageASCII.out'
coveragePrint(path)
path = 'coverageGETTEXT.out'
coveragePrint(path)
path = 'coverage_is_binary_reader.out'
coveragePrint(path)
path = 'coverage_is_binary_writer.out'
coveragePrint(path)
path = 'coverge_make_str.out'
coveragePrint(path)
path = 'coverage_should_strip_ansi.out'
coveragePrint(path)
path = '_get_error_message.txt'
coveragePrint(path)
path = 'core__getattr__.txt'
coveragePrint(path)
