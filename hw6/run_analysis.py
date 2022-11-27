import sys
from iris_analysis.io.load import load_data
from iris_analysis.io.save import save_data
from iris_analysis.calculate import caluclate_mean
from iris_analysis.calculate import caluclate_median
from iris_analysis.calculate import calculate_sd

data = load_data(sys.argv[1])
mean = caluclate_mean(data[1:])
median = caluclate_median(data[1:])
sd = calculate_sd(data[1:], mean)
save_data(sys.argv[2], [mean, median, sd], ['mean', 'median', 'sd'], data[0][0:4])
