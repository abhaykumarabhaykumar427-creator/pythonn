print("Linear search")
array=[10,20,40,50,60]
key=int(input("Enter your search number : "))

for i in range(len(array)):
    if array[i]==key:
        print("found number ",array[i])
        break
    else:
        print("Not Found")
