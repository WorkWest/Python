ip_addr = input("Please input an IP Address: ")

subnet_mask = input("Please input a Subnet Mask: ")

broken_ip = ip_addr.split('.')
broken_subnet = subnet_mask.split('.')
loopthis = 256 - int(broken_subnet[3])

print(broken_ip)
print(broken_subnet)
print(loopthis)

for x in range(0,loopthis):
  print(x)
  