from flask import Flask,request,jsonify
import json
import pymysql.cursors
from flask_mail import Mail, Message
dbb=pymysql.connect(host="localhost",    # your host, usually localhost
                      user="root",         # your username
                      passwd="",  # your password
                      db="Hackathon")
cursormain = dbb.cursor()

class DB:
    conn = None
    cursor = None

    def connect(self):
        self.conn = dbb
        self.cursor = cursormain

    def query(self, sql):
        try:
            self.cursor.execute(sql)
        except (AttributeError):
            self.connect()
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
        dbb.commit()

    def fetch(self,sql):
        try:
            self.cursor.execute(sql)
            ret =  self.cursor.fetchall()
        except (AttributeError):
            self.connect()
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            ret =  self.cursor.fetchall()
        return ret


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main_server():
	db=DB()
	cursormain=dbb.cursor
	print(request.args)
	print(request.data)
	data=request.get_json()
	print(data)

	if data['Type']=='checklogin':
		username=data['username']
		pwd=data['pwd']
		# type1=data['type']
		k="SELECT COUNT(*),`type` FROM `login` WHERE `username`='"+username+"' and `pwd`='"+pwd+"' "
		print(k)
		qr=db.fetch(k)
		sr1=qr[0][0]
		if qr[0][1]=='teacher':
			k="SELECT `name` FROM `teacher` WHERE `email`='"+username+"'"
			
		if qr[0][1]=='princi':
			k="SELECT `name` FROM `principal` WHERE `email`='"+username+"'"
			
		qr1=db.fetch(k)	
		# name1=qr1[0][0]
		print(qr[0][1])
		print(qr1[0][0])
		if sr1==1:
			return json.dumps({'Succ':'True','type':qr[0][1],'name':qr1[0][0]}),200,{'ContentType':'application/json'}
		else:
			return json.dumps({'Succ':'False'}),200,{'ContentType':'application/json'}

	if data['Type']=='forgetpassword':
		email=data['email']
		# type1=data['type']
		
		k="SELECT Count(*) FROM `teacher` WHERE `email`='"+email+"'"
		qr=db.fetch(k)
		if qr[0][0]==1:
			# MAil THEM LINK
			mail=Mail(app)
			app.config['MAIL_SERVER']='smtp.gmail.com'
			app.config['MAIL_PORT'] = 465
			app.config['MAIL_USERNAME'] = 'rvprvprvp78242@gmail.com'
			app.config['MAIL_PASSWORD'] = 'dalKhola24'
			app.config['MAIL_USE_TLS'] = False
			app.config['MAIL_USE_SSL'] = True
			mail = Mail(app)
			msg = Message('Su lya....badam khavnu rakho bhai', sender = 'rvprvprvp78242@gmail.com', recipients = [email])
			msg.body = "http://localhost/changepwd?mail="+email
			mail.send(msg)
		
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='resetpwd':
		cpwd=data['cpwd']
		email=data['email']
		type1=data['type']
		k="UPDATE `login` SET `pwd`='"+cpwd+"' WHERE `email`='"+email+"' "
		db.query(k)
		return json.dumps({'Succ':'Password Successfully reset'}),200,{'ContentType':'application/json'}
			
	if data['Type']=='updateteacher':
		name=data['name']
		contact=data['contact']
		addrs=data['address']
		email=data['email']
		# semail=data['semail']
		qual=data['qualification']
		# pwd=data['pwd']
		k="UPDATE `teacher` SET `name`='"+name+"',`contact`='"+contact+"',`address`='"+addrs+"',`qualification`='"+qual+"' WHERE `email`='"+email+"'"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='addteacheremail':
		temail=data['temail']
		semail=data['pemail']
		k="Select Count(*) from `teacher` WHERE `email`='"+temail+"'"
		qr = db.fetch(k)
		if qr[0][0]==1:
			return json.dumps({'Succ':'Email repeated'}),200,{'ContentType':'application/json'}
		k="INSERT INTO `teacher`( `email`) VALUES ('"+temail+"')"
		print(k)
		db.query(k)
		k="SELECT MAX(`srno`) FROM `teacher`"
		qr=db.fetch(k)
		sr=qr[0][0]
		k="SELECT `srno` FROM `principal` WHERE `email`='"+pemail+"'"
		qr=db.fetch(k)
		sr1=qr[0][0]
		k="SELECT `sid` FROM `school_principal` WHERE `pid`="+str(sr1)+" "
		qr=db.fetch(k)
		sr1=qr[0][0]
		k="INSERT INTO `school_teacher`(`sid`, `tid`) VALUES ("+str(sr1)+","+str(sr)+")"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}
	
	if data['Type']=='registerschool':
		name=data['name']
		contact=data['contact']
		addrs=data['address']
		email=data['email']
		sid=data['schoolid']
		pwd=data['pwd']
		web=data['website']
		pemail = data['pemail']
		k="INSERT INTO `school`(`name`, `address`, `schoolid`, `pwd`, `email`, `website`) VALUES ('"+name+"','"+addrs+"','"+sid+"','"+pwd+"','"+email+"','"+web+"')"
		db.query(k)
		k="SELECT MAX(`srno`) FROM `school`"
		qr=db.fetch(k)
		sr1=qr[0][0]
		k="INSERT INTO `principal`(`email`, `pwd`) VALUES ('"+pemail+"','"+pwd+"')"
		db.query(k)
		k="SELECT MAX(`srno`) FROM `principal`"
		qr=db.fetch(k)
		sr=qr[0][0]
		k="INSERT INTO `school_principal`(`sid`, `pid`) VALUES ("+str(sr1)+","+str(sr)+")"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data["Type"]=='editprincipal':
		name=data['name']
		contact=data['contact']
		addrs=data['address']
		email=data['email']
		# semail=data['semail']
		qual=data['qualification']
		# pwd=data['pwd']
		k="UPDATE `principal` SET `name`='"+name+"',`contact`='"+contact+"',`address`='"+addrs+"',`qualification`='"+qual+"' WHERE `email`='"+email+"'"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

