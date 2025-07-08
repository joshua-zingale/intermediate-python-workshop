# After installing a package (NumPy here for example)
# you can import it into your code like a standard library
# import as follows
import numpy

# Python also lets you rename an import using the "as" keyword.
# It is incredibly idiomatic to import numpy using
import numpy as np

def main():

    arr1 = np.array([1,2,3])
    arr2 = np.array([10,100,1000])

    # numpy allows element wise operations on its data
    print(arr1 + arr2)

if __name__ == "__main__":
    main()