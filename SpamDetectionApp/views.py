
from django.shortcuts import render
from django.apps import apps
from .forms import TextInputForm

def predict(request):
    vectorizer = apps.get_app_config('SpamDetectionApp').vectorizer
    model = apps.get_app_config('SpamDetectionApp').model
    
    mail_is=None
    prediction = None
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            input_data = vectorizer.transform([input_text])
            prediction = model.predict(input_data)[0]

            

            if prediction==1:
                mail_is='Not Spam'
            else:
                mail_is='Spam'
    else:
        form = TextInputForm()
    
    return render(request, 'predict.html', {'form': form, 'mail_is': mail_is})
