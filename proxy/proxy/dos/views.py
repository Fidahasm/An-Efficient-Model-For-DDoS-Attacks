from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# from django.http.response import JsonResponse
from django.shortcuts import render
from datetime import datetime
# from .mlp import predict_fn
# Create your views here.
from dos.mlp import predict_fn
from .models import *
# from scapy.all import sniff, IP, TCP
import requests
url="http://192.168.55.222:8000/"
blocklist=[]



def main(request):
    # try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length,"max_packet_length")
        print(max_packet_length,"max_packet_length")
        print(max_packet_length,"max_packet_length")
        print(max_packet_length,"max_packet_length")
        print(max_packet_length,"max_packet_length")
        # return JsonResponse({'Max Packet Length': max_packet_length})

        if ip in blocklist:
            return HttpResponse("")
        else:
            ob=log_tb()
            ob.ip=ip
            ob.date=datetime.now()
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                # res=0
                res=predict_fn(r)
                print("res",res)
                print("res",res)
                print("res",res)
                print("res",res)
                print("======================================")
                print("======================================")
                print("======================================")
                print("======================================")
                if float(res)==float(1):

                    blocklist.append(ip)

                    ob=block_list()
                    ob.ip=ip
                    ob.save()



    # except Exception as e:
    #     print(e)

        return render(request, 'login_index.html')


def log(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        print(max_packet_length, "max_packet_length")
        print(max_packet_length, "max_packet_length")
        print(max_packet_length, "max_packet_length")
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")

        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res)==float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    uname = request.POST['textfield']
    pswrd = request.POST['textfield2']
    in_values = request.POST
    try:
        res = requests.post(url + "log", data=in_values)
        print(res.text,"================== ")
        ob = login.objects.get(username=uname, password=pswrd)
        if ob.type == "bank":

            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Welcome to Bank Home");window.location='/bank_home'</script>''')
        elif ob.type == "branch":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)

            return HttpResponse('''<script>alert("Welcome to Branch Home");window.location='/branch_home'</script>''')
        elif ob.type == "user":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Welcome to User Home");window.location='/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert("Please Signup....!");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("Please Signup....!");window.location='/'</script>''')
@login_required(login_url='/')
def bank_home(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'bank/index.html')


@login_required(login_url='/')
def manage_branch(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "manage_branch", data=in_values)
    print(res.text, "================== ")
    ob = branch.objects.all()
    return render(request, 'bank/manage branch.html', {'val': ob})


@login_required(login_url='/')
def manage_branch_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "manage_branch_search", data=in_values)
    print(res.text, "================== ")
    Name = request.POST['textfield']
    ob = branch.objects.filter(name__istartswith=Name)
    return render(request, 'bank/manage branch.html', {'val': ob, 'Name': Name})


@login_required(login_url='/')
def add_details(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'bank/Add.html')


@login_required(login_url='/')
def branch_code(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "branch_code", data=in_values)
    print(res.text, "================== ")
    nm = request.POST['textfield']
    pl = request.POST['textfield2']
    po = request.POST['textfield3']
    pn = request.POST['textfield4']
    ph = request.POST['textfield5']
    ifsc = request.POST['textfield6']
    em = request.POST['textfield7']
    un = request.POST['textfield8']
    pw = request.POST['textfield9']

    ob = login()
    ob.username = un
    ob.password = pw
    ob.type = "branch"
    ob.save()

    oj = branch()
    oj.name = nm
    oj.place = pl
    oj.post = po
    oj.pin = pn
    oj.phone = ph
    oj.IFSC = ifsc
    oj.email = em
    oj.LOGIN = ob
    oj.save()
    return HttpResponse('''<script>alert("Added");window.location='/manage_branch'</script>''')


@login_required(login_url='/')
def edit_details(request,id):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "edit_details", data=in_values)
    print(res.text, "================== ")
    ob=branch.objects.get(id=id)
    request.session['nid']=ob.id
    return render(request, 'bank/editbrn.html',{'val':ob})

@login_required(login_url='/')
def edit_branch(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "edit_branch", data=in_values)
    print(res.text, "================== ")
    nm = request.POST['textfield']
    pl = request.POST['textfield2']
    po = request.POST['textfield3']
    pn = request.POST['textfield4']
    ph = request.POST['textfield5']
    ifsc = request.POST['textfield6']
    em = request.POST['textfield7']


    oj = branch.objects.get(id=request.session['nid'])
    oj.name = nm
    oj.place = pl
    oj.post = po
    oj.pin = pn
    oj.phone = ph
    oj.IFSC = ifsc
    oj.email = em
    oj.save()
    return HttpResponse('''<script>alert("Edited");window.location='/manage_branch'</script>''')



