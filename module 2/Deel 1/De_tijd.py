for uur in range(1, 24):
    
    periode_am = uur < 12
    periode_pm = uur >= 12

    print(f"{uur} {'AM' if periode_am else 'PM'}")
