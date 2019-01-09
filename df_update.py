

with open("ins_list.txt", "r") as ins:
    lines = ins.read().split("\n")
new_list=[]
for items in lines:
    if items != '':
        new_list.append(items)
print("Total number of insurance companies:", len(new_list))
#print top 5 names
print(new_list[0:3])


for m in [0,1,2,3,4]:
    for i in range(0, 60):
        if (df.iloc[i]['col_object'] == new_list[m]):
            company = df.loc[i,'col_object']
            contact = df.loc[i+2,'col_value']
            email = df.loc[i+10,'col_value']
            web = df.loc[i+11,'col_value']
            phone = df.loc[i+7,'col_value']
            #s = pd.Series((company, contact, email, web, phone), index =[col_names])
            #print(s)
            #my_df = my_df.append(s, ignore_index = True)
            my_df.loc[len(my_df)] = [company, contact, email, web, phone]
            print("appended")
			
