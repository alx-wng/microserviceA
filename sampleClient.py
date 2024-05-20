# Alex Wong
# wongal2
# CS 361 microservice A

import time


def main():
    '''
    This program is an example of how to request/receive data from
    microserviceA.py.
    '''
    print("sampleClient.py is running")
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
             "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    for sign in signs:
        time.sleep(2)
        # open and write into microserviceA.txt
        f = open("microserviceA.txt", "w")
        print("writing ", sign, " into microserviceA.txt")
        f.write(sign)
        f.close()
        time.sleep(2)
        # read the image file path from microserviceA.txt
        f = open("microserviceA.txt", "r")
        content = f.read()
        print(content, " was read from microserviceA.txt")
        f.close()
    return


main()
