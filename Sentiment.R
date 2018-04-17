
install.packages("tidytext")
install.packages("tidyverse")

library(tidyverse)
library(tidytext)
library(readr)
library(glue)
library(stringr)
library(dplyr)
wine_df <- read.csv("winemag-data-130k-v2.csv", header = TRUE,stringsAsFactors = FALSE)

#wine_df <- wine_df[0:100]
# tokenize
#wine_df$tokens <- wine_df %>% unnest_tokens(word, text)
 
review_words <- wine_df %>%
  select(designation,points, description) %>%
  unnest_tokens(word,description) %>%
  filter(!word %in% stop_words$word,
         str_detect(word, "^[a-z']+$"))

AFINN <- sentiments %>%
  filter(lexicon == "AFINN") %>%
  select(word, afinn_score = score)

AFINN

reviews_sentiment <- review_words %>%
  inner_join(AFINN, by = "word") %>%
  group_by(designation, points) %>%
  summarize(sentiment = mean(afinn_score))

reviews_sentiment


####REVIEW PER WORDxs
words_points <- wine_df %>%
  select(points, description) %>%
  unnest_tokens(word,description) %>%
  filter(!word %in% stop_words$word,
         str_detect(word, "^[a-z']+$"))

words_points  <- words_points %>%
  group_by(word, average(points))

words_useful <- sqldf("SELECT p.word, p.points FROM words_points p, AFINN a WHERE p.word = a.word")
words_averages <- sqldf("SELECT word, AVG(points) as average, COUNT(*) as cnt FROM words_useful GROUP BY word ORDER BY AVG(points) DESC") 
words_complete <- sqldf("SELECT word, cnt, average FROM words_averages  WHERE cnt > 30")
