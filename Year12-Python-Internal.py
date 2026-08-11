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

def validate_stat (values) :
    "Ensure stats is a number between 1-25"
    if:
        value = int(value)
        return 1 <= value <= 25 
    else:
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
        return true 
    return False

def update_monster(name,stat,new_value):
    monster_catalogue_catalogue[name][stat] = new_value
    return monster_catalogue [name]


#GUI FUNCTIONS

