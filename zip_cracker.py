import zipfile 
import os,sys
###################### Jangan di recode bosque, pake aja lah apa susahnya sih, recode gabakalan membuatmu menjadi profiesional
if sys.platform == "linux" or sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32" or sys.platform == "win64":
	os.system("cls")
else:
	os.system("clear")

banner = """Program name : BruteForce Zipfile
Author : Rizal hichijou
Version : 0.1
===============================================
"""
print(banner+"\n")
def main():
	try:
		cmd = raw_input("[*]File_> ")
		if cmd == "" or cmd == " ":
			print("[*] Don't leave blank field")
		else:
			pass
	except KeyboardInterrupt:
		print("[*] Runtime error : Keyboard Interrupt")
		exit()
	except EOFError:
		print("[*] Runtime error : Key break")
		exit()
	try:
		files = str(cmd)
		zip = zipfile.ZipFile(files)
	except IOError:
		print("[!] Cannot open the file")
		exit()
	try:
		passfile = open("wordlist.txt")
	except IOError:
		print("[!] Wordlist.txt file not found, please check again ")
		exit()
	try:
		for line in passfile.readlines():
			try:
				password = line.strip("\n")
				zip.extractall(pwd=password)
				print "[*] Password Found : "+password
				break
			except Exception, e:
				print "[*] Password not match : "+password
	except KeyboardInterrupt:
		print("[*] Runtime error : Keyboard Interrupt")
		exit()
	except EOFError:
		print("[*] Runtime erro : Key break")
		exit()


if __name__ == "__main__":
	main()