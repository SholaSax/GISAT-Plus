create_table_linelist = ("CREATE TABLE IF NOT EXISTS linelist (`IP` varchar(255) DEFAULT NULL, \
  `State` varchar(255) DEFAULT NULL, \
  `SurgeCommand` varchar(255) DEFAULT NULL, \
  `LGA` varchar(255) DEFAULT NULL, \
  `FacilityName` varchar(255) DEFAULT NULL, \
  `Pepid_datim` varchar(30) PRIMARY KEY, \
  `patient_id` double DEFAULT NULL, \
  `Pepid` varchar(255) NOT NULL, \
  `HospitalNo` varchar(255) DEFAULT NULL, \
  `Sex` varchar(255) DEFAULT NULL, \
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL, \
  `AgeAtStartofART` double DEFAULT NULL, \
  `AgeAtStart_InMonth` double DEFAULT NULL, \
`CurrentAge` double DEFAULT NULL, \
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL, \
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL, \
`NextAppmt` timestamp(6) NULL DEFAULT NULL, \
  `DaysOfARVRefill` double DEFAULT NULL, \
  `RegLineAtStart` varchar(255) DEFAULT NULL, \
  `ARTRegAtStart` varchar(255) DEFAULT NULL, \
  `CurrentRegLine` varchar(255) DEFAULT NULL, \
  `CurrentARTReg` varchar(255) DEFAULT NULL, \
  `PregStatus` varchar(255) DEFAULT NULL, \
  `CurrentVL` double DEFAULT NULL, \
  `DateOfCurrentVL` timestamp(6) NULL DEFAULT NULL, \
  `ViralLoadIndication` varchar(255) DEFAULT NULL, \
  `Date_Result_Received` timestamp(6) NULL DEFAULT NULL, \
  `Last_VL_Sample_Date` timestamp(6) NULL DEFAULT NULL, \
  `Initial_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `initial_CD4` double DEFAULT NULL, \
  `Last_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_CD4` double DEFAULT NULL, \
  `CurrentARTStatus_28Days` varchar(255) DEFAULT NULL, \
  `DaysInterval` double DEFAULT NULL, \
  `TI` varchar(255) DEFAULT NULL, \
  `DOB` timestamp(6) NULL DEFAULT NULL, \
  `Surname` varchar(255) DEFAULT NULL, \
  `FirstName` varchar(255) DEFAULT NULL, \
  `Phone_No` double DEFAULT NULL, \
  `Address` varchar(255) DEFAULT NULL, \
  `Pill_Balance` double DEFAULT NULL, \
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL, \
  `DATIMCode` varchar(255) DEFAULT NULL, \
  `MonthOnART` double DEFAULT NULL, \
  `Last_Weight` double DEFAULT NULL, \
  `Last_Weight_Date` timestamp(6) NULL DEFAULT NULL, \
  `Biometrics_Captured` timestamp(6) NULL DEFAULT NULL, \
  `Eligible_For_IPT` varchar(255) DEFAULT NULL, \
  `Date_IPT_start` timestamp(6) NULL DEFAULT NULL, \
  `Outcome_of_IPT` varchar(255) DEFAULT NULL, \
  `Date_of_Outcome` timestamp(6) NULL DEFAULT NULL, \
  `Last_Clinic_Visit_Date` timestamp(6) NULL DEFAULT NULL, \
  `Systolic_BP` double DEFAULT NULL, \
  `Diastolic_BP` double DEFAULT NULL, \
  `Next_Clinical_Appt_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Status` varchar(255) DEFAULT NULL, \
  `TB_Investigations` varchar(255) DEFAULT NULL, \
  `Investig_Result` varchar(255) DEFAULT NULL, \
  `Date_TB_Investig` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Tracking` varchar(255) DEFAULT NULL, \
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Defaulting1` varchar(255) DEFAULT NULL, \
  `Reason_for_Termination` varchar(255) DEFAULT NULL, \
  `Date_of_Termination` timestamp(6) NULL DEFAULT NULL, \
`Facility_Transferred_To` varchar(255) DEFAULT NULL, \
  `Last_EAC_Session_Date` timestamp(6) NULL DEFAULT NULL, \
  `EAC_Session_Type` varchar(255) DEFAULT NULL, \
  `EAC_ARV_Plan` varchar(255) DEFAULT NULL, \
  `Date_VL_Before_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_Before_EAC` double DEFAULT NULL, \
  `Date_VL_After_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_After_EAC` double DEFAULT NULL, \
  `List_Parameters` varchar(255) DEFAULT NULL, \
  `Date_List_Gen` timestamp(6) NULL DEFAULT NULL)")

