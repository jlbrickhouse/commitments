#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import takewhile
import os, sys, string


#pronouns
indep = ['ano','chishno','','pishno','hvppishno','hvchisno']#with at end for h predicative, for 'mine'
definite_personal = ['sia','chia','pia','hvpia','hvchia'] #add h at endfor h predicative
possessive = ['vmmi', 'chimmmi','immi','pimmi','hvppimi','hvchimmi','immi']
personal_possessive = ['salap','chilap','p'+u"\u00EF"+'lap','hvpilap','hvchilap']
personal = ['li','ish','','il','e','iloh','eho','hvsh','hvs'] #ish + sa means h disappears, subject pronouns
negation = ['ak','chik','ik','kil','ke','kiloh','heloh','hvchik']
affirmative_objective_personal = ['s','sa','sv','sai','si','chi','ch','pi','p','hvpi','hvp','hvchi','hvch'] #added to transitive verbs for direct object, adj/participales to indicate subject
negative_objective_personal = ['iks','ik sa','ik sv','ik sai','ik so','ik chi', 'ik ch','ik','ik pi','ik p','ik hvpi','ik hvp','ik hvchi','ik hvch','ik']
affirmative_objective_possessive = ['a','am','vm','vmi','an','sa','sam','sum','sumi','san','ch'+u"\u00EF",'chim','chimi','chin',u"\u00EF", 'im','imi','imi']
negative_objective_possessive = ['ik sa','ik sam','iksvm','ik san','ik ch'+u"\u00EF", 'ikchim','ikchin','ik '+u"\u00EF", 'ik im','ikin','ik p'+u"\u00EF",'ikpim','ikpin','ik hvp'+u"\u00EF", 'ikhvpim','ikhvpin','ik hoch'+u"\u00EF", 'ikhvchim','ikhvchin','ik '+u"\u00EF",'ikim','ikin']
reflexive = ['ille']
reciprocal_personal = ['itti','itt'] #consonant preceeding form, vowel preceeding form

time = ['','tuk','tok','ch'+u"\u00EF"]

irregular_verbs = ['vbi','vmo','vla','vpa','ia']
#lexical arrays
vowels = ['a','e','i','o','u',u"\u00E1",u"\u00E9",u"\u00ED",u"\u00F3",u"\u00FA"] #what about v?
nformprobs = ['b','p','n','l']
nasals = [u"\u00E3",u"\u00EB",u"\u00EF",u"\u00F5",u"\u00FC"]

#def infinitive(verb): returns verb...is uninflected
 #   verb = verb

def subjunctive(verb):
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []
    formkmvt = form+'kmvt' #definite subjective
    formkmah = form+'kmah' #definite objective
    formhokmvt = form+'hokmvt' #distinctive subjective
    formhokmah = form+'hokmah' #distinctive objective

    for i in personal: #only present detailed
        if i == 0:
            output.append(formkmvt + ' ' + i)
            output.append(formkmah + ' ' + i)
            output.append(formhokmvt + ' ' + i)
            output.append(formhokmah + ' ' + i)
        else:
            output.append(i + ' ' + formkmvt)
            output.append(i + ' ' + formkmah)
            output.append(i + ' ' + formhokmvt)
            output.append(i + ' ' + formhokmah)

    return output

def optative(verb): #oh that whatever would happen
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []
    kbat = form+'kbat'
    kbah = form+'kb'+u"\u00E3"+'h'
    bato = form+'kbato'
    bano = form+'kbano'
    hokbat = form+'hokbat'
    hokbah = form+'hokbah'
    hokbato = form+'hokbato'
    hokbano = form+'hokbano'
    all = [kbat,kbah,bato,bano,hokbat,hokbah,hokbato,hokbano]
    for m in all:
        for i in personal:
            for j in time: #if present, add h
                if 'li' in i:
                    #output.append(form+i+' ',j)
                    if j != 0:
                        output.append(m + ' '+i +' '+ j)
                    if j == 0:
                        output.append(m + ' '+ i + 'h')
                else:
                    #output.append(i + form+j)
                    #print(i + form+j)
                    if j != 0:
                        output.append(i + ' ' + m +' '+ j)
                    if j == 0:
                        output.append(i + ' '+ m + 'h')
    return output

def potential(verb):
    #verb (a) + hinlah/hinlvshe/hinla hokek
    potential1 = ['hinlah', 'hinvlshe', 'hinla hokek']#indefinite, definite, distinctive
    potential2 = ['pullah', 'pullvchkeh', 'pulla hokeh']
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []
    # verb (a) + hinlah/hinlvshe/hinla hokek
    verb1 = form[:1]+'a'
    for i in personal:
        for j in potential1:
            if i ==0:
                output.append(verb+ ' '+'la '+ j)
            else:
                output.append(i+' '+ verb1 + ' '+ j)
    #verb + pullah/pullvchkeh/pulla hokeh
    for i in personal:
        for j in potential2:
            if i ==0:
                output.append(verb+ ' '+i + ' '+ j)
            else:
                output.append(i+' '+ verb1 + ' '+ j)

def negateform(verb): #deal with new negation arrays
    type = verb.split(', ')
    form = type[1]
    verb = form[:-1]+'o'
    output = []

    for i in negation:
        for j in time:
            output.append(i+' '+verb+' '+j)

    return output

