def calculate_pi(n):
    odd_numbers = [2*i-1 for i in range(1, n+1, 1)]
    signs = [(-1)**j for j in range(0,n,1)]
    total = 0
    for i in range(0, n, 1):
        total += signs[i]*(1/odd_numbers[i])
    pi_estimate = total*4
    return pi_estimate
