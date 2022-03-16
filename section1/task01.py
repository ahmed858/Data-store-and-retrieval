#data (kickstart ,codejam ,hashcode ,icpc, glassdoor)
import numpy as np


files_names = ['kickstart' ,'codejam' ,'hashcode' ,'icpc', 'glassdoor']

kickstart = open('kickstart.txt', 'r', encoding='utf-8')
codejam = open('codejam.txt', 'r', encoding='utf-8')
hashcode = open('hashcode.txt', 'r', encoding='utf-8')
icpc = open('icpc.txt', 'r', encoding='utf-8')
glassdoor = open('glassdoor.txt', 'r', encoding='utf-8')

kickstart = kickstart.read()
codejam = codejam.read()
hashcode = hashcode.read()
icpc = icpc.read()
glassdoor = glassdoor.read()

docs = [kickstart, codejam, hashcode, icpc, glassdoor]
print("read it heeaa ")


# create document terms matrix
un_terms = {term for doc in docs for term in doc.split()}

doc_term_matrix = {}
for term in un_terms:
    doc_term_matrix[term] = []

    for doc in docs:
        if term in doc:
            doc_term_matrix[term].append(1)
        else:
            doc_term_matrix[term].append(0)


# take query and answer it
docs_array = np.array(docs, dtype='object')

query = input('Enter your query: ')
query_list = query.split()
words1 = []
words2 = []
flip = 0
for x in query_list:
    if x == 'AND' or x == 'OR':
        flip = 1
    if not flip:
        words1.append(x)
    else:
        words2.append(x)

v1, v2 = [], []
if 'AND' in query_list:
    v1 = []
    for word in words1:
        if word != 'AND':
            if word in doc_term_matrix.keys():
                v1.append(doc_term_matrix[word])
            else:
                v1.append([0, 0, 0, 0, 0])

    v2 = []
    for word in words2:
        if word != 'AND':
            if word in doc_term_matrix.keys():
                v2.append(doc_term_matrix[word])
            else:
                v2.append([0, 0, 0, 0, 0])
    # print(v1)
    # print(v2)
    v1 = np.array(v1)
    v2 = np.array(v2)
    left = v1[0]
    for i in range(1, len(v1)):
        left &= v1[i]
    # print(left)
    right = v2[0]
    for i in range(1, len(v2)):
        right &= v1[i]
    # print(right)
    # print(right&left)
    result = right & left
elif 'OR' in query_list:
    v1 = []
    for word in words1:
        if word != 'OR':
            if word in doc_term_matrix.keys():
                v1.append(doc_term_matrix[word])
            else:
                v1.append([0, 0, 0, 0, 0])

    v2 = []
    for word in words2:
        if word != 'OR':
            if word in doc_term_matrix.keys():
                v2.append(doc_term_matrix[word])
            else:
                v2.append([0, 0, 0, 0, 0])
    # print(v1)
    # print(v2)
    v1 = np.array(v1)
    v2 = np.array(v2)
    left = v1[0]
    for i in range(1, len(v1)):
        left &= v1[i]
    # print(left)
    right = v2[0]
    for i in range(1, len(v2)):
        right &= v1[i]
    # print(right)
    # print(right&left)
    result = right & left

else:
    v1 = []
    for word in words1:
        if word != 'AND':
            if word in doc_term_matrix.keys():
                v1.append(doc_term_matrix[word])
            else:
                v1.append([0, 0, 0, 0, 0])
    # print(v1)
    # print(v2)
    v1 = np.array(v1)
    v2 = np.array(v2)
    result = v1[0]
    for i in range(1, len(v1)):
        result &= v1[i]


print('keep it going')

print([files_names[i] for i in range(len(result)) if result[i]])