# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:13:43 2019

@author: degamasandoval

Quick Bowling Game

For running:
    pip install beautifultabl

"""
from beautifultable import BeautifulTable
from random import randint



# =============================================================================
# Class
# =============================================================================

class frame():
    def __init__(self): #instance variable
        self.first=0
        self.scnd=0
        self.score=0
        self.bonus=False
        
        
   
     
        
# =============================================================================
# Main
# =============================================================================
frames=[]
for i in range(10):
    frames.append(frame())
    
   
    
#### START
for i in range(10):
    table = BeautifulTable()
    table.column_headers = ["Frame", "1st Time", "2nd Time","Score"] 
    
    
    esc=input('Press enter to throw the ball')
    if len(esc)>0:
        break
    frames[i].first=randint(0,10)

    
    if i>0 and frames[i-1].bonus==True:
        frames[i-1].score+=frames[i].first
    ##---Strike 
    if frames[i].first==10: 
        print('Strike')
        frames[i].bonus=True
        input('Press enter to throw the ball again')
        frames[i].scnd=randint(0,10)
    else:
        input('Press enter to throw the ball again')
        frames[i].scnd=randint(0,10-frames[i].first)

    
    frames[i].score=frames[i].first+frames[i].scnd
    ##---Spare
    if frames[i].score==10: 
        frames[i].bonus=True
        
    if i>0:
        frames[i].score+=frames[i-1].score                
    for frame in range(i+1):                  
        table.append_row([frame, frames[frame].first, frames[frame].scnd,frames[frame].score])
    print(table)
                    
            
        
    
    
        


        
        
        

    