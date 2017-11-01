import re
import pickle

fp=open("../log.log",'r')
content=fp.readlines()

ip_list=[]
id_list=[]


fp=open("../log.log",'r')
content=fp.readlines()

for line in content:
	if "index.php" in line:
		line=line.split("|")
		ip_list.append(line[1].strip())
	if "Device-Id" in line:
		line=line.split()
		id_list.append(line[1].strip())


dev_ip={}
for i in range(len(id_list)):
	if id_list[i] in dev_ip:
		if ip_list[i] not in dev_ip[id_list[i]]:
			dev_ip[id_list[i]].append(ip_list[i])
	else:
		dev_ip[id_list[i]]=[ip_list[i]]


with open("ip_user_map.pkl",'wb') as f:
	pickle.dump(dev_ip, f)

