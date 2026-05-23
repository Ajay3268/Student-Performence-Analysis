import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("students.csv")

# Display dataset
print("Student Data:")
print(data)

# Calculate average marks
data["Average"] = (
    data["Math"] +
    data["Science"] +
    data["English"]
) / 3

print("\nAverage Marks:")
print(data[["Name", "Average"]])
# Pass or Fail status
data["Result"] = data["Average"].apply(
    lambda x: "Pass" if x >= 75 else "Fail"
)

print("\nPass/Fail Status:")
print(data[["Name", "Average", "Result"]])

top_student = data.loc[data["Average"].idxmax()]

print("\nTop Performer:")
print(top_student)

plt.bar(data["Name"], data["Average"])

for i, avg in enumerate(data["Average"]):
    plt.text(i, avg + 1, round(avg, 1), ha='center')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")

plt.savefig("student_performance_chart.png")
plt.show()