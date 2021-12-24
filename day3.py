def solvePartA(data):
    digits = [{"0": 0, "1": 0} for _ in data[0]]
    for line in data:
        for i, digit in enumerate(line):
            digits[i][digit] += 1
    print(digits)
    gamma = "".join(["0" if curr["0"] > curr["1"] else "1" for curr in digits])
    epilson = "".join(["0" if curr == "1" else "1" for curr in gamma])
    gamma = convertBinaryToDecimal(gamma)
    epilson = convertBinaryToDecimal(epilson)
    return gamma * epilson
    
    
def convertBinaryToDecimal(binary):
    return int(binary, 2)


def solvePartB(data):
    filteredDataGreater = data.copy()    
    filteredDataLesser = data.copy()
    for i in range(len(data)):
        if len(filteredDataGreater) > 1:
            filteredDataGreater = filterDataGreater(filteredDataGreater, i)
            print(f"O2: {filteredDataGreater}")
        if len(filteredDataLesser) > 1:
            filteredDataLesser = filterDataLesser(filteredDataLesser, i)
            print(f"CO2: {filteredDataLesser}")
    oxygenRating = convertBinaryToDecimal(filteredDataGreater[0])
    co2Rating = convertBinaryToDecimal(filteredDataLesser[0])
            
    return oxygenRating * co2Rating
    

def filterDataGreater(data, i):
    digitCount = {"0": [0, []], "1": [0, []]}
    for line in data:
        if line[i] == "0":
            digitCount["0"][0] += 1
            digitCount["0"][1].append(line)
        else:
            digitCount["1"][0] += 1
            digitCount["1"][1].append(line)
    if digitCount["0"] > digitCount["1"]:
        return digitCount["0"][1]
    else:
        return digitCount["1"][1]
    
    
def filterDataLesser(data, i):
    digitCount = {"0": [0, []], "1": [0, []]}
    for line in data:
        if line[i] == "0":
            digitCount["0"][0] += 1
            digitCount["0"][1].append(line)
        else:
            digitCount["1"][0] += 1
            digitCount["1"][1].append(line)
    if digitCount["0"] < digitCount["1"]:
        return digitCount["0"][1]
    else:
        return digitCount["1"][1]


if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(solvePartA(data))
    print(solvePartB(data))
    