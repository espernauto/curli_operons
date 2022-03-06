import random
import numpy as np
import csv

def swap(s):
    s1 = []
    a = random.randint(0, len(s)-1)
    b = random.randint(0, len(s)-1)
    #c = s[a]
    for i in range (len(s)):
        if i != a and i != b:
            s1.append(s[i])
        elif i == a:
            s1.append(s[b])
        else:
            s1.append(s[a])
    return s1

def exchange(s):
    s2=[]
    a = random.randint(0, 10000)
    b= random.randint(0, len(s))
    s3='mmseqs_cluster_'+str(a)
    for i in range (len(s)):
        if i != b:
            s2.append(s[i])
        else:
            s2.append(s3)
    return s2

def add(s):
    a = random.randint(0, 10000)
    s1 = 'mmseqs_cluster_' + str(a)
    s2 = []
    for i in range (len(s)+1):
        if i != len(s):
            s2.append(s[i])
        else:
            s2.append(s1)

    return s2


s = list(['mmseqs_cluster_1225', 'mmseqs_cluster_730', 'mmseqs_cluster_122', 'mmseqs_cluster_512', 'mmseqs_cluster_519', 'mmseqs_cluster_82'])


k=int(input())

label_file = "test.tsv"
with open(label_file, 'w', encoding='utf8', newline='') as tsv_file:
    tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
    tsv_writer.writerow(['number_of_test', 'mutations', 'sequence'])
    tsv_writer.writerow(['test' + str(0), 'swap' + str(0) + 'exchange' + str(0) + 'add' + str(0), ';'.join(s)])
    for j in range (k):
        s = swap(s)
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        tsv_writer.writerow(['test' + str(3*j+1), 'swap' + str(j+1)+ 'exchange' + str(j)+ 'add'+ str(j), ';'.join(s)])
        s = exchange(s)
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        tsv_writer.writerow(['test' + str(3*j+2), 'swap'+ str(j+1) + 'exchange' + str(j+1)+ 'add'+ str(j), ';'.join(s)])
        s = add(s)
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        tsv_writer.writerow(['test' + str(3*j+3), 'swap' + str(j+1) + 'exchange' + str(j+1)+ 'add'+ str(j+1), ';'.join(s)])
        #print (s)
