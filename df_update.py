#below will make a new dataframe my_df using informatiom another dataframe name as df
# , assuming df has 60 lines 
# next for will scan df dataframe and look for a match of the company name from new_list
# when there is a match , it will gather some info and make a new data frame
# many lines are skipped , that is for readers for evaluation , such as opening csv file , writing to new CSV file

# txt file has company name , 1 per line
with open("co_list.txt", "r") as ins:
    lines = ins.read().split("\n")
new_list=[]
for items in lines:
    if items != '':
        new_list.append(items)
print("Total number of companies:", len(new_list))
#print few names, for test only
print(new_list[0:4])


# info in df: df has 2 cols  , 1st col: col_object, 2nd col : col_value, both may have missing values, 
# however, row locations for contact, email , web etc. are all in relative position from the row position of company name

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
			
#test 
print(my_df)
#output will show an xcel style output with 1st row as : company-contact-email-web-phone
