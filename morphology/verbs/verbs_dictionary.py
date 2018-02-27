#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import takewhile
import os, sys, string
person_marker = ['li','ish','','il','hvsh']
objects_of_actions = ['sv','chi','','pi','hvpi','hvchi'] #also subjects of adjectives
indirect_possession = ['vm','chim','im','pim','hvpim','hvchim'] #to him, for him + possession (my object)
indirect_consonantprecede = [u"\u00E3", 'ch'+u"\u00EF", u"\u00EF",'p'+u"\u00EF", 'hvp'+u"\u00EF", 'hvch'+u"\u00EF"] #indirect + possession pronouns before consonants
negation = ['ak', 'chik','ik','kil','hvchik']
tense = ['','tuk','tok','ach'+u"\u00EF"] #present, recent past, remote past, future (a will attach to preceeding word but chin will be separate)

nasals = [u"\u00E3",u"\u00EB",u"\u00EF",u"\u00F5",u"\u00FC"]

def command(verb):
    details = verb.split(',')
    verb = details[1]
    form = verb[1:]
    output = []

    #simple is only verb
    output.append(form)

    #negative
    output.append('ish '+ form+ ' nna') #you
    output.append('hvsh ' + form + ' nna') #you plural

    #lets
    output.append('kil '+ form)

    return output

def present(verb): #no info on transitivity
    details = verb.split(',')
    type = details[0]
    verb = details[1]
    form = verb[1:]
    output = []

    if 'v. t' in details[0]:
        for i in person_marker:
            for j in objects_of_actions:
                if i == 0:
                    output.append(j + ' '+form + ' '+ i)
                else:
                    output.append(i + ' '+ j+ ' '+ form)
    else:
        for i in person_marker:
            if i ==0:
                output.append(form+ ' '+ i)
            else:
                output.append(i+ ' '+ form)
    return output

def future(verb):
    details = verb.split(',')
    type = details[0]
    verb = details[1]
    form1 = verb[1:]
    output = []

    #with achin
    form = form1[:-1]+'a' #achin separates, a attaches to preceeding (doesn't matter if a already at end)
    if 'v. t' in details[0]:
        for i in person_marker:
            for j in objects_of_actions:
                if i == 0:
                    output.append(j + ' '+form + ' '+ i)
                else:
                    output.append(i + ' '+ j+ ' '+ form)
    else:
        for i in person_marker:
            if i ==0:
                output.append(form+ ' '+ i)
            else:
                output.append(i+ ' '+ form)

    #with kma
    if 'v. t' in details[0]:
        for i in person_marker:
            for j in objects_of_actions:
                if i == 0:
                    output.append(j + ' '+form1 + ' '+ i+'kma')
                else:
                    output.append(i + ' '+ j+ ' '+ form1 +'kma')
    else:
        for i in person_marker:
            if i ==0:
                output.append(form1+ ' '+ i+'kma')
            else:
                output.append(i+ ' '+ form1+'kma')

    return output

def past(verb):
    details = verb.split(',')
    type = details[0]
    verb = details[1]
    form = verb[1:]
    output = []
    timepast = ['tuk','tok','h ma']

    for k in timepast:
        if 'v. t' in type:
            for i in person_marker:
                for j in objects_of_actions:
                    if k ==2:#h ma
                        if i == 0:#li at end
                            output.append(j + ' ' + form + ' ' + i+k)
                        else:
                            output.append(i + ' ' + j + ' ' + form +k)
                    else: #not h ma
                        if i == 0:
                            output.append(j + ' ' + form + ' ' + i+' '+k)
                        else: #all other subject pronouns at beginning
                            output.append(i + ' ' + j + ' ' + form +' '+k)
        else: #else verb type
            for i in person_marker:
                if k ==2:
                    if i == 0:
                        output.append(form + ' ' + i+ k)
                    else:
                        output.append(i + ' ' + form+k)
                else:
                    if i == 0:
                        output.append(form + ' ' + i+ ' '+ k)
                    else:
                        output.append(i + ' ' + form+' '+k)
    return output

def negate(verb):
    type = verb.split(', ')
    form = type[1]
    verb = form[:-1] + 'o' #what happens for future?
    output = []

    j = 0
    while j <len(tense-1):
        for i in negation:
                output.append(i + ' ' + verb + ' '+tense[j] )
        j+=1

    return output

