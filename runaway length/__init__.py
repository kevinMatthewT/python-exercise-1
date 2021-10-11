s=eval(input("Enter the plane's take off speed in m/s:"))
a=eval(input("Enter the plane's acceleration in m/s**2"))

mr=s**2/(2*a)

print("The minimum runway length needed for this airplane is" , round(mr,4) ,"meters")
