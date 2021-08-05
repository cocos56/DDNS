from Update.api import updateDomainRecord
from time import sleep
from datetime import datetime


while True:
    print(datetime.now())
    flag = True
    try:
        updateDomainRecord()
    except Exception as e:
        flag = False
        print(e)
        sleep(15)
        print()
    if flag:
        break
