import pandas as pd
import numpy as np

# Example data
data = {'college_name': ['ABC College', 'XYZ College', 'LMN University'],
        'city': ['Mumbai', 'Pune', 'Nagpur'],
        'university': ['Mumbai University', 'Pune University', 'Nagpur University'],
        'contacts': [[1, 2, 3], [1, 2, 3], [1,2]],
        'remarks': ['Excellent', 'Good', 'Average']}

# Create a DataFrame
india_maharashtra_colleges = pd.DataFrame(data)

# Auto-generate 'id' column
india_maharashtra_colleges['id'] = np.arange(1, len(india_maharashtra_colleges) + 1)

# Reorder columns
india_maharashtra_colleges = india_maharashtra_colleges[['id', 'college_name', 'city', 'university', 'contacts', 'remarks']]

# Display the DataFrame
print(india_maharashtra_colleges)

