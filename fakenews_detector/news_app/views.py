import joblib
from django.shortcuts import render
from .forms import NewsForm
from .utils import detect_fake_news, extract_text_from_pdf, vectorize_text

def index(request):
    is_fake = None  # Initialize is_fake to None
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.cleaned_data['news']
            file = form.cleaned_data['file']
            
            if file:
                news = extract_text_from_pdf(file)
            
            if news:
                model = joblib.load(r"C:\\Users\\Anurag\\OneDrive\\Desktop\\PROJECTS\\Fake_news\\best_model.pkl")
                vectorizer = joblib.load(r"C:\\Users\\Anurag\\OneDrive\\Desktop\\PROJECTS\\Fake_news\\vectorizer.pkl")
                news_vector = vectorize_text(news, vectorizer)
                is_fake = detect_fake_news(news_vector, model)
            
            return render(request, 'news_app/index.html', {'form': form, 'is_fake': is_fake})
    else:
        form = NewsForm()
    
    return render(request, 'news_app/index.html', {'form': form, 'is_fake': is_fake})
