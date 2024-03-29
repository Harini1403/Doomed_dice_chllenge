def diceA(ele, length):
    if length == 0:
        return [[]]
    combinations = []
    for e in ele:
        for rest in diceA(ele, length - 1):
            combinations.append([e] + rest)
    return combinations

def diceB(ele, length, start=0):
    if length == 0:
        return [[]]
    combinations = []
    for e in ele[start:]:
        for rest in diceB(ele, length - 1, start):
            combinations.append([e] + rest)
    return combinations

def probSum(arr1, arr2):
    sum_prob = [0] * 12
    for i in arr1:
        for j in arr2:
            k = i + j
            sum_prob[k - 1] += 1.0
    sum_prob = [x / 36.0 for x in sum_prob if x != 0]
    return sum_prob

def transform(dieA, dieB):
    ele1 = [1, 2, 3, 4]
    length = 6
    combo1 = diceA(ele1, length)
    ele2 = [1, 2, 3, 4, 5, 6, 7, 8]
    combo2 = diceB(ele2, length)
    
    sum1 = probSum(dieA, dieB)
    
    for i in combo1:
        for j in combo2:
            if probSum(i, j) == sum1:
                print("New die_a:", *i)
                print("New die_b:", *j)
                return

    print("No matching combinations found.")

def main():
    dieA = [1, 2, 3, 4, 5, 6]
    dieB = [1, 2, 3, 4, 5, 6]
    print("PART-B- Answer\nThe new combination is:")
    transform(dieA, dieB)
    
if __name__ == "__main__":
    main()
