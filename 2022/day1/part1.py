#!/usr/bin/python3

def main():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')

    c_max = 0
    counter = 0
    for item in data:
        if item == '':
            c_max = max(counter, c_max)
            counter = 0
        else:
            counter += int(item)
    print(c_max)


if __name__ == '__main__':
    main()
