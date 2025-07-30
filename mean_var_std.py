# def calculate(lst):
#     for i in lst:

import numpy as np

# def to_3X3_matrix(lst):
#     if (len(lst) == 9):
#         lst_3X3 = np.array(lst).reshape(3,3)
#         return lst_3X3 



def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    # This will ensure that the length of the list is 9 for sure

    lst_3X3 = np.array(lst).reshape(3, 3)
    # Using the reshape function to change the given list to 3X3 matrix using numpy
    calculations = { 
        "mean" : [
           np.mean(lst_3X3, axis = 1).tolist(),
            # axis=0 → down the rows (i.e., column-wise operation)
            # axis=1 → across the columns (i.e., row-wise operation)
           np.mean(lst_3X3, axis = 0).tolist() ,
           np.mean(lst_3X3).item()
        ],
        "variance" : [
            np.var(lst_3X3, axis = 1).tolist(),
            np.var(lst_3X3, axis = 0).tolist(),
            np.var(lst_3X3).item()

        ],
        "standard_deviation" : [
            np.std(lst_3X3,axis=1).tolist(),
            np.std(lst_3X3, axis =0).tolist(),
            np.std(lst_3X3).item()
            ],
        "max" : [
            np.max(lst_3X3, axis=1).tolist(),
            np.max(lst_3X3, axis= 0).tolist(),
            np.max(lst_3X3).item()
            ], 
        "min" : [
            np.min(lst_3X3, axis=1).tolist(),
            np.min(lst_3X3, axis= 0).tolist(),
            np.min(lst_3X3).item()

             ],
        "sum" : [ 
            np.sum(lst_3X3, axis=1).tolist(),
            np.sum(lst_3X3, axis= 0).tolist(),
            np.sum(lst_3X3).item()
            ]
    }
    return calculations


# Get input from user
question = 9
lst = []
for i in range(question):
    lst_num = int(input(f"Please enter a number {i+1}: "))
    lst.append(lst_num)

# Call the function and print
print("\n3x3 Matrix:")
print(np.array(lst).reshape(3, 3))

print("\nCalculated Statistics:")
print(calculate(lst))