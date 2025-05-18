import zmq
import time
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)

# Conecta ao publisher pelo IP real da máquina que o executa
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")

print(f"[Subscriber] Conectado a {p}, aguardando mensagens...")

# Aguarda conexão estabilizar para não perder mensagens
time.sleep(1)

for i in range(5):
    msg = s.recv()
    print("[Subscriber] Recebido:", msg.decode())
