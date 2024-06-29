rooms = int(input())
result = list()
total_chairs = ""
total_visitors = 0
for room in range(1, rooms + 1):
    info = input().split(" ")
    chairs = info[0]
    visitors = int(info[1])
    total_chairs += chairs
    total_visitors += visitors
    if visitors > len(chairs):
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")


chairs_count = len(total_chairs)
if chairs_count >= total_visitors:
    print(f"Game On, {chairs_count - total_visitors} free chairs left")

