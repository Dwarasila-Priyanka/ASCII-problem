# whether given string is in upper or lower without using string methods
v="Chai tYa@Na"
upper=""
lower=""
spe_char =""
for i in v:
    if ord(i)>=65 and ord(i)<90:
        upper+=i
    elif ord(i)>=97 and ord(i)<122:
        lower+=i
    else:
        spe_char+=i
print(upper,lower,spe_char) #CYN haitaa  @
print(upper+lower+spe_char) #CYNhaitaa @