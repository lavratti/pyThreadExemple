import multiprocessing
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

    process_tick = multiprocessing.Process(target=tick, args=(delay, count))
    process_tock = multiprocessing.Process(target=tock, args=(delay, count))

    print("Start tick")
    process_tick.start()

    time.sleep(delay/2)

    print("Start tock")
    process_tock.start()

    print("Wait for all processes to finish")
    process_tick.join()
    process_tock.join()

    print("Finished.")
