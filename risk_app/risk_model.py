
import pickle

class RiskOutput():
    def __init__(self, name = None, risk = None) -> None:
        self.name = name
        self.risk = risk
        self.category = None
        self.category_eval()
    
    def category_eval(self):
        if self.risk < 0.25:
            self.category = "Category A" 
        elif self.risk >= 0.25 and self.risk < 0.50 :
            self.category = "Category B"
        elif self.risk >= 0.50 and self.risk < 0.75 :
            self.category = "Category C"
        elif self.risk >= 0.75 and self.risk < 1.00 :
            self.category = "Category D"
        else:
            self.category = "Category E"



class RiskModel():
    def __init__(self) -> None:
        self.filename = 'risk_app/finalized_model_risk.sav'

    def predict_res(self,cust_data):
        # load the model from disk
        if not cust_data:
            return 1.0

        loaded_model = pickle.load(open(self.filename, 'rb'))
        risk = loaded_model.predict([cust_data])
        risk = risk[0]
        return risk
