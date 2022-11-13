def get_count(sentence):
    vowels = 'aeiou'
    count_vowels = 0
    for letter in vowels:
        count_vowels += sentence.count(letter)
    return count_vowels
