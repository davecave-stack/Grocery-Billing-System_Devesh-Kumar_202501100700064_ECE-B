# Grocery-Billing-System_Devesh-Kumar_202501100700064_ECE-B


**Problem Statement**
A grocery store wants to calculate the total cost of items purchased by a customer.
Calculate the total cost of 5 different items & each items can be taken in multiple numbers.
Add a 10% discount if the total exceeds Rs. 100.
Display the final payable amount.


**Approach**
The program begins by initializing a variable to store the total cost. It then uses a loop to accept the price and quantity for 5 items from the user. For each item, the cost is calculated by multiplying the price with the quantity, and this amount is added to the total cost.
After calculating the total cost, the program checks whether the total exceeds Rs. 100. If it does, a discount of 10% is calculated and subtracted from the total cost. Otherwise, no discount is applied.
Finally, the program displays the original total cost, the discount amount, and the final payable amount.


**Sample Output**
Enter details for Item 1
Enter price of item: Rs. 20
Enter quantity: 2

Enter details for Item 2
Enter price of item: Rs. 15
Enter quantity: 3

Enter details for Item 3
Enter price of item: Rs. 10
Enter quantity: 4

Enter details for Item 4
Enter price of item: Rs. 25
Enter quantity: 1

Enter details for Item 5
Enter price of item: Rs. 30
Enter quantity: 2

--- BILL SUMMARY ---
Original Total: Rs. 175.00
Discount Applied (10%): Rs. 17.50
Final Payable Amount: Rs. 157.50