###############					TEACHER 				#################

	if data['Type']=='fetchteacher':
		semail=data['semail']
		k="SELECT `srno`,`name` FROM `teacher` WHERE `srno` IN (SELECT `tid` FROM `school_teacher` WHERE `sid` IN (SELECT `srno` FROM `school` WHERE `email`='"+semail+"'))"
		qr=db.fetch(k)
		print(qr)
		result = []
		for i in qr:
			temp=[]
			for j in i:
				temp.append(j)
			result.append(temp)
		return json.dumps({'data':result}),200,{'ContentType':'application/json'}	

	if data['Type']=='removeteacher':
		tid=data['tid']
		k="DELETE FROM `teacher` WHERE `srno`='"+str(tid)+"'"
		print(k)	
		db.query(k)
		k="DELETE FROM `school_teacher` WHERE `tid`='"+str(tid)+"'"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data["Type"]=="editteacher":
		tid=data['tid']
		name=data['name']
		contact=data['contact']
		addrs=data['address']
		email=data['email']
		qual=data['qualification']
		# pwd=data['pwd']
		k="UPDATE `teacher` SET `name`='"+name+"',`contact`='"+contact+"',`address`='"+addrs+"',`email`='"+email+"',`qualification`='"+qual+"' WHERE `srno`="+str(tid)
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

###############					FACILITY 				#################

	if data["Type"]=="addfacility":
		facility=data['facility']
		semail=data['semail']
		k="SELECT `srno` FROM `school` WHERE `email`='"+semail+"'"
		qr=db.fetch(k)
		sr1=qr[0][0]
		k="INSERT INTO `school_facilities`(`sid`, `facility`) VALUES ("+str(sr1)+",'"+facility+"')"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data["Type"]=="removefacility":
		facility=data['facility']
		semail=data['semail']
		k="SELECT `srno` FROM `school` WHERE `email`='"+semail+"'"
		qr=db.fetch(k)
		sr1=qr[0][0]		
		k="DELETE FROM `school_facilities` WHERE `facility`='"+facility+"' and `sid`="+str(sr1)+" "
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data["Type"]=="fetchfacility":
		semail=data['semail']
		k="SELECT `srno` FROM `school` WHERE `email`='"+semail+"'"
		qr=db.fetch(k)
		sr1=qr[0][0]
		k="SELECT `facility` FROM `school_facilities` WHERE `sid`="+str(sr1)+""
		qr=db.fetch(k)
		print(qr)
		result = []
		for i in qr:
			temp=[]
			for j in i:
				temp.append(j)
			result.append(temp)

		return json.dumps({'data':result}),200,{'ContentType':'application/json'}	

