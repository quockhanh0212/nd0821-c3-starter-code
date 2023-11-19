# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
A Logistic Regression were trained.

* Model version: 1.0.0
* Model date: 19 November 2023

## Intended Use
The model can be used for predicting income classes on census data. There are two income classes >50K and <=50K (binary classification task).

## Training Data
The UCI Census Income Data Set was used for training. Further information on the dataset can be found at https://archive.ics.uci.edu/ml/datasets/census+income
For training 80% of the 32561 rows were used (26561 instances) in the training set.

## Evaluation Data
For evaluation 20% of the 32561 rows were used (6513 instances) in the test set.

## Metrics
Three metrics were used for model evaluation (performance on test set):
* precision: 0.7266187050359713
* recall: 0.25140012445550713
* fbeta: 0.3735552473416551

## Ethical Considerations
Since the dataset consists of public available data with highly aggregated census data no harmful unintended use of the data has to be addressed.

## Caveats and Recommendations
It would be meaningful to perform an hyperparameter optimization to improve the model performance.