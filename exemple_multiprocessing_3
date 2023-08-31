import multiprocessing
import queue

class Consumidor(multiprocessing.Process):

    def __init__(self, nome, q):
        super().__init__()
        self.nome = nome
        self.q = q
        self.rodar = False

    def run(self):
        while True:
            try:
                item = self.q.get(block=False)
            except queue.Empty:
                break
            print(f"{self.nome}: Comi {item}.")
            self.q.task_done()

if __name__ == "__main__":
    frutas = [ f"(id {a}) {b}" for a, b in zip(range(20),
        [
        "Maçã", "Banana", "Laranja", "Morango", "Uva",
        "Pera", "Abacaxi", "Manga", "Melancia", "Melão",
        "Kiwi", "Cereja", "Limão", "Coco", "Framboesa",
        "Amora", "Pêssego", "Ameixa", "Figo", "Romã"
    ])]

    q = multiprocessing.JoinableQueue()
    for fruta in frutas:
        q.put(fruta)

    processes = []
    for nome in ["João", "Maria", "José"]:
        processo = Consumidor(nome, q)
        processo.start()
        processes.append(processo)

    q.join()
    for process in processes:
        process.join()

    print("Fim")
