from pywallet import wallet
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("I started at ",current_time)
success = 0
i = 0
while i < 1000000:
	seed = wallet.generate_mnemonic()
	w = wallet.create_wallet(network="Doge", seed=seed, children=0)
	if str(w["address"])[0:4].upper() == "DOGE":
		print (w["address"])
		print(str(w["address"])[0:4].upper())
		print (str(w["wif"])[2:len(str(w["wif"]))-1])
		success = 1
		i = 1000000
	i = i+1
	print("current loop: "+str(i), '\r', end="")

print("")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("I ended at ",current_time)
print("It took me "+str(i)+" loops")
if success == 1:
	print("to find a vanity address")
if success == 0:
	print("and I still haven't found what I'm looking for...")
