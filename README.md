# Python-Fibonacci
A simple python script that calculates &amp; prints the fibonacci sequence!

## What's the fibonacci sequence?
The Fibonacci sequence is a series of numbers that starts with 0 and 1, and each subsequent number in the sequence is the sum of the two preceding ones. So, it goes like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Broken down step by step:

Start with 0 and 1.
Add these two numbers together to get the next number in the sequence: 0 + 1 = 1.
The next number is found by adding the last two numbers: 1 + 1 = 2.
Again, add the last two numbers: 1 + 2 = 3.
Repeat this process to generate the rest of the sequence.
You can continue this indefinitely to generate more numbers in the Fibonacci sequence.

Mathematically, this can be expressed  with a recurrence relation like this:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

Here, F(n) represents the nth number in the Fibonacci sequence. So, to find any specific number in the sequence, this formula is used, provided the values of F(0) and F(1) are known. For example, to find F(5), calculate:

'F(5) = F(4) + F(3) = 3 + 2 = 5'
