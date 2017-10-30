# edx
#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

#gcd(2, 12) = 2

#gcd(6, 12) = 6

#gcd(9, 12) = 3

#gcd(17, 12) = 1

#Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal 
#to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test 
#divides both a and b without remainder, or you reach 1.

#itterative

    def gcdIter(a, b):
        '''
        a, b: positive integers

        returns: a positive integer, the greatest common divisor of a & b.
        '''
        # Your code here
        if a <= b:
            minim = a
        else:
            minim = b

        for i in range(1, minim + 1):
            if (a % i == 0) and (b % i == 0):
                otvet = i
        return otvet
#recursive
    def gcdRecur(a, b):
        '''
        a, b: positive integers

        returns: a positive integer, the greatest common divisor of a & b.
        '''
        # Your code here
        amax = max(a, b)
        bmin = min(a, b)
        a, b = amax, bmin
        if a // b == 0:
            return 1
        elif a % b == 0:
            return b
        else:
            c = b
            b = a - (a // b) * b
            a = c
            return gcdRecur(a, b)
