def validateString(string):
	if(len(string)==0):
		return "invalid"
	for i in string:
		if i not in ['{','(','<','[','}',')','>',']']:
			return "invalid String"

	stack=[]
	for i in string:
		if i in ['{','(','<','[']:
			stack.append(i)
		elif i in ['}',')','>',']']:
			if(len(stack)==0):
				return "invalid string"
			a=stack.pop()
			if(i=='>' and a!='<'):
				return "invalid string"
			if(i==']' and a!='['):
				return "invalid string"
			if(i=='}' and a!='{'):
				return "invalid string"
			if(i==')' and a!='('):
				return "invalid string"
	if(len(stack)==0):
		return "valid"
	if(len(stack)!=0):
		return "Invalid"


def countValid_String_inList(list,count):
	
	for i in list:
		if type(i) in ["list","tuple","set"]:
			countValid_String_inList(i,count)
		if type(i)==str:
			if(validateString(i)=="valid"):
				count+=1
	return count;


#print(validateString("<<<>>>"))


print(countValid_String_inList(["{sggs}","{(<>)}",["<>(){()}","{{{}"],"<<<>>>",["()",["(){}"]]],0))

#print(validateString("{sggs}"))
#print(validateString("{121}"))

#print(validateString("{(<>)}"))
#print(validateString("<>(){()}"))
#print(validateString("{{{}"))
