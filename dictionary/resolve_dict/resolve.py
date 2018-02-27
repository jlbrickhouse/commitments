

def findverbs():
    openseseame = open('/Users/linabrixey/PycharmProjects/chahta/resolve_dict/byingtondictionary_original',
                       'r').readlines()
    # closeseseame = open('/Users/brixey/PycharmProjects/chahta/resolve_dict/resolveddictionary', 'w')
    count = 0

    for i in openseseame:
        if 'v. t.' in i:
            print i.strip()
            count += 1
        elif 'v. i.' in i:
            print i.strip()
            count += 1
        elif 'v. n.' in i:
            print i.strip()
            count += 1
        elif 'v. a. i.' in i:
            print i.strip()
            count += 1
        elif 'v. tr.' in i:
            print i.strip()
            count += 1
        elif 'intr.' in i:
            print i.strip()
            count += 1
        elif 'v. n.' in i:
            print i.strip()
            count += 1
        elif 'v., a., i.,' in i:
            print i.strip()
            count += 1
        elif 'v., t.,' in i:
            print i.strip()
            count += 1
        elif 'v., n.,' in i:
            print i.strip()
            count += 1

    print(count)

def replacements():
    openseseame = open('/Users/linabrixey/PycharmProjects/chahta/resolve_dict/verbs_only',
                       'r').readlines()
    for i in openseseame:

        i = i.replace('a n ', u"\u00E3")  # nasalized a is Z
        i = i.replace('e n ', u"\u00EB")
        i = i.replace('i n ', u"\u0129")  # nasalized i is R
        i = i.replace('o n ', u"\u00F5")  # nasalized o is G
        i = i.replace('u n ', u"\u0169")  # nasalized u is X
        i = i.strip()
        print(i)

def replace():
    openseseame = open('/Users/linabrixey/PycharmProjects/chahta/resolve_dict/clean',
                       'r').readlines()
    for i in openseseame:
        i = i.replace('(','')
        i = i.replace(')','')
        i = i.replace('[','')
        i = i.replace(']','')
        i = i.replace("'",'')
        i = i.replace(',,',',')
        i = i.strip()
        print i

def extractverbtype():
    openseseame = open('/Users/linabrixey/PycharmProjects/chahta/resolve_dict/verbs_nasalscorrected',
                       'r').readlines()

    for i in openseseame:
        i = i.partition('.,')[0]

        print i

def switch():
    openseseame = open('/Users/linabrixey/PycharmProjects/chahta/resolve_dict/final_verbs',
                       'r').readlines()
    #u"\u00E3",u"\u00EB",u"\u00EF",u"\u00F5",u"\u00FC"
    for i in openseseame:
        #i = i.replace(u"\u00E3", u"\u00E3")  # nasalized a is Z
        #i = i.replace(u"\u00EB", u"\u00EB")
        i = i.replace(u"\u00EF", u"\u0129")  # nasalized i is R
        #i = i.replace(u"\u00F5", u"\u00F5")  # nasalized o is G
        i = i.replace(u"\u00FC", u"\u0169")  # nasalized u is X
        i = i.strip()
        print(i)

def main():
    #findverbs();
    #replacements();
    #replace()
    #extractverbtype()
    #print(u"\u0169")
    switch()

if __name__ == '__main__':
    main()