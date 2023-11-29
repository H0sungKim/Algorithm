# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

import time
import subprocess

# FILE_NAME = input("Enter the name of the file whose performance you want to measure.\n=> ")
FILE_NAME = "10026.py"

codeInfo = ['python', FILE_NAME]
inputData = """5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""

START_TIME = time.time()

# __import__(FILE_NAME)
process = subprocess.Popen(codeInfo, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate(input=inputData)
print("running...", end="")
END_TIME = time.time()
print("\routput ======================\n")
print(stdout)
print("=============================")
print(f"\ntime : {END_TIME-START_TIME}")