###  	   CERTIFICATE           #####################
	if data['Type']=='addcerti':
		sid=data['studentid']
		tid=data['teacherid']
		c_name=data['certiname']
		typeofcer=data['type']
		rank=data['rank']
		level=data['level']
		inorg=data['certiorg']
		datec=data['certidate']
		verified=0;
		k="INSERT INTO `certificate`(`studentid`, `teacherid`, `certiname`,`certidate`,`certiorg`,`type`,`level`,`rank`,`verified`) VALUES ("+str(sid)+","+str(tid)+",'"+c_name+"',STR_TO_DATE('"+datec+"','%Y-%m-%D'),'"+inorg+"','"+typeofcer+"','"+level+"','"+rank+"',"+str(verified)+")"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	
	if data['Type']=='delete_certi':
		print("HERE")
		sid=data['student_id']
		# tid=data['teachor_id']
		c_name=data['certiname']
		k="DELETE FROM `certificate` WHERE `studentid`="+str(sid)+" AND `certiname`='"+c_name+"'"
		db.query(k)
		print(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='verifycerti':
		studentid=data['studentid']
		certiname=data['certiname']
		k="SELECT `level`, `rank` FROM `certificate` WHERE `studentid`="+str(studentid)+" AND `certiname`='"+certiname+"'"
		qr=db.fetch(k)
		level1=qr[0][0]
		rank1=qr[0][1]
	
		district=25
		school=20
		state=30
		national=35
		international=40
		points=0
		r=0
		l=0
		if level1=="district":
			l=25
		if level1=="school":
			l=20
		if level1=="state":
			l=30
		if level1=="national":
			l=35
		if level1=="international":
			l=40
		if qr[0][1]==1:
			r=35
		if qr[0][1]==2:
			r=30
		if qr[0][1]==3:
			r=25
		if qr[0][1]==4:
			r=20
		if qr[0][1]==5:
			r=15
		points=r+l

		# fetchpoints(level1,rank1)
		k="UPDATE `certificate` SET `verified`="+str(1)+" and `points`="+str(points)+" WHERE `certiname`='"+certiname+"' AND `studentid`="+str(studentid)+""

		print(k)
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json '}

	# def fetchpoints(level1,rank1):

	if data['Type']=='notverifycerti':
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"' "
		qr=db.fetch(k)
		tid=qr[0][0]
		studentid=data['studentid']
		certiname=data['certiname']
		noti_desc=studentid+":"+certiname+"  not verified"
		print(noti_desc)
		k="INSERT INTO `notification`(`tid`, `noti_des`,`seen_status`) VALUES ("+str(tid)+",'"+noti_desc+"',"+str(0)+")"
		print(k)
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	
	if data['Type']=='seennoti':
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"' "
		qr=db.fetch(k)
		tid=qr[0][0]
		k="UPDATE `notification` SET `seen_status`="+str(1)+" WHERE `tid`="+str(tid)+" "
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

################    SUBJECT ######################

	if data['Type']=='addsubject':
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"' "
		qr=db.fetch(k)
		tid=qr[0][0]
		k="SELECT  `class` FROM `teacher_class` WHERE `tid`="+str(tid)+" "
		print(k)
		qr=db.fetch(k)
		class1=qr[0][0]
		k="SELECT  `sid` FROM `school_teacher` WHERE `tid`="+str(tid)+" "
		qr=db.fetch(k)
		schoolid=qr[0][0]
		subjectname=data['subjectname']
		k="INSERT INTO `class_subject`( `class`, `schoolid`, `subject`, `year`) VALUES ("+str(class1)+","+str(schoolid)+",'"+subjectname+"',"+str(2018)+")"
		qr=db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='removesubject':
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"' "
		qr=db.fetch(k)
		tid=qr[0][0]
		k="SELECT  `class` FROM `teacher_class` WHERE `tid`="+str(tid)+" "
		print(k)
		qr=db.fetch(k)
		class1=qr[0][0]
		k="SELECT  `sid` FROM `school_teacher` WHERE `tid`="+str(tid)+" "
		qr=db.fetch(k)
		schoolid=qr[0][0]
		subjectname=data['subjectname']
		k="DELETE FROM `class_subject` WHERE `class`="+str(class1)+" AND `schoolid`="+str(schoolid)+" AND `subject`='"+subjectname+"' "
		qr=db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

###############         MARKS 				##############

	if data['Type']=='uploadmarks':
		studentid=data['studentid']
		subjectname=data['subjectname']
		marks=data['marks']
		year=data['years']
		k="SELECT `srno` FROM `class_subject` WHERE `subject`='"+subjectname+"'"
		qr=db.fetch(k)
		subjectid=qr[0][0]
		k="INSERT INTO `subject_marks` (`studentid`,`subjid`, `marks`, `year`) VALUES ("+str(studentid)+","+str(subjectid)+","+str(marks)+","+str(year)+")"
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='editmarks':
		subjectname=data['subjectname']
		marks=data['marks']
		k="SELECT `srno` FROM `class_subject` WHERE `subject`='"+subjectname+"'"
		qr=db.fetch(k)
		subjectid=qr[0][0]
		k="UPDATE `subject_marks` SET `marks`="+str(marks)+" WHERE `subjid`="+str(subjectid)+""
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='removemarks':
		subjectname=data['subjectname']
		k="SELECT `srno` FROM `class_subject` WHERE `subject`='"+subjectname+"'"
		qr=db.fetch(k)
		subjectid=qr[0][0]
		k="DELETE FROM `subject_marks` WHERE `subjid`="+str(subjectid)+""
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}
		

