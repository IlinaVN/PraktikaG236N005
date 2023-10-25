import matplotlib.pyplot as plt
import seaborn as sns
def knapsack(cap, values, weights):
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            cap_left -= item['weight']
        elif cap_left > 0:
            total += item['vpw'] * cap_left
            cap_left = 0
    return total


def plot_memtable(V, stuffdict):
    plt.figure(figsize=(30,15))
    item_list = list(stuffdict.keys())
    item_list.insert(0, 'empty')
    sns.heatmap(V, yticklabels=item_list)
    plt.yticks(size=25)
    plt.xlabel('Area', size=25)
    plt.ylabel('Added item', size=25)
    plt.title('Value for Area with Set of Items', size=30)
    plt.show()

stuffdict = {'couch_s':(300,75),
             'couch_b':(500,80),
             'bed':(400,100),
             'closet':(200,50),
             'bed_s':(200,40),
             'desk':(200,70),
             'table':(300,80),
             'tv_table':(200,30),
             'armchair':(100,30),
             'bookshelf':(200,60),
             'cabinet':(150,20),
             'game_table':(150,30),
             'hammock':(250,45),
             'diner_table_with_chairs':(250,70),
             'stools':(150,30),
             'mirror':(100,20),
             'instrument':(300,70),
             'plant_1':(25,10),
             'plant_2':(30,20),
             'plant_3':(45,25),
             'sideboard':(175,30),
             'chest_of_drawers':(25,40),
             'guest_bed':(250,40),
             'standing_lamp':(20,30),
             'garbage_can':(30,35),
             'bar_with_stools':(200,40),
             'bike_stand':(100,80),
             'chest':(150,25),
             'heater':(100,25)
            }
cap = 2000
weights = [300, 500, 400, 200, 200, 200, 300, 200, 100, 200, 150, 150, 250, 250, 150, 100, 300, 25, 30, 45, 175, 25, 250, 20, 30, 200, 100, 150, 100]
values = [75, 80, 100, 50, 40, 70, 80, 30, 30, 60, 20, 30, 45, 70, 30, 20, 70, 10, 20, 25, 30, 40, 40, 30, 35, 40, 80, 25, 25]
print(knapsack(cap, values, weights))