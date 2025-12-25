print("📊 Welcome to Sales Tracker System")

sales = []
day = 1

while True:
    user_input = input(f"Enter sales for Day {day} (or type 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        amount = float(user_input)
        sales.append(amount)
        day += 1
    except ValueError:
        print("❌ Please enter a valid number or 'done'.")

print("\n✅ Data entry completed.")
print("Sales Entered:", sales)

total_sales = 0
for s in sales:
    total_sales += s

if len(sales) > 0:
    average_sales = total_sales / len(sales)
else:
    average_sales = 0

print(f"\n💰 Total Sales: {total_sales}")
print(f"📈 Average Daily Sales: {average_sales:.2f}")

# Find highest and lowest sales
if sales:
    print(f"🔝 Highest Sale: {max(sales)}")
    print(f"🔻 Lowest Sale: {min(sales)}")
