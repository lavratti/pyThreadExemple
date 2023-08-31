import threading
import time


def tick(delay, count):
    i = 0
    while i < count:
        i += 1
        time.sleep(delay)
        print(f"Tick {i}")


def tock(delay, count):
    i = 0
    while i < count:
        i += 1
        time.sleep(delay)
        print(f"Tock {i}")


if __name__ == "__main__":

    delay = 1
    count = 10

    thread_tick = threading.Thread(target=tick, args=[delay, count])
    thread_tock = threading.Thread(target=tock, args=[delay, count])

    print("Start tick")
    thread_tick.start()

    time.sleep(delay/2)

    print("Start tock")
    thread_tock.start()

    print("Wait for all threads to finish")
    thread_tick.join()
    thread_tock.join()

    print("Finished.")
