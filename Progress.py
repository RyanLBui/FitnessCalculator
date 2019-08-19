# pip install xlrd
import xlrd

# open excel sheet
calories_list = xlrd.open_workbook("calories.xlsx")
# get first sheet of excel
sheet = calories_list.sheet_by_index(0)

# print all columns in row 
# for col in range(sheet.ncols):
#     print(sheet.cell_value(1,col))

# create list[][]
data = [ [sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

weeklyGoal = 1300
weeklyCalories = 0
averageWeeklyCalories = 0

for i in range(1,8):
    print(str(data[0][i]) + ": " + str(data[1][i]))
    weeklyCalories += (data[1][i])
    print("Total Calories: " + str(weeklyCalories))

print("------------")
# round to two decimal place
averageWeeklyCalories = round((weeklyCalories / 7), 2)
print("Weekly Calorie Average: " + str(averageWeeklyCalories))

if averageWeeklyCalories > weeklyGoal:
    caloricDeficit = round((averageWeeklyCalories - weeklyGoal), 2)
    print("Went over weekly calorie intake goal of " + str(weeklyGoal) + " by " + str(caloricDeficit))
elif averageWeeklyCalories < weeklyGoal:
    caloricDeficit = round((weeklyGoal - averageWeeklyCalories), 2)
    print("Congrats, met weekly calorie intake goal of " + str(weeklyGoal) + "by " + str(caloricDeficit))