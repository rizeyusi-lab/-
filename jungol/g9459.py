def check_info(gender, age):
    gender = gender.lower()

    
    if gender == 'm':
        if age >= 20:
            print("MAN")
        else:
            print("BOY")
    elif gender == 'f':
        if age >= 20:
            print("WOMAN")
        else:
            print("GIRL")

g, a = input().split()
check_info(g, int(a))
    
