from textblob import TextBlob

a=input("")
print("Original text: "+str(a))

b = TextBlob(a)

print("corrected text: "+str(b.correct()))