
total = 0
num_items = int(input("Enter the number of items: "))

for i in range(num_items):
    price = float(input(f"Enter price of item {i+1}: ₹"))
    qty = int(input(f"Enter quantity of item {i+1}: "))
    total += price * qty

gst = total * 0.18
final_amount = total + gst

print("\n--- Bill Summary ---")
print(f"Subtotal: ₹{total:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total Amount: ₹{final_amount:.2f}")
