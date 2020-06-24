from Update.api import updateDomainRecord
from time import sleep
from datetime import datetime


while True:
    print(datetime.now())
    updateDomainRecord()
    sleep(15)
    print()
