def detectCapitalUse(word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word.istitle(): 
            return True
        
        return False
print(detectCapitalUse("salom"))