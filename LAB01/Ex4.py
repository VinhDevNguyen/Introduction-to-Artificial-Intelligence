# %% [markdown]
# Tạo bản đồ với n hòn đảo
coordinates = []
n = input("How many islands?")
n = int(n)
for i in range(0, n):
    islands = input("Enter X and Y").split()
    coordinates.append(islands)
