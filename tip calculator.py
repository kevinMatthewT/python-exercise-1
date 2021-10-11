sb=eval(input("enter the subtotal:$"))
tip=eval(input("Enter tip amount (as a %):"))
t=(tip/100)

print("Subtotal:$",sb)
print("Tip:$",round(sb*t,2))
print("Total:$",round(sb+(sb*t),2))
