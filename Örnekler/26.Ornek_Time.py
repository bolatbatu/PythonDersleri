from datetime import datetime, timedelta
import time

now = datetime.now()

time.sleep(60)

now2 = datetime.now()

fark = now2-now

print(fark)