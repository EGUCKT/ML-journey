from matplotlib import pyplot as plt
import pandas as pd

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, label="Developer")

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]

# plt.plot(ages_x, py_dev_y, label="Python Developer")

# plt.title("Median Salary (USD) by Age")

# plt.xlabel("Ages")

# plt.ylabel("Median Salary (USD)")

# plt.legend()

# plt.show()


plt.style.use("fivethirtyeight")
# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
ages = pd.read_csv("student_performance.csv")["age"]
plt.hist(ages, bins=4, edgecolor="black")

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()