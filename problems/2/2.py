answer = 0
f_nums = [1, 1]
MAX = 4000000
i = 0

"""Utilize dynamic programming since recursion to compute Fib numbers becomes really slow at large n"""
while True:    
    f_curr = f_nums[i] + f_nums[i+1]
    if f_curr > MAX:
        break
            
    f_nums.append(f_curr)
    if f_curr % 2 == 0:
        answer += f_curr
    i += 1
        
print(answer)