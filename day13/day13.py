"""
Day 13: Shuttle Search

Part 1:
all buses depart airport at 0 min
all buses return to airport at ID min

input: time, list of bus IDs and x for buses NOT running
output: ID * min to wait for the bus
"""

def open_file(file_name):
    file = open(file_name, 'r')
    info = []
    bus_ids = []
    for line in file:
        line = line.rstrip('\n')
        if line.isdigit() == True:
            info.append(int(line)) #this is the time of arrival!
        else:
            ids = line.split(',')
            for id in ids:
                if id.isdigit() == True:
                    id = int(id)
                    # consider ONLY including valid bus ids?
                    bus_ids.append(id)
    info.append(bus_ids)
    return info
example = open_file('example.txt')
input = open_file('input.txt')

def earliest_bus(info):
    arrival, bus_ids = info
    bus_times = bus_ids.copy()
    earliest = None
    while True:
        for i, id in enumerate(bus_times):
            bus_times[i] += bus_ids[i]
            if bus_times[i] >= arrival:
                earliest = bus_times[i]
                time_diff = earliest - arrival
                return time_diff * bus_ids[i]
print(earliest_bus(example))
print(earliest_bus(input))
