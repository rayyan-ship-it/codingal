def total_calc(amount,tip_percentage):
 total=amount*(1 + 0.01* tip_percentage)
 total=round(amount,2)
 print("pay the amount ",total)
total_calc(170,20)