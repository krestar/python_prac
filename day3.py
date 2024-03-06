height=int(input("plz correct ur height."))
age=int(input("plz correct ur age."))
if height > 100:
    if age > 20:
        print("over 100! adult paying is $15.")
    else:
        print("over 100! for child, paying is $5.")
else:
    print("under 100 can't ride coaster")