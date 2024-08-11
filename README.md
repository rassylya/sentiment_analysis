# Sentiment Analysis Readme
Models saved in the folder 'models'

## ETAP 1
1. Create a Conda environment using the 'environment.yml' file.
2. Run the script 'twitter_scrapper.py' to parse tweets. It extracts author names, tweet texts, and hashtags. Parsed data files are saved in the 'splitted_data' directory. The data is distributed into 20 files, each containing 10,000 rows to ensure manageability.
3. Perform data cleaning and manipulation in the 'Etaps1_4' notebook. Run each cell sequentially. The file 'allData.csv' contains the cleaned and vectorized data.

## ETAP 2
4. Perform clustering in the 'Etaps1_4' notebook. The data is labeled with 3 clusters. Additionally, compare the clusters with the tags generated by the nltk sentiment analyzer tool. Manually tagged initial points are used for clustering.

## ETAP 3
5. The results of classification by ML models can be found in the same notebook. Decision Tree, Gradient Boosting, and Naive Bayes models were used and compared. The Gradient Boosting classifier showed the best performance with an accuracy of 0.99265.

## ETAP 4
6. The LSTM model was used for this task. GridSearch was performed to find the best model. A validation accuracy of 0.97889 was achieved.

## ETAP 5
7. The DistilBert language model was used for this task. The results are available in the 'Etap 5' notebook. It was executed on Google Colab due to GPU hardware limitations. Evaluation loss obtained: 0.320436
