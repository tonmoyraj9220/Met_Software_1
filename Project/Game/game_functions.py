import json
import os
import random
from classes import Items, Rooms, Player


# This fucntion asks for the players age
def ask_age():
    """Keep asking until the player types a whole number."""
    while True:
        text = input("Enter Player Age: ").strip()
        if text.isdigit():
            return int(text)
        print("Please type your age as a number.")

# The scenarios/ways the game can end
def game_paths():
    return{
        "A": {"name": "Science", "place": "Townhall", 
          "items": ["lab report", "owl photo"]},
        "B": {"name": "Community", "place": "Townhall",
              "items": ["petition sheet", "festival poster", "megaphone"]},
        "C": {"name": "Restoration", "place": "Sea Shore", 
              "items": ["shovel", "tree saplings", "filter net"]}
    }

# reading files from the file directory
def read_file(file_name):
    try:
        with open(os.path.join(base_dir, file_name)) as file:
            return file.read()
    except FileNotFoundError:
        return f"missing file: {file_name}"

# Rooms and the items found in the rooms.
def surroundings():
    village = Rooms("Village", "A small village beside the sea, seagulls soaring over your head.")
    town_hall = Rooms("Townhall", "The hall where the village council meets.")
    river = Rooms("River Bank", "The river water is  muddy brown river flowing towards the bay.")
    sea_shore = Rooms("Sea Shore", "Dead fish piled-up along the shore")
    camp = Rooms("Logging Camp", "Loud machines and piles of cut-down trees")
    clearing = Rooms("Forest Clearing", "A clearing in the forest where only the tree stumps are left along with mud.")
    nest = Rooms("Owl Nest", "An old tree with a hole in its trunk.")

    village.items = [Items("petition sheet"), Items("festival poster")]
    river.items = [Items("water sample kit"), Items("shovel")]
    sea_shore.items = [Items("filter net")]
    camp.items = [Items("megaphone")]
    clearing.items = [Items("tree saplings")]
    nest.items = [Items("owl photo")]

    # Connectin rooms.
    village.connect(town_hall)
    village.connect(river)
    river.connect(sea_shore)
    river.connect(camp)
    camp.connect(clearing)
    clearing.connect(nest)

    all_rooms = [village, town_hall, river, sea_shore, camp, clearing, nest]
    # this is returning the name of the room as string
    return{room.name: room for room in all_rooms}

# weather
def get_weather(days_left):
    if days_left == 2:
        return "A storm is coming."
    elif days_left == 1:
        return "It's raining heavily."
    else:
        options = [
            "The sun is out and sea is also calm.",
            "The sky is cloudy and lightly raining.",
            "It's a foggy day, with low visibility.",
            "The day is windy, cold air flowing from the North."
        ]
        return random.choice(options)

# List the items with an adjacent number to select item.
def select_an_option(options, prompt):
    for number, option in enumerate(options, start=1):
        print(f"[{number}] {option}")
    answer = input(prompt).strip()
    if answer.isdigit() and 1 <= int(answer) <= len(options):
        return int(answer)-1
    return None

# Prints Player info.
def status(player):
    print(f"Player Name: {player.name} | Location: {player.location.name} | Days Left: {player.days_left}")

# Prints the main menu.
def menu():
    print("\n----Main Menu----")
    print("\n[1] Look around.")
    print("[2] Move to another place.")
    print("[3] Pick up an item.")
    print("[4] Check your backpack.")
    print("[5] Test the water.")
    print("[6] Check the weather.")
    print("[7] Try to finish the game.")
    print("[exit] Quit the game")

# Print room desciption and list items in the room.
def look_around(player):
    room = player.location
    print(f"\n{room.name}: {room.description}")
    
    if room.items:
        print("You see:", ", ".join(item.name for item in room.items))
    
    else:
        print("There is nothing useful here.")

    print("Paths lead to:", ", ".join(next_room.name for next_room in room.routes))

