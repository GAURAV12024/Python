def modulo(numerator,denominator):
	
	if(denominator==0):
		return "ZeroDivisionError: integer modulo by zero"
	if(numerator==0):
		return 0


	n=numerator/denominator;
	ans = numerator-(int(n)*denominator);
	return ans;



x=modulo(0,5);
print(x)