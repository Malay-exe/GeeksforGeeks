def word(pattern,s):
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

pattern = 'aabbb'
s = 'ma ma ok ok ok'
print(word(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(word(pattern, s))