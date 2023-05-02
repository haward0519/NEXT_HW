from django.shortcuts import render

# Create your views here.
def count(request):
    # logics here
    return render(request,'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(' ', ''))
    txt_len = len(text.split())

    return render(request, 'result.html', {
        'text':text,
        'total_len': total_len,
        'no_blank_len': no_blank_len,
        'txt_len': txt_len})
