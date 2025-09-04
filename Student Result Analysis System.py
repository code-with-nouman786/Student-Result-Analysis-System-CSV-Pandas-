import pandas as pd

# Step 1: Create sample CSV (run once)
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Bilal", "Hina", "Zara"],
    "Roll No": [101, 102, 103, 104, 105, 106, 107],
    "Subject": ["Math", "Science", "English", "Math", "Science", "English", "Math"],
    "Obtained Marks": [85, 92, 76, 88, 95, 67, 90]
}
df = pd.DataFrame(data)
df.to_csv("results.csv", index=False)

# Step 2: Load CSV
df = pd.read_csv("results.csv")

# Step 3: Add calculations
df["Total Marks"] = 100  # since one subject; if multiple, group by
df["Percentage"] = (df["Obtained Marks"] / 100) * 100
df["Grade"] = df["Percentage"].apply(lambda x: 
    "A" if x >= 80 else ("B" if x >= 60 else "C"))

# Step 4: Sort & display top 5
top_students = df.sort_values(by="Percentage", ascending=False).head(5)
print("Top 5 Students:\n", top_students[["Name", "Roll No", "Percentage", "Grade"]])

# Step 5: Save processed data
df.to_csv("final_results.csv", index=False)
print("\nResults saved to final_results.csv")
