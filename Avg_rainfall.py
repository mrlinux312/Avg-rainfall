#average rainfall
print("Average Rainfall Program")
print("\n")
years = int(input("Please enter number of years to calculate the avg rainfall: "))
tot_rain = 0
month = 0

# Starting point for rain calculation
for years in range(1, years+1):
 for month in range(1,13):
      print(f"Year {years},{month}mnths")
      rainfall = float(input("Enter rainfall amount in inches:"))
     
     #calcualate total and average rainfall
      tot_rain += rainfall
      month = years * 12
      avg = tot_rain / month
print("\n")
print("\n")

print(f"Number of months:{month} \nTotal Inches of rainfall:{tot_rain:.2f}ins \nAverage rainfall per month:{avg:.2f}inches")


   
    
