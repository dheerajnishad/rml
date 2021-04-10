from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer
from django.http import HttpResponse
import time
from django.contrib import messages
from customersupport.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
import pytz
import datetime
from background_task import background
from django.utils import timezone
from datetime import timedelta


#enquiry form 
@api_view(['GET', 'POST'])
def enquiry(request):
    if request.method == 'GET':
        return render(request,'customerDetails.html')
    
    elif request.method == 'POST':
        try:
            CustomerName=request.POST.get("name")
            PhoneNo=request.POST.get("phone")
            Email=request.POST.get("email")
            Query=request.POST.get("message")
            created = Enquiry.objects.get_or_create(CustomerName=CustomerName, PhoneNo=PhoneNo, Email=Email,Query=Query)
            enquiryid=created[0].EnquiryId
            enquiry_mailer(enquiryid)
            messages.success(request, 'Enquiry submitted successfully!')
            return render(request,'customerDetails.html', {'alert_flag': True})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET', 'POST'])
def enquiry_details(request):
    if request.method == 'GET':
        enquiry = Enquiry.objects.all()
        serializer =EnquirySerializer(enquiry, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def enquiry_mailer(enquiryid):
    try:
        enquiry = Enquiry.objects.get(EnquiryId=enquiryid)
        name=enquiry.CustomerName
        email_add = enquiry.Email
        text_content = "Click on the below link to view customer enquiry" +'\n' \
                        "http://127.0.0.1:8000/enquiry/"+str(enquiryid) 
        subject, sender_email, to = name + ' ' + " has sent a Enquiry Message", EMAIL_HOST_USER, email_add
        email = EmailMessage(subject, text_content, sender_email, [to])
        email.send()
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def feedback(request,pk):
    if request.method == 'GET':
        try:
            enquiry = Enquiry.objects.get(EnquiryId=pk)
            serializer =EnquirySerializer(enquiry).data
            return render(request,'feedback.html',serializer)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
    elif request.method == 'POST':
        try:
            enquiry = Enquiry.objects.get(EnquiryId=pk)
            serializer =EnquirySerializer(enquiry).data
            feedback=request.POST.get("message")
            expiry=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            enquiry.Expiry=expiry
            enquiry.Feedback=feedback
            enquiry.save()
            enquiryid=str(enquiry.EnquiryId)
            service_feedback(enquiryid,schedule=timedelta(minutes=30))  #send mail to customer after 30 min.     #set minutes=1 for 1 min
            return render(request,'success.html',{'alert_flag': True})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@background()
def service_feedback(enquiryid):
    try:
        enquiry = Enquiry.objects.get(EnquiryId=enquiryid)
        name=enquiry.CustomerName
        feedback=enquiry.Feedback
        email_add = enquiry.Email
        text_content = "feedback"+feedback+ "\n"\
                        "Click on the below link to provide feedback  " "\n"\
                        "http:/"+"/127.0.0.1:8000/customer-review/"+str(enquiryid)
        subject, sender_email, to ="response from Service Provider", EMAIL_HOST_USER, email_add
        email = EmailMessage(subject, text_content, sender_email, [to])
        email.send()
        return Response(status=status.HTTP_201_CREATED)
    except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def customer_review(request,pk):
    if request.method == 'GET':
        try:
            enquiry = Enquiry.objects.get(EnquiryId=pk)
            expiry=timezone.localtime(enquiry.Expiry)
            current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
            time=(datetime.datetime.now(pytz.timezone('Asia/Kolkata'))-expiry)
            if time<timedelta(minutes=30): 
                serializer =EnquirySerializer(enquiry).data
                return render(request,'customer_satisfaction.html',serializer)
            else:
                return render(request,'404.html')

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
        review=request.POST.get("answer")
        enquiry=Enquiry.objects.get(EnquiryId=pk)
        enquiry.Review=review
        enquiry.save()
        return render(request,'success.html',{'alert_flag': True})


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_400(request, exception):
        data = {}
        return render(request,'400.html', data)