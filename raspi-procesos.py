import os

def raspi_procesos():
    procesos = os.popen("ps -ef | wc -l").readline()
    procesos = int(procesos)
    return procesos

print(raspi_procesos())
