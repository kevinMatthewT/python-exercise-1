sb=eval(input("enter the subtotal:$"))
tip=eval(input("Enter tip amount (as a %):"))
t=(tip/100)

print("Subtotal:$",format(sb,".2f"))
print("Tip:$",format(sb*t,".2f"))
print("Total:$"format(sb+(sb*t),".2f"))
