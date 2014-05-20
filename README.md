NaiveBayes and KNN Classifiers
=====

This is a homework assignment to work on two sets of data and apply two
classifiers: Naive Bayes and K-Nearest Neighbors.

The data sets are:
  * [spam/ham from spamassassins](https://spamassassin.apache.org/publiccorpus/)
  * [movie reviews rotten tomatoes from kaggle](http://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)

My implementation of Naive Bayes works better on both data sets than KNN
(tried k = {5,7,10}).

I even submitted my try on Kaggle and ranked 114/202 (**0.57913 Kaggle score**,
where 0.64993 is the currently best one). [See here](http://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/leaderboard).

Files
---

The code is self explanatory and commented, feel free to check it out.

* main.py is where all code starts, obviously :)
* classifiers/ contains both clasiifiers
* parse/ contains the parsing of the sets of data (spam and movie reviews)

Try it out for yourself
----

All the datasets are included in the repo in `spamassassins/` and
`rotten_tomatoes/` with training and testing data sets.

The spamassassins data sets are split in 70% training, 30% testing.
The rotten tomatoes data are used as got from kaggle directly, the
`train.tsv` for training and the `test.tsv` for testing.

```bash
$ ./main.py mail naive     # runs the NaiveBayes classifier on email data
                           # (included in repo)

$ ./mail.py mail knn 5     # runs a 5-NN classifier on email data

$ ./mail.py rotten naive   # runs a NaiveBayes classifier on the rotten
                           # tomatoes data from kaggle

$ ./mail.py rotten knn 7   # runs a 7-NN classifier on the rotten tomatoes
                           # data from kaggle
```
