import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")




#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-i]", txt)
print(x)


#Find all digit characters:
line=('that will be 65')
x = re.findall("\d", line)
print(x)







#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
sos='hello world'
x = re.findall("he..o",sos)
print(x)

#for more information on regex follow the link
#   https://www.w3schools.com/python/python_regex.asp