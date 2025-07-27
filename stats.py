def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    character_list = list(text.lower())
    character_set = set(character_list)
    character_count = {}
    for character in character_set:
        character_count[character] = 0
    for character in character_list:
        character_count[character] += 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_letters(dict):
    list_of_letters = []
    for character, count in dict:
        list_of_letters.append({"char": character, "num": count})
    list_of_letters.sort(reverse=True, key=sort_on)
