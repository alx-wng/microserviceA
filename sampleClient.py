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
        # open and write into request.txt
        f = open("request.txt", "w")
        print("writing ", sign, " into request.txt")
        f.write(sign)
        f.close()
        time.sleep(2)
        # read the image file path from request.txt
        f = open("request.txt", "r")
        content = f.read()
        print(content, " was read from request.txt")
        f.close()


main()
