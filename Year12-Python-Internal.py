import easygui as e

# Catalogue of monsters

monster_catalogue = {
     "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

            # Main Code
# Validation Structure 

def validate_stat (values):
    """Ensure stats is a number between 1-25"""
    try:
        value = int(value)
        return 1 <= value <= 25 
    except:
        return False
def validate_name(name):
    "Ensure name is not empty."
    return name.strip() !=""

# Core Mechanics 

def add_monster(name,stats):    
    monster_catalogue[name] = stats
    return monster_catalogue [name]

def delete_monster(name):
    if name in monster_catalogue :
        del monster_catalogue [name] 
        return True
    return False

def update_monster(name,stat,new_value):
    monster_catalogue_catalogue[name][stat] = new_value
    return monster_catalogue [name]


#GUI FUNCTIONS

def gui_add_monster():
    "Add a new monster card."
    fields = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
    values = e.multchoicebox("Enter Monsters details","Add Monster", fields)

    name, strength, speed, stealth, cunning = values

    if values is None:
        return

    #Validation
    
    if not validate_name(name):
        e.msgbox("Invalid Name")
        return

    if not all([validate_stat(speed), validate_stat(strength),
                validate_stat(cunning), validate_stat(stealth)]):
        e.msgbox("Stats must between numbers 1-25")
        return

    stats = {
         "Strength": int(strength),
        "Speed": int(speed),
        "Stealth": int(stealth),
        "Cunning": int(cunning)
    }

    added = add_monster(name,stats)

    #Confirmation Loop 
    while True:
        choice = e.buttonbox(
        f"Monster Card added\n\n{name}:{added}\n\nAre these details correct?",
        "Confirm Monster",
        ["Yes","Edit","Cancel"]
        )

        if choice == "Yes":
            break

        elif choice == "Edit":
            gui_add_monster(name)
            break  

        else:
            delete_monster(name)
            e.msgbox("Monster discarded.")
            break

def gui_edit_monster(name):
    "Edit an exsiting monster"
    monster = monster_catalogue[name]

    fields = ["Strength", "Speed", "Stealth", "Cunning"]
    defaults = [monster["Strength"], monster["Speed"], monster["Stealth"], 
    monster["Cunning"]]

    values = e.multenterbox(f"Editing {name}", "Edit Monster", fields, defaults)

    if values is None:
        return

    strength, speed, stealth, cunning = values


    if not all([validate_stat(strength), validate_stat(speed),
                validate_stat(stealth), validate_stat(cunning)]):
        e.msgbox("Stats must be numbers between 1–25.")
        return

    monster_catalogue[name] = {
        "Strength": int(strength),
        "Speed": int(speed),
        "Stealth": int(stealth),
        "Cunning": int(cunning)
    }

    e.msgbox(f"{name} update succesfully")


def gui_output_catalogue():
    "search for a monster and edit it if you want"
    name = e.enterbox("Enter monster name to search:", "Search Monster") 

    if name is None:
        return

    result = search_monster(name)

    if result:
        choice = e.buttonbox(
            f"{name} found:\n{result}\n\nWhat would you like to do?",
            "Monster Found",
            ["Edit", "Delete", "Back"]
        )

        if choice == "Edit":
            gui_edit_monster(name)
        
        elif choice == "Delete":
            if delete_monster(name):
                e.msgbox(f"{name} deleted.")
            else:
                e.msgbox("Error deleting monster.")

    else:
        e.msgbox("Monster not found")


def gui_delete_monster():
    "Delete a monster"
    name = e.enterbox("Enter monster name to delete:", "Delete Monster")

    if name is None:
        return

    elif delete_monster(name):
         e.msgbox(f"{name} deleted.")
    else:
        e.msgbox("Monster not found.")

    def gui_output_catalogue():
        "Print full catalogue to Python Shell."
    for monster, stats in monster_catalogue.items():
        e.msgbox(monster and stats)


# MAIN MENU LOOP (ITERATION)

while True:
    choice = e.buttonbox(
        "Monster Card Catalogue",
        "Main Menu",
        ["Add Monster", "Search Monster", "Delete Monster", "Output Catalogue", 
        "Exit"]
    )
    
    if choice == "Add Monster":
        gui_add_monster()

    elif choice == "Search Monster":
        gui_search_monster()

    elif choice == "Delete Monster":
        gui_delete_monster()

    elif choice == "Output Catalogue":
        gui_output_catalogue()

    else:
        break
