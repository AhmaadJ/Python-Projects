def main():
    # 40 hours a week, 52 weeks a year
    # Hourly to Yearly: hourly wage * hours/week * weeks/year
    # Yearly to Hourly: yearly wage / hours/weeks / weeks/year

    # 40 hours a week, 4.5 weeks a month
    # Hourly to Monthly: hourly wage * hours/week * weeks/month
    # Monthly to Hourly: yearly wage / hours/weeks / weeks/month

    salaryType = input ("Hourly, or Annual Salary?: ")
    if (salaryType == "Hourly" or salaryType == "hourly"):
        hourlySalary = int(input("Enter Hourly Salary: "))
        hourlyToAnnual(hourlySalary)
    elif (salaryType == "Annual" or salaryType == "annual" or salaryType == "Yearly" or salaryType == "yearly"):
        annualSalary = int(input("Enter Annual/Yearly Salary: "))
        annualToHourly(annualSalary)
    else:
        print('Improper Salary Type, Try Again.')

def hourlyToAnnual(hourly):
    newSalary = hourly * 40 * 52
    return print("Annual Salary is: $", newSalary)

def annualToHourly(annual):
    newSalary = (annual / 52) * (1/40)
    return print("Hourly Salary is: $", format(newSalary, '.2f'))

main()