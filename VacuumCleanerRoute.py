# Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. 
# The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...
    # "LR", return true
    # "URURD", return false
    # "RUULLDRD", return true

def vacuum(direction):
    x = 0 # going right adds one. going left subtracts 1
    y = 0 # going up adds one. going down subtracts 1
    for i in direction:
        if i=='L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'D':
            y -= 1
        elif i == 'U':
            y += 1
        else:
            print('You can only have: R L U D')
            return 

    return bool (not (x+y))

if __name__ == "__main__":
    str1 = 'UDLRRULD' # true
    str2 = 'DULLRDUDDLRU' # false
    str3 = 'UDRLULDRULDRULDR' # true
    str4 = '' # trivially true
    
    print(vacuum(str1))
    print(vacuum(str2))
    print(vacuum(str3))
    print(vacuum(str4))