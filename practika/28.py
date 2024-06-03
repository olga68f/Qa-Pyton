
def count_letters(word):
    letter_count = {}
    for i in word:
        if i.isalpha():
            i  = i.lower()
            letter_count[i] = letter_count.get(i,0) +1
    return letter_count


word = input()
print(count_letters(word))

