import time
import os

while True:
    from datetime import datetime
    now = datetime.now()
    print('%02d/%02d/%04d' % (now.month, now.day, now.year))
    print("%02d:%02d:%02d" % (now.hour,now.minute,now.second))
    time.sleep(1)
    os.system('cls')
