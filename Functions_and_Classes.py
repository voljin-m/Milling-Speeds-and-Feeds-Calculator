import math

def Surface_Speed():
    while True:
        d=float(input("Enter Your tool diameter in [mm]: "))
        n = float(input("Enter Your spindle speed in [rev/min]: "))
        if d !=0 and n!=0:
            print("\n\nYour tool diameter is: ",d,"[mm]")
            print("Your spindle speed is: ",n,"[rev/min]")
            vc=int((math.pi*d*n)/(1000))
            print("Your surface speed is: ",vc,"[m/min]")
        else:
            if d<=0:
                print("Your tool diameter is invalid!")
            elif n<=0:
                print("Your spindle speed is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer =="y":
            continue
        else:
            break
def Spindle_Speed():
    while True:
        d=float(input("Enter Your tool diameter in [mm]: "))
        vc = float(input("Enter Your surface speed in [m/min]: "))
        if d != 0 and vc != 0:
            print("\n\nYour tool diameter is: ",d,"[mm}")
            print("Your surface speed is: ",vc,"[m/min]")
            n = round((1000*vc)/(math.pi*d),3)
            print("Your spindle speed is: ",n,"[rev/min]")
        else:
            if d <= 0:
                print("Your tool diameter is invalid!")
            elif vc <= 0:
                print("Your surface speed is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
            continue
        else:
            break
def Feed_Speed():
    while True:
        fz=float(input("Enter Your feed per tooth in [mm/tooth]: "))
        z=float(input("Enter Your teeth quantity: "))
        n=float(input("Enter Your spindle speed in [rev/min]: "))
        if fz !=0 and z!=0 and n!=0:
            print("\n\nYour feed per tooth is: ", fz,"[mm/tooth]")
            print("Your teeth quantity is: ",z,"[-]")
            print("Your spindle speed is: ", n,"[rev/min]")
            vf=fz*z*n
            print("Your feed speed is: ",vf,"[mm/min]")
        else:
            if fz <= 0:
                print("Your feed per tooth is invalid!")
            elif z <= 0:
                print("Your teeth quantity is invalid!")
            elif n<=0:
                print("Your spindle speed is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
           continue
        else:
            break
def Feed_Per_Rev_Fz_z():
    while True:
        fz=float(input("Enter Your feed per tooth in [mm/tooth]: "))
        z=float(input("Enter Your teeth quantity: "))
        if fz !=0 and z!=0:
            print("\n\nYour feed per tooth is: ", fz,"[mm/tooth]")
            print("Your teeth quantity is: ",z,"[-]")
            fn=fz*z
            print("Your feed per revolition is: ",fn,"[mm/rev]")
        else:
            if fz <= 0:
                print("Your feed per tooth is invalid!")
            elif z <= 0:
                print("Your teeth quantity is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
           continue
        else:
            break
def Feed_Per_Rev_vf_n():
    while True:
        vf=float(input("Enter Your feed speed in [mm/min]: "))
        n=float(input("Enter Your spindle speed in [mm/rev]: "))
        if vf !=0 and n!=0:
            print("\n\nYour feed speed is: ", vf,"[mm/min]")
            print("Your spindle speed is: ",n,"[rev/min]")
            fn=vf/n
            print("Your feed per revolition is: ",fn,"[mm/rev]")
        else:
            if vf <= 0:
                print("Your feed speed is invalid!")
            elif n <= 0:
                print("Your spindle speed is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
           continue
        else:
            break
def Feed_Per_Tooth_vf_z_n():
    while True:
        vf=float(input("Enter Your feed speed in [mm/min]: "))
        z=float(input("Enter Your teeth quantity: "))
        n=float(input("Enter Your spindle speed in [rev/min]: "))
        if vf !=0 and z!=0 and n!=0:
            print("\n\nYour feed speed is: ", vf,"[mm/min]")
            print("Your teeth quantity is: ",z,"[-]")
            print("Your spindle speed is: ", n,"[rev/min]")
            fz=vf/(z*n)
            print("Your feed per tooth is: ",fz,"[mm/min]")
        else:
            if vf <= 0:
                print("Your feed speed is invalid!")
            elif z <= 0:
                print("Your teeth quantity is invalid!")
            elif n<=0:
                print("Your spindle speed is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
           continue
        else:
            break
def Feed_Per_Tooth_fn_z():
    while True:
        fn=float(input("Enter Your feed per revolution in [mm/rev]: "))
        z=float(input("Enter Your teeth quantity: "))
        if fn !=0 and z!=0:
            print("\n\nYour feed per revolution is: ", fn,"[mm/rev]")
            print("Your teeth quantity is: ",z,"[-]")
            fz=fn/z
            print("Your feed per tooth is: ",fz,"[mm/min]")
        else:
            if fn <= 0:
                print("Your feed per revolition is invalid!")
            elif z <= 0:
                print("Your tooth quantity is invalid!")
            else:
                print("Your Input is invalid!")

        answer = input("Do You wish to calculate again? (y/n) :")
        if answer == "Y" or answer == "y":
           continue
        else:
            break
def Feed_Choice():
    while True:
        print(
            "Please choose what to calculate: "
            " \n 1) Feed Speed"
            " \n 2) Feed per Revolution using Feed per Tooth and Teeth Quantity"
            " \n 3) Feed per Revolution using Feed speed and Spindle Speed"
            " \n 4) Feed per Tooth using Feed Speed, Teeth Quantity and Spindle speed"
            " \n 5) Feed per Tooth using Feed per Revolution and Teeth Quantity"
            " \n 6) Previous Page")
        user_choice = int(input("Enter Your choice: "))

        if user_choice == 1:
            Feed_Speed()
        elif user_choice == 2:
            Feed_Per_Rev_Fz_z()
        elif user_choice == 3:
            Feed_Per_Rev_vf_n()
        elif user_choice == 4:
            Feed_Per_Tooth_vf_z_n()
        elif user_choice == 5:
            Feed_Per_Tooth_fn_z()
        elif user_choice == 6:
            break
        else:
            print("You choice is invalid!")
        Another_Calculation = input("Do You want to calculate different type of feed? (y/n): ")
        if Another_Calculation == "Y" or Another_Calculation == "y":
            continue
        else:
            break