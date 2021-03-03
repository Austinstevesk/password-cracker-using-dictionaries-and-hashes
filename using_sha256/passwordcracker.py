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


