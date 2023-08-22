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

list_1 = [10,20,30,20,20,20,50,40,40,60,5,10,1,30,30]

print(Repeat(list_1))

