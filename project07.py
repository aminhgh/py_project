# Binary Search
n = int(input("enter number of elements : "))

a = list(map(int,
	input("\nEnter the numbers : ").strip().split()))[:n]


def Binary_search(a , high , low , x ):
    if high >= low:
        mid = (high+low)//2
        if a[mid] == x:
            return mid
        elif arr[mid]>x:
            return Binary_search(a , low , mid-1 , x)
        else:
            return Binary_search(a , mid+1 , high ,x)

    else:
        return -1

b= int(input("enter you number want find : "))

result = Binary_search(a , len(a)-1,0,b)

if result != -1:
    print("your element is present ar index",str(result))

else:
    print("your element is NOT present at index",str(result))