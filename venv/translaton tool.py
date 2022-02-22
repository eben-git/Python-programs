def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "INI"
            else:
                translation = translation + "ini"

        else :
            translation = translation + letter
    return translation

print(translate(input("enter a phrase: ")))

