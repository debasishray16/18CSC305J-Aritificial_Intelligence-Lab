# Toy Problem (Camel-Banana Problem)

A camel is carrying a load of bananas across the desert. The camel can only carry a certain maximum load capacity of bananas at a time. The camel needs to travel a certain distance to reach its destination. However, the camel eats one banana every mile it travels. The task is to find out how many bananas the camel can reach the destination with, given the total number of bananas at the start, the distance to be covered, and the maximum load capacity of the camel.

```py

total = int(input('Enter the total no. of bananas at the start: '))
distance = int(input('Enter the distance which is to be covered: '))
load_capacity = int(input('Enter maximum load capacity of the camel: '))

lost_bananas = 0
bananas = total

for i in range(distance):
    bananas -= load_capacity  # Subtract the load capacity from bananas

    if bananas < 0:
        bananas = 0  # If bananas go negative, set it to 0
        break

    lost_bananas += 1  # Increment lost bananas by 1 for each step

print("Bananas left:", bananas)
print("Total bananas lost:", lost_bananas)

```
