#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import takewhile
import os, sys, string


#pronouns
indep = ['ano','chishno','','pishno','hapishno','hachishno']
sa = ['sa','chi','','pi','hapi','hachi'] #added to transitive verbs for direct object, adj/participales to indicate subject
sap = ['sa','chi','i','pi','hapi','hachi'] #usual pronoun for possessor of body parts and kin terms
a = ['a','chi','i','pi','hapi','hachi'] #used with a few of the body parts and kin terms
am = ['am','chim','im','pim','hapim','hachim'] #indicate indirect objects
negation = ['ak','chik','ik','kil','kiloh','hachik']
personal = ['li','ish','','il','iloh','hash'] #ish + sa means h disappears, subject pronouns
time = ['','tuk','tok','chin']
nominative = ['at','ato','mat','mato','yamat','yammato','pat','pato','ilappat','ilappato']
objective = ['an','ano','man','mano','yamman','yammano','pan','pano','ilappan','ilappano']

#lexical arrays
vowels = ['a','e','i','o','u',u"\u00E1",u"\u00E9",u"\u00ED",u"\u00F3",u"\u00FA"]
nformprobs = ['b','p','n','l']


def ditransitive(verb):
    type = verb.split(', ')
    form = type[1]

    output = []
    #now will print past/present/future forms with appropriate pronouns
    #li has lots of exceptions
    #ish before sa loses h in ish
    for i in personal:
        for j in sa:
            for k in time:
                if i is 'li':
                    output.append(j+form+i+k)
                    #print(j+form+i+k)
                else:
                    output.append(i+j+form+k)
                    #print(i+j+form+k)
    #print(output)
    return output

def intransitive(verb):
    # no objects
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    for i in personal:
        for j in time:
            if i is 'li':
                output.append(form+i+j)
                #print(form+i+j)
            else:
                output.append(i + form+j)
                #print(i + form+j)

    return output

def transitive(verb):
    # needs an object
    type = verb.split(', ')
    form = type[1]


    output = []
    # now will print past/present/future forms with appropriate pronouns
    # li has lots of exceptions
    # ish before sa loses h in ish
    for i in personal:
        for j in time:
            if 'li' in i:
                output.append(form+i+j)
                print(form+i+j)
            else:
                output.append(i + form+j)
                print(i + form+j)

    return output

def imperative(verb):
    details = verb.split(',')
    verb = details[1]
    verb = verb[1:]
    return_affirm = ''
    if 'a' in verb[0]:#a initial
        verb = verb[1:]
        return_affirm = 'ho' + verb
    elif 'i' in verb[0]: #i initial
        return_affirm = 'oh' + verb
    else:
        return_affirm = 'ho' + verb

    # all verbs get ish-/hash- and -nna in NEGATIVE form
    return_neg_ish = 'ish' + verb + 'nna'
    return_neg_hash = 'hash' + verb + 'nna'

    #FORMAL form
    formal_ish = 'ish'+verb + 'k man'
    formal_hash = 'hash'+verb + 'k man'
    formal_affirm = return_affirm + 'k man'
    return return_affirm, return_neg_ish, return_neg_hash, formal_ish, formal_hash, formal_affirm

def exhortation(verb):
    #to say 'let me do something', insistence
    form = highform(verb)
    toreturn = []
    for i in negation:
        toreturn.append(i + form +' nà')

    return toreturn

def highform(verb):
    #no meaning
    #should return an accent?

    details = verb.split(',')
    verb = details[1]
    verb = verb[1:]
    reverseverb = reversed(verb)
    secondtolast = 0
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in reverseverb:
        index += 1
        if letter in vowels and secondtolast < 2:
            secondtolast += 1
            holdindex = index

    location = len(verb) - holdindex
    changed = False
    returnable = ''
    # now rules about this position
    if verb[location] is 'a':
        returnable = verb[:location] +vowels[5]+verb[location+1:]
    elif verb[location] is 'e':
        returnable = verb[:location] +vowels[6]+verb[location+1:]
    elif verb[location] is 'i':
        returnable = verb[:location] +vowels[7]+verb[location+1:]
    elif verb[location] is 'o':
        returnable = verb[:location] +vowels[8]+verb[location+1:]
    elif verb[location] is 'u':
        returnable = verb[:location] +vowels[9]+verb[location+1:]

    #print(returnable)
    return returnable

def nform_infix(verb):#to be doing it
    details = verb.split(',')
    verb = details[1]
    verb = verb[1:]
    reverseverb = reversed(verb)
    secondtolast = 0
    index = 0
    holdindex = 0
   #start at end of verb, find second to last vowel
    for letter in reverseverb:
        index+=1
        if letter in vowels and secondtolast <2:
            secondtolast+=1
            holdindex = index

    location = len(verb) - holdindex
    changed = False
    returnable = ''
    #now rules about this position
    if 'i' in verb[0] and 'm' in verb[1]:#i initial
        vowel = accentvowel(verb[0])
        returnable = vowel + verb[1:] #no change
        changed = True
    if 'a' in verb[0] : #a initial
        returnable = vowels[5]+'m' + verb[1:]
        changed = True
    if 'o' in verb[0]: #o initial, o accented plus insert of n
        returnable = vowels[8] + 'n' + verb[1:]
        changed = True
    elif 'm' in verb[location+1] and changed ==False: #m nasal
        vowel = accentvowel(verb[location])
        returnable = verb[:location] +vowel+ 'm' + verb[location+1:]
        changed = True
    #elif ('k' in verb[location]) and (verb[location+1] in nformprobs) : #k changes to g
     #   returnable = verb[:location-1]+'g'+verb[location+1:]
      #  changed = True
    #elif ('h' in verb[location]) and (verb[location+1] in nformprobs) : #h deletion
     #   returnable = verb[:location-1]+''+verb[location+1:]
      #  changed = True
    elif 'n' in verb[location+1] and changed == False: #non repeating n
        vowel = accentvowel(verb[location])
        returnable = verb[:location] + vowel +verb[location+1:]
        changed=True
    elif changed == False: #else n insertion
        vowel = accentvowel(verb[location])
        returnable = verb[:location] + vowel +'n' +verb[location+1:]
    print(returnable)
    return returnable

