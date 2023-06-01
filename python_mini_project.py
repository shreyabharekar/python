
clist=[]
cid=[]
class course():
    def __init__(self,i,n,f,d):
        
        self.cid=i
        self.cname=n
        self.cfees=f
        self.cduration=d
    def __str__(self):
        return f'Course ID is:-{self.cid},course name is:-{self.cname},course fees is{self.cfees},and course duration is:-{self.cduration}'

blist=[]
b_id=[]
class batch():
    def __init__(self,b,n,t,c):
        self.bid=b
        self.bname=n
        self.btiming=t
        self.cid=c
    def __str__(self):
        return f"Batch ID is:-{self.bid},batch name is:-{self.bname},and batch timing is:-{self.btiming}\nCourse details :-{self.cid}"



slist=[]
sid=[]
class student():
    def __init__(self,n,a,r,m,b):
        self.name=n
        self.address=a
        self.rollno=r
        self.mobileno=m
        self.bid=b
    def __str__(self):
        return f"Student Name is-{self.name}, address is-{self.address},roll no is-{self.rollno},mobile no is-{self.mobileno}\nBatch details are:{self.bid}"

def menu():
    while True:
        ch=int(input('Enter the group\n 1.Course\t 2.Batch\n 3.Students\t 4.Exit\n  :-'))
        print("-------------------------------------------------------------------------")

            
        if ch==1:
            c=int(input('Enter the group\n 1.Add Course\t\t 2.Delete Course\n 3.Update Course\t 4.Show Course\n:-'))

            if c==1:
                #ADD COURSE:
                n=int(input('Enter the no of course to add:'))

                for k in range(n):
                    i=int(input('Enter the course ID:'))
                    if i in cid:
                        print('Entered duplicate course id:',i)
                        #break
                    else:
                        n=input("Enter the course name:")
                        f=int(input('Enter course fees:'))
                        d=int(input('Enter course duration in months:'))
                        c=course(i,n,f,d)
                        clist.append(c)
                        cid.append(i)
                        print('course',n,'added')
                        print("---------------------------------------------------------------------------")
            elif c==2:
                #DELETE COURSE
                #n=int(input('Enter the no of students to delete'))
                if clist==[]:
                    print('No course added yet, please add first')
                else:
                    c=int(input('Enter the course id to delete'))
                    
                    for cl in clist:
                        #print(cl)
                        if cl.cid==c:
                            clist.remove(cl)
                            cid.remove(c)
                            print('The course with course ID:-',c,'deleted')
                            break
                    else:
                        print('Entered wrong course id, please enter correct course id')
                        print("---------------------------------------------------------------------------")

            elif c==3:
                #UPDATE COURSE
                
                if clist==[]:
                    print('No course added yet')
                else:
                    c=int(input('Enter the course ID to update'))
                    if c in cid:
                        for i in clist:
                            if i.cid==c:
                                n=input('Enter the new name :')
                                f=int(input('Enter the new fees :'))
                                d=int(input('Enter the new class duration : '))
                                i.cname=n
                                i.cfees=f
                                i.cduration=d
                                print('The course ID',c,'updated')
                                break
                        else:
                            print('Entered incorrect id, plz enter correct course id')
                    else:
                        print('Entered course ID doesnot exist, please enter correct one')
                        print("---------------------------------------------------------------------------")

                        continue
            elif c==4:
                if clist==[]:
                    print('No course added yet!')
                #SHOW COURSE
                else:    
                    for s in clist:
                        print(s)
        elif ch==2:
            c=int(input('Enter the group\n 1.Add Batch\t 2.Delete Batch\n 3.Update Batch\t 4.Show Batch\n 5.Update Course\n'))

            if clist==[]:
                print('please first add the course :')
                continue
            if c==1:
                #ADD BATCH
                n=int(input('Enter the no of batches to add:-'))
                for k in range(n):
                    ci=int(input('Enter the course ID to add for adding batch:='))
                    if ci in cid:
                        for i in clist:
                            if ci == i.cid:
                                bid=int(input('Enter the batch ID:-'))
                                #global bi
                                if bid in b_id:
                                    print('Batch Id already available')
                                    break
                                else:
                                    bname=input('Enter the batch name:-')
                                    btiming=input('Enter the batch timing:-')
                                    c1=ci
                                    b1=batch(bid,bname,btiming,i)
                                    blist.append(b1)
                                    b_id.append(bid)
                                    print('Batch added with ID',bid)
                                    print("---------------------------------------------------------------------------")

                                    break
                            
                        else:
                            print('Entered wrong course ID, please check')
                            break
                    else:
                        print('Entered course ID doesnot exists, please enter correct one')
                        continue

            elif c==2:
                #DELETE BATCH
                
                if blist==[]:
                    print('No batch added yet to delete')
                else:
                    b=int(input('Enter the batch id to delete:-'))
                    for b1 in blist:
                        #print(b1)
                        if b1.bid==b:
                            blist.remove(b1)
                            print('The Batch with batch ID',b,' deleted')
                            break
                        #elif b1.bid!=b:
                            #print('Entered wrong batch id')
                    else:
                        print('Entered wrong batch id')

            elif c==3:
                #UPDATE BATCH
                
                if blist==[]:
                    print('No batch added yet to update')
                else:
                    b=int(input('Enter the batch ID to update:-'))
                    #if c in cid:
                    for i in blist:
                        if i.bid==b:
                            n=input('Enter the new batch name : ')
                            t=input('Enter the new batch timing :')
                            i.bname=n
                            i.btiming=t
                            print('The Batch with ID',b,'updated')
                            break
                            
                        #elif i.bid!=b:
                         #   print('Entered incorrect id, plz enter correct id')
                    else:
                        print('Entered incorrect id, plz enter correct id')
                        print("---------------------------------------------------------------------------")

            elif c==4:
                #SHOW BATCH
                for s in blist:
                    print(s)
                print("---------------------------------------------------------------------------")


            elif c==5:
                bt=int(input('Enter the batch id to update :'))
                if bt not in b_id:
                    print('Entered batch id doesnot exists')
                    print("---------------------------------------------------------------------------")

                else:
                    courseid_to_update=int(input('Enter the course id to update :'))
                    if blist==[]:
                        print('first add the batch')
                        break
                    else:
                        
                        for b in blist:
                            if bt==b.bid:
                                for cr in clist:
                                    if courseid_to_update==cr.cid:
                                        b.cid=cr
                                        print('Updated done')
                                        print("---------------------------------------------------------------------------")

                                        break
                                else:
                                    break
                        #else:
                         #   break
                                              
        elif ch==3:
            c=int(input('Enter the group\n 1.Add Student\t\t 2.Delete Student\n 3.Update Student\t 4.Show Student\n 5.Update batch\n'))

            if blist==[]:
                print('please first add the batch : ')
                continue
            if c==1:
                #ADD STUDENTS
                n=int(input('Enter the no of students to add:-'))
                for k in range(n):
                    bi=int(input('Enter the batch ID to add for adding students :'))
                    for i in blist:
                        if bi==i.bid:
                            rollno=int(input('Enter the rollno of student:-'))
                            if rollno in sid:
                                print('Batch Student Rollno already available')
                            else:
                                name=input('Enter the name : ')
                                address=input('Enter the address:-')
                                mobileno=int(input('Enter the mobile no:-'))
                                mo=str(mobileno)
                                if len(mo)==10:
                                    b1=bi
                                    s1=student(name,address,rollno,mobileno,i)
                                    slist.append(s1)
                                    sid.append(rollno)
                                    print('Student with rollno:',rollno,' added')
                                    break                                    
                                else:
                                    print('Enter the mobile no with 10 nos. only')
                                    print("---------------------------------------------------------------------------")

                                    break
                                
                        #elif bi!=i.bid:
                            #print('Entered wrong batch ID, please check')
                            #continue
                    else:
                        print('Entered wrong batch ID, please check')
            elif c==2:
                #DELETE STUDENT
                s=int(input('Enter the student roll no to delete : '))
                if slist==[]:
                    print('No students added yet')
                else:
                    for s1 in slist:
                        if s1.rollno==s:
                            slist.remove(s1)
                            sid.remove(s)
                            print('Student with rollno',s,'deleted')
                            break
                        #elif s!=s1.rollno:
                            #print('Entered wrong student rollno')
                    else:
                        print('Entered wrong student rollno')

            elif c==3:
                #UPDATE STUDENT
                s=int(input('Enter the roll no to update :'))
                if slist==[]:
                    print('No students added yet')
                else:
                    for i in slist:
                        if i.rollno==s:
                            n=input('Enter the new name:-')
                            a=input('Enter the new address:-')
                            m=int(input('Enter the mobile no'))
                            mob=str(m)
                            if len(mmob)==10:
                                i.name=n
                                i.address=a
                                i.mobileno=mob
                                break
                            else:
                                print('Enter the mobile no with 10 nos. only')
                                break                            
                        #elif i.rollno!=s:
                            #continue
                    else:
                        print('Entered roll no is wrong, please enter correct roll no.')

            elif c==4:
                if slist==[]:
                    print('first add student :')
                else:
                    #SHOW STUDENTS
                    for j in slist:
                        print(j)

            elif c==5:
                sr=int(input('Enter the student rollno : '))
                if sr not in sid:
                    print('Entered student roll no doesnot exists')
                else:
                    batchid_to_update=int(input('Enter the batch id to update : '))
                    if batchid_to_update in b_id: 
                        if slist==[]:
                            print('first add the student')
                            break
                        else:
                            
                            for s in slist:
                                if sr==s.rollno:
                                    for btc in blist:
                                        if batchid_to_update==btc.bid:
                                            s.bid=btc
                                            print('Updated done')
                                            break
                                    else:
                                        break
                    else:
                        print('Enter the correct batch ID, entered Batch ID doesnot exists')
                        continue
                
        
                        

        elif ch==4:
            break
        else:
            print('Wrong input, please enter the correct option')
            continue


try:
    menu()
except (NameError, ValueError) as e:
    print('Enter the correct value', e)
    menu()
    

    
