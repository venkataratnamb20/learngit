#!/usr/bin/env python3


import sys
import os
print(sys.executable)

def main():
    print("Hello World!")
    print(f'PWD: {os.getcwd()}')
    print('files:')
    print(os.listdir("."))


if __name__ == "__main__":
    main()
