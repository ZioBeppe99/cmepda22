import math

class Vector2d:
    def __init__(self, x, y):
        self._x = float(x)  #cast della variabile a float, restituisce errore se variabile incorretta
        self._y = float(y)  #_x e _y ora sono immutabili
        #self.x = x  #una volta fissati i setter, possiamo chiamare i setter all'interni di init
        #self.y = y

    @property  #emuliamo il valore di self._x che è una variabile privata
    def x(self):
        return self._x    
    
    @property
    def y(self):
        return self._y

    #@x.setter  #con questo non posso cambiare il tipo di x o y nel mio codice
    #def x(self, value):
    #    self._x = float(value)

    #@y.setter
    #def y(self, value):
    #    self.y = float(value)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __str__(self):
        #print(f'Vector2d({self.x:3f},{self.y:3f})')  #metodo non flessibile per stampare 
        #return (f'v({self.x:3f},{self.y:3f})')  #ora la stringa può esssere salavata
        return (str((self.x, self.y))) #si sfrutta il metodo string delle tuple

    def __repr__(self):  #pensata per il debug
        return (f'Vector2d({self.x:3f},{self.y:3f})')

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2) 

    def __add__(self, other):   #metodo magico __add__ per sommare i vettori con l'operatore +
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
           return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2d(scalar * self.x, scalar * self.y)
    
    def __rmul__(self, scalar):  #moltiplicazione a destra
        return self * scalar  #l'operazione viene rimandata a __mul__

    def __iadd__(self, other):  #operazione in place, non funziona se la classe è read_only, bisogna aggiungere un setter
        self.x += other.x
        self.y += other.y
        return self  

    def __eq__(self, other):
        return ((self.x, self.y) == (other.x, other.y))

    def __gt__(self, other):  #funzione greater than
        return abs(self) > abs(other)




if __name__ == '__main__':
    v = Vector2d(3., 1.)
    #v_string = str(v)
    print(str(v))
    print(repr(v))
    print(f'Module of v is {abs(v):3f}')
    v2 = 0.5*v
    #v3 = v.add(v2)  #formalmente non si evidenzia la simmetria dell'operazione di somma
    #print(v.__doc__)  #stampa la doc string della classe
    v4 = 2*v
    print(v4)
    print(v)
    print(v > v2)
    print(hash(v))
    