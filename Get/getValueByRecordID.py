import json
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordInfoRequest import DescribeDomainRecordInfoRequest
from Config.api import client, recordID


def getValueByRecordID():
    request = DescribeDomainRecordInfoRequest()
    request.set_accept_format('json')
    request.set_RecordId(recordID)
    response = client.do_action_with_exception(request)
    jsonObj = json.loads(response.decode("UTF-8"))
    return jsonObj["Value"]


if __name__ == '__main__':
    print(getValueByRecordID())
