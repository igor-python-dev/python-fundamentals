favourite_places = []

print("Welcome to my favourite places in the world!\n")

#loop 1: collect the name of 4 places
while len(favourite_places) < 4:
     place = input(f"Place {len(favourite_places) +1}: ")
     favourite_places.append(place)

print("\n------ YOUR TOP PLACES ------")

for place in favourite_places:
     print(f"- {place}")

print(f"\nTotal Places: {len(favourite_places)}")