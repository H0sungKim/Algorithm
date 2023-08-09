# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

import time

FILE_NAME = input("Enter the name of the file whose performance you want to measure.\n=> ")

START_TIME = time.time()

__import__(FILE_NAME)

END_TIME = time.time()

print(f"time : {END_TIME-START_TIME}")