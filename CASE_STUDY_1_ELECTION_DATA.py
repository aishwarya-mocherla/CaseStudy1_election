import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.DataFrame()  #ek dataset banaya jo hamara result hone wala h
for f in ['C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/2009maharashtraresults.xlsx',
          'C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/2014maharashtraresults.xlsx']: #ek for loop me ek "f" ko dono deta sets junhe hame merge karna h, dono me ek chalaya
    data = pd.read_excel(f,'Sheet1') #ek temopary data set banaya jo har f ko read karke memory me store karega 
    ds = ds.append(data) #append function ke madad sab jo "data" me read karke store kiya usko add kardiya "ds" ke end me  
print(ds)

plt.figure(figsize=(8,4)) #width,height
plt.scatter(data['PARTYNAME'],data['SEATS'],c='blue')#x-axis data,y-axisdata,colour
plt.xlabel("name of the party")
plt.ylabel("seats won")
plt.xticks(rotation=90) #naam vertical print kiya h taki overlap na ho
plt.show()

#make fraph showing total number of seats won by parties in both years
final_data = {} #empty dictionary banaya jisme key and value form me party name aur total seats aayega
for i in ds['PARTYNAME']: #ek loop chalaya jisme har ek row ko go through kiya
    x = i #x declare kiya jiske sath kaam karenge
    t1 = (ds[(ds.PARTYNAME==x)&(ds.YEAR==2009)].SEATS).tolist() #1st empty list banay jisme 2009 ka seats won ka value rhega. so sabse pehle i ka value first wale party pe jaega, fir vaha pe agar "YEAR" wale row me aagey jake "2009" likha h toh uska "SEATS" ka value leke " tolist() " function use karke t1 me daldega
    t2 = (ds[(ds.PARTYNAME==x)&(ds.YEAR==2014)].SEATS).tolist() #same like above  but isntead of "YEAR" being 2009, this time its "2014"
    t3 = t1 + t2 #3rd list banaya jisme t1 aur t2 ke vaues aajaegenge, they will concatenate, not sum up
    print("===================================================================================")
    print("name of party: ",i)
    print("no of seats in 2009: ",int(sum(t1[0:])))
    print("no of seats in 2014: ",int(sum(t2[0:])))
    print("total no of seats: ",int(sum(t3)))
    
    
    final_data.update({i:int(sum(t3))}) #fir finally jo pehla start me dictionary banaya usme key:value format me party name fir liste 3 ka jo values h usko sum karke likha h
    plt.bar(final_data.keys(),final_data.values(),color="blue")
    plt.xlabel("Party name")
    plt.ylabel("number of seats won")
    plt.xticks(rotation=90)

# to find if partyy has done bettr or worse that the previos year
    difference = int(sum(t2[0:])) - int(sum(t1[0:1]))
    if (difference>0):
        print("there has been a increase in the number of votes in",x," by ",abs(difference))
    elif(difference<0):
        print("there has been an decrease in the number of votes in",x," by ",abs(difference))
    else:
        print("there has been no change in the votes in ",x)


