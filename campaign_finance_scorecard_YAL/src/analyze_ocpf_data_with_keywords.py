import matplotlib.pyplot as plt

def get_filtered_data(filename):
    data = []
    keywords_occupation = ["Realtor", "Contractor", "Builder", "Carpenter", "Painter",
                           "Architect", "Developer", "Planner", "Environmental Reviewer", "Surveyor"]
    keywords_employer = ["Real Estate", "Construction", "Building", "Property",
                         "Property Management", "Surveyor", "Civil Engineer"]
    keywords_PACS = ['Greater Boston Real Estate Board', 'Real Estate Bar Association for MA', 'NAIOP MA']

    with open(filename) as file:
        for line in file:
            temp = []
            line = line.replace('\n', '')
            line = line.split(',')
            for i in line:
                temp.append(i)
            flag = False
            for occupation in keywords_occupation:
                if occupation.lower() in line[2].lower():
                    data.append(temp)
                    flag = True
                    break
            if not flag:
                for employer in keywords_employer:
                    if employer.lower() in line[3].lower():
                        data.append(temp)
                        flag = True
                        break
            if not flag:
                for pac in keywords_PACS:
                    if pac.lower() in line[3].lower():
                        data.append(temp)
                        break
    return data

def compute_amount_by_cpfid(data):
    cpf_id = {}
    for row in data:
        try:
            cpf_id[(row[9], row[8])] += float(row[7])
        except KeyError:
            cpf_id[(row[9], row[8])] = float(row[7])
    cpf_id = sorted(cpf_id.items(), key=lambda x:x[1])
    for key in cpf_id:
        print(key[0][0] + ": " + key[0][1] + ": " + str(key[1]))

    # with open('./temp_amount.csv', 'w') as file:
    #     for key in cpf_id:
    #         file.write(key[0][0] + ',' + key[0][1] + ',' + str(key[1]) + ',')
    #         file.write('\n')

def get_season_index(date):
    date_splited = date.split('-')
    if(date_splited[1] >= '01' and date_splited[1] <='03'):
        return 0
    elif (date_splited[1] >= '04' and date_splited[1] <= '06'):
        return 1
    elif (date_splited[1] >= '07' and date_splited[1] <= '09'):
        return 2
    elif (date_splited[1] >= '10' and date_splited[1] <= '12'):
        return 3
    else:
        raise ValueError()

def compute_amount_by_season(data):
    res = {}
    for row in data:
        try:
            res[get_season_index(row[6])] += float(row[7])
        except KeyError:
            res[get_season_index(row[6])] = float(row[7])
    num_list = []
    lable_list = []
    for item in res.items():
        print(str(item[0]) + ": " + str(item[1]))
        lable_list.append(item[0])
        num_list.append(item[1])
    plt.bar(range(len(num_list)), num_list, tick_label=lable_list)
    plt.show()
    return

def compute_amount_by_year(data):
    res = {}
    for row in data:
        try:
            res[row[6].split('-')[0]] += float(row[7])
        except KeyError:
            res[row[6].split('-')[0]] = float(row[7])
    num_list = []
    lable_list = []
    for item in res.items():
        print(str(item[0]) + ": " + str(item[1]))
        lable_list.append(item[0])
        num_list.append(item[1])
    plt.bar(range(len(num_list)), num_list, tick_label=lable_list)
    plt.show()


def computer_amount_by_size(data):
    size = {}
    amount = {}
    for i in range(6):
        size[i] = 0
        amount[i] = 0.
    for entry in data:
        if float(entry[7]) < 25:
            size[0] += 1
            amount[0] += float(entry[7])
        elif 25 <= float(entry[7]) < 100:
            size[1] += 1
            amount[1] += float(entry[7])
        elif 100 <= float(entry[7]) < 250:
            size[2] += 1
            amount[2] += float(entry[7])
        elif 250 <= float(entry[7]) < 500:
            size[3] += 1
            amount[3] += float(entry[7])
        elif 500 <= float(entry[7]) < 1000:
            size[4] += 1
            amount[4] += float(entry[7])
        else:
            size[5] += 1
            amount[5] += float(entry[7])

    print(size)
    lable_list = ['<$25', '$25-$99', '$100-$249', '$250-$499', '$500-$1000', '>$1000']
    # plt.bar(range(len(size)), size.values(), tick_label=lable_list)
    # plt.show()
    plt.bar(range(len(amount)), amount.values(), tick_label=lable_list)
    plt.show()

def computer_amount_by_city(data):
    res = {}
    for row in data:
        try:
            res[row[10].lower()] += float(row[7])
        except KeyError:
            res[row[10].lower()] = float(row[7])
    city = sorted(res.items(), key=lambda x: x[1])
    for key in city:
        print(key[0] + ": " + str(key[1]))
    print(len(city))
    return

def computer_amount_by_state(data):
    res = {}
    for row in data:
        try:
            res[row[11].upper()] += float(row[7])
        except KeyError:
            res[row[11].upper()] = float(row[7])
    state = sorted(res.items(), key=lambda x: x[1])
    distributions = [0, 0]
    for key in state:
        print(key[0] + ": " + str(key[1]))
        if key[0].upper() == 'MA':
            distributions[0] += key[1]
        else:
            distributions[1] += key[1]
    print(len(state))
    print("in state: " + str(distributions[0]))
    print("out of state: " + str(distributions[1]))
    return

def computer_amount_by_contributor_type(data):
    res = {}
    for row in data:
        try:
            res[row[12].lower()] += float(row[7])
        except KeyError:
            res[row[12].lower()] = float(row[7])
    for key in res.items():
        print(key[0] + ": " + str(key[1]))
    return



data = get_filtered_data('./temp_all.csv')
compute_amount_by_cpfid(data)
# compute_amount_by_season(data)
# compute_amount_by_year(data)
# computer_amount_by_size(data)
# computer_amount_by_city(data)
# computer_amount_by_state(data)
# computer_amount_by_contributor_type(data)
