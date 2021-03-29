#mangment system
def getdate(): #function for time and date
	import datetime
	return datetime.datetime.now()
get_time = getdate()
print("mangmanent system by silentace")
while(True):#loop for main page
	while(True):#loop for retry invalid input
		try:#try for int input
			option = int(input("1|For Sleep\n2|For Gaming\n3|For Eating\n4|For Exit\n"))		
			break#asking user waht you want
		except Exception:#for error loop
			print("Something Went Wrong\nTry Again")
			continue#continue using loop if something was in invalid type
	if(option==4):
		print("Thank For Using\ncode by silentace")
		break
	else:
		while(True):
			try: 
				option_2 = int(input("1|For Log\n2|Retrive\n3|For Exit\n"))
				break
			except Exception:
				print("Something Went Wrong\nTry Again")
				continue
	if(option_2==3):
		print("Thank For Using\ncode by silentace")
		break
	elif(option_2==1):#for log
		while(True):#for log loop
			if(option==1):#log for sleep
				while(True):
					with open("sleep.log") as file:
						file = file.readlines()
						for line in file:
							print(line,end="")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Use Again\n3|For Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
							continue
						if(option_3==1):
							break
						elif(option_3==2):
							break
						elif(option_3==3):
							break
						else:
							print("Something Went Wrong\nTry Again")
							continue
					if(option_3==1):
						print("Back")
						break
					elif(option_3==2):
						print("Again")
						continue
					elif(option_3==3):
						print("Quit")
						break
					else:
						break
				if(option_3==3):
					break
				elif(option_3==1):
					break
				else:
					print("Something Went Wrong\nTry Again")
			elif(option==2):#log for gaming
				while(True):
					with open("gaming.log") as file:
							file = file.readlines()
							for line in file:
								print(line,end="")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Use Again\n3|For Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
							continue
						if(option_3==1):
							break
						elif(option_3==2):
							break
						elif(option_3==3):
							break
						else:
							print("Something Went Wrong\nTry Again")
							continue
					if(option_3==1):
						print("Back")
						break
					elif(option_3==2):
						print("\nAgaiin\n")
						continue
					elif(option_3==3):
						print("Quit")
						break
					else:
						break
				if(option_3==3):
					break
				elif(option_3==1):
					break
				else:
					print("Something Went Wrong\nTry Again")
			elif(option==3):#log for eating
				while(True):
					with open("eating.log") as file:
						file = file.readlines()
						for line in file:
							print(line,end="")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Use Again\n3|For Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
							continue
						if(option_3==1):
							break
						elif(option_3==2):
							break
						elif(option_3==3):
							break
						else:
							print("Something Went Wrong\nTry Again")
							continue
					if(option_3==1):
						print("Back")
						break
					elif(option_3==2):
						print("Again")
						continue
					elif(option_3==3):
						print("Quit")
						break
					else:
						break
				if(option_3==3):
					break
				elif(option_3==1):
					break
				else:
					print("Something Went Wrong\nTry Again")				
	elif(option_2==2):#for retrive
		while(True):
			if(option==1):#for sleep
				while(True):
					type_for_sleep = input("Type Here:\n")
					with open("sleep.log","a") as file:
						file.write("["+str(get_time)+"] > "+type_for_sleep+"\n")
					print("Done")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Type Again\n3|Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
						if(option_3==1):
							print("Back")
							break
						elif(option_3==2):
							print("Again")
							break
						elif(option_3==3):
							print("Quit")
							break
						else:
							print("Something Went Wrong\nTry Again")
							break
					if(option_3==2):
						continue
					elif(option_3==3):
						break
					else:
						break
				if(option_3==1):
					break
				elif(option_3==3):
					break
			elif(option==2):#for gamong
				while(True):
					type_for_gaming = input("Type Here:\n")
					with open("gaming.log","a") as file:
						file.write("["+str(get_time)+"] > "+type_for_gaming+"\n")
					print("Done")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Type Again\n3|Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
						if(option_3==1):
							print("Back")
							break
						elif(option_3==2):
							print("Again")
							break
						elif(option_3==3):
							print("Quit")
							break
						else:
							print("Something Went Wrong\nTry Again")
							break
					if(option_3==2):
						continue
					else:
						break
				if(option_3==1):
					break
				elif(option_3==3):
					break
				else:
					break
			if(option==3):#for eating
				while(True):
					type_for_eating = input("Type Here:\n")
					with open("eating.log","a") as file:
						file.write("["+str(get_time)+"] > "+type_for_eating+"\n")
					print("Done")
					while(True):
						try:
							option_3 = int(input("1|For Back\n2|For Type Again\n3|Exit\n"))
						except Exception:
							print("Something Went Wrong\nTry Again")
						if(option_3==1):
							print("Back")
							break
						elif(option_3==2):
							print("Again")
							break
						elif(option_3==3):
							print("Quit")
							break
						else:
							print("Something Went Wrong\nTry Again")
							break
					if(option_3==2):
						continue
					else:
						break
				if(option_3==1):
					break
				elif(option_3==3):
					break
				else:
					break
	if(option_3==3):
		print("Thank For Using\ncode by silentace")
		break
	elif (option_3==3):
		print("Thank For Using\ncode by silentace")
		break
	elif(option_3==1):
		continue
	else:
		print("Something Went Wrong\nTry Again")
		continue
