#asking input
input_num = input("Please Enter Sentence : ")
#converting string into lower case
string_num = input_num.lower()

#printing sentence
print("You typed : ",string_num)

#initializing variable i as 0 that contains number of vowels
i = 0
#list
list = ["a","e","i","o","u"]

#this loop serach each character in a list
for char in string_num:
    if char in list: #checks the character is in list, if character in the list then it will increment the i by one
        i=i+1

#printing total
print("There are ",i,"vowels in the sentence.")
