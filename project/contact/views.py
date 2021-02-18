from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'contact/index.html')

# お問い合わせフォーム画面
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact:complete')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})

# 送信完了画面
def complete(request):
    return render(request, 'contact/complete.html')