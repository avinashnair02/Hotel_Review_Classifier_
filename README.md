<h1 align='center'>CHENNAI HOTEL REVIEWS CLASSIFIER</h1>

<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/five_stars.png" width=600>
</p>

<!-- #-<<strong> Here is a demo application of the review classifier: https://hilton-hotel-app.herokuapp.com/ </strong> -> -->

Try it out by inputting a review that you found online, or wrote yourself, and it will clasify the review title, the review, or both with a score between 1-5.

DEPLOYED VERSION: https://hotelrev.herokuapp.com/

## Business Case

In the modern day, public discussion and critiquing of products and services occurs beyond dedicated mediums, and now also takes place in the realm of social media, too.

Online Hotel reviews are currently found on tripadvisor, trustpilot, and expedia. The majority of reviewers gave a score between 3 and 5, so if a new customer browses online reviews on any of the previously mentioned review sites, they may consider booking a room at the Hilton or any other hotels like marriot.

What if they already made up their mind from hearing what a friend had to say?
Potential customers, could have their hotel choice be influenced by a tweet. Opinions are shared constantly on social media platforms, and are read by their followers. The knowledge, of what these followers think about our hotel, from reading these online posts, could help us better understand the general public's perception of our hotel.

By using sentiment analysis, on existing hotel reviews from Tripadvisor.com, I created a model that can quantify on a scale of 1-5, how the author of a tweet on twitter, or a post on a reddit thread, feels about our hotel, and as a result, also how the readers think about us. If a review classifies to be less than a score of 3, this post/tweet could be looked into, find out why they had a negative opinion of our hotel, and in return fix the problem.

Email: avinashnair02@gmail.com <br>
LinkedIn: https://www.linkedin.com/in/avinash-nair-299b72157/ <br>
Medium: https://avinashnair02.medium.com/ <br>

## Motivation

This project is done to get a hands on understanding of the NLP concepts and Streamlit.

## Table of Contents

<details open>
<summary>Show/Hide</summary>
<br>

