from ctypes import cdll


libc = cdll.LoadLibrary('./sample1/hello.so')


def main():
    libc.hello()


if __name__ == '__main__':
    main()
