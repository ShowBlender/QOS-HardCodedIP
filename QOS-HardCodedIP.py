import subprocess
import os
import time
import datetime

n = 1
delay = 1

ip="showblender.com"

with open('LogandCapture.txt', 'w') as f:
    f.write('file contents')

with open(os.devnull, "wb") as limbo:
        while n == 1:
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                print st
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        time.sleep(delay)
                        print ip, "active"
