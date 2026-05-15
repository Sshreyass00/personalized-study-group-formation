# personalized-study-group-formation
# 📚 Personalized Study Group Formation using Clustering

## 📌 Project Overview
In large classrooms, students often struggle to find effective study partners.  
This project uses **Machine Learning (Clustering)** to automatically form study groups based on student academic performance and learning behavior.

The system groups students with similar characteristics to improve collaborative learning and study effectiveness.

---

# 🎯 Objective
The main objective of this project is to:
- Automatically create study groups
- Improve peer learning
- Reduce manual effort in grouping students
- Build balanced and effective learning teams

---

# 🧠 Machine Learning Technique Used
## K-Means Clustering
K-Means is an **unsupervised machine learning algorithm** used to group similar data points into clusters.

In this project, students are grouped based on:
- Subject-wise marks
- Learning pace
- Preferred study time

---

# 📊 Dataset Features

| Feature | Description |
|---|---|
| Student_ID | Unique student ID |
| Math | Math marks |
| Physics | Physics marks |
| CS | Computer Science marks |
| Learning_Pace | Slow / Medium / Fast |
| Study_Time | Morning / Afternoon / Night |

---

# ⚙️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab

---

# 🚀 Project Workflow

```text
Student Data
     ↓
Data Preprocessing
     ↓
Feature Scaling
     ↓
K-Means Clustering
     ↓
Study Group Formation
```

---

# 🔧 Steps Performed

## 1. Data Collection
Created a student dataset containing marks and learning behavior.

## 2. Data Preprocessing
- Converted categorical data into numerical values
- Applied feature scaling using StandardScaler

## 3. Clustering
Applied K-Means clustering algorithm to form groups.

## 4. Visualization
Generated:
- Elbow Method Graph
- Student Cluster Graph

---

# 📈 Outputs

## ✅ Dataset Preview
Displays student records and features.

## ✅ Elbow Method Graph
Used to determine the optimal number of clusters.

## ✅ Cluster Visualization
Shows grouped students in different clusters.

## ✅ Final Grouped Dataset
Each student is assigned to a study group.

---

# 📂 Project Structure

```text
Personalized-Study-Group-Formation/
│
├── students.csv
├── clustering_project.ipynb
├── grouped_students.csv
├── README.md
├── elbow_method.png
├── cluster_visualization.png
└── requirements.txt
```

---

# ▶️ How to Run the Project

## Step 1
Open Google Colab or Jupyter Notebook

## Step 2
Upload:
- students.csv
- clustering_project.ipynb

## Step 3
Run all cells

## Step 4
View:
- Cluster outputs
- Graphs
- Grouped student data

---

# 📌 Results
The model successfully grouped students into meaningful study teams based on:
- Academic performance
- Learning pace
- Study preferences

This improves collaborative learning and creates balanced study groups.

---

# 🔮 Future Enhancements
- Add attendance and assignment data
- Use advanced clustering algorithms
- Develop a web/mobile application
- Generate personalized recommendations

---

# 👨‍💻 Team Members

- Sharath H V
- Shivaskanda H S
- Shashikantha R G
- Shreyas Gowda K

---

# 📚 Conclusion
This project demonstrates how Machine Learning can be used in education to solve real-world problems such as study group formation.  
K-Means clustering effectively groups students into balanced teams and enhances collaborative learning.

---
