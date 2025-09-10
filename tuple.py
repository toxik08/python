row = int(input("Row: "))
col = int(input("Col: "))

nestedtuple = () 

for x in range(row):
    print(f"Row {x+1}")
    innerList = []
    for y in range(col):
        score = int(input(f"Enter score {y+1}: "))
        innerList.append(score)
    nestedtuple += (tuple(innerList),)  

print("\nNested Tuple:")
for z in nestedtuple:
    print(z)

search_value = int(input("\nEnter a score to search: "))
found = False

for i in range(row):
    for j in range(col):
        if nestedtuple[i][j] == search_value:
            print(f" Found {search_value} at Row {i+1}, Col {j+1}")
            found = True

if not found:
    print(f" {search_value} not found in the nested tuple.")
