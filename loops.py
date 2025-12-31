user=input('please enter your age: ')
User=int(user)
if User>=18:
    print("you're now an adult, u can drink wine! ")
elif User>=15 and User<=17:
    print("hey, just almost to drink, wait until u reach 18y/o")
else:
    print('Go and sleep little guy, u have long journey to go!')
print('thank you!')

while User>=20:
    name=input("please enter your name: ")
    gender=input('please enter your gender: ')
    if gender.lower()=='male':
        print(f'{name}, you are a man please find a girlfriend')
    elif gender.lower()=='female':
        print(f'{name},you are a lady please do some make up to attract boys')
    else:
        print('WE DONT KNOW YOUR GENDER .')
    break

for item in name:
    print(item)
print('bye!')
