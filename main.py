import threading


def find_max(zoznam):
    print(f"Maximum value: {max(zoznam)}")


def find_min(zoznam):
    print(f"Minimum value: {min(zoznam)}")


def main():
    numbers = list(map(int, input("Zadaj ľubovoľný počet celých čísel, každé oddeľ medzerou: ").split()))

    thread1 = threading.Thread(target=find_max, args=(numbers,))
    thread2 = threading.Thread(target=find_min, args=(numbers,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()