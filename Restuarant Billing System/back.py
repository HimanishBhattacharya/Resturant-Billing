import datetime
from datetime import *
#Costs of various items

cost_vegb=40
cost_chkb=60
cost_chsnd=50
cost_chksd=70
cost_ff=35
cost_chkng=55
cost_coke=15
cost_milks=25
cost_limej=10
cost_mansh=35

#Tax for various items

tax_vegb=int(0.05*cost_vegb)
tax_chkb=int(0.05*cost_chkb)
tax_chsnd=int(0.05*cost_chsnd)
tax_chksd=int(0.05*cost_chksd)
tax_ff=int(0.05*cost_ff)
tax_chkng=int(0.05*cost_chkng)
tax_coke=int(0.05*cost_coke)
tax_milks=int(0.05*cost_milks)
tax_limej=int(0.05*cost_limej)
tax_mansh=int(0.05*cost_mansh)


#Fetching units of items ordered and preparing the item costs
def enter_vegb(unit):
    return (unit*cost_vegb)

def enter_chkb(unit):
    return (unit*cost_chkb)

def enter_chsnd(unit):
    return (unit*cost_chsnd)

def enter_chksd(unit):
    return (unit*cost_chksd)

def enter_ff(unit):
    return (unit*cost_ff)

def enter_chkng(unit):
    return (unit*cost_chkng)

def enter_coke(unit):
    return (unit*cost_coke)

def enter_milks(unit):
    return (unit*cost_milks)

def enter_limej(unit):
    return (unit*cost_limej)

def enter_mansh(unit):
    return (unit*cost_mansh)
    


#Preparing the receipt
text="----------YOUR RECEIPT----------\n\n\n VEG BURGER {}             Rs.{}\n CHICKEN BURGER {}         Rs.{}\n CHEESE SANDWICH {}        Rs.{}\n CHICKEN SANDWICH  {}      Rs.{}\n FRENCH FRIES {}           Rs.{}\n CHICKEN NUGGETS {}        Rs.{}\n COKE {}                   Rs.{}\n MILK SHAKE {}             Rs.{}\n LIME JUICE {}             Rs.{}\n MANGO SHAKE {}            Rs.{}\n -------------------------------\n TAX         			  Rs.{}\n SUBTOTAL        			  Rs.{}\n\n TOTAL                    Rs.{}\n\n\n\n Date                "+str(datetime.date(datetime.now()))
