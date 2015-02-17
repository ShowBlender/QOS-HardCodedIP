import subprocess
import os
import time
import datetime

n = 1
delay = 1
uptime = 0
active = 0
inactive = 0
count = 0

#ip="69.38.216.135"
#ip="showblender.com"
ip = raw_input("Please enter ip/domain address(x.x.x.x/xxx.com):")

#with open('LogandCapture.txt', 'w') as f:
#    f.write(string)

with open(os.devnull, "wb") as limbo:
        while n == 1:
                count += 1
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                print st
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=limbo, stderr=limbo).wait()
                if result:
                        inactive += 1
                        uptime = (active * 100) / count
                        time.sleep(delay)
                        print ip, "inactive", count, " with ", uptime, "%", " Uptime"
                        #print result
                else:
                        active += 1
                        uptime = (active * 100) / count
                        time.sleep(delay)
                        print ip, "active", count, " with ", uptime, "%", " Uptime"
                        #print result
