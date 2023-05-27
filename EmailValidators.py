email = input("Enter Your Email : ") #a@g.pk
k,j,d=0,0,0
if len(email)>=6:
	if email[0].isalpha():
		if ("@" in email) and (email.count("@")==1):
			if ("." in email) and ((email[-4]==".") ^ (email[-3]==".")): 
				#if both conditions are turn then false when we use "^"
				for i in email:
					if i==i.isspace():
						k=1
					elif i.isalpha():
						if i==i.upper():
							j=1					
					elif i.isdigit():
						continue
					elif i=="_" or i=="." or i=="@":
						continue
					else:
						d = 1

				if k==1 or j==1 or d==1:
					print("wrong email 5")
				else:
					print("Right Email")
			else:
				print(". before like .com or .pk")

		else:
			print("Email must contain @ and use only 1 time")
	else:
		print("First Character Must be alphabet")
else:
	print("Email must be greater than 6 character")

