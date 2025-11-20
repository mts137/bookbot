def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    counts = {}
    text = text.lower()
    for character in text:
        if character not in counts:
            counts[character] = 0
        counts[character] += 1
    return counts

def sort_on(items):
    return items["num"]

def get_sorted_character_counts(counts):
    sorted_counts = []
    for character, count in counts.items():
        sorted_counts.append({"char": character, "num": count})
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
