#                       (*** IMPORTANT ==>> Any misuse is the responsibility of the individual ***)
#restart - shutdown :/
#import os 
import os 

#immediately action
print("1, shutdown Computer immediately ")
print("2, shutdown Computer after permission ")
print("3, restart Computer after immediately ")
print("4, restart Computer after permission ")
print("5, Exit")
print(end = "enter your choice : " )

choice = int(input())
#immediately action
if choice == 1:
    os.system("shutdown /s /t 0")
#after permission
elif choice ==2:
    print(end = "Enter your time per Sec : ")
    Sec = int(input())
    str_one  = "shutdown /s /t "
    str_two = str(Sec)
    str = str_one + str_two
    os.system(str)
#immediately action
elif choice ==3:
    os.system("shutdown /r /t 0")
#after permission
elif choice ==4:
    print(end = "Enter your time per Sec : ")
    Sec = int(input())
    str_one  = "shutdown /r /t "
    str_two = str(Sec)
    str = str_one + str_two
    os.system(str)
# Exit 
elif choice ==5:
    exit()
else:
    print("your input is Invalid !!!")