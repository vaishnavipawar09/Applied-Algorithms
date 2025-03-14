def AutobotsTransportation(trips, capacity):
    if len(trips) == 0:
        return True
    # Determine the maximum drop-off location
    maxdrop = max([trip[2] for trip in trips])
        
    atpresentload = 0
    
    for kmtravelled in range(maxdrop + 1):
        for trip in trips:
            num_autobots, pickup, dropoffload = trip
            if kmtravelled == pickup:
                atpresentload += num_autobots
            
            if kmtravelled == dropoffload:
                atpresentload -= num_autobots

            if atpresentload > capacity:
                return False

    return True

# Test cases
trips1 = [[2, 1, 5], [3, 3, 7]]
capacity1 = 4
print(AutobotsTransportation(trips1, capacity1))  # Output: False

trips2 = [[2, 1, 5], [3, 3, 7]]
capacity2 = 5
print(AutobotsTransportation(trips2, capacity2))  # Output: True