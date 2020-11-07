'''
  @author [Sundar G]
  @email [sundargopal17@gmail.com]
  @desc [Huffman Encoding Scheme]
 '''
#file = open('doc_aede9a09-f36f-421c-ac4f-1c76376016da.docx','r')
import docx as d 
import heapq
import sys
file = d.Document('HuffmanAssignment.docx')
p = file.paragraphs
dictionary ={}
for i in p:
    for j in i.text:
       num = dictionary.keys()
       k = j.lower()
       if k in num:
           dictionary[k] +=1
       else:
           dictionary[k]=1
print(dictionary)
sum= dictionary.values()
j=0
frequency = {}
clean_dict={}
alphanum_dict = {key: value for key, value in dictionary.items() if key.isalpha()}
num_dict = {key: value for key, value in dictionary.items() if key.isnumeric()}
alphanum_dict.update(num_dict) #alphanumerical dictionary
print('\n')
for i in sum:
    j = j+i
print('Total is :{}'.format(j))


def huffman_encoding(frequency):
    heap=[[weight,[symbol,'']] for symbol,weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0'+ pair[1]
        for pair in hi[1:]:
            pair[1] = '1'+ pair[1]
        heapq.heappush(heap,[lo[0]+hi[0]]+lo[1:]+hi[1:])
    return sorted(heapq.heappop(heap)[1:],key=lambda p:(len(p[-1]),p)) 
coding_scheme=huffman_encoding(dictionary)
print(coding_scheme)
print('\n')
print('\t|Letter/Number  |Probability    |Huffman Code |')
print('\t-----------------------------------------------')
for d  in coding_scheme:
    print('\t|{}\t\t|{:.05f}\t|{}'.format(d[0],dictionary[d[0]]/4579.0,d[1]))
s=0
for i in coding_scheme:
    s += dictionary[i[0]]/4579.0
print('Probability sum is:{}'.format(s))
new_dictionary = {}
for i in coding_scheme:
           num = new_dictionary.keys()
           new_dictionary[i[1]] = i[0]

name = list(input('Enter your name to encode:'))
roll_number = list(input('Enter your roll number to encode:'))
code1 = ''
code2 = ''
for i in name:
    for d in coding_scheme:
        if i==d[0]:
            code1 +=d[1]
for j in roll_number:
    for d in coding_scheme:
        if j==d[0]:
            code2 +=d[1]
print('Huffman Code for your name using the given coding scheme is: {}'.format(code1))
print('Huffman code for your roll number using the given coding scheme is: {}'.format(code2))

def huffman_decode(dictionary, text):
    res = ''
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res

a = huffman_decode(new_dictionary,code1)
b = huffman_decode(new_dictionary,code2)
print('\nDecoded entity 1 is :{}'.format(a))
print('Decoded entity 2 is :{}'.format(b))