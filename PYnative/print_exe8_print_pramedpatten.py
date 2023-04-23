import time

startTime = time.time()

# write your code or functions calls

endTime = time.time()
totalTime = endTime - startTime

print("Total time required to execute code is= ", totalTime)

rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end ='')
    print("")

