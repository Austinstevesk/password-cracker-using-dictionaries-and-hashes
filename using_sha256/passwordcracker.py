user_hash_dict = {}

with open('comm_passwords.txt', 'r') as f:
    comm_passwords = f.read().splitlines() #list

with open('username_hashpass.txt', 'r') as t:
    text = t.read().splitlines()
    for userhash in text:
        username = userhash.split(":")[0]
        print(username)
        hashcode = userhash.split(":")[1]
        user_hash_dict[username] = hashcode


