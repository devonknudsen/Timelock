import time
import hashlib

DEBUG = False

# 
INTERVAL = 60
#
ctime = "2017 03 23 18 02 06"

#
def double_md5(elapsed):
    first_hash = hashlib.md5(str(elapsed).encode()).hexdigest()
    second_hash = hashlib.md5(str(first_hash).encode()).hexdigest()
    if DEBUG:
        print(first_hash)
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

# read epoch from stdin in the format YYYY MM DD HH mm SS
epoch = input()
epoch = time.strptime(epoch, "%Y %m %d %H %M %S")

# convert epoch time to seconds
START_TIME = time.mktime(epoch)

# DEBUG : shows start time
if DEBUG:
    print("Start time: {}".format(START_TIME))

# format current time and convert ctime time to seconds
set_current_time = time.strptime(ctime ,"%Y %m %d %H %M %S")
CURRENT_TIME = time.mktime(set_current_time)

# DEBUG : shows current time
if DEBUG:
    print("Current time: {}".format(CURRENT_TIME))

# calculate time elapse of current system since epoch time
TIME_ELAPSED = int(CURRENT_TIME - START_TIME )

# compute MD5
double_md5(TIME_ELAPSED - (TIME_ELAPSED % INTERVAL))

# DEBUG : shows current time and use current time from computer as new ctime
if DEBUG:
    print("current system time: {} {} {} {} {} {}\n".format(set_current_time.tm_year, set_current_time.tm_mon, set_current_time.tm_mday, set_current_time.tm_hour, set_current_time.tm_min, set_current_time.tm_sec))
    while(True):
        if DEBUG:
            print("Time elapsed: {}".format(TIME_ELAPSED))
        if((TIME_ELAPSED % INTERVAL) ==  0):
            print("Current sytem time: {}\n".format(time.ctime(CURRENT_TIME)))
            double_md5(TIME_ELAPSED)
        time.sleep(1)
        TIME_ELAPSED += 1
        CURRENT_TIME += 1
