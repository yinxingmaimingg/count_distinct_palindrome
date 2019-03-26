from cdp import *
from compare_cdp import *

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def runTest():
	for i in range(1000):
		w = randomString(200)
		a = countDistinctPali(w)
		b = count_pali(w)
		print(w, a, b)
		if (a!=b):
			print("error")
			break

runTest()