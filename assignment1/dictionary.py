row = int(input("Row: "))
col = int(input("Col: "))

nested_dict = {}

for x in range(row):
    print(f"Row {x+1}")
    innerList = []
    for y in range(col):
        score = int(input(f"Enter score {y+1}: "))
        innerList.append(score)
    nested_dict[x+1] = tuple(innerList)

print("\nNested Dictionary (Formatted):")
for i in nested_dict:
    values = " ".join(str(v) for v in nested_dict[i])
    print(f"row {i}: {values}")

search_value = int(input("\nEnter a score to search: "))
found = False

for i in nested_dict:
    for j in range(len(nested_dict[i])):
        if nested_dict[i][j] == search_value:
            print(f" Found {search_value} at Row {i}, Col {j+1}")
            found = True

if not found:
    print(f" {search_value} not found in the dictionary.")
