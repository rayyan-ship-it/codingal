import math
def main():
    try:
        angle_deg=float(input("enter the degrees"))
        angle_rad=math.radians(angle_deg)
        sine_val=math.sin(angle_rad)
        cosine_val=math.cos(angle_rad)
        if math.isclose(cosine_val,0.0,abs_tol=1e-15):
            tangent_val=None
        else:
            tangent_val=math.tan(angle_rad)
        print("angle=",angle_deg)
        print(f"sin({angle_deg}°) = {sine_val:.6f}")
        print(f"cos({angle_deg}°) = {cosine_val:.6f}")
        if tangent_val is None:
         print(f"tan({angle_deg}°) is undefined (cosine is zero).")
        else:
         print(f"tan({angle_deg}°) = {tangent_val:.6f}")
    except ValueError:
     print("invalid input")
if __name__=="__main__":
   main()       
