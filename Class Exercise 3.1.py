def computepay(hours, rate):
    if hours <= 8:
        gross_pay = hours * rate
    else:
        regular_hours_pay = 8 * rate
        overtime_hours = hours - 8
        overtime_pay = overtime_hours * rate * 1.5
        gross_pay = regular_hours_pay + overtime_pay
        
    return gross_pay

def main():
    try:
        hours = float(input("Enter hours worked today: "))
        rate = float(input("Enter hourly rate: "))
        
        daily_gross_pay = computepay(hours, rate)
        
        print("Daily Gross Pay: $", round(daily_gross_pay, 2))
    except ValueError:
        print("Error: Please enter numeric values for hours worked and hourly rate.")

if __name__ == "__main__":
    main()
