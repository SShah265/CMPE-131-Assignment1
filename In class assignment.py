from textblob import TextBlob

user_input = input("Enter some text: ")

analysis = TextBlob(user_input)

if analysis.sentiment.polarity > 0: 
    print(" This statement has a positive Sentiment!")
elif analysis.sentiment.polarity == 0:
    print("This statement has a neutral sentiment.")
else: 
    print("This statement is negative :/")