import hashlib
user_hash_dict = {}

with open('comm_passwords.txt', 'r') as f:
    comm_passwords = f.read().splitlines() #list

with open('username_hashpass.txt', 'r') as t:
    text = t.read().splitlines()
    for userhash in text:
        print(userhash)
        username = userhash.split(":")[0]
        print(username)
        hashcode = userhash.split(":")[1]
        user_hash_dict[username] = hashcode

for user, hash in user_hash_dict.items():
    print(user, hash)

for password in comm_passwords:
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for user, hash in user_hash_dict.items():
        if hashed_pass == hash:
            print(f"Hash found!\n {username}:{password}")


