def main():
    # 입력 받기
    product_name = input("상품명을 입력하세요: ")
    price = input("상품 가격을 입력하세요: ")
    discount_rate = input("할인율을 입력하세요(%): ")

    try:
        # 숫자 변환
        price = float(price)
        discount_rate = float(discount_rate)

        # 할인 금액 및 최종 가격 계산
        discount_amount = price * discount_rate / 100
        final_price = price - discount_amount

        # 결과 출력
        print("\n=== 할인 계산 결과 ===")
        print(f"상품명: {product_name}")
        print(f"원래 가격: {price:,.2f}원")
        print(f"할인율: {discount_rate}%")
        print(f"할인 금액: {discount_amount:,.2f}원")
        print(f"최종 가격: {final_price:,.2f}원")

    except ValueError:
        print("가격과 할인율은 숫자로 입력해야 합니다.")


if __name__ == "__main__":
    main()