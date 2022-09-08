ip_addr = input("Please input an IP Address: ")

subnet_mask = input("Please input a Subnet Mask: ")

broken_ip = ip_addr.split('.')
broken_subnet = subnet_mask.split('.')

print(broken_ip[3])