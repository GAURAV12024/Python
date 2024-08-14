def print_upper_pyramid(x):
    if x % 2 != 0:
        x = x + 1

    x = int(x)
    st = x // 2
    end = x // 2
    h = x // 2
    
    num = (x + 1) - h
    num = int(num)

    for i in range(num - 1):
        for a in range(x + 1):
            if a == st or a == end:
                print(" + ", end="")
            else:
                print("   ", end="")
        print("\n")
        st = st - 1
        end = end + 1

def print_bottom_pyramid(x):
    y = int(x)
    if x % 2 != 0:
        x = x + 1
	
    x = int(x)
    st = 0
    end = x
    h = x // 2
    
    num = (x + 1) - h
    num = int(num)
    mid = x // 2

    for i in range(num):
        for a in range(x + 1):
            if i == 0 and (a == st or a == end):
                print(" + ", end="")
            elif a == st or a == end:
                print(" - ", end="")
            else:
                print("   ", end="")
        print("\n")
        st = st + 1
        end = end - 1

def print_pattern(x):
    if x <= 1 or int(x) != x:
        return "Enter a positive integer greater than 1"
    
    print_upper_pyramid(x)
    print_bottom_pyramid(x)

result = print_pattern(4)
if result:
    print(result)
