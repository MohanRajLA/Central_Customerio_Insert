class Ethnicity(object):
    def __init__(self):
        self.Chinese = 1
        self.Malay = 2
        self.Indonesian = 3
        self.Myanmar = 4
        self.Punjabi = 5
        self.Indian = 6
        self.Eurasian = 7
        self.Caucasian = 8
        self.Korean = 9
        self.German = 10
        self.Thai = 11
        self.Japanese = 12
        self.Filipino = 13
        self.Mixed = 14
        self.Other = 15

class Product(object):
    def __init__(self):
        self.Lunch_Actually=1
        self.Lunch_Actually_Academy=2
        self.Esynchrony=3


class Highest_Education(object):
    def __init__(self):
        self.Junior_College_and_Below = 1
        self.Polytechnic = 2
        self.Basic_Degree = 3
        self.Professional_Qualification = 4
        self.Masters = 5
        self.PhD_and_above = 6
        self.Advanced_Diploma = 7
        self.Diploma = 8
        self.A_levels_and_Below = 9
        self.Certificate = 10

class Income(object):
    def __init__(self):
        self.SGD35k_and_below = 1
        self.SGD36k_to_50k = 2
        self.SGD51K_TO_75K = 3
        self.SGD76K_TO_150K = 4
        self.SGD151K_TO_300K = 5
        self.SGD301K_AND_ABOVE = 6
        self.RMKL15K_AND_BELOW = 7
        self.RMKL16K_TO_20K = 8
        self.RMKL21K_TO_45K = 9
        self.RMKL46K_TO_75K = 10
        self.RMKL76K_TO_150K = 11
        self.RMKL151K_TO_300K = 12
        self.RMKL301K_AND_ABOVE = 13
        self.RMPG15K_AND_BELOW = 14
        self.RMPG16K_TO_20K = 15
        self.RMPG21K_TO_45K = 16
        self.RMPG46K_TO_75K = 17
        self.RMPG76K_TO_150K = 18
        self.RMPG151K_TO_300K = 19
        self.RMPG301K_AND_ABOVE = 20
        self.HKD180K_AND_BELOW = 21
        self.HKD190K_TO_300K = 22
        self.HKD310K_TO_400K = 23
        self.HKD410K_TO_500K = 24
        self.HKD510K_TO_600K = 25
        self.HKD610K_TO_800K = 26
        self.HKD810K_AND_ABOVE = 27
        self.IDR71M_AND_BELOW = 28
        self.IDR72M_TO_95M = 29
        self.IDR96M_TO_143M = 30
        self.IDR144M_TO_240M = 31
        self.IDR241M_TO_480M = 32
        self.IDR481M_TO_500M = 33
        self.IDR501M_AND_ABOVE = 34
        self.THB420K_AND_BELOW = 35
        self.THB430K_TO_600K = 36
        self.THB610K_TO_900K = 37
        self.THB910K_TO_1200K = 38
        self.THB1210K_TO_1800K = 39
        self.THB1810K_TO_3600K = 40
        self.THB3610K_AND_ABOVE = 41

class Gender(object):
    def __init__(self):
        self.Male = 1
        self.Female = 2
        self.Both = 3



class JobLevel(object):
    def __init__(self):
        self.Part_timer = 1
        self.Others = 2
        self.Professionals = 3
        self.Executive = 4
        self.Senior_Executive = 5
        self.Assistant_Manager = 6
        self.Manager = 7
        self.Senior_Manager = 8
        self.Director = 9
        self.C_Level_CEO_COO_CFO_CTO_CIO_etc = 10
        self.Entrepreneurs = 11

