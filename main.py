from sys import stdin

def main():
 x = sorted(map(int,next(stdin).split(" ")[:-1]))
 print(x, end=" ")
 print()

if __name__ == "__main__":
 main()
