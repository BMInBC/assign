#buggy code
def average_temperature(readings):
    total = 0
    for r in readings:
        total += r
    return total / len(readings) + 1  # Bug: "+1" shouldn’t be here

print(average_temperature([22.5, 23.0, 22.8, 23.2]))

#Applying PRAGMATIC debugging 
# Try on a large dataset
import time
readings = [23.0] * 10**6
start = time.time()
print(average_temperature(readings))
print("Time taken:", time.time() - start)

#reproducing the bug 
print(average_temperature([22.0, 22.0]))  # Expect 22.0 but get 23.0 (wrong!)
#automating and narrowing the test case
def test_avg():
    assert average_temperature([22.0, 22.0]) == 22.0, "Average failed!"
test_avg()

#getting visible by using print to inspect variable and computation 
def average_temperature(readings):
    total = 0
    for r in readings:
        total += r
    print(f"Total: {total}, Count: {len(readings)}")
    return total / len(readings) + 1  # suspicious part
#Making it fail every time by using hand code checks to force it to break when wrong 
assert average_temperature([22.0, 22.0]) == 22.0
#analysing the bug behavior and tracking recent change 

#Isolating the bug
def average_temperature(readings):
    return sum(readings) / len(readings) + 1  # same bug but clearer
#then finally confirming the fix
def average_temperature(readings):
    return sum(readings) / len(readings)

test_avg()  # should now pass
