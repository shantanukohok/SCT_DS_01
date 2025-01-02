import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

gender_labels = ['Male', 'Female']
gender_counts = [720, 646] 

np.random.seed(42)
ages = np.random.randint(0, 100, size=1000)  # Random ages between 0 and 100

plt.figure(figsize=(10, 6))
sns.barplot(x=gender_labels, y=gender_counts, palette="Set2")

plt.title("Gender Distribution in India (2021 Estimates)", fontsize=14)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='lightblue', edgecolor='black')

plt.title("Age Distribution in India (Simulated Data)", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
