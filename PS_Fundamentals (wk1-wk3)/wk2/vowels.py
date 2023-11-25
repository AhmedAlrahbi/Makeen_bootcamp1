#vowels_ICA
vowel = "aeiou"
newChr = ""
newRes = ""
i= ""
def countVowels(plainText):
    for ch1 in plainText:
        if(ch1.lower() in vowel):
            for newRes in range (len(plainText)):
                newRes = ch1.upper()
        else:
            newRes = ch1.lower()
        print(newRes, end="")









countVowels(input("Enter the word: "))