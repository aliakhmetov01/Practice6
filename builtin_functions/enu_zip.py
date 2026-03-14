students = ["Ali", "Hussain", "Layla", "Hafsa"]
nicknames = ["SwordShadow", "NeverLose", "CuteCat", "UmmZainab"]

players_data = list(zip(students, nicknames))

print(f"{"Team: Veterans":<25} | {"nick":<15}")
print("-"*45)
for i, (name, nickname) in enumerate(players_data):
    print(f"{i}: {name:<22} | {nickname:<15}")