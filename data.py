import csv
import pandas as pd
import plotly.figure_factory as ff 
import statistics

df = pd.read_csv("StudentsPerformance.csv")
math_score = df["math score"].to_list()
writing_score = df["writing score"].to_list()
math_mean = statistics.mean(math_score)
writing_mean = statistics.mean(writing_score)
math_mode = statistics.mode(math_score)
writing_mode = statistics.mode(writing_score)
math_median = statistics.median(math_score)
writing_median = statistics.median(writing_score)
math_stddevaition = statistics.stdev(math_score)
writing_stddeviation = statistics.stdev(writing_score)
print(math_mean,",",writing_mean)
print(math_mode,",", writing_mode)
print(math_median, ",", writing_median)
print(math_stddevaition,",", writing_stddeviation)

math_1_std_deviation_start, math_1_std_deviation_end = math_mean - math_stddevaition, math_mean + math_stddevaition
math_2_std_deviation_start , math_2_std_devaition_end = math_mean - (2*math_stddevaition), math_mean+(2*math_stddevaition)
math_3_std_deviation_start , math_3_std_deviation_end = math_mean - (3*math_stddevaition), math_mean+(3*math_stddevaition)

math_list_of_data_within_1_std_deviation = [result for result in math_score if result > math_1_std_deviation_start and result< math_2_std_devaition_end ]
data_lies_within_1_std_deviation = len (math_list_of_data_within_1_std_deviation)*100.0/len(math_score)
print(data_lies_within_1_std_deviation)

writing_1_std_deviation_start, writing_1_std_deviation_end = writing_mean - writing_stddeviation, writing_mean+writing_stddeviation
writing_2_std_deviation_start , writing_2_std_deviation_end = writing_mean - (2*writing_stddeviation), writing_mean+(2*writing_stddeviation)
writing_3_std_deviation_start , writing_3_std_deviation_end = writing_mean - (3*writing_stddeviation), writing_mean+ (3*writing_stddeviation)

writing_list_of_data_within_1_std_deviation = [result for result in writing_score if result > writing_1_std_deviation_start and result< writing_1_std_deviation_end]
data_writing_lies_within_1_std_deviation = len (writing_list_of_data_within_1_std_deviation)*100.0/len(writing_score)
print(data_writing_lies_within_1_std_deviation)
