romans = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500,'M':1000}
lastchar = None
currentvalue = 0
romannum = str(input("Enter a roman numeral").upper())
for c in romannum[::-1]:
    if romans[c] >= romans.get(lastchar, 0) :
        currentvalue += romans.get(c, 0)
        print(f"Current value at letter {c}  is {currentvalue}")
    else:
        currentvalue -= romans.get(c, 0)
    lastchar = c
    print(f"{lastchar} ")

print(f"{romannum} is {currentvalue} in arabic numerals")
