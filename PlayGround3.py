min_val = int(input())
max_val = int(input())

prime_list = []

for num in range(min_val, max_val + 1):
    if num > 1:
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False  
                break 
                
        if is_prime:
            prime_list.append(num)

print(f"found: {len(prime_list)}")
print(prime_list)