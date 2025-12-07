import sys

DEBUG = True

def logo():
    print("      ____ ____ ____       ____ ____  ___ ____        _   _ _____ _     ____  _____ ____  ")
    print("     / ___/ ___/ ___|     / ___|  _ \\|_ _|  _ \\      | | | | ____| |   |  _ \\| ____|  _ \\ ")
    print("    | |  | |  | |   _____| |  _| |_) || || | | |_____| |_| |  _| | |   | |_) |  _| | |_) |")
    print("    | |__| |__| |__|_____| |_| |  _ < | || |_| |_____|  _  | |___| |___|  __/| |___|  _ < ")
    print("     \\____\\____\\____|     \\____|_| \\_\\___|____/      |_| |_|_____|_____|_|   |_____|_| \\_\\")
    print("")
    print("    # by danb1551")
    print("")

def render(columns, rows):
    faze = 1 # I know that it don't have any purpose
    if DEBUG:
        print("\n\n")
    else:
        logo()

    if faze == 1:
        print("    ", end="")
        for x in range(columns):
            print(str(x + 1).center(10, " "), end="")
        faze += 1
        print()
    if faze == 2:
        print("    ", end="")
        for x in range(columns):
            print(f"{"-".center(10, "-").replace("-", "|", count=1)}", end="")
        faze += 1
    if faze == 3:
        print("|")
        for y in range(rows):
            if (y + 1) == rows:
                pass
            print("    ", end="")
            for x in range(columns + 1):
                print("|         ", end="")
            print(f"\n{str(y + 1).center(4)}", end="")
            for x in range(columns + 1):
                print("|         ", end="")
            print("\n    ", end="")
            for x in range(columns + 1):
                print("|         ", end="")
            print(f"\n    {"|---------" * columns}|")

    print("\n\n")


def main():
    try:
        columns = int(sys.argv[1])
        rows = int(sys.argv[2])
    except Exception as e:
        print(f"Error when trying to get sys.args: {e}")
        exit(1)

    render(columns, rows)

if __name__ == "__main__":
    main()