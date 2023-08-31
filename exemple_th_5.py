import threading
import queue

class Consumidor(threading.Thread):

    def __init__(self, nome, q):
        super().__init__()
        self.nome = nome
        self.q = q
        self.rodar = False

    def run(self):
        while True:
            try:
                item = q.get(block=False)
            except queue.Empty:
                break
            print(f"{self.nome}: Comi {item}.")
            q.task_done()

if __name__ == "__main__":

    frutas = [ f"(id {a}) {b}" for a, b in zip(range(20),
        [
        "Maçã", "Banana", "Laranja", "Morango", "Uva",
        "Pera", "Abacaxi", "Manga", "Melancia", "Melão",
        "Kiwi", "Cereja", "Limão", "Coco", "Framboesa",
        "Amora", "Pêssego", "Ameixa", "Figo", "Romã"
    ])]

    q = queue.Queue()
    for fruta in frutas:
        q.put(fruta)

    threads = []
    for nome in ["João", "Maria", "José"]:
        thread = Consumidor(nome, q)
        thread.start()
        threads.append(thread)

    q.join()
    for thread in threads:
        thread.join()

    print("Fim")
