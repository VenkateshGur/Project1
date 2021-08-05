from itertools import product
def outcome(n):
    count = 0
    count1 = 0
    sample = [''.join(i) for i in list(product(['p','a'],repeat = n))]
    for i in sample:
        if 'aaaa' not in i:
            count += 1
    print(len(sample))
    print(count)
    sample1 = [''.join(i) for i in list(product(['p','a'],repeat = n-1))]
    for i in sample1:
        if 'aaaa' not in i:
            count1 += 1
    print(len(sample1))
    print(count1)
    outcomes = f'{count - count1}/{count}'
    return "Outcome:",outcomes
n = int(input("Enter the number of days:"))
occurance = outcome(n)
print("Occurrance:",occurance)