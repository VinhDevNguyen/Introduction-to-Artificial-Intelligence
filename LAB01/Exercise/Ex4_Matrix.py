# Read data
data = open("LAB01/Exercise/Maps/map1.txt")
m, n = data.readline().split()
m = int(m)
n = int(n)
D1 = []
D2 = []
max_distance = int(data.readline())
Map_Matrix = []
for i in range(n):
    Map_Matrix.append(data.readline().rstrip('\n').split(' '))
    Map_Matrix[i] = [int(e) for e in Map_Matrix[i]]
print(Map_Matrix)

# Locate D1 and D2
for i in range(m):
    for e in range(n):
        if Map_Matrix[i][e] == 1:
            D1.append(i)
            D1.append(e)
        if Map_Matrix[i][e] == 2:
            D2.append(i)
            D2.append(e)
print(D1)
print(D2)