create_ahd_linelist = ("CREATE TABLE IF NOT EXISTS `ahd_linelist` ( \
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(30) PRIMARY KEY,\
  `Pepid` varchar(255) NOT NULL,\
  `person_id` double DEFAULT NULL,\
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL,\
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL,\
  `Sample_Collection_Date` timestamp(6) NULL DEFAULT NULL,\
  `Indication_for_AHD` varchar(255) DEFAULT NULL,\
  `CD4_LFA_Result` varchar(255) DEFAULT NULL,\
  `TB_LF_LAM_Result` varchar(255) DEFAULT NULL,\
  `Date_TB_LF_LAM_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `Serology_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_Serology_For_CrAg_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `CSF_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_CSF_For_CrAg_Result_Received` varchar(255) DEFAULT NULL,\
  `ICE_WHO_Staging` varchar(255) DEFAULT NULL)")

create_eid_linelist = ("CREATE TABLE IF NOT EXISTS `eid_linelist` (\
`IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `HEI_Number_datim` varchar(30) PRIMARY KEY,\
  `HEI_Number` varchar(255) NOT NULL,\
  `ChildRegistrationDate` varchar(255) DEFAULT NULL,\
  `Surname` varchar(255) DEFAULT NULL,\
  `FirstName` varchar(255) DEFAULT NULL,\
  `DOB` timestamp(6) NULL DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `PhoneNumber` varchar(255) DEFAULT NULL,\
  `WeightAtBirth` varchar(255) DEFAULT NULL,\
  `lengthAtBirth` varchar(255) DEFAULT NULL,\
  `HeadCircumferenceAtBirth` varchar(255) DEFAULT NULL,\
  `ChildMUACAtBirth` varchar(255) DEFAULT NULL,\
  `APGAR_ScoreAtBirth` varchar(255) DEFAULT NULL,\
  `ChildGivenHepatitisB_Immunoglobulin` varchar(255) DEFAULT NULL,\
  `HighRiskHIVExposedInfant` varchar(255) DEFAULT NULL,\
  `ARVProphylaxis` varchar(255) DEFAULT NULL,\
  `TimingOfARVProphylaxis` varchar(255) DEFAULT NULL,\
  `ImmunizationReceivedAtBirth` varchar(255) DEFAULT NULL,\
  `FollowUpDate` varchar(255) DEFAULT NULL,\
  `TimingOfMotherARTInitiation` varchar(255) DEFAULT NULL,\
  `WeightAtFollowUP` varchar(255) DEFAULT NULL,\
  `lengthAtFollowUp` varchar(255) DEFAULT NULL,\
  `HeadCircumferenceAtFollowUp` varchar(255) DEFAULT NULL,\
  `MID_UpperARM_CircumferenceAtFollowUp` varchar(255) DEFAULT NULL,\
  `ChildMUACAtFollowUp` varchar(255) DEFAULT NULL,\
  `BMI_MUACAtFollowUp` varchar(255) DEFAULT NULL,\
  `CTX_GivenToChild` varchar(255) DEFAULT NULL,\
  `InfantFeedingMethod` varchar(255) DEFAULT NULL,\
  `PCR_Type` varchar(255) DEFAULT NULL,\
  `SampleCollectionDate` timestamp(6) NULL DEFAULT NULL,\
  `DateSampleSent` timestamp(6) NULL DEFAULT NULL,\
  `DateResultReceivedAtFacility` timestamp(6) NULL DEFAULT NULL,\
  `DateCaregiverWasGivenPCRResult` timestamp(6) NULL DEFAULT NULL,\
  `PCR_Result` varchar(255) DEFAULT NULL,\
  `RapidTestType` varchar(255) DEFAULT NULL,\
  `RapidTestDate` varchar(255) DEFAULT NULL,\
  `RapidTestResult` varchar(255) DEFAULT NULL,\
  `Outcome_At_18Month` varchar(255) DEFAULT NULL,\
  `ARTStartDate_IfPositive` varchar(255) DEFAULT NULL)")

