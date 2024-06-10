from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from dos.models import *


def main(request):
    return render(request, 'login_index.html')


def log(request):
    uname = request.POST['textfield']
    pswrd = request.POST['textfield2']
    ob = login.objects.get(username=uname, password=pswrd)
    if ob.type == "bank":
        # return JsonResponse({"task":"ok","type":"bank","lid":ob.id})
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


@login_required(login_url='/')
def bank_home(request):
    return render(request, 'bank/index.html')


@login_required(login_url='/')
def manage_branch(request):
    ob = branch.objects.all()
    return render(request, 'bank/manage branch.html', {'val': ob})


@login_required(login_url='/')
def manage_branch_search(request):
    Name = request.POST['textfield']
    ob = branch.objects.filter(name__istartswith=Name)
    return render(request, 'bank/manage branch.html', {'val': ob, 'Name': Name})


@login_required(login_url='/')
def add_details(request):
    return render(request, 'bank/Add.html')


@login_required(login_url='/')
def branch_code(request):
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
    ob=branch.objects.get(id=id)
    request.session['nid']=ob.id
    return render(request, 'bank/editbrn.html',{'val':ob})

@login_required(login_url='/')
def edit_branch(request):
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
    ob=branch.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manage_branch'</script>''')



@login_required(login_url='/')
def users(request):
    oj = branch.objects.all()
    ob = Account_details.objects.all()
    return render(request, 'bank/view user.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def usersearch(request):
    br = request.POST['select']
    ob = Account_details.objects.filter(BRANCH__id=br)
    oj = branch.objects.all()
    return render(request, 'bank/view user.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def reports(request):
    ob = report_table.objects.all()

    return render(request, 'bank/view report.html', {'val': ob})


@login_required(login_url='/')
def reports_search(request):
    date = request.POST['textfield']
    ob = report_table.objects.filter(date=date)

    return render(request, 'bank/view report.html', {'val': ob})


@login_required(login_url='/')
def complaints(request):
    ob = complaint.objects.all()
    return render(request, 'bank/view complaint.html', {'val': ob})


@login_required(login_url='/')
def complaints_search(request):
    date = request.POST['textfield']
    ob = complaint.objects.filter(date=date)
    return render(request, 'bank/view complaint.html', {'val': ob})


@login_required(login_url='/')
def replys(request, id):
    request.session['cid'] = id
    return render(request, 'bank/reply.html')


@login_required(login_url='/')
def reply_code(request):
    rep = request.POST['textfield']
    ob = complaint.objects.get(id=request.session['cid'])
    ob.reply = rep
    ob.save()
    return HttpResponse('''<script>alert("Replied");window.location='/complaints'</script>''')


@login_required(login_url='/')
def feedbacks(request):
    ob = feedback.objects.all()
    return render(request, 'bank/view feedback.html', {'val': ob})


@login_required(login_url='/')
def feedbacks_search(request):
    date = request.POST['textfield']
    ob = feedback.objects.filter(date=date)
    return render(request, 'bank/view feedback.html', {'val': ob})


# ______________________branch____________________________________
@login_required(login_url='/')
def branch_home(request):
    return render(request, 'branch/index_branch.html')


@login_required(login_url='/')
def accept_user(request):
    ob = request_table.objects.filter(BRANCH__LOGIN__id=request.session['lid'])
    return render(request, 'branch/accept user.html', {'val': ob})


@login_required(login_url='/')
def accept_user_search(request):
    name = request.POST['textfield']
    ob = request_table.objects.filter(BRANCH__LOGIN__id=request.session['lid'], USER__first_name__istartswith=name)
    return render(request, 'branch/accept user.html', {'val': ob,'name':name})


@login_required(login_url='/')
def allocate_account_details(request):
    return render(request, 'branch/Allocate account details.html')


@login_required(login_url='/')
def allocation(request, id, rid):
    request.session['USERID'] = id
    request.session['REQid'] = rid
    return render(request, 'branch/Allocation.html')


@login_required(login_url='/')
def allocation_post(request):
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
    ob1 = request_table.objects.get(id=rid)
    ob1.status = 'Rejected'
    ob1.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/accept_user'</script>''')


@login_required(login_url='/')
def send_report(request):
    return render(request, 'branch/send report.html')


@login_required(login_url='/')
def report_post(request):
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
    ob = transaction.objects.filter(ACC_NO__BRANCH__LOGIN__id=request.session['lid'])
    for i in ob:
        ob1 = Account_details.objects.get(id=i.ACC_NO.id)
    ooo = branch.objects.get(LOGIN__id=request.session['lid'])
    name = ooo.name
    ifsc = ooo.IFSC

    return render(request, 'branch/transaction details.html', {'val': ob, 'name': name, 'ifsc': ifsc})



@login_required(login_url='/')
def transaction_details_search(request):
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
    ob = transaction.objects.all()
    oj = Account_details.objects.all()
    return render(request, 'branch/new details.html', {'val': ob, 'val2': oj})


@login_required(login_url='/')
def add_update(request):
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
    ob = feedback.objects.all()
    return render(request, 'branch/view feedback.html', {'val': ob})


@login_required(login_url='/')
def view_feedback_search(request):
    date = request.POST['textfield']
    ob = feedback.objects.filter(date=date)
    return render(request, 'branch/view feedback.html', {'val': ob})


# _________________________USER_______________________________________

@login_required(login_url='/')
def user_home(request):
    return render(request, 'user/index_user.html')


@login_required(login_url='/')
def send_acrequest(request):
    ob = branch.objects.all()
    return render(request, 'user/send ac request.html', {'val': ob})


@login_required(login_url='/')
def send_acc_req(request, id):
    ob = request_table()
    ob.USER = user.objects.get(LOGIN__id=request.session['lid'])
    ob.BRANCH = branch.objects.get(id=id)
    ob.status = 'pending'
    ob.date = datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Request Send");window.location='/user_home'</script>''')


def registration(request):
    return render(request, 'user/registration_index.html')


@login_required(login_url='/')
def send_complaint(request):
    return render(request, 'user/send complaint us.html', )


@login_required(login_url='/')
def send_complaint_post(request):
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
    return render(request, 'user/send feedback.html')


@login_required(login_url='/')
def send_feedback_post(request):
    ob = request.POST['textfield']

    oj = feedback()
    oj.USER = user.objects.get(LOGIN__id=request.session['lid'])
    oj.date = datetime.now()
    oj.feedback = ob
    oj.save()
    return HttpResponse('''<script>alert("Feedback Send");window.location='/user_home'</script>''')


@login_required(login_url='/')
def view_account_detais_new(request):
    # ob=Account_details.objects.filter(USER__id=request.session['lid'])
    ob = Account_details.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/View ACC details.html', {'val': ob})


@login_required(login_url='/')
def view_account_details_search(request):
    name = request.POST['textfield']

    ob = Account_details.objects.filter(BRANCH__name__istartswith=name)
    return render(request, 'user/View ACC details.html', {'val': ob,'name': name})


@login_required(login_url='/')
def send_request(request):
    ob = request_table.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/send request.html', {'val': ob})


@login_required(login_url='/')
def select_branch(request):
    return render(request, 'user/select branch.html')


@login_required(login_url='/')
def view_transaction(request):
    ob = transaction.objects.filter(ACC_NO__USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/view transaction.html', {'val': ob})


@login_required(login_url='/')
def view_transaction_search(request):
    date = request.POST['textfield']
    ob = transaction.objects.filter(date=date)
    return render(request, 'user/view transaction.html', {'val': ob})


@login_required(login_url='/')
def view_reply(request):
    ob = complaint.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/send reply.html', {'val': ob})


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def registration_s(request):
    return render(request, 'user/registration.html')


def Register_post(request):
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
