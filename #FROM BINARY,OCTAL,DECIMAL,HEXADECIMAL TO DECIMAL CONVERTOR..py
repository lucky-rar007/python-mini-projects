#FROM BINARY,OCTAL,DECIMAL,HEXADECIMAL TO DECIMAL CONVERTOR.
#===========================================================

def to_decimal(val,typ):
    try:
        decimal_val=int(val,typ)
        return decimal_val
    
    except ValueError:
        print("Invalid input value , please enter a valid value.")
        return None
    
    except OverflowError:
        print("Value is too large for the specified type.")
        return None
    

def main():
    val=(input("Enter the value to be converted to decimal:"))
    typ=(input("Enter the number type (2/8/10/16):"))
    if typ not in ["2","8","10","16"]:
        print("please input a valid type.")
        return
    
    typ=int(typ)
    decimal_val=to_decimal(val,typ)
    if decimal_val is not None:
        print(f"The decimal equivalent of {val} is {decimal_val}.")

if __name__ == "__main__":
    main()
