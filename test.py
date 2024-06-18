# import csv
# from Question import Question_generae

# API_key='929f069eedcd27fc4c98661fdb7db34505d85489'
# path='./data/QAv1.0.csv'
# new_rows=[]
# i=1

# with open('./data/100条截断v1.2.csv', 'r',encoding = "utf-8") as file:
#     csv_reader = csv.reader(file)
#     rows=[row for row in csv_reader]

# with open(path, 'a',encoding = "utf-8",newline='') as f:
#     writer = csv.writer(f)
#     for row in rows:
#         content=row[2]
#         Q=Question_generae(content,API_key)
#         print(f"正在生成第{i}个题目")
#         result=Q.generate()
#         i+=1
#         new_row=row.extend(result)
#         print(len(new_row))
#         writer.writerow(new_row)

a=[1,2,3]
b=[[1],[2],[3]]
a.extend(b)
print(a)