def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen


user_input = input("Enter currency in ($): ")

dollars = [int(x) for x in user_input.split(",")]

print("\nDollar($)\tPeso(P)\t\tYen(¥)")
for d in dollars:
    if d < 0:
        print("Negative value entered. Stopping.")
        break
    peso, yen = convert_currency(d)
    print(f"{d}\t\t{peso:.2f}\t\t{yen:.2f}")
