import pronouncing

# pronouncing a word

def pronounce(word):
    p = pronouncing.phones_for_word(word)
    print(p)

#Search similar pronounciations

def simPro(word):
    phones = pronouncing.phones_for_word(word)[0]
    p = pronouncing.search(phones)[:5]
    print(p)

#Getting rhymes

def rhyme(word):
    p = pronouncing.rhymes(word)
    print(p)

a = 'y'

while(a =='y' or a == 'Y' ):

    print("Enter a word")
    word = input()

    print("What do you want to know (1, 2 or 3)? \n 1. pronounciations \n 2. Homophones \n 3. Rhyming words")
    ans = input()
    if(ans == "1"):
        pronounce(word)
    elif(ans == "2"):
        simPro(word)
    if(ans== "3"):
        rhyme(word)

    print("Do you want to find another word? y/n")
    a = input()
