# BOHComplexNetworks

## Getting Started
To get started in recreating the experiment done in the paper "INSERT PAPER NAME HERE", begin by downloading the deidentified data. Because the data is not already hot encoded, you will need to perform this. 

### Cleaning the Data
The deidentified data is in its raw form so you will need to perform one-hot encoding in order to use the data. For columns that are a single number there will be a certain cutoff that must be hit to be a 1 or 0. For questions that have multiple answers, each answer is split up and becomes its own variable. Then if a respondent is part of that varaible they would recieve a 1 otherwise they would recieve a 0. ***Include Key Here***

Additionally, there are columns that we deemed unecessary in the data set. These must be removed prior to doing any sort of feature selection as well as taking out the three respondents that did not finish the survey. 

### Feature Selection
Once the data is cleaned you will start in feature selection. To begin create three new sheets, one for each target variable: Black, Covid Finance worse, and HIV+. In each sheet remove all the rows that do not indicate that a respondent is a part of the target variable. For example, if we are targeting the Black variable, then any respondent with a 0 would be removed from that sheet.
