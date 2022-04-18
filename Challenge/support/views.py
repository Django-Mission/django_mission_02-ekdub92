from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    title = request.GET.get('title')
    category = request.GET.get('category')
    email = request.GET.get('email')
    email_box = request.GET.get('email_box')
    sms = request.GET.get('sms')
    sms_box = request.GET.get('sms_box')
    content = request.GET.get('content')
    image = request.GET.get('chooseFile')
    print('title : ', title)
    print('category : ', category)
    print('email : ', email)
    print('email_box : ', email_box)
    print('sms : ', sms)
    print('sms_box : ', sms_box)
    print('content : ', content)
    print('image : ', image)
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO support_inquiry VALUES (?,?,?,?,?,?,?)',
        (1, category, title, email, sms, content, image)
    )
    conn.commit()
    return render(request, 'submit.html')