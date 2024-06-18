color_to_code = {"Blue Green": "#0d98ba", "Chocolate": "#d2691e", "Deep Peach": "#ffcba4", "Greenyellow": "#adff2f",
                 "Lightblue": "#add8e6", "Medium Aquamarine": "#66ddaa", "Olivine": "#9ab973", "Pear": "#d1e231",
                 "Red Orange": "#ff5349", "Skyblue": "#87ceeb"}

color_width = max((len(color) for color in color_to_code.keys()))
for color, code in color_to_code.items():
    print(f"{color:{color_width}} is {code}")


choice = input("Enter a color: ").title()
while choice != "":
    if choice in color_to_code:
        print(f"The code of {choice} is {color_to_code[choice]}")
    else:
        print("Invalid input.")
    choice = input("Enter a color: ").title()
