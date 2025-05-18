import zmq
import time
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)

# Bind para todas as interfaces
p = "tcp://0.0.0.0:" + PORT
s.bind(p)
print(f"[Publisher] Servidor ativo em {p}")

while True:
    time.sleep(5)
    msg = str.encode("TIME " + time.strftime("%H:%M:%S"))
    print("[Publisher] Enviando:", msg.decode())
    s.send(msg)
