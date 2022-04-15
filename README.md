# personalityDetection

This repo contains the code for personalityDetection. 

Here, we are detecting 16 different personality, based on the past tweets of the given twitter handle.

[This page](https://greator.com/en/16-personalities/) contains a thorough information about the 16 personalities that the model is being trained on.

We have use [Gaussian Naive Bayes model](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) as our Machine Learning model. The model is trained on textual data consisting of sentences of users of different personalities.
Before passing the data to the model we have preprocessed the data where we tokenized the string, removed emoticons and preprocessed the input string. The model is then trained on this preprocessed data.

This model is currently deployed on heroku and test file contains the test cases.




