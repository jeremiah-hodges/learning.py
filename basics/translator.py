# all vowels -> g

def translate(word):
    translation = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "g"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a word: ")))