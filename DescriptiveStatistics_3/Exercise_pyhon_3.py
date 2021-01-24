import seaborn as sns
import scipy.stats as scs
import statistics as stat
import matplotlib.pyplot as plt

# 1
print("# 1")
value = (1, 2, 3, 4, 5, 6)
probability = (1/6,1/6,1/6,1/6,1/6,1/6)
rozklad = scs.rv_discrete(values=(value, probability))
print('średnia: ', rozklad.mean())
print('wariancja: ', rozklad.var())
print('odchylenie standardowe: ', rozklad.std())
print('mediana: ', rozklad.median())

# 2
print("# 2")
p = 0.8
n = 10
bernoulliDis = scs.bernoulli.rvs(p, size=100)
binomialDis = scs.binom.rvs(n, p, size=100)
PoissonDis = scs.poisson.rvs(p, size=100)

# 3
print("# 3")
Dis = [["Rozkład Bernouliego", bernoulliDis],
       ["Rozkład dwumianowy", binomialDis],
       ["Rozkład Poissona", PoissonDis]]
for d in Dis:
    print(d[0], ":")
    print("Średnia: ", d[1].mean())
    print("Wariancja: ", stat.pvariance(d[1]))
    print("Kurtoza: ", scs.kurtosis(d[1]))
    print("Skośność: ", scs.skew(d[1]))

# 4
print("# 4")
ax1 = sns.displot(bernoulliDis,
                  kde=False,
                  color='red')
ax1.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
ax2 = sns.displot(binomialDis,
                  kde=False,
                  color='blue')
ax2.set(xlabel='Binomial Distribution', ylabel='Frequency')
ax3 = sns.displot(PoissonDis,
                  kde=False,
                  color='green')
ax3.set(xlabel='Poisson Distribution', ylabel='Frequency')

# 5
print("# 5")
n = 20
p = 0.4
k = 20
binomialDis2 = scs.binom.rvs(n, p, size=20)
ax4 = sns.displot(binomialDis2,
                 kde=False,
                 color='blue')
ax4.set(xlabel='Binomial Distribution', ylabel='Frequency')
print('Suma prawdopodobieństw: ', scs.binom.cdf(k, n, p))

# 6
print("# 6")
normalDis = [100, 500, 1000, 5000, 10000]
for dis in normalDis:
    normal = scs.norm.rvs(size=dis, loc=0, scale=2)
    print(dis, "danych:")
    print('Średnia:', normal.mean())
    print('Wariancja: ', normal.var())
    print('Odchylenie standardowe: ', normal.std())
    print('Mediana: ', scs.norm.median(loc=0, scale=2))
    print('Kurtoza: ', scs.kurtosis(normal))
    print('Skośność: ', scs.skew(normal))

# 7
print("# 7")
normalDis= scs.norm.rvs(size=10000, loc=1, scale=2)
standardDis = scs.norm.rvs(size=10000, loc=0, scale=1)
density = scs.norm.rvs(size=10000, loc=-1, scale=0.5)
f, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.distplot(normalDis,
            kde=True,
            color='blue',
            ax=axes[0, 0])
sns.distplot(standardDis,
            kde=True,
            color='green',
            ax=axes[0, 1])
sns.distplot(density,
            kde=True,
            color='red',
            ax=axes[1, 0])
sns.distplot(normalDis,
            kde=True,
            color='blue',
            ax=axes[1, 1])
sns.distplot(standardDis,
            kde=True,
            color='green',
            ax=axes[1, 1])
sns.distplot(density,
            kde=True,
            color='red',
            ax=axes[1, 1])
plt.show()
