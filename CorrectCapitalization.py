def check_cap(string):
    # A string correctly uses capitalization if:
    # 1- all letters are capitalized
    # 2- no letters are capitalized
    # 3- only the first letter is capitalized.

    # NO capitilization at all
    all_caps = False
    no_caps = False
    first_only_cap = False

    if(string.isupper()):
        all_caps = True
    elif(string.islower()):
        no_caps = True
    elif(string[0].isupper()):
        first_only_cap = True
        for i in range(1,len(string)):
            if(string[i].isupper()):
                first_only_cap = False
    
    return bool (all_caps or no_caps or first_only_cap)


if __name__ == "__main__":
    print(check_cap("USA")) # true
    print(check_cap("Ahmed")) # true
    print(check_cap("true")) # true
    print(check_cap("UsA")) # false
    print(check_cap("ahmeD")) # false

