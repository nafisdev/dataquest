## 1. The Rule of Product ##

n_outcomes=36
p_six_six=1/36
p_not_five_five=1-1/36

## 2. Extended Rule of Product ##

total_outcomes=6**3*52

p_666_ace_diamonds=1/total_outcomes


p_no_666_ace_diamonds=1-p_666_ace_diamonds

## 3. Example Walkthrough ##

p_crack_4=1/(10**4)
p_crack_6=1/(10**6)

## 4. Permutations ##

def factorial(n):
    if(n==1):
        return n
    return n*factorial(n-1)


permutations_1=factorial(6)


permutations_2=factorial(52)

## 5. More About Permutations ##

def factorial(n):
    if(n==1):
        return n
    return n*factorial(n-1)


perm_3_52=factorial(52)/factorial(49)

perm_4_20=factorial(20)/factorial(16)

perm_4_27=factorial(27)/factorial(23)

## 6. Permutations Formulas ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product


def permutation(n,k):
    if(k>=0 and n-k>0):
        return factorial(n)/factorial(n-k)
    return 1


p_crack_pass=1/permutation(127,16)

## 7. Unique Arrangements ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n, k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/denominator


c=permutation(52,5)/factorial(5)
p_aces_7=1/c

c_lottery=permutation(49,6)/factorial(6)

p_big_prize=1/c_lottery

## 8. Combinations ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product


def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/(denominator*factorial(k))


c_18=combinations(34,18)

p_non_Y=1 - 1/c_18