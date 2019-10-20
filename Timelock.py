import time
import hashlib
import sys

DEBUG = True

INTERVAL = 60

epoch = input()
epoch = time.strptime(epoch, "%Y %m %d %H %M %S")
START_TIME = time.mktime(epoch)
while(True):
    TIME = time.time()
    #TIME = time.mktime(time.strptime( "2017 03 23 18 02 06","%Y %m %d %H %M %S"))
    CURRENT_TIME = int(START_TIME - TIME)
    print("current system time: {}\n".format(time.ctime()))
    first_hash = hashlib.md5(str(CURRENT_TIME).encode()).hexdigest()
    if DEBUG:
        print(first_hash)
    second_hash = hashlib.md5(str(first_hash).encode()).hexdigest()
    if DEBUG:
        print(second_hash)
    letters = ''
    numbers = ''
    count_letters = 0
    count_numbers = 0
    for i in range(len(second_hash)):
        if(second_hash[i].isalpha() and count_letters < 2):
            letters += second_hash[i]
            count_letters += 1
        j = len(second_hash) - i -1
        if(second_hash[j].isdigit() and count_numbers < 2):
            numbers += second_hash[j]
            count_numbers += 1
    password = letters + numbers
    print(password)
    time.sleep(INTERVAL)
