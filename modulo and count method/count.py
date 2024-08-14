def count(a,b,c):

	l=len(b)
	index=0
	count_of_string=0
	if a.find(b)==-1:
		return 0
	
	if(c=="true"):
		while(a.find(b,index)!=-1):
			index=a.find(b,index)+l
			count_of_string=count_of_string+1
	else:
		while(a.find(b,index)!=-1):
			index=a.find(b,index)+1
			count_of_string=count_of_string+1


	
	return count_of_string




print(count("sgggggs","gg","false"))