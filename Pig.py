# Get Sentence from Sentence

original = raw_input("Type the sentence").strip().lower()

# Split the sentence into words

words = original.split()

# Loop through the words and convert to Pig Latin
new_words = []
# if it starts with vowel, just add "yay"
# otherwise, move the first consonent to the end and add "aY"
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        new_word = word[vowel_pos:] + word[:vowel_pos].upper() + "aY"
        new_words.append(new_word)

print (" ".join(new_words))


# Stick those words together into Sentence

# Output the final String