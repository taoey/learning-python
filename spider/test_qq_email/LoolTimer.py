import time
from datetime import datetime
def p():
    now_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)


one_day=60*60*24
while True:
    p()
    time.sleep(5)