
import hashlib

counter = 1

password_in = raw_input("Please enter the MD5 Hash: ")
pwfile = raw_input("Please enter the file name: ")

try:
    pwfile = open(pwfile, "r")

except:
    print("\nFile not found.")
    quit()

for password in pwfile:
    m = hashlib.md5(password.strip()).hexdigest()
    print("Trying password number %d: %s" %(counter, password.strip()))
    
    counter +=1

    if password_in == m:
        print("Match found. \nPassword is: %s" %password)
        break
else:
    print("\nPassword not found.")
#7b64d09060db17ca6b96c0af99575903
#/Users/Shared/wordlist/rockyou.txt
