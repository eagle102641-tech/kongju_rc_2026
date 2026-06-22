class Add_test:
    def __add__(self, other):
        return "Add_test 객체끼리 더하기 연산을 수행한다"

def main():
    print(2 ** 4)
    print(2 ** 64)
    print(18/4)
    print(type(18/4))
    print(18//4)
    print(type(18//4))
    
    print(18%4)
    a = Add_test()
    b = Add_test()
    print(a+b)


if __name__ == "__main__":
    main()