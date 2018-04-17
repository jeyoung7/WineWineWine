library(dplyr)
library(ggplot2)
wine_df <- read.csv("winemag-data-130k-v2.csv", stringsAsFactors = FALSE)
# remove useless columns
wine_df <- wine_df[-c(1, 4, 9, 10, 11)]
# remove rows without points or price data
wine_df <- na.omit(wine_df)
summary(lm(points ~ price, data = wine_df))
qplot(price, points, data = wine_df)

