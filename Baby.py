from random import choice

questions = ["Why is the sky blue?","Where is there a face on moon?","Where are all the dinosaurs?"]

question = choice(questions)
answer = raw_input(question).strip().lower()

while answer!="just because":
    answer = raw_input("Why?:").strip().lower()

print "Oh Okay"