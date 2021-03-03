
with open('common_passwords.txt', 'r') as f:
    comm_passwords = f.read().splitlines() #list

with open('username_hashpass.txt', 'r') as t:
    text = t.read().splitlines()
    for userhash in text:

