import data_scan
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import Normalizer
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import time

#NOTE we are doing a decision tree woth tfidf

#import the polished data
X_train, X_test, y_train, y_test = data_scan.main()

#vetrorizing the vords - bag of words
count_vect = CountVectorizer().fit(X_train)
X_train_counts = count_vect.transform(X_train)
X_test_counts = count_vect.transform(X_test) 

#tfidf
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

#l2 normalisation
normalizer_tranformer = Normalizer().fit(X=X_train_tfidf)
X_train_normalized = normalizer_tranformer.transform(X_train_tfidf)
X_test_normalized = normalizer_tranformer.transform(X_test_tfidf)

start = time.time()
#logistic regression
decisiontree = DecisionTreeClassifier().fit(X_train_normalized, y_train)

y_pred = decisiontree.predict(X_test_normalized)

print(time.time()-start)
print(metrics.classification_report(y_test, y_pred))