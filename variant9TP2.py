total_tickets = int(input("Введите общее количество билетов: "))
package_capacity = int(input("Введите количество билетов в одной упаковке: "))

full_packages = total_tickets // package_capacity
remaining_tickets = total_tickets % package_capacity
minimum_packages = (total_tickets + package_capacity - 1) // package_capacity

print("Полных упаковок:", full_packages)
print("Остаток билетов:", remaining_tickets)
print("Минимальное количество упаковок:", minimum_packages)
