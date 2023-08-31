import random
import threading
import time

class Filosofo(threading.Thread):

    def __init__(self, lock, meu_lugar, hashis_compartilhados):
        super().__init__()
        self.lock = lock
        self.meu_lugar = meu_lugar
        self.hashis_compartilhados = hashis_compartilhados
        self.hashis_comigo = 0
        self.fome = random.randint(2, 5)

    def run(self):
        while self.fome > 0:
            self.pensar()
            if self.hashis_comigo == 2:
                self.comer()
            else:
                self.tentar_pegar_hashi()

    def pensar(self):
        print(f"{self.meu_lugar}: Pensando...")
        time.sleep(random.random()/10)

    def comer(self):
        self.fome -= 1
        self.hashis_comigo = 0
        with self.lock:
            self.hashis_compartilhados[self.meu_lugar] += 2
        print(f"{self.meu_lugar}: Comi, fome = {self.fome}.")

    def tentar_pegar_hashi(self):

        lugar_vizinho = self.meu_lugar + 1
        if lugar_vizinho == len(self.hashis_compartilhados):
            lugar_vizinho = 0

        with self.lock:
            if self.hashis_compartilhados[self.meu_lugar] > 0:
                print(f"{self.meu_lugar}: Peguei um hashi.")
                self.hashis_compartilhados[self.meu_lugar] -= 1
                self.hashis_comigo += 1

            elif self.hashis_compartilhados[lugar_vizinho] > 0:
                print(f"{self.meu_lugar}: Peguei um hashi.")
                self.hashis_compartilhados[self.meu_lugar] -= 1
                self.hashis_comigo += 1

            elif self.hashis_comigo == 1:
                print(f"{self.meu_lugar}: Desisti do meu hashi.")
                self.hashis_comigo -= 1
                self.hashis_compartilhados[self.meu_lugar] += 1


numero_de_filosofos = 4
hashis_compartilhados = [1] * numero_de_filosofos

if __name__ == "__main__":
    lock = threading.Lock()

    filosofos = []
    for n in range(numero_de_filosofos):
        filosofo = Filosofo(lock, n, hashis_compartilhados)
        filosofos.append(filosofo)

    for filosofo in filosofos:
        filosofo.start()

    for filosofo in filosofos:
        filosofo.join()

    print("Todos estão satisfeitos.")
