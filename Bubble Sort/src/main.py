#***********************************************************************************************************
# Classic Bubble sort
#***********************************************************************************************************

inputBuffer = [3,1,2,8,7,5,4]

"""
while True:
    inputValue = raw_input("type new value to be sorted: ")

    if (inputValue=='') :
        break
    
    print "Your value is: ",inputValue
    inputBuffer.append(inputValue)
"""   
print "---------------"
print "Original array:", inputBuffer
print "---------------"

for i in range(0,(len(inputBuffer)-1),1):
    for j in range(i,(len(inputBuffer)-1),1):
        if inputBuffer[j]>inputBuffer[j+1]:
            inputBuffer[j+1],inputBuffer[j] = inputBuffer[j],inputBuffer[j+1]   #swap two elements of array

print "---------------"
print "Sorted array:", inputBuffer            
print "---------------"            

# print "Value at position 1:", inputBuffer[1]

#for i in inputBuffer:
#    print i
    