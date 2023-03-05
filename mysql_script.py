#When only IP is selected
check_art_enrolled_date = "SELECT * FROM `linelist` WHERE `ARTStartDate` < `Date_Enrolled` AND (`TI` IS NULL OR `TI`='')" #Check client who started ART before enrolment and not TI
check_art_lastpickup = "SELECT * FROM `linelist` WHERE `ARTStartDate` > `LastPickupDate`" #check last drug pickup before ART Start
check_art_start_date = "SELECT * FROM `linelist` WHERE `ARTStartDate` IS NULL OR `ARTStartDate`=''" #Client with no ART start date
check_pickup_after_discon = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `CurrentARTStatus_28Days` = 'Active' AND (`Reason_for_Termination` != 'Returned to Care' OR `Reason_for_Termination` IS NULL)" #Pickup after discontinuation
check_pickup_after_death = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `Reason_for_Termination` = 'Death'"
check_incomplete_discon = "SELECT * FROM `linelist` WHERE (`CurrentARTStatus_28Days` != 'Active' AND `CurrentARTStatus_28Days` != 'in-Active') AND (`Reason_for_Termination` IS NULL OR `Reason_for_Termination`='')"

#When IP and State are selected
check_art_enrolled_date_ip_state = "SELECT * FROM `linelist` WHERE `ARTStartDate` < `Date_Enrolled` AND (`TI` IS NULL OR `TI`='') AND `IP`=%s AND `State`=%s" #Check client who started ART before enrolment and not TI
check_art_lastpickup_ip_state = "SELECT * FROM `linelist` WHERE `ARTStartDate` > `LastPickupDate` AND `IP`=%s AND `State`=%s" #check last drug pickup before ART Start
check_art_start_date_ip_state = "SELECT * FROM `linelist` WHERE (`ARTStartDate` IS NULL OR `ARTStartDate`='') AND `IP`=%s AND `State`=%s" #Client with no ART start date
check_pickup_after_discon_ip_state = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `CurrentARTStatus_28Days` = 'Active' AND (`Reason_for_Termination` != 'Returned to Care' OR `Reason_for_Termination` IS NULL) AND `IP`=%s AND `State`=%s" #Pickup after discontinuation
check_pickup_after_death_ip_state = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `Reason_for_Termination` = 'Death' AND `IP`=%s AND `State`=%s"
check_incomplete_discon_ip_state = "SELECT * FROM `linelist` WHERE (`CurrentARTStatus_28Days` != 'Active' AND `CurrentARTStatus_28Days` != 'in-Active') AND (`Reason_for_Termination` IS NULL OR `Reason_for_Termination`='') AND `IP`=%s AND `State`=%s"

#When IP, State and Surge Command are selected
check_art_enrolled_date_ip_state_surg = "SELECT * FROM `linelist` WHERE `ARTStartDate` < `Date_Enrolled` AND (`TI` IS NULL OR `TI`='') AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s" #Check client who started ART before enrolment and not TI
check_art_lastpickup_ip_state_surg = "SELECT * FROM `linelist` WHERE `ARTStartDate` > `LastPickupDate` AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s" #check last drug pickup before ART Start
check_art_start_date_ip_state_surg = "SELECT * FROM `linelist` WHERE (`ARTStartDate` IS NULL OR `ARTStartDate`='') AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s" #Client with no ART start date
check_pickup_after_discon_ip_state_surg = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `CurrentARTStatus_28Days` = 'Active' AND (`Reason_for_Termination` != 'Returned to Care' OR `Reason_for_Termination` IS NULL) AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s" #Pickup after discontinuation
check_pickup_after_death_ip_state_surg = "SELECT * FROM `linelist` WHERE `LastPickupDate` > `Date_of_Termination` AND `Reason_for_Termination` = 'Death' AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s"
check_incomplete_discon_ip_state_surg = "SELECT * FROM `linelist` WHERE (`CurrentARTStatus_28Days` != 'Active' AND `CurrentARTStatus_28Days` != 'in-Active') AND (`Reason_for_Termination` IS NULL OR `Reason_for_Termination`='') AND `IP`=%s AND `State`=%s AND `SurgeCommand`=%s"





# Fetch list based on select parameter
select_all_merge_tx_0 = "SELECT * FROM `linelist`"
select_all_merge_tx_1 = "SELECT * FROM `linelist` WHERE `IP`=%s AND `State`=%s"
select_all_merge_tx_2 = "SELECT * FROM `linelist` WHERE `IP`=%s AND `State`=%s AND `SurgeCommand`=%s"
select_all_merge_tx_3 = "SELECT * FROM `linelist` WHERE `IP`=%s AND `State`=%s AND `SurgeCommand`=%s AND `LGA`=%s"

select_all_merge_hts_linelist = "SELECT * FROM `hts_linelist`"
select_all_merge_full_pharmacy_complement = "SELECT * FROM `full_pharmacy_complement`"
select_all_merge_pmtct_linelist = "SELECT * FROM `pmtct_linelist`"
select_all_merge_eid_linelist = "SELECT * FROM `eid_linelist`"
select_all_merge_ahd_linelist = "SELECT * FROM `ahd_linelist`"
select_all_merge_lims_emr_daily_report = "SELECT * FROM `lims_emr_daily_report`"
select_all_merge_last_5_pharmacy = "SELECT * FROM `last_5_pharmacy`"
select_all_merge_otz_linelist = "SELECT * FROM `otz_linelist`"


'''
check_date_ip = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{merge_linelist.val_date2}%'"
check_date_state = f"SELECT * FROM `linelist` WHERE `Date_List_Gen` not like '{merge_linelist.val_date2}%' AND " \
                   f"`state` = '{merge_linelist.state_}' "
'''
'''
elif check_which_list == 'HTS Line List':
df = pd.read_sql(mysql_script.select_all_merge_hts_linelist, mydb)
elif check_which_list == 'Full Pharmacy Complement':
df = pd.read_sql(mysql_script.select_all_merge_full_pharmacy_complement, mydb)
elif check_which_list == 'PMTCT Line List':
df = pd.read_sql(mysql_script.select_all_merge_pmtct_linelist, mydb)
elif check_which_list == 'EID Line List':
df = pd.read_sql(mysql_script.select_all_merge_eid_linelist, mydb)
elif check_which_list == 'AHD Line List':
df = pd.read_sql(mysql_script.select_all_merge_ahd_linelist, mydb)
elif check_which_list == 'LIMS_EMR Daily Report':
df = pd.read_sql(mysql_script.select_all_merge_lims_emr_daily_report, mydb)
elif check_which_list == 'Last 5 Pharmacy':
df = pd.read_sql(mysql_script.select_all_merge_last_5_pharmacy, mydb)
elif check_which_list == 'OTZ Line List':
df = pd.read_sql(mysql_script.select_all_merge_otz_linelist, mydb)
'''

