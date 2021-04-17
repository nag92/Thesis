from Vicon.Mocap import Vicon

#defult opening
data = Vicon.Vicon("path/to/file")
# No interpolation!
data = Vicon.Vicon("path/to/file", interpolate=False)
# If any field is missing more than 100 values in a row, it will not be interpolated.  
data = Vicon.Vicon("path/to/file", maxnansrow=100) 
# If any field is missing more than 1000 values in total, it will not be interpolated.
data = Vicon.Vicon("path/to/file", maxnanstotal=1000)  
#overwrite file
data.save() 
#save to new file
data.save(filename="path/to/new/file")
