import random
import string

with open ("movies.txt", "r") as file:
    lines= file.readlines()

    for i in lines:
            i=i.strip()
            szoveg= i.split(",")
            print(",".join(szoveg))


