import joblib

class SurvivalModel:
    @staticmethod
    def load_model():
        # Method to load pre-trained model
        return joblib.load('app/data/survival_model.pkl')
    
    def __init__(self):
        # Load pre-trained model when a new instance of the class is created
        self.model = SurvivalModel.load_model()

    def predict(self, df):
        # Predict survival probability
        X = df[['DO', 'Salinitas', 'pH', 'TDS', 'Suhu']]
        return self.model.predict(X)
    
    def predict_proba(self, df):
        # Predict survival probability
        X = df[['DO', 'Salinitas', 'pH', 'TDS', 'Suhu']]
        return self.model.predict_proba(X)[:, 1]