###############         INTERESTS 				##############

	if data["Type"]=="addinterest":
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"' "
		print(k)
		qr=db.fetch(k)
		print(qr)
		tid=qr[0][0]
		studentid=data['studentid']
		interest=data['interest']
		k="INSERT INTO `interest`( `tid`, `studentid`, `interest`) VALUES ("+str(tid)+","+str(studentid)+",'"+interest+"')"
		print(k)
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data['Type']=='removeinterest':
		studentid=data['studentid']
		interest=data['interest']
		k="DELETE FROM `interest` WHERE `studentid`="+str(studentid)+" AND `interest`='"+interest+"' "
		db.query(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}
    	
	# if data['Type']=='editinterest':
	# 	studentid=data['studentid']
	# 	interest=data['interest']
	# 	k="UPDATE `interest` SET `interest`='"+interest+"' WHERE `studentid`="+str(studentid)+" "
	# 	db.query(k)
	# 	return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}


###############         STUDENTS 				##############
	if data["Type"]=="addstudentdetails":
		adharnum=data['adharnum']
		parentincome1=data["income"]
		joiningstd=data['joiningstd']
		currentschoolid=data['currentschoolid']
		pwdstatus=data['pwdstatus']
		parent_priority=data['parent_priority']
		k="INSERT INTO `student`(`adharnum`, `parentincome`, `joiningstd`, `currentschoolid`,`pwdstatus`,`parent_priority`) VALUES ("+str(adharnum)+","+str(parentincome1)+","+str(joiningstd)+","+str(currentschoolid)+","+str(pwdstatus)+","+str(parent_priority)+")"
		qr=db.fetch(k)
		print(k)
		return json.dumps({'Succ':'True'}),200,{'ContentType':'application/json'}

	if data["Type"]=="fetchfromadhar":
		adharnum=data['adharnum']
		k="SELECT `name`, `address`, `dateofbirth`, `gender`, `contact` FROM `adhardata` WHERE `adharnum`="+str(adharnum)+" "
		qresult=db.fetch(k)
		print(k)
		datatosend=[]
		tosend={}
		for i in qresult:
			qr = {}
			qr["name"]=i[0]
			qr["address"]=i[1]
			qr["dob"]=str(i[2])
			qr["gender"]=i[3]
			qr["contact"]=i[4]
			datatosend.append(qr)
			tosend={"data":datatosend}
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

	if data['Type']=='fetchstudentdata':
		adharnum=data['adharnum']
		k="SELECT `parentincome`, `joiningstd`, `currentschoolid` ,`pwdstatus`,`parent_priority` FROM `student` WHERE `adharnum`="+str(adharnum)+""
		qresult=db.fetch(k)
		# print(k)
		datatosend=[]
		tosend={}
		for i in qresult:
			qr = {}

			qr["parentincome"]=i[0]
			qr["joiningstd"]=i[1]
			qr["currentschoolid"]=str(i[2])
			qr["pwdstatus"]=i[3]
			qr["parent_priority"]=i[4]
			datatosend.append(qr)
		k="SELECT `name`, `address`, `dateofbirth`, `gender`, `contact` FROM `adhardata` WHERE `adharnum`="+str(adharnum)+" "
		qresult=db.fetch(k)
		# print(k)
		# datatosend1=[]
		# tosend={}
		for i in qresult:
			qr = {}
			qr["name"]=i[0]
			qr["address"]=i[1]
			qr["dob"]=str(i[2])
			qr["gender"]=i[3]
			qr["contact"]=i[4]
			datatosend.append(qr)
			tosend={"data":datatosend}
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

