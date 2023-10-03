import random

binary_choice = ['yes', 'no']
search_choice = ['online', 'in-person']
in_person_jobs = [['cut grass', 10], ['move furniture', 20], ['walk dogs', 15], ['wash cars', 25]]
locations = [['Burger King', 10], ['Walmart', 12], ['Lowes', 15]]
days = [['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], ['Saturday', 'Sunday']]
time = [['Morning', 4], ['Afternoon', 4], ['Evening', 4], ['Night', 12]]
neighbors = ['Bob', 'Ricky', 'Mary', 'Martha', 'David']

weekend = days[1]
weekdays = days[0]
week = weekdays + weekend
daytime = time[0][1] + time[1][1]
nighttime = time[2][1] + time[3][1]
sleep = time[3][1]

bk_pay = locations[0][1]
wmart_pay = locations[1][1]
lowes_pay = locations[2][1]

grass_pay = in_person_jobs[0][1]
furniture_pay = in_person_jobs[1][1]
dog_pay = in_person_jobs[2][1]
car_pay = in_person_jobs[3][1]

all_days = int(len(days[0])+len(days[1]))

def append(x):
    list = []
    new_list = []

    for item in x:
        list.append(item[0])

    for item1 in list:
        new_list.append(item1)

    return new_list

neighbor_jobs = append(in_person_jobs)
n_jobs = random.choice(neighbor_jobs)
