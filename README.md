# BOHComplexNetworks
The instructions below are intended to be used to replicate the experment conducted in the paper "INSERT PAPER NAME". However, the data can provided can be used for other research purposes as well. 

## Getting Started
To get started in recreating the experiment done in the paper "INSERT PAPER NAME HERE", begin by downloading the deidentified data. 

### Cleaning the Data
The deidentified data is in its raw form so you will need to perform one-hot encoding in order to use the data. For columns that are a single number there will be a certain cutoff that must be hit to be a 1 or 0. For questions that have multiple answers, each answer is split up and becomes its own variable. Then if a respondent is part of that varaible they would recieve a 1 otherwise they would recieve a 0. ***Include Key Here***

Additionally, there are columns that we deemed unecessary in the data set. These must be removed prior to doing any sort of feature selection as well as taking out the three respondents that did not finish the survey. ***Put columns we removed***

### Feature Selection
Once the data is cleaned you will start in feature selection. To begin create three new sheets, one for each target variable: Black, Covid Finance worse, and HIV+. In each sheet remove all the rows that do not indicate that a respondent is a part of the target variable. For example, if we are targeting the Black variable, then any respondent with a 0 would be removed from that sheet. After this has been done you are ready to get started with feature selection.

First, open the file titled "FeatureSelection.py". This file contains all code related to feature selection. You will need to update the file path to match where you have the data as well as the sheet name. Next, there is a comment that looks like this:

```HIV+ = 0, Black = 15, COVID = 129```

Those are the column number (-1) of the target attributes in the excel sheet. The next two variables, X and Y will need to know these numbers. Use the number that corresponds to the feature you are targeting and input it where a number appears in the code. Once that is done all you need to do is run the code!

The code will output an array that contains the column numbers of the 30 most important features. Go to your excel sheet and delete the target attribute column. Next using the COLUMN function in excel figure out what the number of each column is. Finally, remove all columns that are not the 30 best features. 

### Creating the KNN Graph
Now that you have the features selected, open the Python file labeled "GraphCreator.py". CHange the file path to lead to the excel as well as the sheet you are using. Then simply run the program. YOu will get a file in GEXF format that a program such as Gephi can read and you can analyze!
