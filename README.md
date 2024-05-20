How to request data:

    To request data using microserviceA.py, there must be a microservice.txt 
    file within the same directory as microserviceA.py. To call 
    microserviceA.py, the string of a name of an astrology sign should be 
    written into microserviceA.txt and then the calling program should wait 
    to give microserviceA.py time to run.

Example call:

    f = open("microserviceA.txt", "w")
    f.write("Leo")
    f.close()
    time.sleep(1)

How to receive data:

    To receive data from microserviceA.py, if the calling program wrote a 
    valid astrology sign into microserviceA.txt, the contents of 
    microserviceA.txt will be overwritten to contain the image file path 
    associated with that astrology sign. The calling program can then read 
    that file path from microserviceA.txt.

UML sequence diagram:
![UML sequence diagram](https://github.com/alx-wng/microserviceA/assets/154235295/5775326b-df21-40b1-89e6-013f30e2bc96)
