import sys
user_string=sys.argv
user_action=sys.argv
if user_action=='lower':
    print(user_string.lower)
elif user_action=='title':
     print(user_string.title)
else:
     print("You have enter wrong user_action")