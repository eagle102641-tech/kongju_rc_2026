import datetime

def main():
    now=datetime.datetime.now()
    
    if now.month in [12, 1, 2, 3]:
        print(f"현재 계절은 {now.month}월로 겨울입니다.")
    elif now.month in [4, 5]:
        print(f"현재 계절은 {now.month}월로 봄입니다.")
    elif now.month in [6, 7, 8]:
        print(f"현재 계절은 {now.month}월로 여름입니다.")
    else:
        print(f"현재 계절은 {now.month}월로 가을입니다.")
        
if __name__ == "__main__":
    main()