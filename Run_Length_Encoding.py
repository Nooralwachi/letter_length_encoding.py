def encoding(st):
	i=0
	temp=st[0]
	result =''
	for letter in st:
		if letter == temp:
			i+=1
		else:
			result +=  str(i) +temp			
			i=1
			temp=letter	
	result +=  str(i) +temp
	print(result)
	return result

print('12W1B12W3B24W1B14W' == encoding('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))