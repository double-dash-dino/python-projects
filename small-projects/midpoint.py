# This function asks the user for the google maps urls of two locations

# It outputs the midway point between the two locations

def midpoint():
    import re
    pos1=input('Please paste in the url of the first location')
    pos1=re.findall(r"@\S+z", pos1)
    
    coordinates1=(float(re.findall(r"-*\d+.\d+",pos1[0])[0]), float(re.findall(r"-*\d+.\d+",pos1[0])[1]))
    
    pos2=input('Please paste in the url of the second location')
    pos2=re.findall(r"@\S+z",pos2)
    
    coordinates2=(float(re.findall(r"-*\d+.\d+",pos2[0])[0]), float(re.findall(r"-*\d+.\d+",pos2[0])[1]))
    
    coordinates_middle = ((coordinates1[0]+coordinates2[0])/2,(coordinates1[1]+coordinates2[1])/2)
    
    print(f'''
    Here is your middle point.
    https://www.google.com/maps/@{coordinates_middle[0]},{coordinates_middle[1]},14z
    ''')

midpoint()