import sys
for line in sys.stdin:
    if line.startswith('#'):
        continue
    user_info = line.strip().split(':')
    username, password, userid, groupid = user_info
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")