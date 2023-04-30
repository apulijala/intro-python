'''
5.1 Capitalize the word starting with m:

<<<<<<< HEAD
song = """When an eel grabs your arm,
 And it causes great harm,
 That's - a moray!"""

"""
=======
>>> song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""
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
'''
>>>>>>> 60724fb... fix: added all code
song = """
When an eel grabs your arm,
And it causes great harm,
That's - a moray!
"""

print(song.replace(" m", " M"))


'''
5.2 Print each list question with its correctly matching answer, in the form:
'''

'''
Q: question
A: answer

>>> questions = [
    ...     "We don't serve strings around here. Are you a string?",
    ...     "What is said on Father's Day in the forest?",
    ...     "What makes the sound 'Sis! Boom! Bah!'?"
    ...     ]
>>> answers = [
    ...     "An exploding sheep.",
    ...     "No, I'm a frayed knot.",
    ...     "'Pop!' goes the weasel."
    ...     ]

'''

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

for i in range(0,len(questions)):
    print(f"Question: {questions[i]} and Answer: {answers[i]}")

'''
5.3 Write the following poem by using old-style formatting. 
Substitute the strings 'roast beef', 'ham', 'head', and 'clam' into this string:

My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.

'''
poem = '''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
'''
print("\nPoem is \n")
poem = poem % ("roast beef", "ham", "head", "clam")
print(poem)
print("\n")


'''
5.4 Write a form letter by using new-style formatting. Save the following string as letter (you’ll use it in the next exercise):

Dear {salutation} {name},

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

5.5 Assign values to variable strings named 'salutation', 'name', 'product', 
'verbed' (past tense verb), 'room', 'animals', 'percent', 'spokesman', and 'job_title'. 
Print letter with these values, using letter.format().
'''
salutation = "Mr."
name = "Arvind K. Pulijala"
product = "Sticks"
verbed = "was"
room = "256A"
animals = "cat, dog"
amount = "500$"
percent = "79"
spokesman = "Arvind Kumar Pulijala"
job_title = "Lead Devops Engineer"


letter = f'''
Dear {salutation} {name},

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
'''

print(letter)

'''
5.6 After public polls to name things, a pattern emerged: an English submarine (Boaty McBoatface), 
an Australian racehorse (Horsey McHorseface), and a Swedish train (Trainy McTrainface). 
Use % formatting to print the winning name at the state fair for a prize duck, gourd, and spitz.
'''
duck = "Boaty McBoatface"
Horse = "Horsey McHorseface"
spitz = "Trainy McTrainface"

prize = """
Duck %s, 
Gourd %s, 
Spits %s
""" % (duck, Horse, spitz)
print("Old Style formatting")
print(prize)


'''
5.7 Do the same, with format() formatting.
'''
prize = """
Duck {}, 
Gourd {}, 
Spits {}
"""
print("String Formatting using format() method")
print(prize.format(duck, Horse, spitz))





'''
5.8 Once more, with feeling, and f strings.
'''
duck = "Boaty McBoatface"
Horse = "Horsey McHorseface"
spitz = "Trainy McTrainface"

prize = f"""
Duck {duck}, 
Gourd {Horse}, 
Spits {spitz}
"""
print("String Formatting using f strings")
print(prize)