@login_required(login_url='/')
def delete_branch(request,id):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "delete_branch", data=in_values)
    print(res.text, "================== ")
    ob=branch.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manage_branch'</script>''')



@login_required(login_url='/')
def users(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    oj = branch.objects.all()
    ob = Account_details.objects.all()
    return render(request, 'bank/view user.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def usersearch(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "usersearch", data=in_values)
    print(res.text, "================== ")
    br = request.POST['select']
    ob = Account_details.objects.filter(BRANCH__id=br)
    oj = branch.objects.all()
    return render(request, 'bank/view user.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def reports(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "reports", data=in_values)
    print(res.text, "================== ")
    ob = report_table.objects.all()

    return render(request, 'bank/view report.html', {'val': ob})


@login_required(login_url='/')
def reports_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "reports_search", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield']
    ob = report_table.objects.filter(date=date)

    return render(request, 'bank/view report.html', {'val': ob})


@login_required(login_url='/')
def complaints(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "complaints", data=in_values)
    print(res.text, "================== ")
    ob = complaint.objects.all()
    return render(request, 'bank/view complaint.html', {'val': ob})


@login_required(login_url='/')
def complaints_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "complaints_search", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield']
    ob = complaint.objects.filter(date=date)
    return render(request, 'bank/view complaint.html', {'val': ob})


@login_required(login_url='/')
def replys(request, id):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "replys", data=in_values)
    print(res.text, "================== ")
    request.session['cid'] = id
    return render(request, 'bank/reply.html')


@login_required(login_url='/')
def reply_code(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "reply_code", data=in_values)
    print(res.text, "================== ")
    rep = request.POST['textfield']
    ob = complaint.objects.get(id=request.session['cid'])
    ob.reply = rep
    ob.save()
    return HttpResponse('''<script>alert("Replied");window.location='/complaints'</script>''')


@login_required(login_url='/')
def feedbacks(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "feedbacks", data=in_values)
    print(res.text, "================== ")
    ob = feedback.objects.all()
    return render(request, 'bank/view feedback.html', {'val': ob})


@login_required(login_url='/')
def feedbacks_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "feedbacks_search", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield']
    ob = feedback.objects.filter(date=date)
    return render(request, 'bank/view feedback.html', {'val': ob})


# ______________________branch____________________________________
@login_required(login_url='/')
def branch_home(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'branch/index_branch.html')


@login_required(login_url='/')
def accept_user(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "accept_user", data=in_values)
    print(res.text, "================== ")
    ob = request_table.objects.filter(BRANCH__LOGIN__id=request.session['lid'])
    return render(request, 'branch/accept user.html', {'val': ob})


@login_required(login_url='/')
def accept_user_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "accept_user_search", data=in_values)
    print(res.text, "================== ")
    name = request.POST['textfield']
    ob = request_table.objects.filter(BRANCH__LOGIN__id=request.session['lid'], USER__first_name__istartswith=name)
    return render(request, 'branch/accept user.html', {'val': ob,'name':name})


@login_required(login_url='/')
def allocate_account_details(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'branch/Allocate account details.html')


@login_required(login_url='/')
def allocation(request, id, rid):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "allocation", data=in_values)
    print(res.text, "================== ")
    request.session['USERID'] = id
    request.session['REQid'] = rid
    return render(request, 'branch/Allocation.html')


@login_required(login_url='/')
def allocation_post(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "allocation_post", data=in_values)
    print(res.text, "================== ")
    accno = request.POST['textfield']
    balance = request.POST['textfield2']
    pin = request.POST['textfield3']

    ob = Account_details()
    ob.USER = user.objects.get(id=request.session['USERID'])
    ob.Account_No = accno
    ob.BRANCH = branch.objects.get(LOGIN__id=request.session['lid'])
    ob.Balance = balance
    ob.pin_num = pin
    ob.save()

    ob1 = request_table.objects.get(id=request.session['REQid'])
    ob1.status = 'Accepted'
    ob1.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/accept_user'</script>''')


@login_required(login_url='/')
def rejection(request, rid):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "rejection", data=in_values)
    print(res.text, "================== ")
    ob1 = request_table.objects.get(id=rid)
    ob1.status = 'Rejected'
    ob1.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/accept_user'</script>''')


