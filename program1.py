# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Profit Prophet
# Date:        11/04/20

names = ["Poop", "Shit", "Crap"]
annual_cost = [500, 600, 800]
annual_value = [3000, 2500, 4300]
net_profit = []

def evaluate():
    for x in range(len(names)):
        net_profit.append(annual_value[x] - annual_cost[x])
    print("The least valueable facility is {}, with a net profit of {}.".format(names[net_profit.index(min(net_profit))], min(net_profit)))

evaluate()