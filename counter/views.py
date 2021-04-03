from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import train_tricket,user_tricket

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter, landscape

def pdf_view(request,id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Rail_Sheba_Trcket.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Start writing the PDF here
    train_data=get_object_or_404(user_tricket, pk=id)
    
    p.drawString(280, 800, "Rail Sheba" )
    p.line(0,780,1000,780)

    p.drawString(100, 700, "Train Name : ")
    p.drawString(100, 650, "From : ")
    p.drawString(100, 600, "To : ")
    p.drawString(100, 550, "Date : ")
    p.drawString(100, 500, "Time : ")

    p.drawString(200, 700, train_data.train_name)
    p.drawString(200, 650, train_data.From)
    p.drawString(200, 600, train_data.To)
    p.drawString(200, 550, train_data.Date)
    p.drawString(200, 500, train_data.time)
    
    # End writing
# drawString(100, 100, 'Hello world.')

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
















def Ticket_counter(request):
    train=train_tricket.objects.all()
    context={
            'train':train
         }
    return render(request,'counter.html',context)


def Purchase_tricket(request):
    if request.method == 'POST':
        adult=request.POST.get('adult')
        child=request.POST.get('child')
        txid=request.POST.get('txid')
        phone=request.POST.get('phone')

        train_name=request.POST.get('train_name')
        From=request.POST.get('From')
        To=request.POST.get('To')
        Date=request.POST.get('Date')
        time=request.POST.get('time')
        
        current_user = request.user

        alldata=user_tricket(adult=adult, child=child, Date=Date, time=time, txid=txid, phone=phone, train_name=train_name, From=From, To=To )
        alldata.user_id = current_user.id
        alldata.save()
    return redirect('account')





def single_tracket(request,id):
    train_data=get_object_or_404(train_tricket, pk=id)
    context={
        'train_data':train_data
    }
    return render(request,'single_tricket.html',context)











