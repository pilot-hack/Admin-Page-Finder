import requests , os , time
# import used modules
from colorama import Fore,init
class colorma:

    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print(colorma.YELLOW+"\n\t [wathing...]")
time.sleep(2)

os.system("clear")

# print red color for all texts
print(colorma.RED)
print("\n[#10٪]")
time.sleep(0.2)
print("\n[##15٪]")
time.sleep(0.2)
print("\n[###20٪]")
time.sleep(0.2)
print("\n[####25٪]")
time.sleep(0.2)
print("\n[#####30٪]")
time.sleep(0.2)
print("\n[######35٪]")
time.sleep(0.2)
print("\n[#######40٪]")
time.sleep(0.2)
print("\n[########45٪]")
time.sleep(0.2)
print("\n[#########50٪]")
time.sleep(0.2)
print("\n[##########55٪]")
time.sleep(0.2)
print("\n[###########60٪]")
time.sleep(0.2)
print("\n[############65٪]")
time.sleep(0.2)
print("\n[#############70٪]")
time.sleep(0.2)
print("\n[##############75٪]")
time.sleep(0.2)
print("\n[###############80٪]")
time.sleep(0.2)
print("\n[################85٪]")
time.sleep(0.2)
print("\n[#################90٪]")
time.sleep(0.2)
print("\n[##################95٪]")
time.sleep(0.2)
print("\n[###################100٪]")
time.sleep(0.2)

os.system("clear")

#--------------------------------------
init()

test = open('Panel.txt').read().split()

print(Fore.RED+"[!]"+Fore.GREEN+"Please enter your URL with"+Fore.RED+"http"+Fore.GREEN+"or"+Fore.RED+"https")

url = input("Enter your URL =>")
for page in test:
  req = requests.get(str(url)+"/"+page)
  # check status_code
  if req.status_code==200:
  	print(Fore.GREEN+"[+]" + Fore.BLUE+" well is done "+Fore.GREEN+url+"/"+page)
  else:
  	print(Fore.RED+"[-]" + Fore.YELLOW+"well is not done "+Fore.CYAN+url+"/"+page)
