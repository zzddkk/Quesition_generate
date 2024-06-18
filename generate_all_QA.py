import csv
from Question import Question_generae

class QA:
    def __init__(self,path):
        self.path=path
        self.api_key='929f069eedcd27fc4c98661fdb7db34505d85489'
    def generate(self):
        with open(self.path, 'r',encoding = "utf-8") as file:
            csv_reader = csv.reader(file)
            rows=[row for row in csv_reader]
        i=0
        with open(self.path, 'a',encoding = "utf-8",newline='') as f:
            writer = csv.writer(f)
            for row in rows:
                if i==0:
                    i+=1
                    continue
                if i==1:
                    head=(['title','content','story'])
                    writer.writerow(head)
                    i+=1
                    continue
                content=row[2]
                # print(type(content))
                Q=Question_generae(content,self.api_key)
                # print(f"正在生成第{i}个题目")
                result=Q.generate()
                # print(type(result))
                # print(result)
                # i+=1
                for r in result:
                    row.extend(r)
                # print(type(new_row))
                # print(len(new_row))
                writer.writerow(row)