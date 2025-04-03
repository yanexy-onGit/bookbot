from collections import defaultdict

def count_words(text):
    return len(text.split())

def char_dict_from(text):
    default_dict = defaultdict(lambda: 0)
    for char in text:
        char = char.lower()
        default_dict[char] += 1
    return dict(default_dict)

def dict_to_sorted_list(dict):
    output = []
    for key, val in dict.items():
        output.append({ "char": key, "count": val})
    return sorted(output, key=lambda dict: dict["count"], reverse=True)