words = ["this", "that", "did", "deed", "them!", "a"]
# words = ["that", "this", "did", "deed", "them!", "a"]



def minimumCharactersForWords(words):
    all_words = {}
    for word in words:
        current_word = {}
        for letter in word:
            if letter not in current_word:
                current_word[letter] = 1
            else:
                current_word[letter] += 1
        compare_current_word_with_all_words(current_word, all_words)

            
    characters = convert_set_to_list(all_words)
    return characters


def compare_current_word_with_all_words(current_word, all_words):
    for key in current_word:
        if key not in all_words:
            all_words[key] = current_word[key]
        elif key in all_words and current_word[key] >= all_words[key]:
            all_words[key] = current_word[key]


def convert_set_to_list(all_words):
    all_characters = []
    for character in all_words:
        frequency = all_words[character]
        
        for _ in range(frequency):
            all_characters.append(character)
    return all_characters



minimumCharactersForWords(words)
