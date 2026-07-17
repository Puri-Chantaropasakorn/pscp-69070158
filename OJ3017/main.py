"""Bill"""

in_price = int(input())

service = in_price * 0.1

if service < 50 :
    service = 50
elif service > 1000 :
    service = 1000

tax = (in_price + service) * 0.07
out_price = in_price + service + tax

print(f"{out_price:.2f}")
