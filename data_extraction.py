import pandas as pd

def compute_average(filename,variable_fields):

    form_user = pd.read_json("/Users/gerarddanjou/Downloads/{}.json".format(filename))
    data_interesting = form_user['data'][2]
    nb_user = len(data_interesting)
    cpt = []
    return_variable = []
    return_variable_name, return_variable_average = [], []

    for i in range (nb_user):
        
        entry_id = int(data_interesting[i]['entry_id']) 
        sum = 0
        
        if entry_id not in cpt :
            for j in range (nb_user):
                if int(data_interesting[j]['entry_id']) == entry_id and int(data_interesting[j]['field_id']) == 1 :
                    name_user = data_interesting[j]['value'] 
                if int(data_interesting[j]['entry_id']) == entry_id and int(data_interesting[j]['field_id']) in variable_fields :
                    sum += int(data_interesting[j]['value'])
            if sum != 0:
                #print("The average for user id : {}, name : {}".format(entry_id,name_user))            
                #print(sum/len(variable_fields))
                return_variable.append("The average for user id : {}, name : {}".format(entry_id,name_user) + "Average : " + str(sum/len(variable_fields)))
                return_variable_name.append(name_user)
                return_variable_average.append(sum/len(variable_fields))

                cpt.append(entry_id)
    
    return return_variable, return_variable_name, return_variable_average

#compute_average("file_data_2",[3,12,13,14,15,16,17,19])