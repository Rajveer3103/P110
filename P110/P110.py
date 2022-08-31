import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

#A code to find mean and standard deviation of 100 data points
dataset=[]
for i in range(0,30):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=st.mean(dataset)
std_deviation=st.stdev(dataset)
print("Mean of sample: ",mean)
print("Standard deviation of sample: ",std_deviation)

#Code to find mean of 100 data points, 1000 times and plot it.
#Function to get mean of given data samples
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value-data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean
#Function to plot mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=st.mean(df)
    fig=ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
#Pass the number of time, you want the mean of datapoints as parameter in range function
def setup():
    mean_list=[]
    for i in range(0,30):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=st.mean(mean_list)
    print("mean of sampling distribution: ",mean)

setup()
#Code to find the mean of raw data(population data)
population_mean=st.mean(data)
print("population mean: ",population_mean)
#Code to find standard deviation of sample data
def standard_deviation():
    mean_list=[]
    for i in range(0,30):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    sd_deviation=st.stdev(mean_list)
    print("Standard deviation of sampling distribution: ",sd_deviation)
standard_deviation()

