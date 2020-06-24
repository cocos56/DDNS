from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from Config.api import domainName, client
import json


def getRecords():
    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')
    request.set_DomainName(domainName)
    response = client.do_action_with_exception(request)
    # print(str(response, encoding='utf-8'))
    jsonObj = json.loads(response.decode("UTF-8"))
    return jsonObj["DomainRecords"]["Record"]