class Industry(object):
    def __init__(self):
        self.Computer_related = 1
        self.Builder = 2
        self.Engineering = 3
        self.Government = 4
        self.Legal = 5
        self.Other = 6
        self.Advertising = 7
        self.Entertainment = 8
        self.Media = 9
        self.Education = 10
        self.Real_Estate = 11
        self.Accounting_or_Finance = 12
        self.Hospitality = 13
        self.Air_Travel = 14
        self.Shipping = 15
        self.Health_Care = 16
        self.Arts = 17
        self.Banking_and_Financial = 18
        self.Non_Profit_and_Community = 19
        self.Law_Enforcement_and_Security = 20
        self.Marketing = 21
        self.Biotech_and_Pharmaceutical = 22
        self.Manufacturing = 23
        self.Customer_Service = 24
        self.Publishing = 25
        self.Consulting = 26
        self.Transportation = 27
        self.Telecommunication = 28
        self.Food_and_Beverages = 29

class LeadStatus(object):
    def __init__(self):
        self.Not_Interested=5
        self.Followup=8

class Reason(object):
    def __init__(self):
        self.Too_expensive_or_No_budget=14
        self.Client_have_other_commitments=15
        self.Not_ready_to_enrol_in_dating_service=16
        self.Waiting_for_credit_card_application_to_enjoy_installment_plan=17
        self.Not_an_impulse_buyer=18
        self.Wants_to_compare_with_other_dating_agencies=19
        self.Need_to_go_back_to_discuss_with_parents_or_friends=20
        self.Does_not_see_the_service_value_or_not_convincing_enough=21
        self.Wants_to_see_more_testimonial=22
        self.NA=23

class AppointmentSatus(object):
    def __init__(self):
        self.To_Be_Confirmed=1
        self.Appointment_Confirmed=2
        self.Client_Turned_Up=3
        self.Rescheduled=4
        self.Rescheduled_ByUs=5
        self.Client_Did_Not_Turn_Up=6
        self.Cancelled=7
        self.Cancelled_ByUs=8

class AppointmentSalesResult(object):
    def __init__(self):
        self.Successful=1
        self.Unsuccessful=2
        self.Not_Suitable=3
        self.Nonsales=4
        self.Sold_Addon_Only=5
        self.Pending=6

class FollowupType(object):
    def __init__(self):
        self.Sales=1
        self.Document=2
        self.Member=3
        self.Match=4
        self.Date=5
        self.Coaching=6
        self.Feedback=7
        self.Renewal=8

class FollowupPurpose(object):
    def __init__(self):
        self.Sell=1
        self.Confirm_Appointment=2
        self.Ask_for_Appointment_Feedback=3


class FollowupResult(object):
    def __init__(self):
        self.Did_not_pick_up=1
        self.Not_Interested=2
        self.Unsuitable=3
        self.SPAM=4
        self.Follow_Up=5
        self.Made_Appointment=6

class FollowupDone(object):
    def __init__(self):
        self.False=0
        self.True=1

class QueryType(object):
    def __init__(self):
        self.lc_cross_sell=1
        self.esync_lc_cross_sell=2
        self.la_esync_cross_sell=3
        self.laa_esync_cross_sell=4
        self.la_new_query=5
        self.laa_la_cross_sell=6
        self.esync_la_cross_sell=7
        self.la_laa_cross_sell=8
        self.events_sign_up=9
        self.la_membership_renewal=10
        self.laa_events_cross_sell=11
        self.laa_date_coaching_session=12
        self.la_available_cross_sell=13
        self.laa_image_coaching_session=14
        self.la_profile_review=15
        self.la_unsuccessful_appt=16
        self.laa_new_query=17
        self.la_other=18
        self.la_esync_promo_la_free_date=19
        self.esync_new_query=20
        self.grp_hiring_interview=21
        self.la_events_cross_sell=22
        self.laa_irfl_workshop=23
        self.laa_image_workshop=24
        self.la_setipe_cross_sell=25
        self.laa_bundle_coaching_session=26
        self.laa_lc_cross_sell=27
        self.esync_laa_cross_sell=28
        self.la_sweet_ring_cross_sell=29






