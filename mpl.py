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





# plt.style.use("fivethirtyeight")
# # ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# ages = pd.read_csv("student_performance.csv")["age"]
# plt.hist(ages, bins=4, edgecolor="black")

# plt.title('Ages of Respondents')
# plt.xlabel('Ages')
# plt.ylabel('Total Respondents')

# plt.tight_layout()

# plt.show()







# plt.style.use("fivethirtyeight")
# df = pd.read_csv("student_performance.csv")
# # plt.plot(df["marks"], label="marks")

# plt.hist(df["study_hours"], bins=7, edgecolor="black")

# plt.tight_layout()
# plt.show()





# plt.style.use("fivethirtyeight")
# df = pd.read_csv("student_performance.csv")
# plt.scatter(df["study_hours"], df["marks"], edgecolor="black", c=df["age"], cmap="viridis", s=100)
# colorbar = plt.colorbar()
# colorbar.set_label("Age of Student")
# plt.title("Study Hours vs Marks")
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.tight_layout()
# plt.show()



plt.style.use("fivethirtyeight")
df = pd.read_csv("student_performance.csv")
# correlation = df[["study_hours", "marks"]].corr()

"""study_hours has the strongest correlation with marks"""
print(df.corr(numeric_only=True))
plt.style.use("fivethirtyeight")
plt.scatter(df["study_hours"], df["marks"], edgecolor="black", c=df["sleep_hours"], cmap="viridis", s=100)
colorbar = plt.colorbar()
colorbar.set_label("Sleep Hours")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# mean = df["marks"].mean()
# median = df["marks"].median()
# mode = df["marks"].mode()[0]
# std = df["marks"].std()
# print(f"Mean: {mean}")
# print(f"Median: {median}") 
# print(f"Mode: {mode}")
# print(f"Standard Deviation: {std}")
# print(f"Correlation between Study Hours and Marks: {corr}")
