# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”

for i in ip_addresses:
	if i in allow_list:
		print(i ,"is allowed" )
	else:
		print(i ,"is not allowed")
  
  
for i in [0, 5]:

    print(i)
    
def multiples(num):
    multiple = num*3
    return multiple
multiples(2)
print(multiples(2))