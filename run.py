import requests
import os
from fake_useragent import UserAgent
from torrequest import TorRequest
    
with TorRequest(password='none') as tr:

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}

a = str(input("URL    - "))
x = int(input("Amount - "))

def run():
	for i in range(x):
		tr.reset_identity()
		response= tr.get(a)
		print(i+1)

run()
