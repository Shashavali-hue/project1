import pandas as pd
# 1. Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 100000]
}
df = pd.DataFrame(data)   
 
file_path_alt = r"C:\Users\Shashavali\Downloads\sem_wise_marks.csv"
try:
    df1 = pd.read_csv(file_path_alt)
    print("--- File Loaded Successfully (using forward slashes) ---")
    print(df1.head()) 
    print("\n")
except FileNotFoundError:
    print(f"Error: File not found at path: {file_path_alt}")
except Exception as e:
    print(f"An error occurred: {e}") 

print("--- 1. Original DataFrame ---")
print(df)
print("\n")
