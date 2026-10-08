colors = ["red", "green", "blue"]

color = input("color: ").strip().lower()



if color in colors:
    print("Valid color")
else:
    print("Invalid color")
