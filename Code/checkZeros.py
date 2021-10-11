filePath = '/Users/bruceymac/Documents/CTF-Writeup/Code/data.dat'
cnt = 0

with open(filePath) as file:
    Lines = file.readlines()
    for line in Lines:
        zero = line.count('0')
        one = line.count('1')
        if (zero % 3 == 0) or (one % 2 == 0):
            cnt += 1

print("CTFLearn{{{}}}".format(cnt))
