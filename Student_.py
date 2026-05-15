# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load Dataset
df = pd.read_csv("students.csv")

# Encode Categorical Columns
df['Learning_Pace'] = df['Learning_Pace'].map({
    'Slow': 0,
    'Moderate': 1,
    'Fast': 2
})

df['Preferred_Study_Time'] = df['Preferred_Study_Time'].map({
    'Morning': 0,
    'Evening': 1,
    'Night': 2
})

# Handle Missing Values
df.dropna(inplace=True)

# Select Features
X = df[[
    'Math',
    'Physics',
    'Chemistry',
    'Biology',
    'Computer_Science',
    'English',
    'History',
    'Learning_Pace',
    'Preferred_Study_Time',
    'Attendance_Percent',
    'Assignments_Completed_Percent',
    'Average_Score'
]]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans Clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Create Student Groups
df['Group'] = kmeans.fit_predict(X_scaled)

# Display Result
print(df.head())

# Save Output
df.to_csv("grouped_students.csv", index=False)

print("\nStudent grouping completed successfully!")

# =========================
# Graph Visualization
# =========================

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    df['Math'],
    df['Average_Score'],
    c=df['Group'],
    s=100
)

# Graph Labels
plt.title("Student Clusters")
plt.xlabel("Math Marks")
plt.ylabel("Average Score")

# Grid
plt.grid(True)

# Show Graph
plt.show()