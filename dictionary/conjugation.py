transitive = open('/Users/linabrixey/PycharmProjects/chahta/transitive','r').readlines()
ditransitive = open('/Users/linabrixey/PycharmProjects/chahta/ditransitive').readlines()
intransitive = open('/Users/linabrixey/PycharmProjects/chahta/intransitive','r').readlines()
personal_pronouns = ['li','ish','','il','hash','']
pronoun_form = ['1st singular','2nd singular','3rd','1st plural','2nd plural']
object = ['sa','chi','','pi','hapi','hachi','']
negation = ['ak','chik','ik','kil','kiloh','hachik','ik']
time = ['','tuk','achin']
time_tense = ['present','past','future']

def ditransitive_simple_affirm():
    a = 0

def ditransitive_simple_neg():
    a = 0

def transitive_simple_neg(perpron,obj, stem, tiempo):
    print(negation[perpron] + object[obj] + stem + time[tiempo])

def transitive_simple_affirm(perpron,obj, stem, tiempo):
    #takes second series pronouns (chi, hachi) for object
    #takes first series for subject pronoun (negation attaches here)
    #ish sa pinsa = you saw me
    print(personal_pronouns[perpron]+object[obj]+stem+time[tiempo])

def intransitive_simple_neg(perpron,stem,tiempo):
    stem = stem[:-1]+'o'
    print(negation[perpron]+stem+time[tiempo])

def intransitive_simple_affirm(perpron,stem,tiempo): #start here
    #apilalituk (I help)
    if tiempo == 2 and perpron !=0:
        #a = stem.split()
        #print(a)
        a = stem[:-1]
        print(a)
        stem = ''.join(a)
        print(stem)
        if perpron == 0:
            print(stem+personal_pronouns[0]+time[tiempo])
        else:
            print(personal_pronouns[perpron]+stem+time[tiempo])
    if tiempo == 2 and perpron ==0:
        print(stem+'l'+time[tiempo])

def recognize(word):

    #recognize time
    i = 1
    not_present = True
    while i <len(time):
        if time[i] in word:
            print(time_tense[i])
            not_present = False
            #now remove the time marker
            removetime = len(time_tense[i])-1
            word = word[:-removetime]
        i+=1
    if not_present == True:
        print('present')
    #print(word)


    #negative personal prounouns
    midway = len(word)/2
    foundpronoun = False
    if 'k' in word[:-midway]:
        i = 0
        while i<len(negation) and (foundpronoun == False):
            if negation[i] in word[:-midway]:
                foundpronoun = True
                print("negative "+ pronoun_form[i])
                remove = len(negation[i])
                word = word[remove:]
            i+=1
        #and remove o suffix
        word = word[:-1]

    #affirmative personal prounouns
    choppedstem = word[:4]
    i=1
    midway = len(word) / 2
    #print(choppedstem)
    while (i< (len(personal_pronouns)-1)) and (foundpronoun == False):
        if i !=2:#skips 3rd
            a = personal_pronouns[i]
            if a in choppedstem:
                foundpronoun=True
                #print(a)
                print(pronoun_form[i])
                #print('found')
                b = len(a)
                word = word[b:]
        i+=1
    if foundpronoun == False:
        choppedforli = list(word)
        lengthchopped = len(choppedforli)-1
        #print(choppedforli)
        choppedforli2 = choppedforli[lengthchopped-1]+choppedforli[lengthchopped]
        if 'l' in choppedforli[lengthchopped]:
            foundpronoun = True
            print('1st singular pronoun')
            # update stem
            word = word[:-1]
        elif 'li' in choppedforli2:
            foundpronoun = True
            print('1st singular pronoun')
            #update stem
            word = word[:-2]
            #print(word)
    if foundpronoun == False:
        print('3rd person pronoun')
    #print(word)

    #print(choppedstem)
    for i in transitive:
        if word in i:
            print('transitive verb')
            print(i.strip())
            j = transitive.index(i)
            print(transitive[j+1])
    for k in intransitive:
        if word in k:
            print('intransitive verb')
            print(k.strip())
            l = intransitive.index(k)
            print(intransitive[l+1])
    for m in ditransitive:
        if word in m:
            print('ditransitive verb')
            print(m.strip())
            n = ditransitive.index(m)
            print(ditransitive[n+1])


def build():
    given = 'pinsa'
    affirm = 1
    if affirm == 0:
        #intransitive_simple_affirm(0, given, 2)
        transitive_simple_affirm(1,3,given,0)
    else:
        #intransitive_simple_neg(0, given, 0)
        transitive_simple_neg(1,3,given,0)

def main():
    build()
    #recognize('ishpinsatuk')

if __name__ == '__main__':
    main()