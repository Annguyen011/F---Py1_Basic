def calculate_total_price(quantity, price_per_unit=200):
    return quantity * price_per_unit

def calculate_change(amount_paid, total_price):
    return amount_paid - total_price

def main():
    try:
        quantity = int(input("Nhập số lượng sản phẩm: "))
        total_price = calculate_total_price(quantity)
        print(f"Số tiền bạn phải trả là: {total_price}")
        
        amount_paid = int(input("Nhập số tiền bạn muốn trả: "))
        change = calculate_change(amount_paid, total_price)
        print(f"Số tiền dư của bạn là: {change}")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
    main()