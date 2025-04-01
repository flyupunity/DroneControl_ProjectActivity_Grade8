import pickle                                                               # Import the pickle library to load and save Python objects

from sklearn.ensemble import RandomForestClassifier                         # Import the Random Forest Classifier model
from sklearn.model_selection import train_test_split                        # Import train_test_split to split data into training and testing sets
from sklearn.metrics import accuracy_score                                  # Import accuracy_score to evaluate model performance
import numpy as np                                                          # Import numpy for numerical operations, using alias 'np'


data_dict = pickle.load(open('./data.pickle', 'rb'))                        # Load the data dictionary from the pickle file

# Convert the data and labels from the dictionary into numpy arrays
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(                        # Split the data into training and testing sets
    data, labels, test_size=0.2, shuffle=True, stratify=labels              # 20% of the data will be used for testing, data is shuffled, and labels are stratified
)
                                                                            
model = RandomForestClassifier()                                            # Create a Random Forest Classifier model with default parameters
model.fit(x_train, y_train)                                                 # Train the model using the training data


y_predict = model.predict(x_test)                                           # Use the trained model to make predictions on the test data
score = accuracy_score(y_predict, y_test)                                   # Calculate the accuracy of the model by comparing predictions with actual labels
print('{}% of samples were classified correctly !'.format(score * 100))     # Print the accuracy score as a percentage

#f = open('model.p', 'wb')                                                  # Open a binary file to write the trained model
#pickle.dump({'model': model}, f)                                           # Save the trained model into the file using pickle
#pickle.dump(model, open('model.p', 'wb'))
pickle.dump({'model': model}, open('model.p', 'wb'))
#f.close()                                                                   # Close the file to complete the writing process
































