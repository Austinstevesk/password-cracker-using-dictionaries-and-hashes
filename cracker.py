import hashlib

password = 'password1'
hash_pass = hashlib.sha256(password.encode('utf-8'))
print(hash_pass.hexdigest()) #password1 = 0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e