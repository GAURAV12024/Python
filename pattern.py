def print_simple_line(x):
    x = int(x)
    
    for a in range(x):
        for i in range(x):
            print("  *  ", end="")
        print("\n")

def print_upper_pyramid(x, space):
    
    if x % 2 != 0:
        x = x + 1

    x = int(x)
    st = x // 2
    end = x // 2
    h = x // 2
    
    num = (x + 1) - h
    num = int(num)

    for i in range(num - 1):
        print(" " * space, end="")
        for a in range(x + 1):
            if a == st or a == end:
                print(" * ", end="")
            else:
                print("   ", end="")
        print("\n")
        st = st - 1
        end = end + 1

def print_bottom_pyramid(x, space):
    
    y=int(x)
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
        print(" " * space, end="")
        for a in range(x + 1):
            if a == mid and i == 0:
                print(y, end="")
            if a == st or a == end:
                print(" * ", end="")
            else:
                print("   ", end="")
        print("\n")
        st = st + 1
        end = end - 1

def print_pattern(x):
    
    if x <= 1 or int(x) != x:
        return "Enter a positive integer greater than 1"
    
    x=int(x)
    
    space =x// 2

    print_upper_pyramid(x, space)
    print_bottom_pyramid(x, space)
    print_simple_line(x)
	

result = print_pattern(10.00000)
if result:
    print(result)
