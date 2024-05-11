# import pandas as pd

# df=pd.read_csv("Test_new.csv")

# dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}

# d=pd.DataFrame(dis)
# print(df.head())
# print(dis)
# dis["a"].append(7)
# print(dis)

# df=pd.concat([df,dis])
# d.to_csv("Test_new.csv")

#####################################################################################################
# Append Pandas DataFrame to Existing CSV File
# importing pandas module
# import pandas as pd
 
# # data of Player and their performance
# data = {
#     'Name': ['Hardik', 'Pollard', 'Bravo'],
#     'RPM': [50, 63, 15],
#     'SPEED': [0, 2, 3],
#     'COOLANT_TEMP': [4, 2, 1]
# }
 
# # Make data frame of above data
# df = pd.DataFrame(data)
 
# # append data frame to CSV file
# df.to_csv('GFG.csv', mode='a', index=False, header=False)
 
# # print message
# print("Data appended successfully.")
###############################################################################################
# import pandas as pd

# # data of Player and their performance
# data = {'RPM': [50, 63, 15],
#         'SPEED': [0, 2, 3],
#         'COOLANT_TEMP': [4, 2, 1]}

# # Make data frame of above data
# df = pd.DataFrame(data)

# # Reorder the columns to make 'RPM' the second column
# df = df[['RPM', 'SPEED', 'COOLANT_TEMP']]

# # append data frame to CSV file
# df.to_csv('GFG.csv', mode='a', index=False, header=False)

# # print message
# print("Data appended successfully.")

# # Create a new DataFrame with only the new RPM values
# new_rpm_values = [75, 80, 65, 90]

# # Write the new RPM values to the same CSV file
# with open('GFG.csv', 'a') as f:
#     for rpm in new_rpm_values:
#         f.write(f',{rpm},,\n')

# print("Additional data appended successfully.")

###############################################################################
import pandas as pd

# data of Player and their performance
data = {'RPM': ['1'],
        'SPEED': ['1'],
        'COOLANT_TEMP': ['1']}

# Make data frame of above data
df = pd.DataFrame(data)

# Reorder the columns to make 'RPM' the second column
df = df[['RPM', 'SPEED', 'COOLANT_TEMP']]

# Write the header row to the CSV file
header = ','.join(df.columns) + '\n'
with open('GFG.csv', 'w') as f:
    f.write(header)

# append data frame to CSV file
df.to_csv('GFG.csv', mode='a', index=False, header=False)

# print message
print("Data appended successfully.")

# Create a list with the new RPM values
new_rpm_values = [75, 80, 65, 90]

# Write the new RPM values to the same CSV file
with open('GFG.csv', 'a') as f:
    for rpm in new_rpm_values:
        f.write(f',{rpm},,\n')

print("Additional data appended successfully.")