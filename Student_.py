# =========================================================
# Personalized Study Group Formation using Clustering
# Complete Error-Free Code
# =========================================================

# =========================
# STEP 1: Import Libraries
# =========================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# =========================
# STEP 2: Create Dataset
# =========================

data = {
    'Student_ID':[
        'S1','S2','S3','S4','S5',
        'S6','S7','S8','S9','S10',
        'S11','S12','S13','S14','S15',
        'S16','S17','S18','S19','S20'
    ],

    'Math':[
        85,60,92,70,55,
        88,73,64,95,78,
        82,59,74,91,67,
        58,86,72,63,90
    ],

    'Physics':[
        78,72,88,68,60,
        91,75,58,94,80,
        79,65,77,89,70,
        55,84,74,61,92
    ],

    'CS':[
        90,65,95,72,58,
        85,70,62,96,76,
        84,61,73,93,66,
        60,88,71,64,89
    ],

    'Learning_Pace':[
        'Fast','Slow','Fast','Medium','Slow',
        'Fast','Medium','Slow','Fast','Medium',
        'Fast','Slow','Medium','Fast','Medium',
        'Slow','Fast','Medium','Slow','Fast'
    ],

    'Study_Time':[
        'Night','Morning','Night','Afternoon','Morning',
        'Night','Afternoon','Morning','Night','Afternoon',
        'Night','Morning','Afternoon','Night','Afternoon',
        'Morning','Night','Afternoon','Morning','Night'
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("students.csv", index=False)

print("Dataset Created Successfully!\n")

# Display dataset
print(df.head())

# =========================
# STEP 3: Encode Categorical Data
# =========================

df['Learning_Pace'] = df['Learning_Pace'].map({
    'Slow':0,
    'Medium':1,
    'Fast':2
})

df['Study_Time'] = df['Study_Time'].map({
    'Morning':0,
    'Afternoon':1,
    'Night':2
})

# =========================
# STEP 4: Select Features
# =========================

X = df[['Math','Physics','CS','Learning_Pace','Study_Time']]

# =========================
# STEP 5: Feature Scaling
# =========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =========================
# STEP 6: Elbow Method
# =========================

wcss = []

for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8,5))

plt.plot(range(1,11), wcss, marker='o')

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.show()

# =========================
# STEP 7: Apply KMeans
# =========================

kmeans = KMeans(
    n_clusters=3,
    init='k-means++',
    random_state=42,
    n_init=10
)

df['Group'] = kmeans.fit_predict(X_scaled)

# =========================
# STEP 8: Display Results
# =========================

print("\nStudents Grouped Successfully!\n")

print(df)

# =========================
# STEP 9: Save Output File
# =========================

df.to_csv("grouped_students.csv", index=False)

print("\nGrouped student data saved as 'grouped_students.csv'")

# =========================
# STEP 10: Visualize Clusters
# =========================

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    df['Math'],
    df['Physics'],
    c=df['Group'],
    s=100
)

plt.title("Student Clusters")

plt.xlabel("Math Marks")

plt.ylabel("Physics Marks")

plt.grid(True)

plt.show()