# Importing the necessary libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression  
from sklearn.ensemble import RandomForestClassifier

# Load the DataFrame
csv_file = 'penguin.csv'
df = pd.read_csv(csv_file)

# Display the first five rows of the DataFrame
df.head()

# Drop the NAN values
df = df.dropna()

# Add numeric column 'label' to resemble non numeric column 'species'
df['label'] = df['species'].map({'Adelie': 0, 'Chinstrap': 1, 'Gentoo':2})


# Convert the non-numeric column 'sex' to numeric in the DataFrame
df['sex'] = df['sex'].map({'Male':0,'Female':1})

# Convert the non-numeric column 'island' to numeric in the DataFrame
df['island'] = df['island'].map({'Biscoe': 0, 'Dream': 1, 'Torgersen':2})


# Create X and y variables
X = df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)


# Build a SVC model using the 'sklearn' module.
svc_model = SVC(kernel = 'linear')
svc_model.fit(X_train, y_train)
svc_score = svc_model.score(X_train, y_train)

# Build a LogisticRegression model using the 'sklearn' module.
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
log_reg_score = log_reg.score(X_train, y_train)

# Build a RandomForestClassifier model using the 'sklearn' module.
rf_clf = RandomForestClassifier(n_jobs = -1)
rf_clf.fit(X_train, y_train)
rf_clf_score = rf_clf.score(X_train, y_train)

# Create a function that accepts 'model', island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' and 'sex' as inputs and returns the species name.
def prediction(model, island, bill_length, bill_depth, flipper_length, body_mass, sex):
  pre = model.predict(island, bill_length, bill_depth, flipper_length, body_mass, sex)
  species = species[0]
  if species == 0:
    return "Adelie"
  elif species == 1:
    return "Chinstrap"
  else:
    return "Gentoo"

# Design the App
st.title('Penguin Predict')

bill_length = st.slider("Bill Length", df['bill_length_mm'].min(), df['bill_length_mm'].max())
bill_depth = st.slider("Bill Depth", df['bill_depth_mm'].min(), df['bill_depth_mm'].max())
flipper_length = st.slider("Flipper Length", df['flipper_length_mm'].min(), df['flipper_length_mm'].max())
body_mass = st.slider("Body Mass", df['body_mass_g'].min(), df['body_mass_g'].max())

island = st.sidebar.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
sex = st.sidebar.selectbox('Sex',('Male', 'Female'))

classifier = st.sidebar.selectbox('Classifier', ('Support Vector Machine', 'Logistic Regression', 'Random Forest Classifier'))

if st.sidebar.button("Predict"):
  if classifier == 'Support Vector Machine':
    species_type = prediction(svc_model, s_len, s_wid, p_len, p_wid)
    score = svc_model.score(X_train, y_train)

  elif classifier =='Logistic Regression':
    species_type = prediction(log_reg, s_len, s_wid, p_len, p_wid)
    score = log_reg.score(X_train, y_train)

  else:
    species_type = prediction(rf_clf, s_len, s_wid, p_len, p_wid)
    score = rf_clf.score(X_train, y_train)

if st.button("Predict"):
        st.subheader("Prediction results:")
        st.write(prediction(model, island, bill_length, bill_depth, flipper_length, body_mass, sex))