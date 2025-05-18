import zmq
import time
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)

p = "tcp://" + HOST + ":" + PORT
s.connect(p)

# Assina todos os tópicos
topics = ["TIME", "TEMP", "STATUS"]
for topic in topics:
    s.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"[Subscriber] Conectado a {p}, aguardando mensagens de: {', '.join(topics)}")
time.sleep(1)

while True:
    msg = s.recv()
    print("[Subscriber] Recebido:", msg.decode())
