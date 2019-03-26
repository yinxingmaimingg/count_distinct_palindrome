
def check_pali(s):
	for i in range(len(s)//2):
		if (s[i]!=s[-i-1]):
			return False
	return True

def check_rich(s):
	dict = {}
	for i in range(len(s)):
		for j in range(i+1, len(s)+1):
			if (check_pali(s[i:j])):
				dict[s[i:j]] = 1
	print("Word:", s, "Pali:", len(dict)+1)
	if (len(dict)==len(s)):
		return True
	else:
		return False

def count_pali(s):
	dict = {}
	for i in range(len(s)):
		for j in range(i+1, len(s)+1):
			if (check_pali(s[i:j])):
				dict[s[i:j]] = 1
	# print("Word:", s, "Pali:", len(dict)+1)
	return len(dict)+1


# x = "10011"
# y = "0110"
# print(count_pali("abbabaababa"))
# print(count_pali("abbabaabbba"))