import joblib

class SurvivalModel:
    @staticmethod
    def load_model():
        # Method to load pre-trained model
        # Returns: pre-trained model object
        return joblib.load('app/data/survival_model.pkl')
    
    def __init__(self):
        # Constructor to load pre-trained model
        # when a new instance of the class is created
        self.model = SurvivalModel.load_model()

    def predict(self, df):
        # Method to predict survival probability
        # Input: X - input features
        # Returns: predicted survival probability
        X = df.drop('Survival Rate', axis=1)
        return self.model.predict(X)
    
    def predict_proba(self, df):
        # Method to predict survival probability
        # Input: X - input features
        # Returns: predicted survival probability
        X = df.drop('Survival Rate', axis=1)
        return self.model.predict_proba(X)[:, 1]