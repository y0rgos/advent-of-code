#!/usr/bin/python3

def main():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')

    c_max = [0,0,0]
    counter = 0
    for item in data:
        if item == '':
            c_max.append(counter)
            c_max.remove(min(c_max))
            counter = 0
        else:
            counter += int(item)
    print(sum(c_max))


if __name__ == '__main__':
    main()
