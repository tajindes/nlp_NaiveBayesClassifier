Name: Tajinder Singh

Steps for Naive Bayes Classifier:
1. Use preprocessing_training.py to convert TRAINING_DATA to TRAINING_FILE (spam_training.txt)
2. Then execute Naive_Bayes_learn.py to create spam.nb (MODEL FILE)
3. Use preprocessing_test.py to convert TEST_DATA to test file format.
4. Then execute Naive_Bayes_classify.py to create spam.out using TEST_FILE and MODEL_FILE. syntax is:
     "python3 Naive_Bayes_classify spam.nb TESTFILE > spam.out"

Similar steps for Sentiment analysis.


# Precision, Recall and F-score on the development data for Naive Bayes Classifier for each of the two datasets:

SPAM Dataset:
class: SPAM
precision for class SPAM  is: 0.9587912087912088
recall for class SPAM  is: 0.9614325068870524
F-SCORE for class SPAM  is: 0.9601100412654747
class: HAM
precision for class HAM  is: 0.985985985985986
recall for class HAM  is: 0.985
F-SCORE for class HAM  is: 0.9854927463731865


SENTIMENT Dataset:
class: NEG
precision for class NEG  is: 0.8271947527749748
recall for class NEG  is: 0.8744
F-SCORE for class NEG  is: 0.8501425978739953
class: POS
precision for class POS  is: 0.8667986425339367
recall for class POS  is: 0.8173333333333334
F-SCORE for class POS  is: 0.8413395553115566