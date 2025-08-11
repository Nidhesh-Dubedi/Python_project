import qrcode

menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 59,
    'aalo parata': 30,
    'salad': 70,
    'coffee': 80
}

print('''Welcome to our PY Restaurant
        Pizza           :        40Rs
        Pasta           :        50Rs
        Burger          :        59Rs
        Aalo parata     :        30Rs
        Salad           :        70Rs
        Coffee          :        80Rs
   ''')

order_total = 0
ordered_items = []

while True:
    item = input("Enter your order: ").lower()
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available!")

    another_order = input("Anything else, sir? (Yes or No): ").lower()
    if another_order == "no":
        break
    elif another_order != "yes":
        print("Please answer with Yes or No.")
        continue

print("Thanks for your order!!")
print("You ordered: " + ", ".join(ordered_items))
print(f"\n\tYour total bill is {order_total} Rs \n\n\t")


payment_mode = input("YOUR PAYMENT MODE PLZ: (netbanking/cash): ").lower() 

if payment_mode =="netbanking":
           #taking upi id as a input
      upi_id = "nidhesh966@axl"

   
      phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&am={order_total}&cu=INR'
      


     #create QR Codes for each payment apps
      phonepe_qr = qrcode.make(phonepe_url)
      
     
     #Display the QR Codes (you may need to install PIL/Pillow Library)
    
      print(f"Your total amount is {order_total} Rs. Please scan the QR code to complete the payment.")
      phonepe_qr.show()

    #   paytm_qr.show(order_total)
    #   google_pay_qr.show(order_total)

      print("\n\n\tThanks sir!! ENJOY YOUR MEAL SIR")

elif payment_mode =="cash":
    print("\n\n\tThanks sir!! ENJOY YOUR MEAL ")

else:
    print("\n\tUDHAR BAND HAI BHAI")

