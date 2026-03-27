
text = """
Belong
Kehillah commits to creating and holding a welcoming space for all students to
come as they are, express their diverse identities, build community, and forge
meaning relationships with faculty and peers. We understand that a sense of
belonging is the foundation for deep learning, risk-taking, and individuality.
As we create this space for each student, they can help create it for others.

Build

Learning at Kehillah is not a passive act --- it's a co-constructed cycle of
discovery, challenge, and growth. Our expert faculty, deeply attuned to
adolescent development and progressive education practices, partner with
students to build academic prowess, self-refleciton, agency, wellness,
character, and joy.

Become

Kehillah is a launchpad for purpose. Our graduates leave not just prepared for
top universities, but as compassionate individuals who define success through
achievement, contribution, and character. Grounded in curiosity and integrity,
they are ready to navigate complexity, think critically, and drive meaningful
change in their communities and beyond.
"""

# Make a dictionary where the keys are all the unique words in the string
# (Hint: use the `.split()` method to get a list of all the words) and the
# values are the number of times each word appears. Print the dicitonary.


# 1. Remove all new lines and punctuation, and convert to all lowercase.
#### YOUR CODE HERE
x=text.split()
y=text.lower()
z="".join(y)
punctuation=[".", "," "-" "'", "---", ":"]
for symbol in punctuation:
    z=z.replace(symbol, "")
words=z.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1
print(word_count)





# 2. Use the `.split()` method to split into a list of words.
#### YOUR CODE HERE

# 3. Initialize an empty dictionary to keep track of word counts.
#### YOUR CODE HERE


# 4. loop through the list of words and update the dictionary. If the word is
# already a key in the dicitonary, increment the count. If not, add the new key
# with a count of 1.
#### YOUR CODE HERE
