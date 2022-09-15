import requests
import sys
import urllib3
urllib3.disable_warnings()

target_url = sys.argv[1]
with open(target_url, 'r') as f:
	for line in f.readlines():
		dict_x = dict()
		test1 = line.strip().split('?')
		test2 = test1[1].split('&')
		url = line.strip().split('?')[0]
		for i in test2:
			b1 = i.split('=')[0]
			b2 = i.split('=')[1]
			dict_x[b1] = b2
		resp = requests.post(url, data = dict_x, verify = False)
		print(resp.request.url, resp.request.method, resp.request.body, resp.status_code)
