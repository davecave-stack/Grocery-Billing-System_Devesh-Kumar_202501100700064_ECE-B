total_cost = 0
for i in range(1, 6):
    print(f"\nEnter details for Item {i}")
    price = float(input("Enter price of item: Rs. "))
    quantity = int(input("Enter quantity: "))
    item_total = price * quantity
    total_cost += item_total
print("\n--- BILL SUMMARY ---")
print(f"Original Total: Rs. {total_cost:.2f}")
discount = 0
if total_cost > 100:
    discount = total_cost * 0.10
    print(f"Discount Applied (10%): Rs. {discount:.2f}")
else:
    print("No Discount Applied")
final_amount = total_cost - discount
print(f"Final Payable Amount: Rs. {final_amount:.2f}")