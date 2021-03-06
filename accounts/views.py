from django.shortcuts import render,redirect
from .models import ledger,Payments,Receipts,Account
from django.db.models import Avg, Count, Min, Sum,Max
# Create your views here.
from addshg.models import Loan,shg
def first(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')
    if(request.method=="POST"):
        account_name=request.POST['account']
        transctionType=request.POST['TransctionType']
        particulars=request.POST['particulars']
        amount=request.POST['amount']
        if account_name=="" or particulars=="" or amount==0:
            return render(request,'ledger.html',{"failure":"All the fields need to be entered"})
        l = ledger(AccountName=account_name,TransctionType=transctionType,Particulars=particulars,Amount=amount,RegIMO=request.user.username)
        l.save()
        if transctionType=="Debit":
            l1=ledger(AccountName=particulars,TransctionType="Credit",Particulars=account_name,Amount=amount,RegIMO=request.user.username)
            l1.save()
        else:
            l1 = ledger(AccountName=particulars, TransctionType="Debit", Particulars=account_name, Amount=amount,RegIMO=request.user.username)
            l1.save()
        return render(request,'ledger.html',{"success":"Account Statement Added"})
    return render(request,'ledger.html')

def disp(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')
    list_accounts = ledger.objects.raw('SELECT DISTINCT AccountName,id from accounts_ledger WHERE RegIMO=%s',[request.user.username])
    l=[]
    for i in list_accounts:
        if i.AccountName not in l:
            l.append(i.AccountName)
    if(request.method=="POST"):
        AccountName=request.POST['AccountName']
        Account = ledger.objects.all().filter(AccountName=AccountName,RegIMO=request.user.username)
        bal_debit = ledger.objects.filter(AccountName=AccountName,TransctionType="Debit",RegIMO=request.user.username).aggregate(debit=Sum('Amount'))
        bal_credit = ledger.objects.filter(AccountName=AccountName,TransctionType="Credit",RegIMO=request.user.username).aggregate(credit=Sum('Amount'))
        d=0
        c=0
        print(bal_debit)
        debit=bal_debit['debit']
        credit=bal_credit['credit']
        if credit==None:
            credit=0
        if debit==None:
            debit=0
        total = max(debit, credit)
        if debit>credit:
            d=debit-credit
            return render(request, 'dispLedger.html',
                          {'account': Account, 'list': l, 'debit': d,'total':total})
        else:
            c=credit-debit
            return render(request,'dispLedger.html',{'account':Account,'list':l,'credit':c,'total':total})
    else:
        return render(request,'dispLedger.html',{'list':l})

def edit(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')
    edit_details=ledger.objects.filter(RegIMO=request.user.username,TransctionType="Debit")
    if request.method=="POST":
        if "edit-button" in request.POST:
            acc = request.POST["account"]
            ttype = request.POST["TransctionType"]
            part = request.POST["particulars"]
            amt = request.POST["amount"]
            l=ledger(AccountName=acc, TransctionType=ttype, Particulars=part, Amount=amt,RegIMO=request.user.username)
            l.save()
            if ttype=="Debit":
                l=ledger(AccountName=part, TransctionType="Credit", Particulars=acc, Amount=amt,RegIMO=request.user.username)
                l.save()
            else:
                l=ledger(AccountName=part, TransctionType="Debit", Particulars=acc, Amount=amt,RegIMO=request.user.username)
                l.save()
            return render(request,"edit.html",{"success":"Successfully Updated"})
        acc=request.POST["account"]
        ttype=request.POST["TransctionType"]
        part = request.POST["particulars"]
        amt = request.POST["amount"]
        edit_l = ledger.objects.filter(AccountName=acc, TransctionType=ttype, Particulars=part, Amount=amt,RegIMO=request.user.username).delete()
        if ttype == "Debit":
            edit_l = ledger.objects.filter(AccountName=part, TransctionType="Credit", Particulars=acc,
                                           Amount=amt,RegIMO=request.user.username).delete()
        else:
            edit_l = ledger.objects.filter(AccountName=part, TransctionType="Debit", Particulars=acc,
                                           Amount=amt,RegIMO=request.user.username).delete()
        if request.POST["action"]=="delete":
            return render(request,"edit.html",{"success":"Successfully Deleted"})
        return render(request, "dispedit.html", {"an": acc, "tt": ttype, "part": part, "amt": amt})
    return render(request, "edit.html", {"details": edit_details})

def FinRecords(request):
    return render(request,"financial_index.html")

def CashAccountDisp(request):
    AccountName = "Cash"
    Account = ledger.objects.all().filter(AccountName=AccountName, RegIMO=request.user.username)
    bal_debit = ledger.objects.filter(AccountName=AccountName, TransctionType="Debit",
                                      RegIMO=request.user.username).aggregate(debit=Sum('Amount'))
    bal_credit = ledger.objects.filter(AccountName=AccountName, TransctionType="Credit",
                                       RegIMO=request.user.username).aggregate(credit=Sum('Amount'))
    d = 0
    c = 0
    print(bal_debit)
    debit = bal_debit['debit']
    credit = bal_credit['credit']
    if credit == None:
        credit = 0
    if debit == None:
        debit = 0
    total = max(debit, credit)
    if debit > credit:
        d = debit - credit
        return render(request, 'dispLedger.html',
                      {'account': Account, 'debit': d, 'total': total})
    else:
        c = credit - debit
        return render(request, 'dispLedger.html', {'account': Account, 'credit': c, 'total': total})


