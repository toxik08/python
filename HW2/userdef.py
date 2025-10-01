def char_frequency(txt):
    fdict = {}
    for char in txt:
        if char.isalpha():
            if char in fdict:
                fdict[char] += 1
            else:
                fdict[char] = 1
    return fdict


input_str = input("Enter string: ")

parts = input_str.split(",")

for part in parts:
    word = part.strip()
    result = char_frequency(word)
    output = []
    for k, v in result.items():
        output.append(f"{k}={v}")
    print(", ".join(output))
