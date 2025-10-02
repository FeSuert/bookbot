def calculate_words(text):
    return len(text.split())

def calculate_characters(text):
    character_dict = {}
    for character in text:
        character = character.lower()
        character_dict[character] = character_dict.get(character,0) + 1
    return character_dict

def sort_on(items):
    return items["num"]
def sort_dictionary(dict):
    sorted = []
    for key in dict.keys():
        d = {}
        d["char"] = key
        d["num"] = dict[key]
        sorted.append(d)
    sorted.sort(reverse=True, key=sort_on)
    return sorted