############## fetchsubjectfromclass ########
	if data['Type']=='fetchsubjectfromclass':
		temail=data['temail']
		k="SELECT `srno` FROM `teacher` WHERE `email`='"+temail+"'"
		qr=db.fetch(k)
		tid=qr[0][0]
		k="SELECT `class` FROM `teacher_class` WHERE `tid`="+str(tid)+" "
		qr=db.fetch(k)
		tclass=qr[0][0]
		k="SELECT `srno`,`subject` FROM `class_subject` WHERE `class`="+str(tclass)+""
		qresult=db.fetch(k)
		# print(k)
		datatosend=[]
		# tosend={}
		for i in qresult:
			qr = {}
			qr["srno"]=i[0]
			qr["subject"]=i[1]
			datatosend.append(qr)
			tosend={"data":datatosend}
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

############## Educational #################0
	if data['Type']=='sports':
	# 	first=35
	# 	second=30
	# 	third=25
	# 	forth=20
	# 	fifth=15
		
	# 	district=25
	# 	school=20
	# 	state=30
	# 	national=35
		# international=40

		class1=data['class']
		
		k="SELECT `studentid` FROM `student_class` WHERE `class`="+str(class1)+" "
		qresult=db.fetch(k)
		# print(k)
		# datatosend=[]
		tosend1=[]
		# tosend={}
		for i in qresult:
			# temp = {}
			datatosend=[]
			temp = []
			
			temp["studentid"]=i[0]
			sid=i[0]
			k="SELECT SUM(`points`) FROM `certificate` WHERE `verified`=1 AND `type`= 'sports' AND `studentid`="+str(sid)+""
			qr=db.fetch(k)
			print(k)
			# points=qr[0][0]
			if qr[0][0]!=None:
				print("yay")
				temp.append(i[0])
				temp.append(int(qr[0][0]))
			# temp["points"]=qr[0][0]
				tosend1.append(temp)
			 
			# points=qr[0][0]
			temp["points"]=qr[0][0]
			datatosend.append(temp)
			tosend1.append(datatosend)
		print(tosend1)
		print(sorted(tosend1, key=lambda x: x[1], reverse=True))
		tosend={"data":tosend1}
		# 	temp["points"]=qr[0][0]
		# 	datatosend.append(temp)
		# 	tosend1.append(datatosend)
		# 	print(tosend1)

		# tosend={"data":tosend1}
		# print(tosend)
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

	if data['Type']=='extrawithcerti':
		
		class1=data['class']
		
		k="SELECT `studentid` FROM `student_class` WHERE `class`="+str(class1)+" "
		qresult=db.fetch(k)
		# print(k)
		# datatosend=[]
		tosend1=[]
		# tosend={}
		for i in qresult:
			# temp = {}
			datatosend=[]
			temp = []
			
			# temp["studentid"]=i[0]
			sid=i[0]
			k="SELECT SUM(`points`) FROM `certificate` WHERE `verified`=1 AND `type`='cultural' AND `studentid`="+str(sid)+""
			print(k)
			qr=db.fetch(k)
			if qr[0][0]!=None:
				print("yay")
				temp.append(i[0])
				temp.append(int(qr[0][0]))
			# temp["points"]=qr[0][0]
				tosend1.append(temp)
			 
			# points=qr[0][0]
			temp["points"]=qr[0][0]
			datatosend.append(temp)
			tosend1.append(datatosend)
		print(tosend1)
		print(sorted(tosend1, key=lambda x: x[1], reverse=True))
		tosend={"data":tosend1}
		# tosend={"data":tosend1}
		# print(tosend) 
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

