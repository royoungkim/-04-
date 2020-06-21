#!/usr/bin/env python
# coding: utf-8

# In[15]:


import nltk
import shutil
from nltk.corpus import*
#corpus root에 변수 정의
corpus_root = "C:/Users/82106/AppData/Roaming/nltk_data/corpora/cess_esp/Genomics-Informatics-Corpus-master/raw_text2/"
#genomics and Informatics를 Corpus화하기
GNICorpus = PlaintextCorpusReader(corpus_root,'.*\.txt', encoding='utf-8') 


# In[3]:


GNICorpus.fileids()


# In[16]:


giRaw = GNICorpus.raw('gni-3-3-53.txt')


# In[17]:


giRaw


# In[18]:


import re
pattern = re.findall(r'[a-z]+-\n[a-z]+', giRaw)
len(pattern)


# In[19]:


match =re.findall(r'[\r\n]{2,}', giRaw)
match


# In[20]:


print(re.sub(r'[\r\n]{2,}',' ', giRaw))


# In[21]:


match =re.findall(r'3 1 UTR', giRaw)
match


# In[22]:


print(re.sub(r'3 1 UTR','3\'UTR', giRaw))


# In[23]:


match =re.findall(r'www.sanger . ', giRaw)
match


# In[24]:


print(re.sub(r'www.sanger . ',r'www.sanger.', giRaw))


# In[25]:


match =re.findall(r'/tfcraRAM', giRaw)
match


# In[26]:


print(re.sub(r'/tfcraRAM', 'MicroRNA', giRaw))


# In[27]:


match =re.findall(r'miRNA[a-z]+.', giRaw)
match


# In[28]:


print(re.sub(r'miRNA[a-z]+.', r'miRNA:human ', giRaw))


# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


giRaw1 = GNICorpus.raw('gni-9-4-173.txt')


# In[32]:


giRaw1


# In[33]:


import re
pattern = re.findall(r'[a-z]+-\n[a-z]+', giRaw1)
len(pattern)


# In[34]:


pattern= re.findall('pvalue', giRaw1)
len(pattern)
giRaw1.replace('pvalue', 'p-value')


# In[35]:


pattern = re.findall(r'[a-z]-[a-z]+', giRaw1)
len(pattern)


# In[36]:


pattern


# In[37]:


pattern = re.findall(r'[a-z]{11,}', giRaw1)


# In[38]:


pattern


# In[39]:


match = re.findall(r'[a-z]. org', giRaw1)


# In[40]:


match


# In[41]:


print(re.sub('[a-z]. org', '[a-z].org', giRaw1))


# In[42]:


[re.sub(r'-\n', '',p) for p in pattern]


# In[43]:


#이메일 관련 text는 없는 것으로 보인다. 
match = re.findall(r'([\w.-]+)@([\w.-]+)', giRaw1)


# In[44]:


match


# In[45]:


match =re.findall(r'www. [a-z]+.  net', giRaw1)


# In[46]:


match


# In[47]:


print(re.sub(r'www. [a-z]+.  net', r'www.[a-z]+.net', giRaw1))


# In[48]:


match =re.findall(r'[a-z]+.  pound', giRaw1)
match


# In[49]:


print(re.sub(r'[a-z]+.  pound',r'[a-z]+.pound', giRaw1))


# In[50]:


match =re.findall(r'[ER]+negative', giRaw1)
match


# In[51]:


print(re.sub(r'[ER]+negative',r'[ER]+-negative', giRaw1))


# In[52]:


match =re.findall(r'miR26b.  pound', giRaw1)
match


# In[ ]:





# In[53]:


##우수과제 추가 내용-진유리
#1) 3' UTR, 5' UTR에서 '이 1로 나오는 오류: 1을 기준으로 양 옆에 공백 존재
match =re.findall(r'[0-9]\s1\s{1,}', giRaw1)
print(match)
##해당 과제에서는 없는 듯


# In[55]:


#2) 문자(.) + 공백 + 1 + 공백의 조합, but re,sub를 이용해 수정은 불가능
match = re.findall(r'[a-z]\s1\s', giRaw1) + re.findall(r'[A-Z]\s1\s', giRaw1)+ re.findall(r'\.\s1\s', giRaw)
print(match)
##해당과제에서는 없는 듯


