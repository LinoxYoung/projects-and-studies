word = input("word: ")
def palindromo(word):
    if word[::-1] == word:
        return f'{word}:this is a palindrome'
    else:
        return f'{word}:this is not a palindrome'
print(palindromo(word))