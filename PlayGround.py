distance = int(input())
total_fare = 0.0

if distance <= 0:
    print(f"{total_fare:.1f}")
else:
    total_fare += 35.00
    distance -= 1

    if distance > 0:
        cal = min(distance, 9)
        total_fare += cal * 5.50
        distance -= cal

    if distance > 0:
        cal = min(distance, 10)
        total_fare += cal * 6.50
        distance -= cal

    if distance > 0:
        cal = min(distance, 20)
        total_fare += cal * 7.50
        distance -= cal

    if distance > 0:
        cal = min(distance, 20)
        total_fare += cal * 8.00
        distance -= cal

    if distance > 0:
        cal = min(distance, 20)
        total_fare += cal * 9.00
        distance -= cal

    if distance > 0:
        total_fare += distance * 10.50

    print(f"{total_fare:.1f}")