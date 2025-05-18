import zmq
import time
import random
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)

p = "tcp://0.0.0.0:" + PORT
s.bind(p)
print(f"[Publisher] Servindo em {p}")

status_flag = True

while True:
    # TIME
    time_msg = "TIME " + time.strftime("%H:%M:%S")
    s.send_string(time_msg)
    print("[Publisher] Enviado:", time_msg)

    # TEMP
    temp_value = round(random.uniform(20.0, 30.0), 2)
    temp_msg = f"TEMP {temp_value}°C"
    s.send_string(temp_msg)
    print("[Publisher] Enviado:", temp_msg)

    # STATUS
    status_msg = "STATUS OK" if status_flag else "STATUS FAIL"
    s.send_string(status_msg)
    print("[Publisher] Enviado:", status_msg)
    status_flag = not status_flag

    time.sleep(5)
