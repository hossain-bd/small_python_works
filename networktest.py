# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:10:40 2017

@author: nazmul
"""

# NetworkTest

from socket import socket, gethostname, gethostbyname, gethostbyaddr, getfqdn, \
                    gethostbyname_ex, getaddrinfo, AF_INET, SOCK_RAW ,IPPROTO_IP     


Host_Name = gethostname()    # Return a string containing the hostname of the machine
host_ip_addr = gethostbyname(Host_Name)  # Translate a host name to IPv4 address format
domain_name = getfqdn(host_ip_addr) # Return a fully qualified domain name

print('\n::::::::::::::::::::::::::::::::::::::::::::::::::')
print('Host Name: \t' + Host_Name)
print('IP Address: \t' + host_ip_addr)
print('Domain Name: \t' + domain_name)

print('::::::::::::::::::::::::::::::::::::::::::::::::::\n')

print(gethostbyaddr(host_ip_addr))   # Return a triple (hostname, aliaslist, ipaddrlist)

print(gethostbyname_ex(gethostname()))  # Return a triple (hostname, aliaslist, ipaddrlist)


# create a raw socket and bind it to the public interface
#s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)

#s.connect(("www.mcmillan-inc.com", 80))
#print (s.bind((host_ip_addr, 12345)))

