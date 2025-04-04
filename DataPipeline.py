from functions import * 
import time 
import datetime

# print what time the piepline started to run
print("starting pipeline at: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M%S ' ))
print("-------------------------------------------")

# step 1: extract video IDs
t0 = time.time()
getVideoIDs()
t1 = time.time()
print("step 1 done")
print("---> Video IDs downloaded in ", str(t1-t0), "seconds", "\n")

# step 2: extract transcripts from videos
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("step 1 done")
print("---> Transcripts downloaded in ", str(t1-t0), "seconds", "\n")

# step 3: transform data
t0 = time.time()
transformData()
t1 = time.time()
print("step 3 done")
print("--->  Data transformed in ", str(t1-t0), "seconds", "\n")




