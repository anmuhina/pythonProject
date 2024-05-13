#ВАРИАНТ 10
import xmltodict
from geopy.distance import geodesic

fin = open('10.osm', 'r', encoding = 'utf-8')
#fin = open('10 - 2.osm', 'r', encoding = 'utf-8')
osm_dict = xmltodict.parse(fin.read())

# Получаем все скамейки и их координаты
benches = []
benches_coordinates = []
for element in osm_dict['osm']['node'] + osm_dict['osm']['way'] + osm_dict['osm']['relation']:
    if 'tag' in element:
        tags = element['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'amenity' and tag['@v'] == 'bench':
                    benches.append(element)
                    if '@lat' in element and '@lon' in element:
                        bench_coords = (float(element['@lat']), float(element['@lon']))
                        benches_coordinates.append(bench_coords)
                    break
        elif isinstance(tags, dict):
            if tags['@k'] == 'amenity' and tags['@v'] == 'bench':
                benches.append(element)
                if '@lat' in element and '@lon' in element:
                    bench_coords = (float(element['@lat']), float(element['@lon']))
                    benches_coordinates.append(bench_coords)
count_benches = len(benches)
print("Общее количество скамеек:", count_benches)

# Подсчет количества скамеек каждого типа
benches_types = {}
for bench in benches:
    if 'tag' in bench:
        tags = bench['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag.get('@k') == 'bench:type':
                    bench_type = tag.get('@v', 'unknown')
                    benches_types[bench_type] = benches_types.get(bench_type, 0) + 1
        elif isinstance(tags, dict):
            if tags.get('@k') == 'bench:type':
                bench_type = tags.get('@v', 'unknown')
                benches_types[bench_type] = benches_types.get(bench_type, 0) + 1

if not benches_types:
    print("В данном файле у скамеек не указаны типы с помощью тега 'bench:type'.")
else:
    print("Количество скамеек каждого типа:")
    for bench_type, count in benches_types.items():
        print(f"{bench_type}: {count}")

# Получаем все аптеки и их координаты
pharmacies = []
pharmacies_coordinates = []
for element in osm_dict['osm']['node'] + osm_dict['osm']['way'] + osm_dict['osm']['relation']:
    if 'tag' in element:
        tags = element['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'amenity' and tag['@v'] == 'pharmacy':
                    if '@lat' in element and '@lon' in element:
                        pharmacies.append(element)
                        pharmacy_coords = (float(element['@lat']), float(element['@lon']))
                        pharmacies_coordinates.append(pharmacy_coords)
                    break
        elif isinstance(tags, dict):
            if tags['@k'] == 'amenity' and tags['@v'] == 'pharmacy':
                if '@lat' in element and '@lon' in element:
                    pharmacies.append(element)
                    pharmacy_coords = (float(element['@lat']), float(element['@lon']))
                    pharmacies_coordinates.append(pharmacy_coords)
count_pharmacies = len(pharmacies)
print("Общее количество аптек:", count_pharmacies)

# Считаем количество скамеек, рядом с которыми есть аптеки (в радиусе 100м)
radius = 100
count_benches_near_pharmacies = 0
for bench in benches_coordinates:
    for pharmacy in pharmacies_coordinates:
        distance = geodesic(bench, pharmacy).meters
        if distance < radius:
            count_benches_near_pharmacies += 1
            break
print("Количество скамеек, рядом с которыми есть аптеки:", count_benches_near_pharmacies)
