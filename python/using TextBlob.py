from textblob import TextBlob
y= TextBlob("I am a bad person")

print(y.sentiment.polarity)
