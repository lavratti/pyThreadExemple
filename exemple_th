import random
import threading
import time


def worker(name, list_of_things):
    for thing in list_of_things:
        sleep_time = 1 + (random.random() * 2)
        print(f"{name} is busy with '{thing}' and will sleep for ({sleep_time:0.2f}s)")
        time.sleep(sleep_time)
        print(f"{name} is done with '{thing}'!")


if __name__ == "__main__":

    threads = []

    frutas = ["maçã", "banana", "laranja", "uva", "melancia", ]
    animais = ["cachorro", "gato", "leão", "elefante", "girafa",]
    paises = ["Brasil", "Argentina", "China", "Índia", "Japão",]
    cidades = ["Curitiba", "Nova York", "Tóquio", "Londres", "Paris",]

    tarefas = {
        "Ana": frutas,
        "João": animais,
        "Maria": paises,
        "Pedro": cidades
    }

    for key in tarefas:
        nome_da_pessoa = key
        lista_de_itens = tarefas[key]
        thread = threading.Thread(target=worker, args=[nome_da_pessoa, lista_de_itens])
        threads.append(thread)

    for thread in threads:
        print(f"Starting thread {thread._args[0]}.")
        thread.start()

    print("Wait for all threads to finish")
    for thread in threads:
        thread.join()

    print("Finished.")