@login_required(login_url='/')
def send_report(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()



    except Exception as e:
        print(e)

    return render(request, 'branch/send report.html')


@login_required(login_url='/')
def report_post(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "report_post", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield1']
    rq = request.POST['textfield2']

    ob = report_table()
    ob.BRANCH = branch.objects.get(LOGIN__id=request.session['lid'])
    ob.report = rq
    ob.date = date
    ob.save()
    return HttpResponse('''<script>alert("Report Send");window.location='/send_report'</script>''')


@login_required(login_url='/')
def transaction_details(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "transaction_details", data=in_values)
    print(res.text, "================== ")
    ob = transaction.objects.filter(ACC_NO__BRANCH__LOGIN__id=request.session['lid'])
    for i in ob:
        ob1 = Account_details.objects.get(id=i.ACC_NO.id)
    ooo = branch.objects.get(LOGIN__id=request.session['lid'])
    name = ooo.name
    ifsc = ooo.IFSC

    return render(request, 'branch/transaction details.html', {'val': ob, 'name': name, 'ifsc': ifsc})



@login_required(login_url='/')
def transaction_details_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "transaction_details_search", data=in_values)
    print(res.text, "================== ")
    tr = request.POST['textfield']
    ob = transaction.objects.filter(ACC_NO__Account_No=tr,ACC_NO__BRANCH__LOGIN__id=request.session['lid'])
    for i in ob:
        ob1 = Account_details.objects.get(id=i.ACC_NO.id)
    # print(ob1, "========================")
    ooo=branch.objects.get(LOGIN__id=request.session['lid'])
    name = ooo.name
    ifsc = ooo.IFSC
    return render(request, 'branch/transaction details.html', {'val': ob, 'name': name, 'ifsc': ifsc})


@login_required(login_url='/')
def update(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)
                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "update", data=in_values)
    print(res.text, "================== ")
    ob = transaction.objects.all()
    oj = Account_details.objects.all()
    return render(request, 'branch/new details.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def add_update(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "add_update", data=in_values)
    print(res.text, "================== ")
    s = request.POST['select']
    a = request.POST['select2']
    b = request.POST['select3']
    c = request.POST['textfield']
    ob = transaction()
    ob.Type = s
    ob.Transaction_type = a
    ob.Amount = c
    ob.ACC_NO = Account_details.objects.get(id=b)
    ob.date = datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='transaction_details'</script>''')


@login_required(login_url='/')
def view_feedback(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_feedback", data=in_values)
    print(res.text, "================== ")
    ob = feedback.objects.all()
    return render(request, 'branch/view feedback.html', {'val': ob})


@login_required(login_url='/')
def view_feedback_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_feedback_search", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield']
    ob = feedback.objects.filter(date=date)
    return render(request, 'branch/view feedback.html', {'val': ob})


# _________________________USER_______________________________________

@login_required(login_url='/')
def user_home(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob=log_tb.objects.filter(ip=ip).order_by("-id")
            r=[]
            if len(ob)>=8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()







    except Exception as e:
        print(e)

    return render(request, 'user/index_user.html')


@login_required(login_url='/')
def send_acrequest(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "send_acrequest", data=in_values)
    print(res.text, "================== ")
    ob = branch.objects.all()
    return render(request, 'user/send ac request.html', {'val': ob})


@login_required(login_url='/')
def send_acc_req(request, id):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "send_acc_req", data=in_values)
    print(res.text, "================== ")
    ob = request_table()
    ob.USER = user.objects.get(LOGIN__id=request.session['lid'])
    ob.BRANCH = branch.objects.get(id=id)
    ob.status = 'pending'
    ob.date = datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Request Send");window.location='/user_home'</script>''')


def registration(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'user/registration_index.html')


