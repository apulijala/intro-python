# Capitalize the strings. Use the questions at the end of the chapter

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

"""
Declare a song as 
When an eel grabs your arm,
And it causes great harm,
That's - a moray!

Replace m with M

"""


# print(song)

# Capitailzie the word starting with m.
print(song.replace(" m", " M"))

# Declare the array of questions.
# We don't serve strings around here. Are you a string?
# What is said on Father's Day in the forest?
# What makes the sound 'Sis! Boom! Bah!'?
# Declare answer as An exploding sheep., No, I'm a frayed knot, Pop!' goes the weasel
#
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
    ]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

# Iterate over the questions

for i in range(0,len(questions)):
    print(f"Q: {questions[0]}")
    print(f"A: {answers[0]}\n")

# Letter question .Question 5.5
salutation = "Mr."
name = "Arvind K. Pulijala"
product = "Kit Kat"
verbed = "was"
room = "Room 240"
animals = "cat, dog"
percent = 50
amount = 87.9
spokesman = "Priya"
job_title = "Devops Engineer"

letter = """
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""

print(letter.format(salutation=salutation,product=product,amount=amount,percent=percent,
                    name=name,verbed=verbed, room=room, animals=animals,
                    spokesman=spokesman,job_title=job_title
                    ))


submarine = "Boaty McBoatface"
racehorse = "Horsey McHorseface"
train = "Trainy McTrainface"

print(f"Submarine prize : {submarine}")
print(f"Race Horse prize : {racehorse}")
print(f"Train prize : {train}")