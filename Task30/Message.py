a1 = int(input("Enter the first element: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of elements: "))

arr = [a1 + (i-1)*d for i in range(1, n+1)]

print("The array is:", arr)
