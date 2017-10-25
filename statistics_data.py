import csv,glob
import numpy as np

def write_csv(file_name,row):
	with open(file_name, 'a') as out_f:
		wr = csv.writer(out_f)
		wr.writerow(row)

activties=['ScreenUsage', 'HeartRate', 'ActivFit', 'storage', 'Notif', 'BatterySensor', 'Bluetooth', 'LightSensor', 'Activity','SA','Errors']

users=glob.glob("../data/data_20Oct_2017/*")
all_activities = set()
sub_act_count="sub_act_count.csv"
user_count_list=[]
for user_file in users:
	acitivity_count=[0.]*len(activties)
	days=glob.glob(user_file+"/watch*")
	for df in days:
		activity_list=[f[f.rfind('/')+1:] for f in glob.glob(df+"/*")]
		activity_list=[f for f in activity_list if f!='watchInfo.txt']
		# activity_list=[f for f in activity_list if f!='SA' ]
		# activity_list=[f for f in activity_list if f!='Errors']
		# activity_list=[f for f in activity_list if f!='watchInfo.txt']
		for activity in activity_list:
			i=activties.index(activity)
			acitivity_count[i]+=1

	# acitivity_count.insert(0,user_file[user_file.rfind('/')+1:])
	# write_csv(sub_act_count,acitivity_count)
	user_count_list.append(acitivity_count)



user_count_list=np.array(user_count_list)

col_sum=np.sum(user_count_list,dtype=np.int32,axis=0)
print(activties)
print(col_sum)

print(np.count_nonzero(user_count_list,axis=0))










