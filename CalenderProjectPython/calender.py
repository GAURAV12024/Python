#code for getting day name by date 
def get_day():
	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	dd=int(input("enter date"))
	mm=int(input("enter month"))
	yy=int(input("enter year"))
	
	#calulating the date using zeller's congruence algorithm
	
	if mm < 3:
		mm+=12
		yy-=1
	c=yy//100
	yy=yy%100
	h=(c//4 -2 * c + yy  + yy//4 +13 * (mm+1)//5 +dd -1)%7
	
	return days[(h + 7) % 7]



print(get_day())
	
