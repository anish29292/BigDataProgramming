def lcs(str1, str2):
    if not str1 or not str2:
        return ""
    a, s1, b, s2 = str1[0], str1[1:], str2[0], str2[1:]
    if a == b:
        return a + lcs(s1, s2)
    else:
        return max(lcs(str1, s2), lcs(s1, str2), key=len)

test_text1 = input ("Enter string 1: ")
test_text2 = input ("Enter string 2: ")

test = lcs(test_text1,test_text2)

print ("Answer is: ", test)  




