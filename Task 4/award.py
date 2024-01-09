#Get the times for the three events
cycling_time = int(input("Please enter a time for the cycling portion of the triathalon:"))
running_time = int(input("Please enter a time for the running portion of the triathalon:"))
swimming_time = int(input("Please enter a time for the swimming portion of the triathalon:"))
#add them all up
total_time = cycling_time + running_time + swimming_time
#check if an award is appropriate, replacing value with award with each succesfull if passed
award = "None"
if total_time < 111:
    award = "Provincial Scroll"
    if total_time < 106:
        award = "Provincial Half Colours"
        if total_time < 101:
            award = "Provincial Colours"
#output award if any
print(award)