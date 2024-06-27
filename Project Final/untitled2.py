# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:53:56 2021

@author: bhojr
"""

import matplotlib.pyplot as plt
import pandas as pd

def menu():
    print("---------------------------------------------------------")
    print("   👞👞👠👠🥾🥾✨✨Shoes Managment✨✨👟👟👢👢👡👡   ")
    print("---------------------------------------------------------")
    print("[1].Display csv Files")
    print("---------------------------------------------------------")
    print("Indexing:")
    print("[2].Index as ID:")
    print("---------------------------------------------------------")
    print("[3].Buy Shoe")
    print("---------------------------------------------------------")
    print("Line Chart")
    print("[4].Plot line Chart:")
    print("---------------------------------------------------------")
    print("Bar Chart")
    print("[5].Plot Bar Chart:")
    print("---------------------------------------------------------")
    print("Accessing:")
    print("[6].Accessing Brands Names")
    print("---------------------------------------------------------")
    print("MAX and MIN Values:")
    print("[7].Maximum Values")
    print("[8].Minimum Values")
    print("---------------------------------------------------------")  
   
menu()   

def readcsv():
    print("Data Frame")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv")
    print(df)
    
def no_index():
    print("WithOut Index")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv",index_col=0)
    print(df)



def line_plot():
    Sales=[7,5,9,6,2,3,1,4,8]
    years=[1,2,3,4,5,6,7,8,9] 
    plt.plot(years,Sales)
    plt.title('Perfomance')
    plt.xlabel("years")
    plt.ylabel("Sales")
    plt.show()

def bar_plot():
    Brands=["adidas","Nike","Paragon","Bahamas","Sparks","Bata","Campus","Reebok","Puma"]
    Quantity=[7,5,8,3,9,2,4,1,6]
    plt.bar(Quantity,Brands)
    plt.title("Quantity Observation")
    plt.xlabel("Shoes Quantity")
    plt.ylabel("Different Brands")
    plt.show  
     
def column():
    print("Brands")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv",index_col=0)
    print(df.Brands) 

def M():
    print("Maximum Values")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv")
    print(df.Cost.max())
    
def MI():
    print("Minimum Values")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv")
    print(df.Cost.min())

def shoe():
    print("HELLO")
    df=pd.read_csv("E:\Holy Cross School Class-12 'A' PCM\Project and Activits\IP\Pandas Project\Pandas Code\project.csv")   
    print(df[["Brands","Cost"]])
    a= str(input("Enter Brand Name:"))
    if a=="adidas":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*5999)
        print("Order Placed")
            
    elif a=="Nike":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*5970)
        print("Order Placed")
   
    elif a=="Paragon":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*4999)
        print("Order Placed")
    
    elif a=="Bahamas":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*7999)
        print("Order Placed")
 
    elif a=="Sparks":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*4990)
        print("Order Placed")

    elif a=="Bata":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*3799)
        print("Order Placed")

    elif a=="Campus":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*1500)
        print("Order Placed")
   
    elif a=="Reebok":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*9666)
        print("Order Placed")
    
    elif a=="Puma":
        print("ConFirm")
        c= input("Enter the size:")
        b= int(str(input("Enter the Quantity:")))
        print("The Price of",b,a,"will be",b*9999)
        print("Order Placed")
   
    else:
        print("Entered Wrong Brand")
        

opt=int(input("Enter Your Choice:"))

if opt==1:
    readcsv()
elif opt==2:
   no_index()
elif opt==3:
       shoe()
elif opt==4:
  line_plot()
elif opt==5:
   bar_plot()
elif opt==6:
     column()
elif opt==7:
     M()
elif opt==8:
     MI()     
     
   
  
  
