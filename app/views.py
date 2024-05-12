from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q







'''##########---- logical operator in orm#######
-----> for and you can just use , comma between 2 queries to perform and operations else you can use & symbol also

------>for using or operator  as or operator means concatenation  of 2 or more querysets which means querysets of list of multiple objects
so you can't directly use |(parellel pipe symbol for or operation directly here)so first you need 
to convert the querysets into queryobject so that you can perform concatenation(+)/or operation between 2 objects
for thta you need to import Q (queryobject) from django.db.models import Q.

------>1) when you are writing a query using both or , and operators then you need to use & symbol here for 
performing and operation ;
       2) in this case your and as well as or operator query must be written with using Q(or operator query)&Q(and operator query)

------>for using not operator we have exclude() operator with us-that gives all the data except what we pass as agrument
       to exclude
'''



def logicaloperators(request):


    #fetching data using and(,),(|)or operator,exclude (not) from our table

    JDED=Emp.objects.select_related('deptno').all()
    JDED=Emp.objects.select_related('deptno').filter(Q(job='SALESMAN')|Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(job='SALESMAN',deptno=30)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982,sal__gt=2500)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lte=1982,deptno=30,sal__lte=1500)
    JDED=Emp.objects.select_related('deptno').filter((Q(ename__startswith='a')|Q(ename__endswith='n')|Q(ename__endswith='s'))&Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=2000,deptno=20)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__gt=1982,job='ANALYST')
    JDED=Emp.objects.select_related('deptno').exclude(job='PRESIDENT')


    d={'JDED':JDED}
    return render(request,'logicaloperators.html',d)







''''for performing joins in orm we have two methods-i)select_related-used when one to one ,many to one relationship is their
ii)prefetch-related---used when we have many to many,one to many relationship is their'''






def innerEquijoins(request):
    JDED=Emp.objects.select_related('deptno').all()

    #fetching data usng select_related using innner equi joins
    JDED=Emp.objects.select_related('deptno').filter(job='CLERK')
    JDED=Emp.objects.select_related('deptno').filter(Q(job='SALESMAN')|Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(job='SALESMAN',deptno=30)
    JDED=Emp.objects.select_related('deptno').filter(mgr=7839)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982)
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=3000)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982,sal__gt=2500)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lte=1982,deptno=30,sal__lte=1500)
    JDED=Emp.objects.select_related('deptno').filter(comm=0)
    JDED=Emp.objects.select_related('deptno').filter((Q(ename__startswith='a')|Q(ename__endswith='n')|Q(ename__endswith='s'))&Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(hiredate__day__lt=28)
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=2000,deptno=20)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__gt=1982,job='ANALYST')
    JDED=Emp.objects.select_related('deptno').filter(sal__lt=3000)
    JDED=Emp.objects.select_related('deptno').filter(empno__gte=7500)
    JDED=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')# AS DNAME IS PRESENT IN OUR DEPT TABLE SO WE CAN ACCESS DATA BY COMMONCOLOUMNNAME__COLUMNNAME=VALUE
    

    


    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)








def innerselfjoins(request):
    JDEM=Emp.objects.select_related('mgr').all()

    #fetching data usng select_related using innner self joins


    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    JDEM=Emp.objects.select_related('mgr').filter(Q(mgr__ename='BLAKE')|Q(mgr__ename='CLARK'))
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='F')
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=30,sal__gt=1500)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=20,hiredate__year__gt=1981)
    JDEM=Emp.objects.select_related('mgr').filter(job='CLERK',mgr__sal__gte=2500)
    JDEM=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    JDEM=Emp.objects.select_related('mgr').filter(job='SALESMAN',mgr__sal__gte=1200)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    #JDEM=Emp.objects.select_related('mgr').filter((mgr__deptno)__IN=(Emp.objects.select_related('mgr').filter(deptno=10)))#here subqueries will be used
   
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__in=['FORD','KING'])
    JDEM=Emp.objects.select_related('mgr').filter(sal__gte=1500,mgr__ename__contains='a')
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=10) 
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__in=['FORD','KING'])
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno__in=(20,30))
    
    JDEM=Emp.objects.select_related('mgr').filter(mgr__hiredate__year__in={1981,1982})


    d={'JDEM':JDEM}
    return render(request,'innerselfjoins.html',d)







''''JOINING MORE THAN 2 TABLES  IN OUR ORM IN SQL WE NEED TO MENTION TABLE NAME FOR JOINING THE TABLES BUT IN OUR ORM WE JUST
NEED TO MENTION OUR COMMON  COLUMN NAMES AND MY ORM WILL SEARCH FOR THAT FOREIGN KEY COLUMN AND JOINED THAT TABLE BY ITSELF'''




def multitablejoins(request):
    JDEMD=Emp.objects.select_related('deptno','mgr').all()#we are using select_related because that mgr and dept no are foreign key

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE',deptno__loc='CHICAGO')

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2000,deptno__loc__in={'CHICAGO','DALLAS'})

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2000,deptno__loc__in={'CHICAGO','DALLAS'},ename__contains='s')

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000,deptno__dname__in={'RESEARCH','SALES'})# FOR SEARCHING DATA OF JOINED TABLE YOU SHOULD GIVE:COMMONCOLOUMN NAME__COLUMNNAME='VALUE'

    #JDEMD=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000,deptno__dname='RESEARCH',mgr__deptno='RESEARCH')# FOR SEARCHING DATA OF JOINED TABLE YOU SHOULD GIVE:COMMONCOLOUMN NAME__COLUMNNAME='VALUE'

   




    
    d={'JDEMD':JDEMD}
    return render(request,'multitablejoins.html',d)









