import random

# Function to count the length of the string
def count_char(n):
    return (len(n))

# Function to count the number of spaces in the string
def count_word(n):
    space_count = n.count(" ")
    return (space_count)

# Function to generate permutations of the string
def getPermutations(n):

    n=list(n)
    
    #factorial
    def factorial(num):
        fact=1
        if(num<0):
            raise ("value not found")
        while(num!=0):  
            fact=fact*num
            num=num-1
        return fact
    

    #now doing main logic
    p = set()
    while len(p) < factorial(len(n)):
        random.shuffle(n)
        s_word = ''.join(n)
        p.add(s_word) 

    return p,f"    total words are : {len(p)}"


# Function to convert the string to title case
def make_title(n):
    return (n.title())


# Function to normalize spaces by splitting and rejoining the string
def normalize(n):
   p= n.split()
   return (" ".join(p))



# Function to remove punctuation (only keeps alphanumeric characters
def remove_Punctuation(s):
   str=""
   for i in s:
       if(i.isalpha() or i.isdigit()):
           str=str+i
   return (str)


# Function to reverse a string
def reverse_words(n):
    return (n[::-1])


# Function to find all occurrences of a substring and return their positions
def spansub(s,n):
    strt = 0
    p = []
    while strt < len(s):
        strt = s.find(n, strt) #return 2
        if strt == -1:
            break
        ed = strt + len(n) #4
        p.append((strt, ed))
        strt = ed  
    return ([len(p),p])


# Function to swap the case of each character in the string
def transformm(s):
   return (s.swapcase())

 
# Main function
def plaGame():
    print("...............................................................welcome to new world.........................................")

    while True:
        print("1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s) \n 5.charecterMap(s) "
            "6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit" )
        p=int(input(" please select the number : "))

        if p==1:
            strr = input("enter the string: ")
            sub_str = input("enter the substring: ")
            print(spansub(strr,sub_str))
        elif p==2:
            print (reverse_words(input("Enter the word : ")))

        elif p==3:
            print (remove_Punctuation(input("Enter the word : ")))

        elif p==4:
            print (count_word(input("Enter the word : ")))
        
        elif p==5:
            print (count_char(input("Enter the word : ")))

        elif p==6:
            print (make_title(input("Enter the word : ")))

        elif p==7:
            print (normalize(input("Enter the word : ")))

        elif p==8:
            print (transformm(input("Enter the word : ")))

        elif p==9:
            print (getPermutations(input("Enter the word : ")))

        elif p==10:
            break

plaGame()

