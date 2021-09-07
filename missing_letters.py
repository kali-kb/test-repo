import string

def find_missing_letter(lst):
	letter_u = string.ascii_uppercase
	letter = string.ascii_lowercase
	ranges = string.ascii_lowercase[letter.find(lst[0]):letter.find(lst[-1])+1]
	ranges_u = string.ascii_uppercase[letter.find(lst[0]):letter.find(lst[-1])+1]
	
	for j in set(ranges):
	   if j not in set(lst):
	   	return j
	   	break
	   	
if __name__=="__main__":
	print(find_missing_letter("abd"))
	