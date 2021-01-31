n_shoes = int(input())
all_shoes = [int(shoe) for shoe in list((input().split()))]
n_customers = int(input())

demand_price = []
for i in range(n_customers):
    demand_price.append(tuple(int(i) for i in input().split()))

receivables = 0  
    
for customer in demand_price:
    shoe_size = customer[0]
    if shoe_size in all_shoes:
        receivables += customer[1]
        del all_shoes[all_shoes.index(shoe_size)]
    else:
        pass
    
print(receivables)