from collections import Counter

print(Counter)

l = [1,1,1,1,2,1,2,3,2,4,3,5,1,2,3,4,2,1]

print(Counter(l))

s = 'asdasdasdaassdd'
print(Counter(s))

sentence = 'How many times does each word show up in this sentence word word word sentence word'
words = sentence.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(1))