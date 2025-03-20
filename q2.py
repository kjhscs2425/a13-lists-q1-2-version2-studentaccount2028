# Use a loop to print out *another* copy of the letter for every cat

cats = ["Zoe", "Ella", "Jessie", "Josie"]

form_letter = """

We regret to inform you that your request for infinite treats has been denied.
Please let us know if you have any further questions.

Sincerely,
The Management

*******************************************************

"""

for cat in cats:
    print("Dear " + cat + "," + form_letter)