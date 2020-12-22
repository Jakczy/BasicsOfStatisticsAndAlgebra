import pandas as pd
import numpy as np
import scipy
from scipy.stats import scoreatpercentile, kurtosis, describe, skew, norm, uniform, binom
import statistics
import matplotlib.pyplot as plt

# 1
data = pd.read_csv('MDR_RR_TB_burden_estimates_2020-11-11.csv')
print(data.shape)
print(data.head())
print(data.columns)
print(data.dtypes)
e_rr_pct_new = data['e_rr_pct_new']
print(e_rr_pct_new)
print(e_rr_pct_new.mean())
print(e_rr_pct_new.describe())

# 2
increase = np.loadtxt('Wzrost.csv', delimiter=',')
print("Max: ", increase.max)
print("Max(numpy): ", np.max(increase))
print("Min: ", increase.min)
print("Min(numpy): ", np.min(increase))
print("Mean: ", increase.mean())
print("Mean(numpy): ", np.mean(increase))
print("Std ", increase.std())
print("Std(numpy): ", np.std(increase))
print("Median(numpy): ", np.median(increase))
print("Median: ", scoreatpercentile(increase, 50))
print("Median high: ", statistics.median_high(increase))
print("Median low: ", statistics.median_low(increase))
print("Standard deviation of the population: ", statistics.pstdev(increase))
print("Standard deviation of the sample: ", statistics.stdev(increase))
print("Kurtosis: ", kurtosis(increase))
print("Skew: ", skew(increase))
print("Basic statistics: ", describe(increase))

# 3

#4
brain_size = pd.read_csv('brain_size.csv', delimiter=';')
df = pd.DataFrame(brain_size)
df.replace('\.','0', regex=True, inplace=True)
viq_mean = df[df['Gender'] == 'Female']['VIQ'].mean()
print('VIQ mean: ', viq_mean)
group_by_gender = df.groupby(['Gender'])
gender_mean = group_by_gender.mean()
viq_list =list(df['VIQ'])
plt.hist(viq_list, density=True, bins=30)
piq_list = list(df['PIQ'])
plt.hist(piq_list, density=True, bins=30)
fsiq_list = list(df['FSIQ'])
plt.hist(fsiq_list, density=True, bins=30)
female_list_viq = list(df[df['Gender'] == 'Female']['VIQ'])
plt.hist(female_list_viq, density=True, bins=30)
female_list_piq = list(df[df['Gender'] == 'Female']['PIQ'])
plt.hist(female_list_piq, density=True, bins=30)
female_list_fsiq = list(df[df['Gender'] == 'Female']['FSIQ'])
plt.hist(female_list_fsiq, density=True, bins=30)