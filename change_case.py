
def convert_to_lowerCase(str):
	a=list(str)
	
	
	length=len(a)

	
	for i in range(length):
		
		if(not a[i].isalpha() or a[i].isspace()):
			continue
		if(ord(a[i])< 90):
			a[i]=chr(ord(a[i])+32)
			
	string=""
	for i in range(length):
		string+=a[i]


	
	return string


def convert_to_upperCase(str):
	a=list(str)
	
	
	length=len(a)

	
	for i in range(length):
		if(not a[i].isalpha() or a[i].isspace()):
			continue
		if(ord(a[i])> 90):
			a[i]=chr(ord(a[i])-32)
			
	string=""
	for i in range(length):
		string+=a[i]


	
	return string

def reverse_the_caseOfChar(str):
	a=list(str)
	
	
	length=len(a)

	
	for i in range(length):
		if(not a[i].isalpha() or a[i].isspace()):
			continue
		if(ord(a[i])> 90):
			a[i]=chr(ord(a[i])-32)
		else:
			a[i]=chr(ord(a[i])+32)
		
	string=""
	for i in range(length):
		string+=a[i]


	
	return string

def convert_to_titleCase(str):
    a = list(str)
    length = len(a)
    
    j = True      
    for i in range(length):
        if not a[i].isalpha():
            j = True
            continue
        if j and ord(a[i]) >= 90:
            a[i] = chr(ord(a[i]) - 32)
            j = False
        elif not j and ord(a[i]) < 90:
            a[i] = chr(ord(a[i]) + 32)
    
    string = ""
    for i in range(length):
        string += a[i]

    return string




def change_case(str,style):
	if(style=="c" or style=="C"):
		return convert_to_upperCase(str)
	if(style=="s" or style=="S"):
		return convert_to_lowerCase(str)
	if(style=="r" or style=="R"):
		return reverse_the_caseOfChar(str)
	if(style=="u" or style=="U"):
		return convert_to_titleCase(str)


print(change_case(" gERIRRJKHKJ ","U"))