# In[57]:


#3) 공백이 1번 이상 들어가거나 문장이 끝나기 전에 줄 바꿈이 있는 오류 추출
#공백이 2번 이상 들어가는 경우는 .(마침표) 이후를 제외하고 없다는 판단 하에 문장이 끝나기 전에 마침표가 두 번 이상 들어가는 것을 추출한다.
#한 문장에서 마침표가 나오기 전에 줄바꿈이 발생하는 경우를 모두 찾는다.
#re.findall(r'\w+\s{2,}\w+', giRaw) : 문자 (개수 무관) + 공백 (2개 이상) + 문자 (개수 무관)의 오류를 찾아 list 생성

match = re.findall(r'\w+\s{2,}\w+', giRaw)
print(match)


# In[60]:


#4) 하나의 단어가 pdf에서 줄 바꿈을 하여 -이 생기는 경우
match = re.findall(r'\w+\-\s{1,}\w+', giRaw)
print(match)
#간혹 단어 하나가 pdf에서 줄 바꿈을 하여 – 이 생기는 일이 있다. 이런 경우 –양 옆에 공백이 존재한다면 공백을 지워줘야 한다.
#공백이 하나일 경우 txt 파일에서 눈으로 확인 시 큰 문제는 없어 보이지만 공백이 여러 개인 경우 오류로 판단 가능하기 때문이다.
#글은 위부터 아래, 왼쪽부터 오른쪽으로 써 나가므로 –뒤에 공백이 있는지 없는 지만 확인하면 된다.
#re.findall(r'\w+\-\s{1,}\w+', giRaw) : 문자 (개수 무관) + 하이픈 + 공백 (1개 이상) + 문자(개수 무관)
#‘high-\r\n\r\n\r\nquality’ 와 같은 과도한 줄 바꿈 + 공백의 오류를 잡을 수 있다.
#단어 사이에 줄 바꿈이 일어나는 경우는 pdf에서 모두 –표시를 해주기 때문에 모두 잡을 수 있다.
#하지만 txt에서 줄 바꿈이 일어나지 않은 단어 내에 공백이 있다면 re.findall() 로는 찾을 수 없다


# In[64]:


#5) 특수 문자 뒤에 공백이 2번 이상 나오는 경우
match = re.findall(r'\w+[,|)&%$#}*@/:;]\s{2,}\w+',giRaw)
print(match)


# In[66]:


#6) url주소 안에 공백이 들어간 경우
match = re.findall('\{3}', giRaw1)+ re.findall('^http',giRaw1) + re.findall('\.com$', giRaw1)
print(match)


# In[71]:


#9) et al에서의 오류 추출: etal로 표기된 것이나 eta!로 표기된 단어 추출
match = re.findall(r'etal', giRaw) + re.findall(r'et\s*a\!', giRaw)
print(match)


# In[75]:


##우수과제 추가내용-김소현
#1) ever-expanding이 ever\xad expanding으로 출력
match= re.findall(r'[a-z]*\xad[a-z]*[a-z]*', giRaw)
print(match)


# In[78]:


#2)공백 문자가 2번 이상 발생하는 경우
match = re.findall(r'[a-z]+ [ ]+',giRaw)
print(match)
#해결
[re.sub(r'[]+','',p) for p in match]


# In[79]:


#3) URL 다음에 오는 단어까지 URL의 일부로 인식
match = re.findall(r'bio.cc/\r\n\r\nThe', giRaw)
print(match)


# In[83]:


#4) trans-가 txt 파일에서 trans\xad로 나타남  ##이거 이상함
match = re.findall(r'[a-z]*\xad* [a-z]*', giRaw1)
print(match)


# In[88]:


#5) URL 주소 안에 공백문자가 삽입되어 있는 경우 이를 삭제=> 이거 good
match = re.findall(r'[]*[.][ ]+com|[ ]*[.][ ]+net|[ ]+[.][ ]+org|www[ ]*[.][ ]+',giRaw1)
print(match)
#해결
[re.sub(r'[ ]+','',p) for p in match]


# In[90]:


#6) 모든 url을 찾아서 공백이 있으면 제거
match = re.findall(r'//[a-z./ ]+', giRaw)
print(match)
#해결
[re.sub(r'[ ]+', '', p) for p in match]


# In[ ]:




