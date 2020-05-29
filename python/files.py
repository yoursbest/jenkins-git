def main():
    f = open('lines.txt', 'r') # f is an iterator
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
