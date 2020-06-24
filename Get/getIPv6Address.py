import os
import re


def getIPv6Address():

    output = os.popen("ipconfig /all").read()
    # print(output)
    result = re.findall(r"(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", output, re.I)
    return result[0][0]


if __name__ == "__main__":
    print(getIPv6Address())

