""" string 
strings come with a variety of built-in methods
 that allow you to manipulate and work with text data efficiently. 
Here are some commonly used string methods:"""


arjun="githa govidam "
print(type(arjun))
malik="rahul minus bai"
print(malik[6])
print(malik[-5])
print(malik[4:8])
print(malik[-3:-2])

prabhas=("chratapathi bahubai salaar")
print(prabhas[1])
print(prabhas[-1])
print(prabhas[1:4])
print(prabhas[-1:3])

king=("chratapathi kingdown")
print(king[7])
print(king[-7])
print(king[4:8])
print(king[-1:-4])

guru=("ckalyan kushi og")
print(guru[4])
print(guru[-3])
print(guru[7:9])
print(guru[-4:3])

NTR=("devara shakthi badusha rabhasa")
print(NTR[7])
print(NTR[-6])
print(NTR[3:8])
print(NTR[-2:-4])

nani=("ega daserha nani inteligent")
print(nani[5])
print(nani[-2])
print(nani[1:5])
print(nani[-9:-1])

mahesh=("sarileru pokiri snehithidu spider ")
print(mahesh[4])
print(mahesh[-3])
print(mahesh[0:5])
print(mahesh[-4:-1])

""" concating """
ram="srirama"
ram2="rajyam"
con=(ram+ram2)
print(con)

pspk="pavan"
pspk2="kalyan"
con=(pspk+" "+pspk2)
print(con)

""" repiting """

train="golukoda express "
print(train*30)
train2="krishna express "
print(train2*20)

""" methods of string """
kanappa=" Veera  Venkata Ramurthi ramu "
# Converts all characters in the string to uppercase.
print(kanappa.upper())
# Converts all characters in the string to lowercase.
print(kanappa.lower())
print(len(kanappa))
# Removes any leading and trailing whitespace from the string.
print(kanappa.strip())
# Splits the string into a list of substrings based on a specified separator.
print(kanappa.split()) 
# Checks if the string starts with the specified prefix. Returns True or False.
print(kanappa.startswith("Veera"))
# Checks if the string ends with the specified suffix. Returns True or False
print(kanappa.endswith("ramu"))
# Replaces occurrences of a specified substring with another substring.
print(kanappa.replace("Veera","python"))
# Capitalizes the first character of the string.


text = "hello world"
print(text.capitalize()) 
# Capitalizes the first character of the string.
print(kanappa.capitalize())
# Returns the lowest index in the string where the specified substring is found. Returns -1 if the substring is not found.
print(kanappa.find("Veera"))
# join(),convert into list to string
conect=["jjj","jjjhg","jhg","jhg","kjh"]
print("".join(conect))

""" tuple 

1. collection of elements
2.it is represented by '()'."""

tup=("rahul","krisha","anil","ankitha","malli","mani","kishore","rahul")
print(type(tup))
print(tup.count("rahul"))
print(tup[2])
print(len(tup))

