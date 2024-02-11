with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()
user_data = []
for line in lines:
    if line.startswith('#'):
        continue
    user_info = line.strip().split(':')
    user_data.append(user_info)
print("Printing out User Data:")
for user_info in user_data:
    username, password, userid, groupid = user_info
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("End of User Data")
