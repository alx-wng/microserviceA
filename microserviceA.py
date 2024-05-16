# Alex Wong
# wongal2
# CS 361 microservice A

import time


def main():
    '''
    This microservice program will open request.txt, read the file, and if the
    file contains the name of an astrological sign, will write the path of an
    image associated with that sign, erase the astroligcal sign from
    request.txt, and write the image file path name into request.txt

    pre: request.txt is in the same directory as microserviceA.py
    post: the contents of request.txt may be changed to contain a file path
    returns: None
    '''
    print("microservice A is running")
    signs = {
        "Aries": "./images/aries.jpg",
        "Taurus": "./images/taurus.jpg",
        "Gemini": "./images/gemini.jpg",
        "Cancer": "./images/cancer.jpg",
        "Leo": "./images/leo.jpg",
        "Virgo": "./images/virgo.jpg",
        "Libra": "./images/libra.jpg",
        "Scorpio": "./images/scorpio.jpg",
        "Sagittarius": "./images/sagittarius.jpg",
        "Capricorn": "./images/capricorn.jpg",
        "Aquarius": "./images/aquarius.jpg",
        "Pisces": "./images/pisces.jpg"
    }
    while True:
        time.sleep(1)
        # open and read request.txt
        f = open("request.txt", "r")
        content = f.read()
        f.close()

        # if request.txt contains an astrological sign, write the corresponding
        # file path into request.txt
        if content in signs:
            f = open("request.txt", "w")
            print("writing image file path for ", content, " into request.txt")
            f.write(signs[content])
            f.close()
    return


main()
