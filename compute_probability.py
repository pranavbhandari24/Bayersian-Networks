import sys

def compute_probability(b, e, a, j, m):
    result = 1
    if b:
        result = result * 0.001
    else:
        result = result * 0.999

    if e:
        result = result * 0.002
    else:
        result = result * 0.998

    if b and e:
        temp = 0.95
    elif b and not e:
        temp = 0.94
    elif not b and e:
        temp = 0.29
    else: 
        temp = 0.001

    if a:
        result = result * temp
        temp1 = 0.9
        temp2 = 0.7
    else:
        result = result * (1 - temp)
        temp1 = 0.05
        temp2 = 0.01
 
    if j:
        result = result * temp1
    else:
        result = result * (1-temp1)
    
    if m:
        result = result * temp2
    else:
        result = result * (1-temp2)
    
    return result

def total_prob(values):
    b_values = []
    e_values = []
    a_values = []
    j_values = []
    m_values = []
    
    if 'b' in values:
        b_values.append(values['b'])
    else:
        b_values.append(True)
        b_values.append(False)

    if 'e' in values:
        e_values.append(values['e'])
    else:
        e_values.append(True)
        e_values.append(False)

    if 'a' in values:
        a_values.append(values['a'])
    else:
        a_values.append(True)
        a_values.append(False)

    if 'j' in values:
        j_values.append(values['j'])
    else:
        j_values.append(True)
        j_values.append(False)
    
    if 'm' in values:
        m_values.append(values['m'])
    else:
        m_values.append(True)
        m_values.append(False)

    result = 0
    for b1 in b_values:
        for e1 in e_values:
            for a1 in a_values:
                for j1 in j_values:
                    for m1 in m_values:
                        result = result + compute_probability(b1, e1, a1, j1, m1)
    return result

def main(argc, argv):
    if argc == 1:
        print('Please Enter Arguments to calculate Probability')
        exit(0)
    var = {}
    given= {}
    temp = 0
    for word in argv:
        if word == argv[0]:
            continue
        if word == 'given':
            temp = 1
            continue
        if temp == 0:
            if word[1].lower() == 't':
                var[word[0].lower()] = True
            else:
                var[word[0].lower()] = False
        else:
            if word[1].lower() == 't':
                given[word[0].lower()] = True
            else:
                given[word[0].lower()] = False

    var.update(given)
    num = total_prob(var)

    if given:
        den = total_prob(given)
    else:
        den = 1
    print("Probability =  {}".format(num/den))
    

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)