from Config.api import hostName
from Get.api import getRecords

if __name__ == '__main__':
    for each in getRecords():
        if each["RR"] == hostName:
            print(each["RecordId"], each["Value"])
