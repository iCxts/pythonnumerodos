def words_from_string():
    sentence = "Generators use less memory then list comprehensions, since they don't store the results of previous calls"
    sentence = sentence.split()
    for i in range(len(sentence)):
        sentence[i] = sentence[i].removesuffix(',')
    
    for i in sentence:
        yield i

for i in words_from_string():
    print(i)