create_hts_linelist = ("CREATE TABLE IF NOT EXISTS `hts_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `City` varchar(255) DEFAULT NULL,\
  `Datim_Code` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Datim_HTS_ClientCode` varchar(30) PRIMARY KEY,\
  `HTS_ClientCode` varchar(255) NOT NULL,\
  `PEPFAR_Number_IfOnART` varchar(255) DEFAULT NULL,\
  `birthdate` timestamp(6) NULL DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(255) DEFAULT NULL,\
  `family_name` varchar(255) DEFAULT NULL,\
  `PhoneNumber` varchar(255) DEFAULT NULL,\
  `VisitDate` varchar(255) DEFAULT NULL,\
  `Test_VisitDate_Validation` varchar(255) DEFAULT NULL,\
  `KindOfHTS` varchar(255) DEFAULT NULL,\
  `setting` varchar(255) DEFAULT NULL,\
  `FirstTimeVisit` varchar(255) DEFAULT NULL,\
  `TypeOfSession` varchar(255) DEFAULT NULL,\
  `ReferredFrom` varchar(255) DEFAULT NULL,\
  `MaritalStatus` varchar(255) DEFAULT NULL,\
  `FromIndex` varchar(255) DEFAULT NULL,\
  `IndexClientID_Validation` varchar(255) DEFAULT NULL,\
  `IndexClientID` varchar(255) DEFAULT NULL,\
  `IndexType` varchar(255) DEFAULT NULL,\
  `IndexClientName` varchar(255) DEFAULT NULL,\
  `HIVScreeningTest` varchar(255) DEFAULT NULL,\
  `HIVScreeningTestDate` varchar(255) DEFAULT NULL,\
  `HIVConfirmatoryTest` varchar(255) DEFAULT NULL,\
  `HIVConfirmatoryTestDate` varchar(255) DEFAULT NULL,\
  `HIV_FinalResult` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI?` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI_Validation` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestName` varchar(255) DEFAULT NULL,\
  `VerifyRecencyNumber` varchar(255) DEFAULT NULL,\
  `ControlLine` varchar(255) DEFAULT NULL,\
  `VerificationLine` varchar(255) DEFAULT NULL,\
  `LongTermLine` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestDate` varchar(255) DEFAULT NULL,\
  `RecencyInterpretation` varchar(255) DEFAULT NULL,\
  `ViralLoadRequest` varchar(255) DEFAULT NULL,\
  `VLSampleCollectionDate` varchar(255) DEFAULT NULL,\
  `PCR_LabNo` varchar(255) DEFAULT NULL,\
  `SampleType` varchar(255) DEFAULT NULL,\
  `PCR_Laboratory` varchar(255) DEFAULT NULL,\
  `HIV_ViralLoad` varchar(255) DEFAULT NULL,\
  `FinalHIVRecencyResult` varchar(255) DEFAULT NULL,\
  `NoOfPatnerElicited` varchar(255) DEFAULT NULL,\
  `PartnerFullName_1` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_1` varchar(255) DEFAULT NULL,\
  `IndexType_Partner1` varchar(255) DEFAULT NULL,\
  `PartnerFullName_2` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_2` varchar(255) DEFAULT NULL,\
  `IndexType_Partner2` varchar(255) DEFAULT NULL,\
  `PartnerFullName_3` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_3` varchar(255) DEFAULT NULL,\
  `IndexType_Partner3` varchar(255) DEFAULT NULL,\
  `PartnerFullName_4` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_4` varchar(255) DEFAULT NULL,\
  `IndexType_Partner4` varchar(255) DEFAULT NULL,\
  `PartnerFullName_5` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_5` varchar(255) DEFAULT NULL,\
  `IndexType_Partner5` varchar(255) DEFAULT NULL,\
  `PartnerFullName_6` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_6` varchar(255) DEFAULT NULL,\
  `IndexType_Partner6` varchar(255) DEFAULT NULL)")

create_lims_emr_linelist = ("CREATE TABLE IF NOT EXISTS `lims_emr_daily_report` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Manifest_id` varchar(255) DEFAULT NULL,\
  `Sample_Collected_Date` varchar(255) DEFAULT NULL,\
  `Date_Sample_sent` varchar(255) DEFAULT NULL,\
  `Sample_Status` varchar(255) DEFAULT NULL,\
  `sample_id` varchar(255) DEFAULT NULL,\
  `patient_id` varchar(255) DEFAULT NULL,\
  `PEPID` varchar(255) NOT NULL,\
  `Date_Sample_Receieved_at_PCRlab` varchar(255) DEFAULT NULL,\
  `Assay_Date` varchar(255) DEFAULT NULL,\
  `Date_Result_Dispatched` varchar(255) DEFAULT NULL)")


create_otz_linelist = ("CREATE TABLE IF NOT EXISTS `otz_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(30) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `Pepid` varchar(255) NOT NULL,\
  `Visit_Date` timestamp(6) NULL DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ` varchar(255) DEFAULT NULL,\
  `Full_Disclosure` varchar(255) DEFAULT NULL,\
  `Full_Disclosure_Date` timestamp(6) NULL DEFAULT NULL,\
  `Positive_Living` varchar(255) DEFAULT NULL,\
  `Positive_Living_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Treatment_Literacy` varchar(255) DEFAULT NULL,\
  `Treatment_Literacy_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Adolescents_Participation` varchar(255) DEFAULT NULL,\
  `Adolescents_Participation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Leadership_Training` varchar(255) DEFAULT NULL,\
  `Leadership_Training_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Peer_to_Peer_Mentorship` varchar(255) DEFAULT NULL,\
  `Peer_to_Peer_Mentorship_Comp_Date` varchar(255) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95` varchar(255) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95_Comp_Date` varchar(255) DEFAULT NULL,\
  `Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `Date_Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `OTZ_Program_Outcome` varchar(255) DEFAULT NULL)")

