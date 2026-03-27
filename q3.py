import random
# Update this dictionary with questions and answers:
flashcards = {
    "what is the capital of france":"paris",
    "what country did the bolshviek revolution happen in":"russia",
    "what is 2+3(2)":"8"
}

# Get a list of keys (questions) from the dictionary
#### YOUR CODE HERE
questions= list(flashcards.keys())


# Randomly sample one question
#### YOUR CODE HERE

question=random.choice(questions)


# Use the `input` function to ask the user the question and get their response
#### YOUR CODE HERE
user_answer=input(f"{question} ")



# Use the question as a key to look up the answer in the dicitonary
#### YOUR CODE HERE
correct_answer= flashcards[question]

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE
if user_answer.lower()==correct_answer.lower():
    print("correct!")
else:
    print(f"that is incorrect, the answer is {correct_answer}")