# Move to a different room.
def switch_rooms(player):
    print("\nWhere do you want to go?")
    names = [room.name for room in player.location.routes]
    choice = select_an_option(names, "\nChoose a number: ")

    if choice is None:
        print("\nYou stay where you are.")

    else:
        player.move(player.location.routes[choice])
        print(f"\nYou travel to {player.location.name}. One day passes.")

# Pickup item from a room.
def pick_up(player):
    items = player.location.items
    if not items:
        print("\nThere is nothing to pick up here.")
        return
    print("\nWhat do you want to pick up?")
    names = [item.name for item in items]
    choice = select_an_option(names, "\nChoose a number: ")
    if choice is None:
        print("\nYou picked up nothing.")

    else:
        item = items[choice]
        player.collect(item)
        print(f"\nYou put the {item.name} in your backpack")

# Prints out the list of items in players backpack.
def inventory(player):
    if not player.items:
        print("\nYour backpack is empty.")

    else:
        print("\nItems in your backpack:")
        for item in player.items:
            print(" -", item.name)

# Test the river water.
def test_water(player):
    if player.location.name != "River Bank":
        print("\nYou need to be at the river bank to take a water sample.")

    elif not player.has_item("water sample kit"):
        print("\nYou do not have a water sample kit.")

    else:
        player.items = [item for item in player.items if item.name != "water sample kit"]
        player.items.append(Items("lab report"))
        player.collected.append("lab report")
        player.days_left -= 1
        print("\nThe test takes a day. The water is full of mud and chemicals.")
        print("The report proves the damage comes from upstream!")

# This functions checks if the player meets the requirement for game completion.
def check_endinng(player):
    game_path = game_paths()
    for letter, path in game_path.items():
        place = player.location.name == path["place"]
        everything_needed = all(player.has_item(name) for name in path["items"])
        if place and everything_needed:
            return letter
    return None

# If the requirements are met this function ends the game.
def end_game(letter):
    if letter == "A":
        print("\nYou present the lab report and owl photo to the village council at Townhall.")
        print("The evidence is clear and the logging is stopped by law")

    elif letter == "B":
        print("\nWith the megaphone you gather the whole village.")
        print("Hundreds sign the petition and the logging company backs down")

    else:
        print("\nYou replant slope with saplings and set the net at the river mouth.")
        print("The mud stops and water becomes clean.")

    print("The festival goes ahead smoothly and the bay lives on.")
    print("YOU WIN!")


# Save file path
base_dir = os.path.dirname(os.path.abspath(__file__))
def save_by_player(name):
    save_player = ''.join(ch for ch in name.lower() if ch.isalnum()) or "player"
    return os.path.join(base_dir, f"save_{save_player}.json")

# Auto-save the game on exit.
def save_game(player):
    data = {
        "name": player.name,
        "age": player.age,
        "location": player.location.name,
        "days_left": player.days_left,
        "items": [item.name for item in player.items],
        "collected": player.collected
    }

    with open(save_by_player(player.name), "w") as file:
        json.dump(data, file, indent=4)
    print("\nGame saved.")

# Deletes the game save file for the player who finished the game.
def delete_save(name):
    path = save_by_player(name)
    if os.path.exists(path):
        os.remove(path)

# Loads the game from where the player left it.
def load_game(name):
    try:
        with open(save_by_player(name)) as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    if data.get("name", "").lower() == name.lower():
        return data
    return None

# Player data is restored.
def restore_player(data, rooms):
    player = Player(data["name"], data["age"], rooms[data["location"]], data["days_left"])
    carried = data["items"]
    player.collected = data["collected"]
    for room in rooms.values():
        for item in room.items[:]:
            if item.name in player.collected:
                room.items.remove(item)
                if item.name in carried:
                    player.items.append(item)

    if "lab report" in carried:
        player.items.append(Items("lab report"))

    return player