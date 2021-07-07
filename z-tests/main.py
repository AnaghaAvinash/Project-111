import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#Reading and converting the data to a list
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#function to get the mean of the given data samples
def random_set_of_mean(counter):
  dataset = []
  for i in range(0, counter):
      random_index= random.randint(0,len(data)-1)
      value = data[random_index]
      dataset.append(value)
  mean = statistics.mean(dataset)
  return mean

# Function to get the mean of 30 data sets
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

# calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

#Standard deviation 1, 2 and 3
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#Finding the mean of interversion and plotting on graph
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1: ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 1], mode="lines", name="mean after intervension"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="Standard deviation 1 "))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="Standard deviation 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1], mode="lines", name="Standard deviation 3"))
fig.show()

#Z-score using formula
z_score = (mean_of_sample1 - mean)/std_deviation
print("The Z-Score is ",z_score)