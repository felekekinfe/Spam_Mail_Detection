from django.apps import AppConfig
import joblib

class SpamdetectionappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "SpamDetectionApp"
    model=None
    vectorizer=None


    def ready(self):
        self.model = joblib.load('model.pkl')
        self.vectorizer = joblib.load('vectorizer.pkl')
