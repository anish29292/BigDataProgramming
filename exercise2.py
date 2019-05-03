
def match(str1, str2): 

	if len(str1) == 0 and len(str2) == 0: 
		return True

	if len(str2) > 1 and str2[0] == '*' and len(str1) == 0: 
		return False

	if (len(str2) > 1 and str2[0] == '.') or (len(str1) != 0
		and len(str2) !=0 and str1[0] == str2[0]): 
		return match(str1[1:],str2[1:]); 
 
	if len(str2) !=0 and str2[0] == '*': 
		return match(str1,str2[1:]) or match(str1[1: ],str2) 

	return False

def test(str1, str2): 
	if match(str1, str2): 
		print ("True")
	else: 
		print ("False")

test("aba","*ab")
test("aa","a*")
test("ab",".*")
test("ab",".") 
test("aab","c*a*b") 
test("aaa","a*")