name = input("Name: ").strip()

if name.startswith("S") or name.startswith("s"):
    print(f"Name starts with {name[0]}")
else:
    print("Name does not start with S")