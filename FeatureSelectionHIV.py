import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from numpy import delete
 

features = []
X = []
Y = []
index = 1 #start at 1 because easier to find in excel sheet
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel("PutPathToExcelSheetHere", "PutExcelSheetNameHere")
df = dataframe1.values
X = delete(df, 0, axis=1) #Drop The column we are looking to target
Y = df[:,0] #Set Y equal to column we are targeting. This and the above line of code allow for the RFE feature selection
print(X)
print(Y)

model = LogisticRegression(solver='lbfgs') # Use linear regression as model to do feature selection. It will then be fed into KNN
rfe = RFE(model, n_features_to_select=30) #Create RFE
fit2 = rfe.fit(X, Y) #Fit RFE
print("Num Features: %d" % fit2.n_features_) #Print information about the fitting
print("Selected Features: %s" % fit2.support_)
print("Feature Ranking: %s" % fit2.ranking_)
for i in fit2.support_: # Find where in excel sheet are the top X features (in our case 30)
    if (i == True):
        features.append(index) 
    index += 1

print(features)

