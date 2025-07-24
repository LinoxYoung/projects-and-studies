
word = "IV"
word = list(word)
print(word)

    
def filter(word):
    if 'I'== word:
       return 1
    elif 'V' == word:
       return 5
    elif 'X' == word:
       return 10
    elif 'L' == word:
       return 50
    elif 'C'== word:
       return 100
    elif 'D'== word:
       return 500
    elif 'M'== word:
        return 1000
        
word = list(word)        
if filter(word[0]) < filter(word[1]):
    print(filter(word[1]) - filter(word[0]))
    