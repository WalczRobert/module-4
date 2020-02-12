"""Robert Walczak
You are online shopping at SuperAwesomeCouponDealsAndStuff.com. They offer two types of discounts. The first is cash-off
coupons, that you earn by shoppings. You may apply one $5 or $10 cash off per order. The second is percent discount
coupons for 10%, 15%, or 20% off. If you have cash-off coupons, those must be applied first, then apply the percent
discount coupons on the pre-tax amount. Then you add tax at 6% and shipping according to these guidelines:

"""
def calculate_price(price, cash_coupon, percent_coupon):
    Total_Cash = price - cash_coupon
    Total_Coupon = round(Total_Cash * (1-(percent_coupon/100)),2)
    if Total_Coupon <0:
        Total_Coupon =0
    print('Discount price is: ' + str(round(Total_Coupon,2)))
    Total_Tax = Total_Coupon * 1+(0.06)
    print('Your total with tax is : '+ str(round(Total_Tax,2)))
    calculate_shipping(Total_Coupon, Total_Tax)
    return(Total_Coupon)

def calculate_shipping(Total_Coupon, Total_Tax):
        if Total_Coupon < 10:
            shipping = 5.95
        elif 10 < Total_Coupon < 30:
            shipping = 7.95
        elif 30 < Total_Coupon < 50:
            shipping = 11.95
        else:
            shipping = 0
        grand_total = shipping + Total_Tax
        print('Shipping charges are: '+ str(shipping))
        print('our Total with shipping is: ' + str(round(grand_total,2)))




if __name__ == '__main__':
    price = int(input('What is your total?'))
    cash_coupon = int(input('Do you have a $5 or $10  coupon? if yes which do you have?'))
    percent_coupon = int(input("Do you have a 10%, 15% or 20% off coupon, if yes which do you have?"))
    calculate_price(price, cash_coupon, percent_coupon)

