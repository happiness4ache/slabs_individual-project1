# Author: Nthabiseng Maya

"""
This program calculates the student's two examination/assessment tasks and brings the output whether they passed or failed
"""
# this calculates the student's marks as a floating point
practical = float(input("Enter practical assessment mark: "))
theory = float(input("Enter theory examination mark: "))

# this calculates the output of the two tasks
overall = (practical * 0.40) + (theory * 0.60)
print("overall mark:", overall,"%")

# ovearll mark whether the student has passed or the other way around
passed = overall >= 50
result = ["FAIL", "PASS"][passed]
print(result)
