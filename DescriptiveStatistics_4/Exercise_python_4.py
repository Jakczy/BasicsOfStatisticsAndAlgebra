import scipy.stats as scs
import pandas as pd
import pylab

# 1
normalDis = scs.norm.rvs(size=200, loc=2, scale=30)
disMean = normalDis.mean()
print(disMean)
tset, pval = scs.ttest_1samp(normalDis, 2.5)
print('p-values: ', pval)
if pval < 0.05:
    print('Odrzucamy hipotezę')
else:
    print('Przyjmujemy hipotezę')

# 2
napoje = pd.read_csv('napoje.csv',  delimiter=';')
df_napoje = pd.DataFrame(napoje)
print(df_napoje)
srednia = df_napoje[['lech', 'cola', 'regionalne']].mean()
print(srednia)
ttest, pval = scs.ttest_rel(df_napoje['lech'], df_napoje['cola'])
print(pval)

# 3
pepsi = df_napoje['pepsi']
scs.probplot(pepsi, dist='norm', plot=pylab)
pylab.show()
pepsi_stat, p = scs.shapiro(pepsi)
print('Pepsi: pepsi_stat=%.3f, p=%.3f\n' % (pepsi_stat, p))
if pepsi_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - pepsi: ', scs.mstats.normaltest(pepsi))
fanta = df_napoje['fanta']
scs.probplot(fanta, dist='norm', plot=pylab)
pylab.show()
fanta_stat, p = scs.shapiro(fanta)
print('Fanta: fanta_stat=%.3f, p=%.3f\n' % (fanta_stat, p))
if pepsi_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - fanta: ', scs.mstats.normaltest(fanta))
zywiec = df_napoje['zywiec']
scs.probplot(zywiec, dist='norm', plot=pylab)
pylab.show()
zywiec_stat, p = scs.shapiro(zywiec)
print('Zywiec: zywiec_stat=%.3f, p=%.3f\n' % (zywiec_stat, p))
if zywiec_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - zywiec: ', scs.mstats.normaltest(zywiec))
okocim = df_napoje['okocim']
scs.probplot(okocim, dist='norm', plot=pylab)
pylab.show()
okocim_stat, p = scs.shapiro(okocim)
print('Okocim: okocim_stat=%.3f, p=%.3f\n' % (okocim_stat, p))
if okocim_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - okocim: ', scs.mstats.normaltest(okocim))
regionalne = df_napoje['regionalne']
scs.probplot(regionalne, dist='norm', plot=pylab)
pylab.show()
regionalne_stat, p = scs.shapiro(regionalne)
print('Regionalne: regionalne_stat=%.3f, p=%.3f\n' % (regionalne_stat, p))
if regionalne_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - regionalne: ', scs.mstats.normaltest(regionalne))
cola = df_napoje['cola']
scs.probplot(cola, dist='norm', plot=pylab)
pylab.show()
cola_stat, p = scs.shapiro(cola)
print('Cola: cola_stat=%.3f, p=%.3f\n' % (cola_stat, p))
if cola_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - cola: ', scs.mstats.normaltest(cola))
lech = df_napoje['lech']
scs.probplot(lech, dist='norm', plot=pylab)
pylab.show()
lech_stat, p = scs.shapiro(lech)
print('Lech: lech_stat=%.3f, p=%.3f\n' % (lech_stat, p))
if lech_stat > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')
print('Normal test - lech: ', scs.mstats.normaltest(lech))

# 4
print('okocim-lech: ', scs.ttest_ind(okocim,lech))
print('fanta–regionalne: ', scs.ttest_ind(fanta,regionalne))
print('cola–pepsi: ', scs.ttest_ind(cola,pepsi))

# 5
stat, p = scs.levene(okocim, lech)
print('okocim-lech: stat=%.3f, p=%.3f' % (stat, p))
stat, p = scs.levene(zywiec, fanta)
print('zywiec-fanta: stat=%.3f, p=%.3f' % (stat, p))
stat, p = scs.levene(regionalne, cola)
print('regionalne-cola: stat=%.3f, p=%.3f' % (stat, p))

# 6
print(df_napoje)
napoje_2001 = df_napoje[df_napoje['rok'] == 2001]
regionalne_2001 = napoje_2001['regionalne']
print(regionalne_2001)
napoje_2001 = df_napoje[df_napoje['rok'] == 2015]
regionalne_2015 = napoje_2001['regionalne']
print(regionalne_2015)
print('2001 i 2015 dla piw regionalnych: ', scs.ttest_ind(regionalne_2001,regionalne_2015))

# 7
napoje_po_reklamie = pd.read_csv('napoje_po_reklamie-2.csv',  delimiter=';')
df_napoje_po_reklamie = pd.DataFrame(napoje_po_reklamie)
napoje_2016 = df_napoje[df_napoje['rok'] == 2016]
cola = napoje_2016['cola']
cola_po_reklamie = napoje_po_reklamie['cola']
stat, p = scs.ttest_ind(cola, cola_po_reklamie)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Odrzucamy hipotezę H0')
else:
    print('Przyjmujemy hipotezę H0')

fanta = napoje_2016['fanta']
fanta_po_reklamie = napoje_po_reklamie['fanta']
stat, p = scs.ttest_ind(fanta, fanta_po_reklamie)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Odrzucamy hipotezę H0')
else:
    print('Przyjmujemy hipotezę H0')

pepsi = napoje_2016['pepsi']
pepsi_po_reklamie = napoje_po_reklamie['pepsi']
stat, p = scs.ttest_ind(pepsi, pepsi_po_reklamie)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Odrzucamy hipotezę H0')
else:
    print('Przyjmujemy hipotezę H0')