##############  PWD  ##################
	
	if data['Type']=='fetchpwdscholars':
		k="SELECT `student_id` FROM `student` WHERE `pwdstatus`=1 "
		qresult=db.fetch(k)
		tosend1=[]
		print(qresult)
		for i in qresult:
			datatosend=[]
			temp = []
			k="SELECT SUM(`points`) FROM `certificate` WHERE `verified`=1 AND `studentid`="+str(i[0])+""
			qr=db.fetch(k)
			# points=qr[0][0]
			print("qr",qr)
			if qr[0][0]!=None:
				print("yay")
				temp.append(i[0])
				temp.append(int(qr[0][0]))
			# temp["points"]=qr[0][0]
				tosend1.append(temp)

			# tosend1.append(datatosend)

		print(tosend1)
		print(sorted(tosend1, key=lambda x: x[1], reverse=True))
		tosend={"data":tosend1}
		# print(tosend)
		return json.dumps(tosend), 200, {'ContentType':'application/json'}

		# print(k)
		# qr=db.fetch(k)
		
		
	if data['Type']=='changeoverallranks':
		print(data)
		kk="SELECT `srno` FROM `school` WHERE 1"
		print(kk)
		qr = db.fetch(kk)
		print(qr)
		for i in qr:
			kk = "SELECT `marks` FROM `subject_marks` WHERE `subjid` IN (SELECT `srno` FROM `class_subject` WHERE `schoolid`="+str(i[0])+")"
			# print(kk)
			qr1 = db.fetch(kk)
			if len(qr1)>0:
				d=[]
				for j in qr1:
					d.append(j[0])
				print(d)
				datasend=[]
				tosend1=[]
				
				kk = "SELECT `rank`,`studentid` FROM `student_class` WHERE `schoolid`="+str(i[0])
				print(kk)
				qr2 = db.fetch(kk)
				
				print(qr2)
				
				
				# data = [24,56,23,65,78,56,87,11,23,34]
				for k in qr2:
					print(str(k[0]))
					print("stdev",statistics.stdev(d))
					print(sum(d) / float(len(d)))
					std1 = statistics.stdev(d)
					mean = sum(d) / float(len(d))
					# print((float(str(k[0]))-mean)/std1)
					ans = (float(str(k[0]))-mean)/std1
					# print()
					kk="UPDATE `student_class` SET `overall_rank`="+str(ans)+" WHERE `studentid`="+str(k[1])+" AND `year`=2018"
					datasend.append(qr2[0][1])
					
					datasend.append(ans)
					tosend1.append(datasend)
				# print(sorted(tosend1, key=lambda x: x[1], reverse=True))
				tosend={"data":tosend1}
				# print(tosend)
					# db.query(kk) 
		return json.dumps({'Succ':ret}), 200, {'ContentType':'application/json'}

	if data['Type']=='changeoverallranks1':
		print(data)
		kk="SELECT `srno` FROM `school` WHERE 1"
		print(kk)
		qr = db.fetch(kk)
		print(qr)
		for i in qr:
			kk = "SELECT `marks` FROM `subject_marks` WHERE `subjid` IN (SELECT `srno` FROM `class_subject` WHERE `schoolid`="+str(i[0])+")"
			# print(kk)
			qr1 = db.fetch(kk)
			if len(qr1)>0:
				d=[]
				for j in qr1:
					d.append(j[0])
				print(d)
				datasend=[]
				tosend1=[]
				
				kk = "SELECT `rank`,`studentid` FROM `student_class` WHERE `schoolid`="+str(i[0])
				print(kk)
				qr2 = db.fetch(kk)
				
				print(qr2)
				
				
				# data = [24,56,23,65,78,56,87,11,23,34]
				for k in qr2:
					print(str(k[0]))
					print("stdev",statistics.stdev(d))
					print(sum(d) / float(len(d)))
					std1 = statistics.stdev(d)
					mean = sum(d) / float(len(d))
					# print((float(str(k[0]))-mean)/std1)
					ans = (float(str(k[0]))-mean)/std1
					# print()
					kk="UPDATE `student_class` SET `overall_rank`="+str(ans)+" WHERE `studentid`="+str(k[1])+" AND `year`=2018"
					datasend.append(qr2[0][1])
					
					datasend.append(ans)
					tosend1.append(datasend)
				# print(sorted(tosend1, key=lambda x: x[1], reverse=True))
				tosend={"data":tosend1}
				# print(tosend)
					# db.query(kk) 
		return json.dumps({'Succ':ret}), 200, {'ContentType':'application/json'}

	# if data['Type']=='sportsandacademics':
	# 	k="SELECT `overall_rank` FROM `student_class`"
	# 	qr=db.fetch(k)
	# 	academicrank=

if __name__=='__main__':
	app.run(host='0.0.0.0',port=7824,debug=True)
 