@login_required(login_url='/')
def send_complaint(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    return render(request, 'user/send complaint us.html', )


@login_required(login_url='/')
def send_complaint_post(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "send_complaint_post", data=in_values)
    print(res.text, "================== ")
    oj = request.POST['textfield']

    ob = complaint()
    ob.USER = user.objects.get(LOGIN__id=request.session['lid'])
    ob.complaint = oj
    ob.date = datetime.now()
    ob.reply = 'Nil'
    ob.save()

    return HttpResponse('''<script>alert("Complaint Send");window.location='/user_home'</script>''')


@login_required(login_url='/')
def send_feedback(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'user/send feedback.html')


@login_required(login_url='/')
def send_feedback_post(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "send_feedback_post", data=in_values)
    print(res.text, "================== ")
    ob = request.POST['textfield']

    oj = feedback()
    oj.USER = user.objects.get(LOGIN__id=request.session['lid'])
    oj.date = datetime.now()
    oj.feedback = ob
    oj.save()
    return HttpResponse('''<script>alert("Feedback Send");window.location='/user_home'</script>''')


@login_required(login_url='/')
def view_account_detais_new(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_account_detais_new", data=in_values)
    print(res.text, "================== ")
    # ob=Account_details.objects.filter(USER__id=request.session['lid'])
    ob = Account_details.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/View ACC details.html', {'val': ob})


@login_required(login_url='/')
def view_account_details_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_account_details_search", data=in_values)
    print(res.text, "================== ")
    name = request.POST['textfield']

    ob = Account_details.objects.filter(BRANCH__name__istartswith=name)
    return render(request, 'user/View ACC details.html', {'val': ob,'name': name})


@login_required(login_url='/')
def send_request(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "send_request", data=in_values)
    print(res.text, "================== ")
    ob = request_table.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/send request.html', {'val': ob})


@login_required(login_url='/')
def select_branch(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'user/select branch.html')


@login_required(login_url='/')
def view_transaction(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_transaction", data=in_values)
    print(res.text, "================== ")
    ob = transaction.objects.filter(ACC_NO__USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/view transaction.html', {'val': ob})


@login_required(login_url='/')
def view_transaction_search(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_transaction_search", data=in_values)
    print(res.text, "================== ")
    date = request.POST['textfield']
    ob = transaction.objects.filter(date=date)
    return render(request, 'user/view transaction.html', {'val': ob})


@login_required(login_url='/')
def view_reply(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "view_reply", data=in_values)
    print(res.text, "================== ")
    ob = complaint.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/send reply.html', {'val': ob})


def logout(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    auth.logout(request)
    return render(request, 'login.html')


def registration_s(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")

        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()
    except Exception as e:
        print(e)

    return render(request, 'user/registration.html')


def Register_post(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip, "****************")
        packet_data = request.POST.getlist('packet_data[]')

        max_packet_length = 0
        for packet_entry in packet_data:
            packet_length = len(packet_entry)
            if packet_length > max_packet_length:
                max_packet_length = packet_length
        print(max_packet_length, "max_packet_length")
        if ip in blocklist:
            return HttpResponse("")
        else:
            ob = log_tb()
            ob.ip = ip
            ob.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()

            ob = log_tb.objects.filter(ip=ip).order_by("-id")
            r = []
            if len(ob) >= 8:
                t1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(ob[0].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[1].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[2].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[3].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[4].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[5].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[6].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)

                t2 = datetime.strptime(str(ob[7].date).split(".")[0], "%Y-%m-%d %H:%M:%S")
                # Calculate the time difference
                time_difference = t2 - t1
                # Get time difference in milliseconds
                milliseconds = int(time_difference.total_seconds() * 1000)
                r.append(milliseconds)
                res = predict_fn(r)
                if float(res) == float(1):
                    blocklist.append(ip)

                    ob = block_list()
                    ob.ip = ip
                    ob.save()


    except Exception as e:
        print(e)

    in_values = request.POST
    res = requests.post(url + "Register_post", data=in_values)
    print(res.text, "================== ")
    first_name = request.POST['textfield']
    last_name = request.POST['textfield2']
    photo = request.FILES['file2']
    FS = FileSystemStorage()
    fn1 = FS.save(photo.name, photo)
    Signature = request.FILES['file']
    fn2 = FS.save(Signature.name, Signature)
    place = request.POST['textfield3']
    dob = request.POST['textfield4']
    email = request.POST['email']
    phone = request.POST['textfield5']
    gender = request.POST['radio']

    idproof = request.FILES['file3']
    fn3 = FS.save(idproof.name, idproof)
    Username = request.POST['textfield6']
    Password = request.POST['textfield7']

    ob = login()
    ob.username = Username
    ob.password = Password
    ob.type = 'user'
    ob.save()

    ob1 = user()
    ob1.login = ob
    ob1.first_name = first_name
    ob1.last_name = last_name
    ob1.photo = fn1
    ob1.place = place
    ob1.phone = phone
    ob1.email = email
    ob1.idproof = fn3
    ob1.dob=dob
    ob1.signature = fn2
    ob1.LOGIN=ob
    ob1.gender=gender
    ob1.save()

    return HttpResponse('''<script>alert("Registration Successfull");window.location='/user_home'</script>''')
