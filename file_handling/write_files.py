with open("sometext.txt", "a") as f:
    f.write("\nHello, my name is Ali!")
with open("sometext.txt") as f:
    print(f.read())
