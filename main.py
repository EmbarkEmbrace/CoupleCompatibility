print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

Lowercase_names  = name1.lower() + name2.lower()

T = Lowercase_names.count("t")
R = Lowercase_names.count("r")
U = Lowercase_names.count("u")
E = Lowercase_names.count("e")
True_final = T + R + U + E

L = Lowercase_names.count("l")
O = Lowercase_names.count("o")
V = Lowercase_names.count("v")
E = Lowercase_names.count("e")
Love_final = L + O + V + E

Answer = str(True_final) + str(Love_final)
Score = int(Answer)

if Score < 10 or Score > 90:
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif Score > 40 and Score < 50:
    print(f"Your score is {Score}, you are alright together.")
else:
    print(f"Your score is {Score}.")