# FlipkartReviews_NLP
Flipkart Product Reviews NLP : Gives better rating of Flipkart products using normalized bag-of-words sentimental analysis of Reviews and incorporating star-ratings.
# Requirements
* pymongo: for MongoDB
* textblob: for Sentimental Analysis
* selenium:  for PhantomJS
* requests:  to make HTTP request
* bs4:  Beautiful Soup 4
# Getting Started
1. Make sure you have install all Dependencies.
2. Start the MongoClient Server.
3. Execute Main_FlipkartReviewsNLP.py
4. Enter Name of the Product.
5. It will scrap the data from the first page and shows in a sequence.
6. Enter the Sequence no. of that product.
7. Now it will start WebDriver to get the Text of Reviews and Likes & Dislikes on each reviews.
8. Weightage of each review is bounded by Sigmoidal Function in Range of (-1 to 1)
9. Average of Rating Calculated through Analysing Revies and Rating Given by Flipkart(out of 5) is calculated is Final.



