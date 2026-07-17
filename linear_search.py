arr = [5, 8, 12, 20, 30]

target = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
