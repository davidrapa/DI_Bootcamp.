def divide_by_zero():
    try:
        num = float(input("Enter a number: "))
        result = num / 0
    except ZeroDivisionError:
        print("Error: divide by 0 wrong")
    except ValueError:
        print("Error: Invalid entry, please another number")
    except Exception as e:
        print(f"Error: {str(e)}")
    else:
        print(f"the resul is {result}")
    finally:
        print("Operation complete")

if __name__ == '__main__':
    divide_by_zero()