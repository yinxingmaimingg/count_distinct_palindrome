# Count distinct palindromes in a word

This project implements the algorithm to count distinct palindromes in a word in linear time by Groult et al.

To run the program, use the command:
```
python3 cdp.py
```
Input a word in the screen, then the program will output the number of distinct palindromes.


To test the program, use the command:
```
python3 test_cdp.py
```
The test program will generate random test cases, compute the results using the given algorithm and another naive algorithm, compare the results to evaluate the correctness.

Note: The program is not in linear time. The main algorithm is in linear time, assuming lcp and LPF are given. But in the program I compute lcp and LPF using naive algorithms.




Reference:

Groult R, Prieur É, Richomme G. Counting distinct palindromes in a word in linear time. Information Processing Letters. 2010 Sep 30;110(20):908-12.
