require(randomForest)
wine_df <- read.csv("winemag-data-130k-v2.csv", stringsAsFactors = FALSE)
library(randomForest)
wine_df <- read.csv("winemag-data-130k-v2.csv", stringsAsFactors = FALSE)
# remove useless columns
wine_df <- wine_df[-c(1, 4, 9, 10, 11)]
# remove rows without points or price data
wine_df <- na.omit(wine_df)

samp <- sample(nrow(wine_df), 0.6 * nrow(wine_df))
train <- wine_df[samp, ]  #training set
test <- wine_df[-samp, ]  #testing set
model <- randomForest(as.factor(points) ~ price + province +variety , data = train,importance=TRUE, 
                      ntree=2000) #randomforest model
pred <- predict(model, newdata = test)
table(pred, test$model)

head(train)


library(xgboost)
tester <- model.matrix(~.+0,data = test) 

