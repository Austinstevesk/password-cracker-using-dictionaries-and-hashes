#The procedure can be automated so that the hash can be generated automatically
import hashlib #Previously MD5

flag = 0
pass_hash = input("Enter MD5 hash: ") #eg d55e2b075670edeffabb2d23bfb6c1
wordlist = input("Enter File name: ") #should be existing, can be downloaded. eg passlist.txt

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found!!")
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()
 
    if digest == pass_hash:
        print("Password found")
        print('Password is ', word)
        flag = 1
        break

if flag == 0:
    print('Passcode not in the list')


    
