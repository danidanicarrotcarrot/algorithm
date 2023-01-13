def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    gcd = arr[0]
    lcm = arr[0]
    for i in range(len(arr)):
        gcd = GCD(lcm, arr[i])
        lcm = (lcm * arr[i]) // gcd
    return lcm