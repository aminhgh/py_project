#func  -list - for in for - find repeated number  : 

def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        count = i+1
        for j in range(count,size):
            if x[i] == x[j] not in repeated:
                repeated.append(x[i])
    return repeated

# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int,
	input("\nEnter the numbers : ").strip().split()))[:n]




print(a)

print(Repeat(a))

