from customerio_enum import *
from datetime import datetime

# API call request to customer.io website for profile
def customerIOProfileAPICall(querystmt, cio):
    try:
        for v in querystmt:
            id=v[0]
            full_name=v[7]
            full_name=str(full_name).decode('utf-8','ignore')
            email=v[14]
            created_at=datetime.now()
            age=v[3]
            birth_month=v[4]
            first_name=v[11]
            first_name=str(first_name).decode('utf-8', 'ignore')
            preferred_name=v[8]
            branch_name=v[1]
            if str(branch_name) == "":
                branch_name="No Branch"
            else:
                branch_name=branch_name
            highest_educationtemp=v[5]
            highesteducationim=Highest_Education()
            for attr, value in highesteducationim.__dict__.iteritems():
                if str(highest_educationtemp) == "":
                    highest_education="NA"
                elif highest_educationtemp is None:
                    highest_education=highest_educationtemp
                elif int(highest_educationtemp) == value:
                    highest_education=attr


            producttemp=v[2]
            productim=Product()
            for attr, value in productim.__dict__.iteritems():
                if str(producttemp) == "":
                    product="NA"
                elif producttemp is None:
                    product=producttemp
                elif int(producttemp) == value:
                    product=attr

            ethnicitytemp=v[6]
            ethnicityim=Ethnicity()
            for attr, value in ethnicityim.__dict__.iteritems():
                if str(ethnicitytemp) == "":
                    ethnicity="NA"
                elif ethnicitytemp is None:
                    ethnicity=ethnicitytemp
                elif int(ethnicitytemp) == value:
                    ethnicity=attr

            gendertemp=v[9]
            genderim=Gender()
            for attr, value in genderim.__dict__.iteritems():
                if str(gendertemp) == "":
                    gender="NA"
                elif gendertemp is None:
                    gender=gendertemp
                elif int(gendertemp) == value:
                    gender=attr

            incometemp=v[10]
            incomeim=Income()
            for attr, value in incomeim.__dict__.iteritems():
                if str(incometemp) == "":
                    income="NA"
                elif incometemp is None:
                    income=incometemp
                elif int(incometemp) == value:
                    income=attr

            job_leveltemp=v[12]
            joblevelim=JobLevel()
            for attr, value in joblevelim.__dict__.iteritems():
                if str(job_leveltemp) == "":
                    job_level="NA"
                elif job_leveltemp is None:
                    job_level=job_leveltemp
                elif int(job_leveltemp) == value:
                    job_level=attr


            industrytemp=v[13]
            industryim=Industry()
            for attr, value in industryim.__dict__.iteritems():
                if str(industrytemp) == "":
                    industry="NA"
                elif industrytemp is None:
                    industry=industrytemp
                elif int(industrytemp) == value:
                    industry=attr

            try:
                cio.identify(id=id,email=email,created_at=created_at,age=age,birth_month=birth_month,gender=gender,branch_name=branch_name,full_name=full_name,Preffered_name=preferred_name,first_name=first_name,Ethnicity=ethnicity,Highest_education=highest_education,Income=income,industry_name=industry,job_levels=job_level,product=product)
            except:
                pass
    except:
        pass


def customerIOProfileProductLeadAPICall(queryprofileproductleadStmt, cio):
    try:
        for m in queryprofileproductleadStmt:
            id=m[0]
            lead_create_date=m[2]
            hearusfrom=m[3]

            query_typetemp=m[4]
            query_typeim=QueryType()
            for attr, value in query_typeim.__dict__.iteritems():
                if (str(query_typetemp)) == "":
                    query_type="NA"
                elif query_typetemp is None:
                    query_type=query_typetemp
                elif int(query_typetemp) == value:
                    query_type=attr

            lead_statustemp=m[1]
            lead_statusim=LeadStatus()
            for attr, value in lead_statusim.__dict__.iteritems():
                if (str(lead_statustemp)) == "":
                    lead_status="NA"
                elif lead_statustemp is None:
                    lead_status=lead_statustemp
                elif int(lead_statustemp) == value:
                    lead_status=attr

            reasontemp=m[5]
            reasonim=Reason()
            for attr, value in reasonim.__dict__.iteritems():
                if (str(reasontemp)) == "":
                    reason="NA"
                elif reasontemp is None:
                    reason=reasontemp
                elif int(reasontemp) == value:
                    reason=attr

            try:
                cio.identify(id=id, lead_status=lead_status, lead_create_date=lead_create_date,
                                     hearusfrom=hearusfrom, reason=reason, query_type=query_type)
            except:
                pass
    except:
        pass



def customerIOAppointmentAPICall(queryapptStmt, cio):
    try:
        for i in queryapptStmt:
            id=i[0]
            appointment_date=i[1]
            if (str(appointment_date)) == "" or appointment_date is None:
                appointment_date="No Appointment"

            sales_associtae=i[3]

            appointment_statustemp=i[2]
            appointment_statusim=AppointmentSatus()
            for attr, value in appointment_statusim.__dict__.iteritems():
                if (str(appointment_statustemp)) == "":
                    appointment_status="NA"
                elif appointment_statustemp is None:
                    appointment_status=appointment_statustemp
                elif int(appointment_statustemp) == value:
                    appointment_status=attr

            appointment_sales_resulttemp=i[4]
            appointment_sales_resultim=AppointmentSalesResult()
            for attr, value in appointment_sales_resultim.__dict__.iteritems():
                if (str(appointment_sales_resulttemp)) == "":
                    appointment_sales_result="NA"
                elif appointment_sales_resulttemp is None:
                    appointment_sales_result=appointment_sales_resulttemp
                elif int(appointment_sales_resulttemp) == value:
                    appointment_sales_result=attr

            try:
                cio.identify(id=id, appointment_date=appointment_date, sales_associate=sales_associtae,
                                         appointment_status=appointment_status,
                                         appointment_sales_result=appointment_sales_result)
            except:
                pass
    except:
        pass



def customerIOFollowupAPICall(queryfollowupStmt, cio):
    try:
        for m in queryfollowupStmt:
            id=m[0]
            callback_todo_date=m[1]
            contacted_by=m[6]
            callback_done_date=m[4]

            followup_typetemp=m[2]
            followup_typeim=FollowupType()
            for attr, value in followup_typeim.__dict__.iteritems():
                if (str(followup_typetemp)) == "NA":
                    followup_type=""
                elif followup_typetemp is None:
                    followup_type=followup_typetemp
                elif int(followup_typetemp) == value:
                    followup_type=attr

            followup_purposetemp=m[3]
            followup_purposeim=FollowupPurpose()
            for attr, value in followup_purposeim.__dict__.iteritems():
                if (str(followup_purposetemp)) == "NA":
                    followup_purpose=""
                elif followup_purposetemp is None:
                    followup_purpose=followup_purposetemp
                elif int(followup_purposetemp) == value:
                    followup_purpose=attr

            followup_resulttemp=m[5]
            followup_resultim=FollowupResult()
            for attr, value in followup_resultim.__dict__.iteritems():
                if (str(followup_resulttemp)) == "NA":
                    followup_result=""
                elif followup_resulttemp is None:
                    followup_result=followup_resulttemp
                elif int(followup_resulttemp) == value:
                    followup_result=attr

            try:
                cio.identify(id=id, callback_todo_date=callback_todo_date, followup_type=followup_type,
                                     callback_done_date=callback_done_date, contacted_by=contacted_by,
                                         followup_purpose=followup_purpose, followup_result=followup_result)
            except:
                pass
    except:
        pass
