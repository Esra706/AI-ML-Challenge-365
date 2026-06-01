# .upper() Method
name="isra memon"
print(name.upper()) #print ISRA MEMON

# .lower() Method 
name2="BSSE"
print(name2.lower())  #bsse

# .strip()  Method  (Remove extra spaces from start and end)

name3="  Programming Language "
print(name3.strip())


# .replace()  (This method replaces a specific part of a string with a new text.)
txt="I Love java"
new_txt=txt.replace("java","Python")
print(txt) #print old text (I love java)
print(new_txt) #print (I love Python)


# .split()  (It will split the sentence wherever it finds a space)
sentence="Python is fun"
words=sentence.split()
print(words)  #['Python', 'is', 'fun']


# F-string
item="Coffee"
price=250
status="Orderd"
sentence=f"Your {item} is {status}.Please pay {price} rupees Thanks"
print(sentence)