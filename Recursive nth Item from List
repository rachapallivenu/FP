def nth(n, alist):
    if n == 1:
        return alist[0]
    return nth(n - 1, alist[1:])

def program_10():
    alist = input("Enter list elements separated by space: ").split()
    pos = int(input("Enter position (1-based index): "))
    
    if 1 <= pos <= len(alist):
        print(f"{pos}th item is:", nth(pos, alist))
    else:
        print("Invalid position")

program_10()
