# The following is a solution to a kata
# You can find it here: https://www.codewars.com/kata/591eab1d192fe0435e000014


def escape(carpark):
    instructions=[]
    start=0
    num_continuous_stairs=1
    # find starting point
    for i in range(len(carpark)):
        if 2 in carpark[i]:
            start = i
    for i in range(start,len(carpark)):
        
        # If we start on the exit floor:

        if 2 in carpark[i] and 1 not in carpark[i]:
            num_spots_to_exit=len(carpark[i])-carpark[i].index(2)
            if num_spots_to_exit!=1:
                # Add nothing if we start on the exit spot
                instructions.append(f"R{num_spots_to_exit-1}")

        # Find the stairs in the first floor

        elif 2 in carpark[i] and 1 in carpark[i]:
            num_spots_to_stairs=carpark[i].index(1)-carpark[i].index(2)
            # Add directions 
            if num_spots_to_stairs<0:
                instructions.append(f"L{abs(num_spots_to_stairs)}")
            else:
                instructions.append(f"R{num_spots_to_stairs}")
                # Replace 2 with 0 and 1 with 2 to mimic movement
            carpark[i][carpark[i].index(2)]=0
            carpark[i][carpark[i].index(1)]=2

#       Now for the middle stairs
        elif 1 in carpark[i]:
            
            num_spots_to_stairs=carpark[i-1].index(2)-carpark[i].index(1)
            if num_spots_to_stairs==0:
            # Then the stairs are aligned
                num_continuous_stairs+=1
                carpark[i][carpark[i].index(1)]=2

            # If the stairs are on the right
            elif num_spots_to_stairs<0:

                carpark[i][carpark[i].index(1)]=2
                instructions.append(f"D{num_continuous_stairs}")
                num_continuous_stairs=1
                instructions.append(f"R{abs(num_spots_to_stairs)}")
            else:
                # If the stairs are on the left
                carpark[i][carpark[i].index(1)]=2
                instructions.append(f"D{num_continuous_stairs}")
                num_continuous_stairs=1
                instructions.append(f"L{num_spots_to_stairs}")
        # For the last floor
        else:
            num_spots_to_exit=len(carpark[i])-carpark[i-1].index(2)-1
            if num_spots_to_exit!=0:
            # Don't add lateral directions if we're on the exit spot
                instructions.append(f"D{num_continuous_stairs}")
                instructions.append(f"R{num_spots_to_exit}")
            else:
                instructions.append(f"D{num_continuous_stairs}")
# Finally,

    return instructions