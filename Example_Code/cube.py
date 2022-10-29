import multiprocessing as mp
import os

def cube(x):
    print (str(os.getpid())+" "+str(os.getppid()))
    return x**3

#MAIN
if __name__=="__main__":
    #il computer ha a disposizione un certo numero di core, ogni processo viene assegnato dall'interprete ad uno di questi core
    pool = mp.Pool(processes=4) #insieme di spazi in cui si possono svolgere i processi
    results = pool.map(cube,range(1,7)) #associa le funzioni cube a pool, pool.ap_async funzione in asincrono e non in sincrono (non aspetta il termine di tutti i processi)
    print(results)
    #print(results.get(timeout=1))