def hform_infix(verb):
    #to do it all of a sudden
    details = verb.split(',')
    verb = details[1]
    verb = verb[1:]
    #print(verb)
    reverseverb = reversed(verb)
    secondtolast = 0
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in reverseverb:
        index += 1
        if letter in vowels and secondtolast < 2:
            secondtolast += 1
            holdindex = index

    location = len(verb) - holdindex


    changed = False
    returnable = ''

    # now rules about this position
    if (verb[location+1] not in vowels) and (verb[location+2] not in vowels): #h insertion before
        changed = True
        vowel = accentvowel(verb[location])
        returnable = verb[:location] + vowel +'h' +verb[location:] #repeats vowel before h insertion
    elif changed == False:
        vowel = accentvowel(verb[location])
        print(vowel)
        returnable = verb[:location] +vowel +'h' +verb[location+1:] #does not repeat vowel before h insertion
    #print(verb, ' ',returnable)
    #print(returnable)
    return returnable

def hnform_infix(verb):
    #to keep doing it,to do it several times
    #n attaches first
    firstround = nform_infix(verb)
    details = verb.split(', ')
    details[1] = firstround #swap in new verb form
    verb = ' , '.join(details)
    #h attaches second
    returnable = hform_infix(verb)
    #print(returnable)
    return returnable

def yform_infix(verb):
    #to finally do it
    #double y or double l
    details = verb.split(', ')
    verb = details[1]
    reverseverb = reversed(verb)
    secondtolast = 0
    third = 0
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel

    for letter in reverseverb:
        index += 1
        if letter in vowels and secondtolast <= 2:
            secondtolast += 1
            holdindex = index
        if letter in vowels and (secondtolast>2):
            if third<5:
            #this will be a type one transformation
                third = index
                #print(third)

    location = len(verb) - holdindex
    thirdloc = len(verb) - third
    group1 = False
    group2 = False
    # determine group : only 2 vowels = group2, 2 consonants in front of
    if third ==0:
        group2 = True
    elif (verb[location+1] not in vowels) and (verb[location+2] not in vowels):
        group2 = True
    elif (verb[location+1] not in vowels) and (verb[location+2] in vowels): #vcv formation
        if group2==False:
            group1 = True

    #print(group1, ' ',group2)

    returnable = ''
    #group 1
    if group1 == True:
        #accent 3rd vowel and double next consonant
        #print(verb[thirdloc])
        vowel = accentvowel(verb[thirdloc])
        #print(vowel)
        returnable = verb[:thirdloc] + vowel + verb[thirdloc+1] + verb[thirdloc+1:]
        #print(returnable)

    elif group2 == True:
            vowel = accentvowel(verb[location])
            returnable = verb[:location] + vowel+ 'yy' + verb[location:]
            returnable = doubleycheck(returnable) #double y is omitted completely
         #   print(returnable)

    return returnable

#change vowel to accented form
def accentvowel(word):
    print(word)
    if word is 'a':
        return vowels[5]
    if word is 'i':
        return vowels[7]
    if word is 'e':
        return vowels[6]
    if word is 'o':
        return vowels[8]
    if word is 'u':
        return vowels[9]
    if word == vowels[5]:
        print('yes')
        return 'a'
    else:
        return word

#exceptions
def doubleycheck(returnable):
    s = str(returnable)
    if 'íyyi' in s:
        #delete iyyi and replace with
        s = string.replace(s,"íyyi", "í")
        #print(s)
    return s




def main():
    a = open('/Users/linabrixey/PycharmProjects/inprogress/dictionary','r').readlines()
    b = []
    print(u"e\u0331")
    print(u"\u00E3")#a
    print(u"\u00F5")#o
    print(u"\u00EF")#i
    print(u"\u00EB")#e
    print(u"\u00FC")
    print(hnform_infix('VT, tahli'))
    #broken
    #ona
    #ikbi
    #takchi


    """for i in a:
        b.append(nform_infix(i))
        b.append(hform_infix(i))
        b.append(hnform_infix(i))
        b.append(yform_infix(i))
        b.append(imperative(i))
        b.append(exhortation(i))
        if 'VT' in i:
            c.append(transitive(i))
        if 'VD' in i:
            c.append(ditransitive(i))
        if 'VI' in i:
            c.append(intransitive(i))
        else:
            print('no verb type')


    #print out b
    for j in b:
        print(j)"""



if __name__ == '__main__':
    main()