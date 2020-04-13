# %% [markdown]
# Tạo bản đồ với n hòn đảo
coordinates = []
n = input("How many islands? ")
n = int(n)
for i in range(0, n):
    islands = input("Enter X and Y of island {}: ".format(i)).split()
    coordinates.append(islands)

# %% [markdown]
# Chọn đảo D1 và D2
D1_Index = int(input("Which islands do you want to choose for D1? (0-{})".format(n)))
D1 = coordinates[D1_Index]
D1
# %%
D2_Index = int(input("Which islands do you want to choose for D2? (0-{})".format(n)))
D2 = coordinates[D2_Index]
D2

# %% [markdown]
# Nhập khoảng cách dài nhất mà ca nô đi được
max_distance = int(input("Max distance that Canoe reach?(km) "))
max_distance
