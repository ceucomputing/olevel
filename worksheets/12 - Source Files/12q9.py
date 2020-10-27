x = int(input("Enter a PSI value :"))
if x <= 50:
    print("The PSI level is good.")
elif x > 50 and x <= 100:
    print("The PSI Level is moderate.")
elif x > 100 and x <= 200:
    print("The PSI Level is unhealthy.")
elif x > 200 and x <= 300:
    print("The PSI Level is very unhealthy.")
else:
    print("The PSI Level is hazardous.")
