names = ["Penis", "Dick", "Cunt"]
annual_cost = [500, 600, 800]
annual_value = [3000, 2500, 4300]
net_profit = []

def evaluate():
    for x in range(len(names)):
        net_profit.append(annual_value[x] - annual_cost[x])
    print("The least valueable facility is {}, with a net profit of {}.".format(names[net_profit.index(min(net_profit))], min(net_profit)))

evaluate()