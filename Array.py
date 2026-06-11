# 1. Create an Array

from array import *

arr = array('i', [10, 20, 30, 40, 50])

print(arr)

# Output:
# array('i', [10, 20, 30, 40, 50])



# 2. Access Array Elements

from array import *

arr = array('i', [10, 20, 30, 40])

print(arr[0])
print(arr[2])

# Output:
# 10
# 30



# 3. Traverse Array using Loop

from array import *

arr = array('i', [10, 20, 30, 40])

for i in arr:
    print(i)

# Output:
# 10
# 20
# 30
# 40



# 4. Insert Element in Array

from array import *

arr = array('i', [10, 20, 40])

arr.insert(2, 30)

print(arr)

# Output:
# array('i', [10, 20, 30, 40])



# 5. Append Element in Array

from array import *

arr = array('i', [10, 20, 30])

arr.append(40)

print(arr)

# Output:
# array('i', [10, 20, 30, 40])



# 6. Remove Element from Array

from array import *

arr = array('i', [10, 20, 30, 40])

arr.remove(20)

print(arr)

# Output:
# array('i', [10, 30, 40])



# 7. Search Element in Array

from array import *

arr = array('i', [10, 20, 30, 40])

print(arr.index(30))

# Output:
# 2



# 8. Update Array Element

from array import *

arr = array('i', [10, 20, 30])

arr[1] = 25

print(arr)

# Output:
# array('i', [10, 25, 30])




# 9. Length of Array

from array import *

arr = array('i', [10, 20, 30, 40])

print(len(arr))

# Output:
# 4



# 10. Reverse Array

from array import *

arr = array('i', [10, 20, 30, 40])

arr.reverse()

print(arr)

# Output:
# array('i', [40, 30, 20, 10])
