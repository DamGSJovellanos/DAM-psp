import os
import sys

print("INICIO")
pid = os.fork()
pid_2 = os.fork()
pid_3 = os.fork()
if pid != 0 and pid_2 != 0 and pid_3 != 0: # padre
    os.wait() # Espera a que termine el primer hijo
    os.wait() # Espera a que termine el segundo hijo
    os.wait() # Espera a que termine el tercer hijo
    print(f"Hola desde el padre, mi PID es: {os.getpid()}")
elif pid != 0 and pid_2 != 0 and pid_3 == 0: # 1er hijo del padre
    print(f"Hola desde el tercer hijo: {os.getpid()}, mi padre es el: {os.getppid()}")
elif pid != 0 and pid_2 == 0 and pid_3 != 0: # 2º hijo del padre
    print(f"Hola desde el segundo hijo: {os.getpid()}, mi padre es el: {os.getppid()}")
elif pid == 0 and pid_2 != 0 and pid_3 != 0: # 1er hijo del padre
    print(f"Hola desde el primer hijo: {os.getpid()}, mi padre es el: {os.getppid()}")
print("FINAL")