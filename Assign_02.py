
# coding: utf-8

# <h3>Q no 1:  Write a python program to find number of occurrences of given number in a list with out using built-in methods</h3>
# <h4>**1 generate a list of some random num which is repeated again and again</h4>
# <h4>**2 take user input any number</h4>
# <h4>**3 find the number of occurrences of that num in your list</h4>
# <h4>**4 print some message to user with that result</h4>

# In[2]:


random_number=[0,0,4,15,1,1,5,5,6,8,7,2,5,4,6,9,1,2,5,]
occurrence = 0
Num = int(input("Enter any numbere from 0-9: "))

for x in random_number:
    if x==Num:
        occurrence += 1
print("{} occurs {} times in the list.".format(Num,occurrence))


# <h3>Q no 2:   ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# <br/><br/><br/><br/><br/>
# Write a python program to print website suffixes (com , org , net ,in) from this list
# </h3>

# In[3]:


list=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"] 
for li in list:
    suffix=li.split('.')
    print(suffix[-1])


# <h3> Q no 3 : Write a program which can compute the factorial of a given numbers.</h3>
# <br/>
# <br/>
# <h4>**1 first take user input any number</h4>
# <h4>**2 calculate factorial of that input and then print the result to user</h4>

# In[4]:


user=int(input("enter number: "))


# In[5]:


fact=1
for x in range(user,0,-1):
    fact *=x


# In[6]:


print("factorial ",fact)


# <h3>Q 4 (a) :  If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.</h3>

# In[7]:


invitation_ist=['person_A','person_B','person_C','person_D',]
invitation_ist


# In[8]:


for q in invitation_ist:
    print(q+", I invide you for dinner")


# <h3>Q 4 (b) : You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.<br/></br><br/>
# •	 Start with your program from Q 4 (a). Add a print statement at the
# end of your program stating the name of the guest who can’t make it.<br/></br><br/>
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.<br/></br><br/>
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.<br/></br><br/></h3>

# In[9]:


unavaile_person="person_D"
print(unavaile_person, "is not available")


# In[10]:


new_person="Person_xyz"
invitation_ist.remove('person_D')
invitation_ist.insert(5,"Person_xyz")



# In[12]:


New_invitation_ist=invitation_ist
New_invitation_ist


# <h3>Q 4 (c) : You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.<br/></br><br/>
# •	 Start with your program from Q 4 (a) and (b) Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.<br/></br><br/>
# •	 Use insert() to add one new guest to the beginning of your list.<br/></br><br/>
# •	 Use insert() to add one new guest to the middle of your list.<br/></br><br/>
# •	 Use append() to add one new guest to the end of your list.<br/></br><br/>
# •	 Print a new set of invitation messages, one for each person in your list.<br/></br><br/></h3>

# In[13]:


New_invitation_ist.insert(0,"guest_1")
New_invitation_ist


# In[14]:


New_invitation_ist.insert(3,"guest_2")
New_invitation_ist


# In[16]:


New_invitation_ist.append("guest_3")
New_invitation_ist


# <h5> Q 5 : Here you have some data in variable below, your task is to make a list of specific word Surah then print the list and length of list</h5>
# 

# In[ ]:


data = "Sura I Who believe in the Unseen, Sura Are steadfast in prayer, And spend Sura out of what We Have provided for them;"


# In[26]:


data = "Surah I Who believe in the Unseen, Surah Are steadfast in prayer, And spend Surah out of what We Have provided for them;"
content = data.split()
s_list=[]
for c in content:
    if c == 'Surah':
        s_list.append(c)
print(s_list)
print('length: {},'.format(len(s_list)))

