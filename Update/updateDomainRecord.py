from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from Config.api import client, hostName, recordID
from Get.api import getIPv6Address, getValueByRecordID


def updateDomainRecord():
    addr = getIPv6Address()
    print(addr)
    if addr == getValueByRecordID():
        print("已是最新，无需更新")
        return
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_RecordId(recordID)
    request.set_RR(hostName)
    request.set_Type("AAAA")
    request.set_Value(addr)
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


if __name__ == "__main__":
    updateDomainRecord()
