library(ggplot2)
theme_set(theme_bw())  

# Data Prep


wine_df <- read.csv("winemag-data-130k-v2.csv", stringsAsFactors = FALSE)


wine_df$wine_avg <- round((wine_df$points) - mean(wine_df$points)/sd(wine_df$points, 2))  # compute normalized mpg
wine_df$points_type <- ifelse(wine_df$wine_avg < 0, "below", "above") 
                               
wine_df <- wine_df[order(wine_df$points_type), ]  # sort
# Diverging Barcharts
ggplot(wine_df, aes(x=designation, y=wine_avg, label=points)) + 
  geom_bar(stat='identity', aes(fill=points_type), width=.5)  +
  scale_fill_manual(name="Price", 
                    labels = c("Above Average", "Below Average"), 
                    values = c("above"="#00ba38", "below"="#f8766d")) + 
  labs(subtitle="Normalised mileage from 'mtcars'", 
       title= "Diverging Bars") + 
  coord_flip()

