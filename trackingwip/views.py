from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import datetime

"""

1                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
 VRP1100                                      LIST OF WORK ORDER FOR AN INTERVAL OF DAYS           PRINTED ON  27FEB20      PAGE:   1                                                                                                                                                                                                                                                                                                                              
                                                     FROM 01JAN18  UNTIL  13FEB20                                                                                                                                                                                                                                                                                                                                                                                  
0PG CUS PO-NUMBER            WO-NUMBR WIP#   CREATD W T P C JOB PART-NUMBER          SERIAL-NUMBER        TYPE-NUMBR TYPE-DESCRIPTION     RECEIVED OPENED  CLOSED  START   DAYS E.C.D   Q-REST T TARGET   REMARK                                                       X TOT-QUOTATION   QTY MAT-QUOTATION    M/H-QUOTATION    OTH-QUOTATION    SBU   NAMA-CUSTOMER                  MTU CUR=VP40 FINAL-QUOT                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    MAY DUMMY                W1800124 437359 871545 0     1     N/A                  -                    331 730102 DUPLEX FUEL MANIF             15MAY18                 0000         001                                                                              0000000000000.00001 0000000000000.00 0000000000000.00 0000000000000.00 ITS   PT. MAYORA INDAH TBK WAFER                              0.00                                                 
    PTM SPJ PERTAMINA GRUP   W1900488 456635 940004 0     1     GEN090002                                 GEN 090002 GENERAL REQUESTS              15NOV19                 0000         001                                                                              0000000000000.00001 0000000000000.00 0000000000000.00 0000000000000.00 ITS   PERTAMINA DIT. PPDN                                     0.00                                                 
    SIE 4509363173           W1900400 454683 940004 0     1     GEN020009                                 GEN 020009 ST.TURB.DIAPHRAGM             27SEP19                 0000         001                                                                              0000000000000.00001 0000000000000.00 0000000000000.00 0000000000000.00 ITS   PT SIEMEN INDONESIA                                     0.00                                                 
    SSI 1713CG               W1800056 435238 871520 0     2     EC4501-80-G                               ROT 720222 CENTAUR GP ASSY               21FEB18                 0000         001                                                                              0000000000000.00001 0000000000000.00 0000000000000.00 0000000000000.00 ITS   SOLAR SERVICES IND, PT                                  0.00                                                 
    TAL RAB PUS AL TA 2019   W1800301 441895 871454 0     1     3102170-7            P-37688C             331 720041 GARRETT ENG.                  04OCT18                 0000         001                                                                              0000000000000.00001 0000000000000.00 0000000000000.00 0000000000000.00 AERO  TNI-AL                                                  0.00                                                 


"""
def pars_vrp1100(filepath="C:/development/wip-tracker/wiptracker/trackingwip/_asset/vrp1100"):
    file=open(filepath,"r")
    lines=file.readlines()
    data={
        "WOM": "437359",
        "Contract": "0000000000000.00001",

    }
    list1=[
        {
        "WOM": "437359",
        "Contract": "0000000000000.00001",

        },
        {
        "WOM": "456635",
        "Contract": "0000000000000.00001",
        }
    ]
    

    data_list=[]
    
    for i,line in enumerate(lines):
        if i > 4 :
            data={
                "WOM" : line[38:44],
                "Customer" : line[342:372],
                "Contract" : line[385:402],
                "Paid" : line[265:284],
                "Unpaid" : float(line[385:402]) - float(line[265:284]), 
                "Material" : line[285:301],
                "Manhour" : line[302:318],
                "PIC" : line[45:51],
                "FinishEstimation" : datetime.datetime.strptime(line[176:183], "%d%b%y").strftime("%Y-%m-%d") if line[176:183].strip() else None,
                "CostFinish" : float(line[287:301]) + float(line[302:318]) + float(line[319:336])
            }
            
            data_list.append(data)

    return data_list

    # return JsonResponse(data_list,safe=False)
# Create your views here.
