def convert_date(date_str):
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", 
        "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    month, day, year = date_str.split("/")
    
    if month in months:
        month_name = months[month]
    else:
        print("Invalid month entered.")
        return
    
    if 1 <= int(day) <= 31:
        day = str(int(day))
    else:
        print("Invalid day entered.")
        return
    
    print(f"Date Output: {month_name} {day}, {year}")

date_input = input("Enter the date (mm/dd/yyyy): ")
convert_date(date_input)