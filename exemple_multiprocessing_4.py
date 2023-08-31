import multiprocessing

def comer(fruta):
    print(f"Comi {fruta}.")

if __name__ == "__main__":
    frutas = [ f"(id {a}) {b}" for a, b in zip(range(20),
        [
        "Maçã", "Banana", "Laranja", "Morango", "Uva",
        "Pera", "Abacaxi", "Manga", "Melancia", "Melão",
        "Kiwi", "Cereja", "Limão", "Coco", "Framboesa",
        "Amora", "Pêssego", "Ameixa", "Figo", "Romã"
    ])]

    with multiprocessing.Pool(3) as p:
        p.map(comer, frutas)

    print("Fim")