1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)
3. [ Structure ](#Structure)
4. [ Executive Summary ](#Executive_Summary)
   - [ 1. Webscraping, Early EDA, and Cleaning ](#Webscraping_Early_EDA_and_Cleaning)
     - [ Webscraping ](#Webscraping)
     - [ Early EDA and Cleaning](#Early_EDA_and_Cleaning)
   - [ 2. Further EDA and Preprocessing ](#Further_EDA_and_Preprocessing)
   - [ 3. Modelling and Hyperparameter Tuning ](#Modelling)
   - [ 4. Evaluation ](#Evaluation)
     - [ Future Improvements ](#Future_Improvements)
   - [ 5. Neural Network Modelling ](#Neural_Network_Modelling)
   - [ 6. Revaluation and Deployment ](#Revaluation)
   </details>

## File Descriptions

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
    
* <strong>[ Data ](https://github.com/avinashnair02/Hotel_Review_Classifier_/tree/master/Data)</strong>: folder containing all data files
    * <strong>1.tripadvisor_scraped_hotel_reviews.csv</strong>: webscraped data before any changes
    * <strong>2.hotel_reviews_structured.csv</strong>: data after balancing and cleaning
    * <strong>3.x_train_data.csv</strong>: training data with x values from preprocessed dataset
    * <strong>3.y_train_data.csv</strong>: training data with y values from preprocessed dataset
    * <strong>4.x_test_data.csv</strong>: test data with x values from preprocessed dataset
    * <strong>4.y_test_data.csv</strong>: test data with y values from preprocessed dataset
* <strong>[ Images ](https://github.com/avinashnair02/Hotel_Review_Classifier_/tree/master/Images</strong>: folder containing images used for README and presentation pdf
* <strong>[ Models ](https://github.com/avinashnair02/Hotel_Review_Classifier_/tree/master/Models)</strong>: folder containing trained models saved with pickle
    * <strong>Adabooost.pkl, Decision Tree.pkl, KNN.pkl, Logistic Regression.pkl, Naive Bayes.pkl, Neural Network.pkl, Random Forest.pkl, Stacking.pkl, SVM.pkl, Voting.pkl, XGBoost.pkl</strong>
* <strong>[ Tripadvisor_Webscrape ](https://github.com/avinashnair02/Hotel_Review_Classifier_/tree/master/TRip_Advisory%20scrapper)</strong>: folder containing all webscraping files
    * <strong>Tripadvisor</strong>: folder containing .py files and spiders used
        * <strong>spiders</strong>: folder containing spider files and datasets
            * <strong>hotels.py</strong>: main spider .py file for scraping hotel reviews from Tripadvisor
            * <strong>tripadvisor_scraped_hotel_reviews.csv</strong>: csv file with data to be used for project
        * <strong>_init_.py, items.py, middlewares.py, pipelines.py, settings.py: default scrapy files used for webscrape</strong>
    * <strong>scrapy.cfg</strong>: scrap config file
* <strong>[ 1.Webscraping_Early_EDA_and_Cleaning.ipynb ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/1.Webscraping_Early_EDA_and_Cleaning.ipynb)</strong>: notebook with early data exploration and data manipulation
* <strong>[ 2.Further_EDA_and_Preprocessing.ipynb ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/2.Further_EDA_and_Preprocessing.ipynb)</strong>: notebook with feature engineering and nlp preprocessing
* <strong>[ 3.Modelling_and_Hyperparameter_Tuning.ipynb ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/3.Modelling_and_Hyperparameter_Tuning.ipynb)</strong>: notebook with all the models created
* <strong>[ 4.Evaluation ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/4.Evaluation.ipynb)</strong>: notebook with final model selection, testing, and model evaluation
* <strong>[ 5.Neural_Network_Modelling ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/5.Neural_Network_Modelling.ipynb)</strong>: notebook with an extra model training using neural networks
* <strong>[ 6.Revaluation_and_Deployment ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/6.Revaluation_and_Deployment.ipynb)</strong>: notebook comparing old best model and NN model, and deployment
* <strong>[ Classification.py ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Classification.py)</strong>: contains classes with classifcation methods
* <strong>[ Ensemble.py ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Ensemble.py)</strong>: contains classes with ensemble methods
* <strong>[ Helpers_NN.py ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Helpers_NN.py)</strong>: contains methods used to help with neural network processes
* <strong>[ Hilton_Hotel_App.py ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Hilton_Hotel_App.py)</strong>: contains script to run app
* <strong>[ Hilton__Hotel_Presentation.pdf ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Hilton_Hotel_Presentation.pdf)</strong>: presentation summarising project case, processese, and findings
* <strong>[ Procfile ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Procfile)</strong>: file supporting Heroku application
* <strong>[ requirements.txt ](https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/requirements.txt)</strong>: dependencies for heroku application
</details>

## Tecnologies Used:

<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>
    
* <strong>Python</strong>
* <strong>Pandas</strong>
* <strong>Numpy</strong>
* <strong>Matplotlib</strong>
* <strong>Seaborn</strong>
* <strong>NLTK</strong>
* <strong>Scrapy</strong>
* <strong>Scikit-Learn</strong>
* <strong>Keras</strong>
* <strong>Tensorflow</strong>
* <strong>Streamlit</strong>
* <strong>Heroku</strong>
</details>

## Structure of Notebooks:

<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>
    
1. Early EDA and Cleaning
   * 1.1 Webscrape Process Explained
   * 1.2 Imports
   * 1.3 Checking for Nulls
   * 1.4 Converting Score Column
   * 1.5 Adjusting Class Imbalance for Scores
   * 1.6 Joining Review Part 1 with Review Part 2 in New Column Review
   * 1.7 Removing Review Part 1 and Review Part 2 Columns
   * 1.8 Saving Structured Dataset as a CSV

2. Further EDA and Preprocessing

   - 2.1 Imports
   - 2.2 Checking Frequency of Words and Phrases in Review Summaries
   - 2.3 Checking Frequency of Words and Phrases in Reviews
   - 2.4 Stemming and Lemming
   - 2.5 Train Test Split
   - 2.6 TF-IDF Vectorisation for Reviews
   - 2.7 TF-IDF Vectorisation for Review Summaries
   - 2.8 Joining Reviews With Review Summaries
   - 2.9 Saving Preprocessed Dataset as CSVs

3. Modelling and Hyperparameter Tuning

   - 3.1 Imports
   - 3.2 Train and Validation Split
   - 3.3 Decision Tree (Baseline)
   - 3.4 Random Forest
   - 3.5 Logistic Regression
   - 3.6 Support Vector Machines
   - 3.7 Guassian Naive Bayes
   - 3.8 KNN
   - 3.9 Adaboost (Logistic Regression)
   - 3.10 XGBoost (Logistic Regression)
   - 3.11 Voting
   - 3.12 Stacking
   - 3.13 All Models Compared
   - 3.14 Best Model (Logistic Regression) - Deeper Look
   - 3.15 Saving Best Model

4. Evaluation
   - 4.1 Imports
   - 4.2 Best Model Selection
   - 4.3 Best Model Tested
   - 4.4 Deeper Diver Into Best Model
   - 4.5 Application Deployability
5. Neural Network Modelling
   - 5.1 Imports
   - 5.2 One Hot Encoding Score Column
   - 5.3 Train Test Split
   - 5.4 Add Suffix to the Review Summary to Distinguish the Difference
   - 5.5 Removing Punctuation and Tokenizing Review Column
   - 5.6 Creating a Dictionary With Words That Appear in Reviews and an Index
   - 5.7 Indexing Words in Reviews Using Dictionary
   - 5.8 Combining Indexed Review Summary and Indexed Review Into a Single Column Called All Preprocessed Review
   - 5.9 Modelling
   - 5.10 Testing Model
   - 5.11 Test Confusion Matrix
   - 5.12 Saving Model
6. Revaluation and Deployment
_ 6.1 Imports
_ 6.2 Comparing Stacking Model with Neural Network Model \* 6.3 Deployment
</details>

<a name="Executive_Summary"></a>

## Executive Summary

<a name="Webscraping_Early_EDA_and_Cleaning"></a>

### Webscraping, Early EDA, and Cleaning:

<details open>
<summary>Show/Hide</summary>
<br>

<a name="Webscraping"></a>

#### Webscraping

I set a goal of a minimum of 5000 reviews to scrape, before choosing the specific hotels. I then chose the 8 hotels in Chennai with the highest number of reviews, to scrape;The*Park_Chennai-Chennai*,
GreenPark_Chennai-Chennai
Hilton_Chennai-Chennai_Ma
Hyatt_Regency_Chennai-Che
Taj_Club_House-Chennai_Ma
Radisson_Blu_Hotel_GRT_Ch
Lemon_Tree_Hotel_Chennai-.

<h5 align="center">Tripadvisor Review Example</h5>
<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/Trip_sample.PNG" width=600>
</p>

The structure of each review consisted of a 1-5 scale score rating in bubble form, a review summary, and a detailed review split into p1 and p2 (depending on if there was a read more option). Each page on tripadvisor had 5 reviews per page, so I had to navigate between pages using tripadvisor's next page function.

The root URL I used was 'www.tripadvisor.co.in'

The 8 starting URL extensions I used were:

-'/Hotel_Review-g304556-d301636-Reviews-The_Park_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d730057-Reviews-GreenPark_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d1597314-Reviews-Hilton_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d1872115-Reviews-Hyatt_Regency_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d1164749-Reviews-Taj_Club_House-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d306744-Reviews-Radisson_Blu_Hotel_GRT_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'
-'/Hotel_Review-g304556-d1382155-Reviews-Lemon_Tree_Hotel_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html'

From these pages I chose to extract 5 different features:

- hotel_name
- review_summary
- review_p1
- review_p2
- score

I used a scrapy spider to crawl the website to scrape the requested data. Scrapy proved the be efficient and fast at extracting the data. I ran the spider script (hotels.py) for around 30 minutes, on the 13th March 2021.

<h5 align="center">Histogram of Scores for Each Hotel</h5>
<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/hotel_name.PNG" width=600>
</p>

<a name="Early_EDA_and_Cleaning"></a>

#### Early EDA and Cleaning:

The initial shape of the dataset was (48640, 5)). The 5 columns was as expected, but there were double the number of rows as the number of reviews scraped. There were null rows with only hotel_name and no other values, so I removed those rows, bringing us back to the expected 4000

This project entailed the use of classification models, and for reliable results, I had to remove reviews to undo class imbalance. Using this visualisation I saw that were much less reviews with a score of 1 compared to reviews with a score of 3, 4, and 5. To combat this imbalance, I randomly removed reviews with scores of 2, 3, 4, and 5, to match with 1 (1881 reviews).

<h5 align="center">Histogram of Scores for All Hotels (With  Class Imbalance (Left) vs Without  Class Imbalance (Right))</h5>
<table><tr><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/scores.PNG' width=500></td><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/balanced%20class.PNG' width=500></td></tr></table>

I combined the review p1 and review p2 column into one to make future vectorisation much easier, then I saved the cleaned dataset as a csv, for the next stage.

</details>

<a name="Further_EDA_and_Preprocessing"></a>

### Further EDA and Preprocessing

<details open>
<summary>Show/Hide</summary>
<br>

Using the FreqDist function in the ntlk library I plotted a graph with the most frequent words and phrases in both columns. Stopwords were removed to capture the more meaningful words.

<h5 align="center">Distribution Plot of Frequent Words and Phrases in Text ( Review Summary (Left) and Review (Right) )</h5>
<table><tr><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/frequecy_dist_review.png' width=500></td><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/Frequecny_review_sum.png' width=500></td></tr></table>

I had noticed a lot of the most frequent words in the review text happened to be words with no sentimental impact, so I iteratively removed unmeaningful words such as 'room', 'hotel', 'hilton' etc. I did this as a precaution, as some of these words may impact my model accuracies.

<h5 align="center">World Cloud of Frequent Words and Phrases in Text After Removing Unmeaningful Words ( Review Summary (Left) and Review (Right) )</h5>
<table><tr><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/chenniat.png' width=500></td><td><img src='https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/review_wordclod.png' width=500></td></tr></table>

To narrow down the feature words I applied stemmation and lemmitisation to both the reviews and review summaries.

<h5 align="center">Example of Lemmatisation and Stemmation Applied to a Review and Review Summary</h5>
<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/lemm_stemm_review.PNG" width=600>
</p>

Stemmation had broken down some words into words that don't exist, whereas lemmitisation had simplified adjectives and verbs to their root form. I chose to continue with the lemmitised version of the texts for further processing.

Prior to vectorising the current dataset, I did a train, test split to save the test data for after modelling.

Using the lemmed texts for review and review summary I used TF-IDF vectorisation with an ngram range of 2, leaving me with a vectorised dataset with 138 words and phrases (112 from reviews and 26 from review summaries). I then saved the x and y train data in separate csv files for modelling.

</details>

<a name="Modelling"></a>

### Modelling:

<details open>
<summary>Show/Hide</summary>
<br>

I have created .py files; Classifiction.py and Ensemble.py with classes, that contain functions to simplify the modelling process, and to neaten up the modelling notebook.

I did another data split into Train and Validation data in preparation for using GridSearch Cross Validation. I also chose Stratified 5-fold has a my choice for cross validating.

For the majority of models I created, I applied hyperparameter tuning, where I started with a broad range of hyperparameters, and tuned for optimal train accuracy and validation accuracy.

<h5 align="center">Table Comparing Best Models</h5>
<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/XGboost.PNG" width=600>
</p>

Initially, I thought the validation accuracy was low for most of the models I created, but when considering these models were attempting to classify for 5 different classes, 0.45 and greater seems very reasonable (where 0.2 = randomly guessing correctly).

I have saved all the models using the pickle library's dump function and stored them in the Models folder.

</details>

<a name="Evaluation"></a>

### Evaluation

<details open>
<summary>Show/Hide</summary>
<br>

I focused on 3 factors of defining a good model:

1. Good Validation Accuracy
2. Good Training Accuracy
3. Small Difference between Training and Validation Accuracy

I chose the Stacking ensemble model ( (Adaboost with log_reg_2) stacked with log_reg_2 ) as my best model, because it has the highest validation accuracy with only around 3.5% drop from train to validation in accuracy. I wanted to minimise overfitting and make the model as reusable as possible. Stacking achieved a reasonable training accuracy as well, although it did not reach the level of some of the other ensemble techniques.

I next tested the best model with the earlier saved test data. The model managed to get a high test accuracy, similar to the validation data from the model training stage. This is very good, proving that prioritising a high validation score, and minimising the difference between train and validation accuracy, has helped it classify new review texts very well.

<h5 align="center">Test Results</h5>
<p align="center">
  <img src="https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Images/test_results.png" width=600>
</p>

Looking at the precision, recall, and f1 score, I also noticed the scores were higher around scores of 1 and 5, lower for 2, 3, and 4. This shows that the models performs well on more extreme opinions on reviews than mixed opinions.

Looking into different metrics and deeper into my best model; Stacking, I learnt that most the False Postives came from close misses (e.g. predicting a score of 4 for a true score of 5). This is best shown by these two confusion matrixes (validation and test).

<h5 align="center">Confusion Matrix for Validation and Test Data Predictions ( Validation (Left) and Test (Right) )</h5>
<table><tr><td><img src='https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Images/validation_conf_matrix.png' width=500></td><td><img src='https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Images/test_conf_matrix.png' width=500></td></tr></table>

The adjacent squares of the diagonal going across the confusion matrix, shows that the model's second highest prediction for a given class (review score) is always a review score that is +-1 the true score.
Very few reviews that have a score of 5, have been predicted to have a score of 1 or 2. This is very relieving to know, the majority of the error for the model, is no different to the error a human may make classifying a review to a score with a scale of 1-5.

- most errors were near misses (e.g. 5 predicted as 4)
- extreme scores (1 and 5) were relatively accurate
- comparable to human prediction
- reusable and consistent

Given the classifcation problem is 5 way multi-class one and the adjacent classes can have overlap in the english language even to humans, this model I have created can be deployed.

Applying this model will address the problem of not having a full understanding of public opinion of our hotel. We can apply this to new sources for opinions on our hotel and yield more feedback then we did had before.

<a name="Future_Improvements"></a>

#### Future Improvements

- Model using neural networks - see if better accuracy can be achieved
- Create a working application to test new reviews written by people
- Try a different pre-processing approach and see if model performances change
- Bring in new sources of data to see if there are significant differences on frequent words used

</details>

<a name="Neural_Network_Modelling"></a>

### Neural Network Modelling:

<details open>
<summary>Show/Hide</summary>
<br>
    
I experimented with different classifcation and ensemble methods to help classify hotel review scores. Some performed well, but there was definitely room for improvement, so I wanted to explore a deep learning approach. 
    
    
<h5 align="center">Neural Network Architecture</h5>
<p align="center">
  <img src="https://github.com/avinashnair02/Hotel_Review_Classifier_/blob/master/Images/NN_architecture.png" width=600>
</p>
    
* Input Layer: 17317 Nodes (one for each word in training data + 4 extra for padding, unknown words, start of review, and unused words)
* Embedding Layer: takes 17317 unique items and maps them into a 16 dimensional vector space
* Global Average 1D Pooling Layer: scales down 16 dimensional layer
* Dense Hidden Layer: 16 Nodes (using relu activation function)
* Dense Output Layer: 5 nodes for each score (using sigmoid activation function)
    
</details>

<a name="Revaluation"></a>

### Revaluation and Deployment:

<details open>
<summary>Show/Hide</summary>
<br>

I tested the neural network model using the test data and achieved an accuracy of <strong>0.5710</strong> which is better than the stacking model accuracy of <strong>0.5077</strong>, by <strong>over 5%</strong>.

I wanted to look at the confusion matrix, as this gives a better idea of how the model is performing over all 5 classes.

<h5 align="center">Neural Network Model Test Confusion Matrix</h5>
<p align="center">
  <img src="https://github.com/awesomeahi95/Hotel_Review_NLP/blob/master/Images/nn_conf_matrix.png" width=600>
</p>
    
The error is more contained within adjacent scores with the neural network model. Almost zero confusion between extreme scores 1 and 5, and minimal confusion with scores 2 and 4. Although a score of 3 can be harder to predict, there is definitely an improvement from the Stacking model. Around 97% of the time the model predicts at least the adjacent score to the actual score.

#### Deployment and Application

After seeing the improvements from the Stacking model, I was more confident about deploying the model for actionable use.

<!-- #I planned on future improvements being the addition of the neural network model and then creating an application for the app #using Heroku: https://hilton-hotel-app.herokuapp.com/.  -->

Using this model, we will learn more about our new and old customers, then we can improve Hilton Hotel's guest satisfaction, and as a result increase customer retention and bring in new travelers.

#### Future Development

- Create a webscraper spider for twitter, reddit, etc for further model assessment

</details>

#### Project Partner

Pranav-bansod : LinkedIn: https://www.linkedin.com/in/avinash-nair-299b72157/ <br>
