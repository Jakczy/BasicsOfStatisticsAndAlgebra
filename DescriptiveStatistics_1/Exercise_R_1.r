> library(readr)
> napoje_po_reklamie <- read_delim("napoje_po_reklamie.csv", 
+     ";", escape_double = FALSE, trim_ws = TRUE)
Parsed with column specification:
cols(
  mies = col_double(),
  pepsi = col_double(),
  fanta = col_double(),
  zywiec = col_double(),
  okocim = col_double(),
  regionalne = col_double(),
  cola = col_double(),
  lech = col_double()
)
> View(napoje_po_reklamie)
> summary(napoje_po_reklamie$pepsi)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 102809  105214  107600  109204  112886  119110 
> summary(napoje_po_reklamie$fanta)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  34145   39233   41932   42626   46058   51504 
> summary(napoje_po_reklamie$zywiec)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 178564  182884  183946  184355  185737  191763 
> summary(napoje_po_reklamie$okocim)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  52596   58661   61654   60541   63143   67979 
> summary(napoje_po_reklamie$regionalne)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  48793   54606   57046   57229   60445   64720 
> summary(napoje_po_reklamie$cola)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 215468  221066  226084  226458  232854  235802 
> summary(napoje_po_reklamie$lech)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  54589   60722   63404   62980   66017   68841 
> quantile(napoje_po_reklamie$pepsi)
      0%      25%      50%      75%     100% 
102809.0 105214.2 107600.5 112886.5 119110.0 
> quantile(napoje_po_reklamie$fanta)
      0%      25%      50%      75%     100% 
34145.00 39233.25 41931.50 46057.75 51504.00 
> quantile(napoje_po_reklamie$zywiec)
      0%      25%      50%      75%     100% 
178564.0 182883.8 183946.0 185737.2 191763.0 
> quantile(napoje_po_reklamie$okocim)
      0%      25%      50%      75%     100% 
52596.00 58660.75 61654.50 63142.75 67979.00 
> quantile(napoje_po_reklamie$regionalne)
      0%      25%      50%      75%     100% 
48793.00 54606.00 57046.00 60444.75 64720.00 
> quantile(napoje_po_reklamie$cola)
      0%      25%      50%      75%     100% 
215468.0 221065.5 226084.0 232853.5 235802.0 
> quantile(napoje_po_reklamie$lech)
      0%      25%      50%      75%     100% 
54589.00 60721.75 63404.50 66017.00 68841.00 
> var(napoje_po_reklamie$pepsi)
[1] 28221322
> var(napoje_po_reklamie$fanta)
[1] 24284894
> var(napoje_po_reklamie$zywiec)
[1] 10081647
> var(napoje_po_reklamie$okocim)
[1] 22158312
> var(napoje_po_reklamie$regionalne)
[1] 24001077
> var(napoje_po_reklamie$cola)
[1] 45801208
> var(napoje_po_reklamie$lech)
[1] 22745711
> install.packages("moments")
> library(moments)
> skewness(napoje_po_reklamie$pepsi)
[1] 0.3948059
> skewness(napoje_po_reklamie$fanta)
[1] 0.07781449
> skewness(napoje_po_reklamie$zywiec)
[1] 0.6147738
> skewness(napoje_po_reklamie$okocim)
[1] -0.5178914
> skewness(napoje_po_reklamie$regionalne)
[1] -0.06758553
> skewness(napoje_po_reklamie$cola)
[1] -0.06013935
> skewness(napoje_po_reklamie$lech)
[1] -0.4242237
> pepsi <- c(napoje_po_reklamie$pepsi)
> fanta <- c(napoje_po_reklamie$fanta)
> summary(pepsi)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 102809  105214  107600  109204  112886  119110 
> summary(fanta)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  34145   39233   41932   42626   46058   51504 
> hist(pepsi, col='red', xlab = 'wartości', main='Pepsi po reklamie')
> hist(fanta, col='blue', xlab = 'wartości', main='Fanta po reklamie')

> library(readr)
> Wzrost <- read_csv("Wzrost.csv", 
+     col_names = FALSE)
> View(Wzrost)
> rowMeans(Wzrost)
[1] 174.1667
> rowSums(Wzrost)
[1] 3135
> max(Wzrost)
[1] 199
> min(Wzrost)
[1] 151
> quantile(Wzrost)
# A tibble: 1 x 5
   `0%` `25%` `50%` `75%` `100%`
  <dbl> <dbl> <dbl> <dbl>  <dbl>
1   151  160.  168.  188.    199
> range(Wzrost)
[1] 151 199
> IQR(Wzrost)
[1] 27.25
> length(Wzrost)
[1] 18
> wzrost <- as.matrix(Wzrost)
> png(file = "wzrost_skewness.png")
> skewness(wzrost[1,])
[1] 0.2960808
> hist(wzrost)
> dev.off()

  