import os


def main():
    os.environ["MYVAR"] = "ciao muloniii"
    print(os.environ)

if __name__ == '__main__':
    main()
