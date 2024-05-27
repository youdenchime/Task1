# import the LifeQueue class from the queue #
from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None
Noofvisits = int(input("enter the number of URL history:"))
print('enter URL to visit:')
for i in range(Noofvisits):
    url = input('URL')
    print(f'visiting{url}')
    backward_history.put(current_page)
    current_pagr=url
#display current page
print(f"current_page :{current_page}")
#go back
while input ('do you want to go back?(yes/no):').lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page= backward_history.get()
        print(f'going forward to{current_page}')
    else:
        print("no forward page available")