def instantaneous_quickly(verb):
    #insert h, possibly duplicate vowel
    # to do it all of a sudden
    details = verb.split(',')
    verb = details[1]
    verb = verb[1:]
    # print(verb)
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
    if (verb[location + 1] not in vowels) and (verb[location + 2] not in vowels):  # h insertion before
        changed = True
        vowel = accentvowel(verb[location])
        returnable = verb[:location] + vowel + 'h' + verb[location:]  # repeats vowel before h insertion
    elif changed == False:
        vowel = accentvowel(verb[location])
        print(vowel)
        returnable = verb[:location] + vowel + 'h' + verb[location + 1:]  # does not repeat vowel before h insertion
    # print(verb, ' ',returnable)
    # print(returnable)
    return returnable

def iterative(verb):#repeatedly
    #insert h, duplicate preceeding vowel and nasalize
    # to keep doing it,to do it several times
    # n attaches first
    firstround = nform_infix(verb)
    details = verb.split(', ')
    details[1] = firstround  # swap in new verb form
    verb = ' , '.join(details)
    # h attaches second
    returnable = hform_infix(verb)
    # print(returnable)
    return returnable

def finallydone(verb):
    #iy and duplicate preeceeding vowel (like yform insert)
    # to finally do it
    # double y or double l
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
        if letter in vowels and (secondtolast > 2):
            if third < 5:
                # this will be a type one transformation
                third = index
                # print(third)

    location = len(verb) - holdindex
    thirdloc = len(verb) - third
    group1 = False
    group2 = False
    # determine group : only 2 vowels = group2, 2 consonants in front of
    if third == 0:
        group2 = True
    elif (verb[location + 1] not in vowels) and (verb[location + 2] not in vowels):
        group2 = True
    elif (verb[location + 1] not in vowels) and (verb[location + 2] in vowels):  # vcv formation
        if group2 == False:
            group1 = True

    # print(group1, ' ',group2)

    returnable = ''
    # group 1
    if group1 == True:
        # accent 3rd vowel and double next consonant
        # print(verb[thirdloc])
        vowel = accentvowel(verb[thirdloc])
        # print(vowel)
        returnable = verb[:thirdloc] + vowel + verb[thirdloc + 1] + verb[thirdloc + 1:]
        # print(returnable)

    elif group2 == True:
        vowel = accentvowel(verb[location])
        returnable = verb[:location] + vowel + 'yy' + verb[location:]
        returnable = doubleycheck(returnable)  # double y is omitted completely
        #   print(returnable)

    return returnable


def tobedoing(verb):
    #nasalize first vowel
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
    if 'i' in verb[0] and 'm' in verb[1]:  # i initial
        vowel = accentvowel(verb[0])
        returnable = vowel + verb[1:]  # no change
        changed = True
    if 'a' in verb[0]:  # a initial
        returnable = vowels[5] + 'm' + verb[1:]
        changed = True
    if 'o' in verb[0]:  # o initial, o accented plus insert of n
        returnable = vowels[8] + 'n' + verb[1:]
        changed = True
    elif 'm' in verb[location + 1] and changed == False:  # m nasal
        vowel = nasalvowel(verb[location])
        returnable = verb[:location] + vowel + 'm' + verb[location + 1:]
        changed = True
        # elif ('k' in verb[location]) and (verb[location+1] in nformprobs) : #k changes to g
        #   returnable = verb[:location-1]+'g'+verb[location+1:]
        #  changed = True
        # elif ('h' in verb[location]) and (verb[location+1] in nformprobs) : #h deletion
        #   returnable = verb[:location-1]+''+verb[location+1:]
        #  changed = True
    elif 'n' in verb[location + 1] and changed == False:  # non repeating n
        vowel = nasalvowel(verb[location])
        returnable = verb[:location] + vowel + verb[location + 1:]
        changed = True
    elif changed == False:  # else n insertion
        vowel = nasalvowel(verb[location])
        returnable = verb[:location] + vowel + 'n' + verb[location + 1:]
    print(returnable)
    return returnable

def main():
    #a = open('/Users/linabrixey/PycharmProjects/inprogress/dictionary','r').readlines()
    b = []


    #broken
    #ona
    #ikbi
    #takchi




if __name__ == '__main__':
    main()