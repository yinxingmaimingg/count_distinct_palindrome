
def isFactor(factor, whole):
	for i in range(len(whole)-len(factor)+1):
		if (factor==whole[i:i+len(factor)]):
			return True
	return False

# stupid algorithm
def computeLpf(w):
	n = len(w)
	lpf = []
	for i in range(len(w)):
		lpf.append(0)
		for l in range(1, n-i+1):
			if (isFactor(w[i:i+l], w[:i+l-1])):
				lpf[i] = l
	return lpf

# stupid algorithm
def getWordsLcp(u, v):
	l = min(len(u), len(v))
	for i in range(l):
		if (u[i]!=v[i]):
			return i
	return l

# stupid algorithm
def computeLcp(w):
	lcp = []
	w_ = w[::-1]
	for i in range(len(w)):
		lcp.append([])
		for j in range(len(w)):
			lcp[i].append(getWordsLcp(w[i:], w_[j:]))
	return lcp

def computeLmp(w):
	n = len(w)
	lcp = computeLcp(w)
	lmp = []
	for i in range(n):
		lmp.append(-1)
	for k in range(n):
		i = k + lcp[k][n-k-1] - 1
		lmp[i] = max(lmp[i], 2*lcp[k][n-k-1] -1)
	for k in range(1, n):
		i = k + lcp[k][n-k] - 1
		lmp[i] = max(lmp[i], 2*lcp[k][n-k])
	for i in range(n):
		if (lmp[i]==0):
			lmp[i] = -1
	return lmp

def countDistinctPali(w):
	n = len(w)
	lpf = computeLpf(w)
	lmp = computeLmp(w)
	lps = []
	for i in range(n):
		lps.append(lmp[i])
	for i in range(n-2, -1, -1):
		lps[i] = max(lps[i], lps[i+1]-2)
	nbPal = 1
	for i in range(n):
		if (lpf[i-lps[i]+1]<lps[i]):
			nbPal += 1
	# print(lmp)
	# print(lps)
	# print(lpf)
	return nbPal



# w = "abbabaabbba"
# print(countDistinctPali(w))