import re 
PAN=input("enter pan  number: ")
if re.search("^[A-Za-z]{5}\d{4}[A-Za-z]$",PAN):
    print("valid number")
else:
    print("invalid")
    
