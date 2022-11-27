def caluclate_mean(data):
    mean = [0, 0, 0, 0]
    for row in data:
        for i in range(0, 4):
            mean[i] = mean[i]+float(row[i])
    mean[:] = [x / (len(data)-1) for x in mean ]
    return mean

def caluclate_median(data):
    median = [[], [], [], []]
    for row in data:
        for i in range(0, 4):
            median[i].append( float(row[i] ) )
    median[:] = [sorted(x) for x in median ]
    res = []
    for i in range(0, 4):
        res.append(  median[i][ int( len(data)/2 ) ] )
    return res

def calculate_sd(data, mean):
    sd = [0, 0, 0, 0]
    for row in data:
        for i in range(0, 4):
            sd[i] = sd[i] + pow( (float(row[i])-mean[i]), 2)
    sd[:] = [x / (len(data) - 1) for x in sd]
    return sd