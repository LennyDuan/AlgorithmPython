A prime is a natural number greater than  that has no positive divisors other than  and itself. Given  integers, determine the primality of each integer and return Prime or Not prime on a new line.

Note: If possible, try to come up with an  primality algorithm, or see what sort of optimizations you can come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

Function Description

Complete the primality function in the editor below.

primality has the following parameter(s):

int n: an integer to test for primality
Returns

string: Prime if  is prime, or Not prime
Input Format

The first line contains an integer, , the number of integers to check for primality.
Each of the  subsequent lines contains an integer, , the number to test.

Constraints

Sample Input

STDIN   Function
-----   --------
3       p = 3 (number of values to follow)
12      n = 12 (first number to check)
5       n = 5
7       n = 7
Sample Output

Not prime
Prime
Prime
Explanation

We check the following  integers for primality:

 is divisible by numbers other than  and itself (i.e.: , , , ).
 is only divisible  and itself.
 is only divisible  and itself.
Python 3



12345678910111213141516171819202122232425
