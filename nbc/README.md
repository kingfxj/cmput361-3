## REMINDERS

1. Code that does not read all inputs from the command line will get zero for correctness in this assignment.
+ You **MUST** list all consultations you had, including websites you have read while working on this assignment.


### Videos

1. Links to videos explaining your Naive Bayes Classifier
    *xinjian's: https://drive.google.com/drive/folders/1Qiv9mghBvNpjhn3UePAWjPz3Syer-_bX?usp=sharing
    *skavalin's: https://drive.google.com/drive/folders/1aOAo00KkEhMWncM1dAPGmsJyzZLXt1IE?usp=sharing
1. Links to videos explaining how you did Feature Selection:
    * xinjian's: https://drive.google.com/drive/folders/1Qiv9mghBvNpjhn3UePAWjPz3Syer-_bX?usp=sharing
    * skavalin's: https://drive.google.com/drive/folders/1egLY9QX3qK0bAWVSEFbHWJz0hezuG_2a?usp=sharing

### TODO: Impact of feature selection

Complete the table below with the F1 obtained on the test corpus based on training using only the top-k features per class, for the following values of k. The selectipon must be based on Mutual Information.

Report the F1 for each class separately, as well as the micro and macro averages for all classes.

|   | top-10 | top-20 | top-40 | top-80 | top-160|
|---|--------|--------|--------|--------|--------|
tech |0.8571428571428571|1.5714285714285716|1.8571428571428572 | 2.428571428571429| 2.428571428571429|
business |2.8846153846153846 |2.769230769230769|2.5384615384615383 | 2.6538461538461537|2.6538461538461537 |
sport |0.8076923076923077|1.3846153846153846 |1.7307692307692306 |1.8461538461538465 | 1.9615384615384617|
entertainment | 1.2000000000000002|1.5 |1.6500000000000001 |1.7999999999999998 |2.25 |
politics |0.8571428571428571 |0.8571428571428571| 1.0|1.4285714285714284 |1.7142857142857142 |
|---|--------|--------|--------|--------|--------|
ALL-micro | 0.45614035087719296| 0.5526315789473685| 0.5964912280701754| 0.6842105263157895|0.7368421052631579|
ALL-macro |1.321318681318681 |1.6164835164835165|1.7552747252747252 | 2.0314285714285716| 2.2016483516483514|
