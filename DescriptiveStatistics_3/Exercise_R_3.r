> install.packages("Rlab")
> library("Rlab")

# 1
> result <- sample(1:6, 100, replace=TRUE)
> table(result)
result
 1  2  3  4  5  6
10 21 11 19 16 23
> sum(result)
[1] 379
> mean(result)
[1] 3.79
> median(result)
[1] 4
> sd(result)
[1] 1.707352
> var(result)
[1] 2.915051
> hist(result)

# 2
> p <- 0.4
> n <- 5
> bernoulliDis <- rbern(100, p)
> bernoulliDis
 [1] 0 1 1 1 0 1 0 0 0 0 0 0 1 1 1 0 1 0 1 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0
 [53] 1 1 0 1 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 1 1 1 1
> binomialDis <- rbinom(100,n,p)
> binomialDis
  [1] 3 2 2 3 2 3 2 0 2 2 2 2 2 0 1 1 1 1 2 1 1 2 0 2 2 3 3 1 1 1 2 1 2 3 3 2 2 3 1 1 0 2 1 1 1 2 1 2 2 2 2 1
 [53] 2 1 3 1 4 0 1 2 2 2 1 2 3 4 2 1 2 1 2 4 1 1 0 3 3 2 1 1 1 1 3 2 3 3 2 2 2 3 2 1 3 1 3 2 3 2 3 0

> PoissonDis <- rpois(100, p)
> PoissonDis
 [1] 0 1 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 2 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 2 0 1 0 0
 [53] 1 0 2 1 0 0 1 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 3 2 1 0 0 0 1 1 0 1 0 2 0 0 1 0 1 0 0 0 3 2 0 0 0 0

 # 3
> print('Statystyka dla rozkładu Bernoulliego: ')
[1] "Statystyka dla rozkładu Bernoulliego: "
> srednia_bernoulli <- mean(bernoulliDis)
> srednia_bernoulli
[1] 0.34
> wariacja_bernoulli <- var(bernoulliDis)
> wariacja_bernoulli
[1] 0.2266667
> library("e1071") 
> kurtoza_bernoulli <- kurtosis(bernoulliDis)
> kurtoza_bernoulli
[1] -1.572653
> skosnosc_bernoulli <-skewness(bernoulliDis)
> skosnosc_bernoulli
[1] 0.6654131
> print('Statystyka dla rozkładu Dwumianowego: ')
[1] "Statystyka dla rozkładu Dwumianowego: "
> srednia_rozkladu_dwumianowego <- mean(binomialDis)
> srednia_rozkladu_dwumianowego
[1] 1.81
> wariancja_rozkladu_dwumianowego <- var(binomialDis)
> wariancja_rozkladu_dwumianowego
[1] 0.8827273
> kurtoza_rozkladu_dwumianowego <- kurtosis(binomialDis)
> kurtoza_rozkladu_dwumianowego
[1] -0.4635812
> skosnosc_rozkladu_dwumianowego <- skewness(binomialDis)
> skosnosc_rozkladu_dwumianowego
> print('Statystyka dla rozkładu Poissona: ')
[1] "Statystyka dla rozkładu Poissona: "
[1] 0.09041015
> srednia_poisson <- mean(PoissonDis)
> srednia_poisson
[1] 0.45
> wariancja_poisson <- var(PoissonDis)
> wariancja_poisson
[1] 0.4924242
> kurtoza_poisson <- kurtosis(PoissonDis)
> kurtoza_poisson
[1] 2.127528
> skosnosc_poisson <- skewness(PoissonDis)
> skosnosc_poisson
[1] 1.564903

# 5
> k<- 0:20
> n <- 20
> p <- 0.4
> plot(k, dbinom(k, size=20, prob = p), type='h', main='Binomial Distribution (n=20, p=0.4'), ylab='Probability', xlab='k', lwd=3)

# 6
> rozklad_normalny <- rnorm(30, 0, 2)
> rozklad_normalny
 [1]  3.47264090 -0.03758733 -5.09276255  3.57466976  1.24337598 -1.27841324  0.07059846  0.67953743  1.53913176 -0.82533796 -1.56556256 -1.02823382
[13] -1.29218063 -3.34774518 -2.73319004 -0.89355410 -0.65964300  2.35616540 -0.65281367  2.28442759  1.01195601  1.76460098 -0.07618607 -1.78518540
[25]  3.01059438 -0.36100204  2.20422550 -3.34836128 -0.32919876 -0.10634448
> mean(rozklad_normalny)
[1] -0.07337927
> var(rozklad_normalny)
[1] 4.355543
> skewness(rozklad_normalny)
[1] -0.1964267
> rozklad_normalny_2 <- rnorm(100, 0, 2)
> rozklad_normalny_2
  [1] -0.13630897 -0.43228578  1.77772474  1.05049696 -3.03722988 -0.90186839  2.96019499 -2.73295398 -1.01696004  0.67923891 -0.89084383 -1.26409415
 [13] -0.30528879 -0.20372344 -1.11584483 -0.26927703  1.77204490 -0.36941896 -3.90035020  1.01634881 -1.53125109  2.76771767  1.12897551 -2.63890956
 [25] -2.45725586 -0.07879337  1.06280621 -0.57116764 -3.99590817 -2.11493341 -2.55967988 -1.00212300 -1.71020502  1.75115602  1.49757606  0.31183993
 [37] -0.38849745 -0.83228490 -1.34914912 -0.41420217  2.00616073 -0.70565759 -0.07723050  2.02630746  2.57149738  0.89517487 -0.04183847 -1.49666832
 [49]  1.62842856  1.16858519 -0.70512533 -1.06579449  2.09065664  1.94221800 -1.27781441 -2.49065194 -0.86906885  1.65725107 -6.44397427  1.17155270
 [61]  0.98233056 -2.70767323 -3.60014803  1.63758361 -0.08640036 -0.67780654  3.72332225 -1.03470786  0.34865539  1.98537612 -2.04678533 -1.59681823
 [73]  0.99698389  1.47646285 -1.45448005  1.35361840  3.31126677 -0.05239988  1.58440277  1.44323190  1.12282019  3.24182608  0.71976763  2.36037350
 [85] -2.07408991  3.12072549 -2.84605567 -2.80909417  0.37420914 -4.48720009 -0.24781284  0.70460663 -2.06181292 -1.26592054  0.04277061 -2.24175934
 [97]  0.12394025  0.10312534  1.07561861  0.90439134
> mean(rozklad_normalny_2)
[1] -0.1701424
> var(rozklad_normalny_2)
[1] 3.619823
> kurtosis(rozklad_normalny_2)
[1] 0.108368
> rozklad_normalny_3 <- rnorm(1000, 0, 2)
> mean(rozklad_normalny_3)
[1] -0.06614603
> var(rozklad_normalny_3)
[1] 3.763068
> kurtosis(rozklad_normalny_3)
[1] 0.1192986


