from multiprocessing import Process
import time

def f(name):
    print("Hello" + name)
    time.sleep(1)

if __name__ == '__main__':
    p = Process(target=f, args=('Gianluca'))
    p.start() #avvia il processo p, il flusso dei comandi prosegue nel main
    print('ciao')
    p.join() #non fa proseguire il flusso finchè il processo non termina