create_pmtct_linelist = ("CREATE TABLE IF NOT EXISTS `pmtct_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `City` varchar(255) DEFAULT NULL,\
  `Datim_Code` varchar(255) DEFAULT NULL,\
  `ANC_Number_datim` varchar(30) PRIMARY KEY,\
  `ANC_Number` varchar(255) NOT NULL,\
  `PEPFAR_Number(IfOnART)` varchar(255) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `birthdate` timestamp(6) NULL DEFAULT NULL,\
  `Gender` varchar(255) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(255) DEFAULT NULL,\
  `family_name` varchar(255) DEFAULT NULL,\
  `PhoneNumber` varchar(255) DEFAULT NULL,\
  `Address` varchar(255) DEFAULT NULL,\
  `Client_LGA` varchar(255) DEFAULT NULL,\
  `LGA_Latitude` varchar(255) DEFAULT NULL,\
  `LGA_Longitude` varchar(255) DEFAULT NULL,\
  `GeneralANC_VisitDate` varchar(255) DEFAULT NULL,\
  `LMP_DATE` varchar(255) DEFAULT NULL,\
  `GA` double DEFAULT NULL,\
  `Gravida` double DEFAULT NULL,\
  `Parity` double DEFAULT NULL,\
  `Point_Of_Entry` varchar(255) DEFAULT NULL,\
  `EDD` varchar(255) DEFAULT NULL,\
  `PMTCT_HTS_Date` varchar(255) DEFAULT NULL,\
  `PMTCT_HTS_SettingRegister` varchar(255) DEFAULT NULL,\
  `PMTCT_HTS_Register_Date` varchar(255) DEFAULT NULL,\
  `Previously_Known_HIV_Status` varchar(255) DEFAULT NULL,\
  `Date_Previously_Tested_Positive` varchar(255) DEFAULT NULL,\
  `HIV_TestAccepted` varchar(255) DEFAULT NULL,\
  `HIV_ReTesting` varchar(255) DEFAULT NULL,\
  `ResultOfHIVTest` varchar(255) DEFAULT NULL,\
  `Received_HIV_Test_Result` varchar(255) DEFAULT NULL)")

create_full_pharmacy_complement = ("CREATE TABLE IF NOT EXISTS `full_pharmacy_complement` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `DATIMCode` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(30) PRIMARY KEY,\
  `PEPID` varchar(255) NOT NULL,\
  `patient_id` double DEFAULT NULL,\
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `encounter_id` double DEFAULT NULL,\
  `DaysOfARVRefill` double DEFAULT NULL,\
  `Pill_Balance` varchar(255) DEFAULT NULL,\
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL,\
  `CurrentARTReg` varchar(255) DEFAULT NULL,\
  `CurrentRegLine` varchar(255) DEFAULT NULL,\
  `ARV_Drug_Strength` varchar(255) DEFAULT NULL,\
  `OI_Drug_CTX` varchar(255) DEFAULT NULL,\
  `CTX_Strength` varchar(255) DEFAULT NULL,\
  `OI_Drug_INH` varchar(255) DEFAULT NULL,\
  `INH_Strength` varchar(255) DEFAULT NULL,\
  `DSD_Model` varchar(255) DEFAULT NULL,\
  `DDD_Fac_Disp` varchar(255) DEFAULT NULL,\
  `PregStatus` varchar(255) DEFAULT NULL)")

create_last_5_pharmacy = ("CREATE TABLE IF NOT EXISTS `last_5_pharmacy` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `DatimCode` varchar(255) DEFAULT NULL,\
  `Pepid_Datim` varchar(30) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `PEPID` varchar(255) NOT NULL,\
  `1_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `1_DaysOfARVRefill` double DEFAULT NULL,\
  `1_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `2_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `2_DaysOfARVRefill` double DEFAULT NULL,\
  `2_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `3_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `3_DaysOfARVRefill` double DEFAULT NULL,\
  `3_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `4_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `4_DaysOfARVRefill` double DEFAULT NULL,\
  `4_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `5_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `5_DaysOfARVRefill` double DEFAULT NULL,\
  `5_NextAppmt` timestamp(6) NULL DEFAULT NULL)")


