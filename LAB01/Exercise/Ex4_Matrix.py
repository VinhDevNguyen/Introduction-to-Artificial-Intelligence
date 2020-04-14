# Read data
data = open("LAB01/Exercise/Maps/map1.txt")
m, n = data.readline().split()
m = int(m)
n = int(n)
max_distance = int(data.readline())
Map_Matrix = []
for i in range(n):
    Map_Matrix.append(data.readline().rstrip('\n').split(' '))
    Map_Matrix[i] = [int(e) for e in Map_Matrix[i]]
print(Map_Matrix)
