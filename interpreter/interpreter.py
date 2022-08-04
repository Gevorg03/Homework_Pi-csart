import sys    

f = open(sys.argv[1])                                                                                                   
dict_variables = {}

def is_pop(lst):
    if lst[0] == "pop":                                                                                                         
        if lst[1][0] not in range(10):                                                                                              
            if lst[2] == ":":                                                                                                           
                if len(lst)-1 == 3:                                                                                                        
                    dict_variables[lst[1]] = lst[3]                                                                                     
                else:                                                                                                                       
                    print("Popoxakanin veragrel arjeq")                                                                                     
                    sys.exit(0)                                                                                                     
            else:                                                                                                                       
                print("Veragrman operatory sa e` :")                                                                                    
                sys.exit(0)                                                                                                     
        else:                                                                                                                       
          print("Popoxakani anuny chi karox sksvel tvov")                                                                         
          sys.exit(0)        
      
      
def is_tpel(lst):                                                                                                           
    is_finded = None                                                                                                        
    if lst[0] == "tpel":                                                                                                        
        for key in dict_variables:                                                                                                  
            if key == lst[1]:                                                                                                           
                print(dict_variables[key])                                                                                              
                is_finded = "finded"                                                                                        
    if lst[0] == "tpel":   
                if lst[1][0] == '"' and lst[1][len(lst[1])-1] == '"':
            for i in range(1, len(lst[1])-1):
                print(lst[1][i], end="")
            print("")
            return
        elif is_finded == None:
            print("Aydpisi popoxakan chi gtnvel")
            sys.exit(0)
        else:
            print("Bac e toxnvac chakert")
            sys.exit(0)


def is_ete(lst):
    if lst[0] == "ete":
        pop1, pop2 = None, None
        for key in dict_variables:
            if key == lst[1]:
                pop1 = key
            if key == lst[3]:
                pop2 = key

        if lst[2] == '>':
            if dict_variables[pop1] > dict_variables[pop2]:
                katari(lst)
        if lst[2] == '<':
            if dict_variables[pop1] < dict_variables[pop2]:
                katari(lst)
        if lst[2] == '>=':
            if dict_variables[pop1] >= dict_variables[pop2]:
                katari(lst)
        if lst[2] == '<=':
            if dict_variables[pop1] >= dict_variables[pop2]:
                katari(lst)
        if lst[2] == '==':
            if dict_variables[pop1] == dict_variables[pop2]:
                katari(lst)
        if lst[2] == '!=':
            if dict_variables[pop1] != dict_variables[pop2]:
                katari(lst)

def katari(lst):
    if lst[3] == 'katari':
        is_pop(lst[len(lst)-1])
        is_tpel(lst[len(lst)-1])


for line in f:
    lst = line.split()
    is_pop(lst)
    is_tpel(lst)
    is_ete(lst)
