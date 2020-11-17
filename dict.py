import os
direc= 'files/'
file_dic= {}
#import pdb;pdb.set_trace()
list_files= [i for i in os.listdir(direc)]
#list_time = [j for j in  os.path.getctime()]
for j in list_files:
    m_time = ""
    m_time = os.path.getctime("files/"+j)
    file_dic[j] = m_time

print(file_dic)
