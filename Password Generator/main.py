import string  # to generate password
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase 
    #print(s1) : abcdefghijklmnopqrstuvwxyz
    s2 = string.ascii_uppercase 
    # print(s2) : ABCDEFGHIJKLMNOPQRSTUVWXYZ
    s3 = string.digits 
    #print(s3): 0123456789
    s4 = string.punctuation 
    # print(s4): !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    while True: # handle gibberish(anything is entered except int)
        a = input("Enter password length\n") 
        b = a.isdigit()
        if b==True:
            plen= int(a)
            break
        else:
            print(f"Invalid value! Please enter the valid value")
    s = [] # empty list
    s.extend(list(s1)) # create the list of string s1  and its elements are added to the empty list
    s.extend(list(s2))# create the list of string s2  and its elements are added ahead of s1 elements
    s.extend(list(s3))# create the list of string s3  and its elements are added ahead of s2 elements
    s.extend(list(s4))# create the list of string s4  and its elements are added ahead of s3 elements
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your password is:")
    print("".join(s[:plen])) # it will join all the elemets of length plen from the list after shuffling the elements of s



