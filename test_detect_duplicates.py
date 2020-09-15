# Test script for detect_duplicates function
# Author: Jose Lise
# September 2020

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.db', echo=False)
con = engine.connect()
df_patient = pd.read_sql('select * from patient', con=con)
df_pcr = pd.read_sql('select * from test', con=con)
con.close()

from detect_duplicates import detect_duplicates


#
df_clean = detect_duplicates(df_patient)

def test_dup_given_name():
    assert len( df_clean[df_clean.duplicated(subset=['phone_number','date_of_birth', 'given_name', 'address_2', 'suburb'], 
                          keep = False)].sort_values(by=['phone_number','date_of_birth', 'given_name']))== 0
def test_dup_surname():                          
	assert len(df_clean[df_clean.duplicated(subset=['phone_number','date_of_birth','surname', 'postcode'],
                        keep = False)].sort_values(by=['phone_number','date_of_birth','surname', 'postcode'])) == 0
                        
def test_dup_typo():
    assert len(df_clean[df_clean.duplicated(subset=['phone_number','date_of_birth','address_2', 'postcode'], 
                           keep = False)].sort_values(by=['phone_number','date_of_birth','address_2', 'postcode'])) == 0
def test_dup_name_address():
    assert len(df_clean[df_clean.duplicated(subset=['given_name','surname','address_1', 'postcode'],
                           keep = False)].sort_values(by=['given_name','surname','address_1', 'postcode'])) == 0
 
	
	