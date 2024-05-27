from queue import LifoQueue
patiant_list=LifoQueue()
current_list=None
while True:
    print("""Desk manager-select  the ption below :
          1. register patiant 
          2.remove patiant from the queue
          3. Display queue
          4.exist""")
    Ans=int(input("select an option from above>>>>" ))

    if Ans==1:
        name=input("enter the name of patiant>>" )
        patiant_list.put(name)
        current_list=name 
        print(f"registration successful {name}")
    elif Ans==2:
        patiant_list.get()
        print(f"remove successfully{current_list}")
    elif Ans==3:
        for i in patiant_list.queue :
            print(i)
    elif Ans==4:
        print("thank you for registration")
        break
    else:
        print("exist")