def passive(verb):
    verb = verb

def intransitive(verb):
    # no objects
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    for i in personal:
        for j in time:
            if i is 'li':
                if j != 0:
                    output.append(form + ' ' + i + ' ' + j)
                if j == 0:
                    output.append(form + ' '+ i + 'h')
            else:
                #print(i + form+j)
                if j != 0:
                    output.append(i + ' ' + form + ' ' + j)
                if j == 0:
                    output.append(i + ' '+ form + 'h')

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
        for j in time: #if present, add h
            if 'li' in i:
                #output.append(form+i+' ',j)
                if j != 0:
                    output.append(form + ' '+i +' '+ j)
                if j == 0:
                    output.append(form + ' '+ i + 'h')
            else:
                #output.append(i + form+j)
                #print(i + form+j)
                if j != 0:
                    output.append(i + ' ' + form +' '+ j)
                if j == 0:
                    output.append(i + ' '+ form + 'h')
    return output

def imperative(verb):
    details = verb.split(',')
    verb = details[1]
    form = verb[1:]
    output = []
    #what are these pronouns?
    use = ['ik','ak','hvsh','ho','ke','keho']

    for i in use:
        output.append(i +' '+ form)
        output.append(i + ' ' + form+ ' '+ 'kiah') #negative
        output.append(i + ' ' + form[:-1]+ 'ashkeh')#imperative in shape of wish

    output.append(personal[1]+' '+form + ' nah')#don't
    output.append(personal[1]+' '+form[:-1] + 'a wah') #won't
    output.append(personal[1] + ' ' + form[:-1] + 'a heto')  # shan't
    output.append(personal[1] + ' ' + form[:-1] + 'o he keyu')  # shan't

    return output

def iterative(verb):
    #insert h + repeated vowel nasalized
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    found = False
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in form:
        if letter in vowels and found == False:
            holdindex = index
            found = True
        index += 1

    newletter = swapnasal(form[holdindex])
    newform = form[:holdindex+1] + 'h' +newletter + form[holdindex:]

    for i in personal:
        if i == 0:
            output.append(newform + ' ' + i)
        else:
            output.append(i + ' ' + newform)
    return output

def quickform(verb):
    # insert h
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    found = False
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in form:
        if letter in vowels and found == False:
            holdindex = index
            found = True
        index += 1

    #newletter = swapnasal(form[holdindex])
    newform = form[:holdindex + 1] + 'h' + form[holdindex:]

    for i in personal:
        if i == 0:
            output.append(newform + ' ' + i)
        else:
            output.append(i + ' ' + newform)
    return output

def swapnasal(letter):
    def accentvowel(letter):
        #print(letter)
        if letter is 'a':
            return nasals[0]
        if letter is 'i':
            return nasals[1]
        if letter is 'e':
            return nasals[2]
        if letter is 'o':
            return nasals[3]
        if letter is 'u':
            return nasals[4]
        else:
            return letter

def distinctive(verb):
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    found = False
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in form:
        if letter in vowels and found == False:
            holdindex = index
            found = True
        index += 1

    newletter = swapnasal(form[holdindex])
    newform = form[:holdindex] + newletter + form[holdindex:]

    for i in personal:
        if i ==0 :
            output.append(newform + ' ' + i)
        else:
            output.append(i + ' '+ newform)
    return output

def sudden(verb): #if v in verb change to a? what happens if no v?
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    if 'v' in form: #swap v for a
        form = form.replace('v','a')

    for i in personal:
        if i == 0:
            output.append(form + ' ' + i)
        else:
            output.append(i + ' ' + form)

    return output

def causal(verb):
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []
    #-chi causing of action by primitive verb
    formchi = form +'chi'
    #-chechi subject caused action (do to other,I made him put his clothes on himself)
    formchechi = form+'chechi'
    #chi plus a locative to say two things acted on each other ???
    formchilocative = form

    for i in personal:
        if i == 0:
            output.append(formchi + ' ' + i)
            output.append(formchechi + ' ' + i)
        else:
            output.append(i + ' ' + formchi)
            output.append(i + ' ' + formchechi)

    return output

def repetitive(verb):
    type = verb.split(',')
    form = type[1]
    form = form[1:]
    output = []

    #find first vowel
    found = False
    index = 0
    holdindex = 0
    # start at end of verb, find second to last vowel
    for letter in form:
        if letter in vowels and found == False:
            holdindex = index
            found = True
        index += 1

    insert = form[holdindex] + form[holdindex+1]
    newform = form[:holdindex+2] + insert + insert + form[holdindex+3:]

    for i in personal:
        if i ==0 :
            output.append(newform + ' ' + i)
        else:
            output.append(i + ' '+ newform)

    return output


#def diminitive(verb): # changes adjective to verb? such as chito --> chihto (to be largish); hopaki --> hopahki (to be rather far off)
    #verb = verb

#def intensive(verb): See page 35, there are 9 rules with no explanation of which happens when

#exceptions


def main():
    #a = open('/Users/linabrixey/PycharmProjects/inprogress/dictionary','r').readlines()
    #b = []

    #print('p'+u"\u00EF"+'lap')
    #print(negateform('VT, tahli'))
    print(imperative('vt, takchi'))




if __name__ == '__main__':
    main()