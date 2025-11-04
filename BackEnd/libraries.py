import pandas as pd
import numpy as np 

try:
    # Step 1: Create sample data if you don't have data.csv
    data = {
        'A': np.random.randint(0, 100, 6),
        'B': np.random.randint(0, 100, 6),
        'C': np.random.randint(0, 100, 6),
        'D': np.random.randint(0, 100, 6)
    }
    
    # Save sample data to CSV
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)
    
    # Step 2: Read the CSV file
    df = pd.read_csv("data.csv")
    print("Loaded DataFrame:\n", df)
    
    # Step 3: Convert DataFrame to NumPy 2D array
    arr_2d = df.to_numpy()
    print("\n2D NumPy Array:\n", arr_2d)
    print("2D Array Shape:", arr_2d.shape)
    
    # Step 4: Reshape to 3D (3, 2, 4)
    # This assumes 6 rows (3×2) and 4 columns
    arr_3d = arr_2d.reshape(3, 2, 4)
    print("\n3D NumPy Array:\n", arr_3d)
    print("3D Array Shape:", arr_3d.shape)
    
    # Step 5: Access example element
    print("\nExample element [1][0][2] =", arr_3d[1][0][2])

except FileNotFoundError:
    print("Error: data.csv not found")
except ValueError as e:
    print(f"Error reshaping array: {e}")
    print("Make sure your data has exactly 6 rows and 4 columns")
except Exception as e:
    print(f"Unexpected error: {e}")