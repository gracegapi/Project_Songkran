"""Show a number of accidents during songkarn festival between 10-18."""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
def main():
    """"""
    file = open('database.txt')
    data = csv.reader(file)
    table = [row for row in data]
    print("แสดงจำนวนการเกิดอุบัติเหตุในช่วงเทศกาลสงกรานต์ระหว่างวันที่ 10-18")
    year = False
    while year == False:
        year = to_range(input("ช่วงเวลา(Ex. 2554-2557) : "), list(range(2551, 2558)))
        if year == False:
            print("Please input year between 2551-2557.")
    province = input("จังหวัด(Ex. กรุงเทพมหานคร) : ")
    print("Processing...")
    total, status, vehicle, parties_vehicle = {}, {}, {}, {}
    drink_status, day_dict, age_dict, sex_dict = {}, {}, {}, {}
    for num in year: ## Create dict.
        total[num] = 0
        status[num] = {"ผู้ขับขี่": 0, "ผู้โดยสาร": 0, "คนเดินเท้า": 0, "ไม่ทราบ": 0}
        vehicle[num] = {"รถเก๋ง/แท็กซี่": 0, "จักรยานยนต์": 0, "รถจักรยาน": 0, "ไม่ทราบ": 0, \
                        "สามล้อถีบ": 0, "สามล้อเครื่อง": 0, "ไม่มี/ล้มเอง": 0, "ปิคอัพ": 0, \
                        "อื่นๆ": 0, "รถโดยสารใหญ่": 0, "รถโดยสาร4ล้อ": 0, "รถบรรทุก": 0, "รถตู้": 0}
        parties_vehicle[num] = {"รถเก๋ง/แท็กซี่": 0, "จักรยานยนต์": 0, "รถจักรยาน": 0, \
                                "ไม่ทราบ": 0, "สามล้อถีบ": 0, "สามล้อเครื่อง": 0, \
                                "ไม่มี/ล้มเอง": 0, "ปิคอัพ": 0, "อื่นๆ": 0, "รถโดยสารใหญ่": 0, \
                                "รถโดยสาร4ล้อ": 0, "รถบรรทุก": 0, "รถตู้": 0}
        drink_status[num] = {"ดื่ม": 0, "ไม่ดื่ม": 0, "ไม่ทราบ": 0}
        day_dict[num] = {'10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}\
            if num == '2552' else {'12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0}\
            if num == '2553' else {'11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0}
        age_dict[num] = {'ไม่ทราบ': {'ชาย': 0, 'หญิง': 0}, '1-20': {'ชาย': 0, 'หญิง': 0}, '21-40': {'ชาย': 0, 'หญิง': 0}, \
                         '41-60': {'ชาย': 0, 'หญิง': 0}, '61-100': {'ชาย': 0, 'หญิง': 0}}
        sex_dict[num] = {"ชาย": 0, "หญิง": 0}
    for row in table:
        if row[0] in year and row[1] == province:
            total[row[0]] += 1
            status[row[0]][row[5]] += 1
            vehicle[row[0]][row[6]] += 1
            parties_vehicle[row[0]][row[7]] += 1
            drink_status[row[0]][row[8]] += 1
            day_dict[row[0]][row[2]] += 1
            sex_dict[row[0]][row[3]] += 1
            if int(row[4]) in range(1, 21):
                age_dict[row[0]]['1-20'][row[3]] += 1
            elif int(row[4]) in range(21, 41):
                age_dict[row[0]]['21-40'][row[3]] += 1
            elif int(row[4]) in range(41, 61):
                age_dict[row[0]]['41-60'][row[3]] += 1
            elif int(row[4]) in range(61, 100):
                age_dict[row[0]]['61-100'][row[3]] += 1
            else:
                age_dict[row[0]]['ไม่ทราบ'][row[3]] += 1
    for num in sorted(total):
        print("ผู้ประสบอุบัติเหตุในปี "+num+" : "+str(total[num])+" คน")
        if total[num] != 0:
            print("* จำนวนผู้ประสบอุบัติเหตุในแต่ละวัน *")
            for day in sorted(day_dict[num]):
                print("วันที่ "+day+" จำนวน "+str(day_dict[num][day])+" คน")
            print("* เพศของผู้ประสบอุบัติเหตุ *")
            for text in sorted(sex_dict[num]):
                if sex_dict[num][text] != 0:
                    print(text+" : "+str(sex_dict[num][text])+" คน")
            print("* สถานะของผู้ประสบอุบัติเหตุ *")
            for text in sorted(status[num]):
                if status[num][text] != 0:
                    print(text+" : "+str(status[num][text])+" คน")
            print("* ยานพาหนะของผู้ประสบอุบัติเหตุ *")
            for text in sorted(vehicle[num]):
                if vehicle[num][text] != 0:
                    print(text+" : "+str(vehicle[num][text])+" คัน")
            print("* ยานพาหนะของคู่กรณี *")
            for text in sorted(parties_vehicle[num]):
                if parties_vehicle[num][text] != 0:
                    print(text+" : "+str(parties_vehicle[num][text])+" คัน")
            print("* สถานะการดื่มของผู้ประสบอุบัติเหตุ *")
            for text in sorted(drink_status[num]):
                if drink_status[num][text] != 0:
                    print(text+" : "+str(drink_status[num][text])+" คน")
            graph_seven(day_dict, num, province) ## Creat graph of seven dangerous days.
            graph_drink_status(drink_status, num, province) ## Create graph of drink status.
            graph_vehicle(vehicle, parties_vehicle, num, province) ## Create graph of vehicles.
            graph_sex(sex_dict, age_dict, num, province) ## Creat graph of sex.
        print()

def to_range(text, period):
    """Return list each number in this period depends on values incame, False otherwise."""
    if text[0] == '-':
        return False
    for char in text:
        if char.isalpha():
            return False
    if "-" in text:
        text = [int(num) for num in text.split("-")]
    else:
        text = [int(text), int(text)]
    if text[0] not in period or text[1] not in period: ## Fix period.
        return False
    return [str(num) for num in list(range(text[0], text[1]+1))]

def graph_vehicle(vehicle, parties_vehicle, year, province):
    """Creat graph of vehicles depends on values incame."""
    data = []
    for text in sorted(vehicle[year]):
        if vehicle[year][text] == 0 and parties_vehicle[year][text] == 0:
            continue
        data.append(go.Bar(x = ["ยานพาหนะของผู้ประสบอุบัติเหตุ", "ยานพาหนะของคู่กรณี"], \
                           y = [vehicle[year][text], parties_vehicle[year][text]], name = text))
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Vehicles graph '+year+' '+province)

def graph_seven(day_dict, year, province):
    """Creat graph of seven dangerous days depends on values incame."""
    days_list, num_people = [], []
    for days in sorted(day_dict[year]):
        if day_dict[year][days] != 0:
            days_list.append('วันที่ ' + str(days))
            num_people.append(day_dict[year][days])
    fig = {'data': [{'labels': days_list, 'values': num_people, 'type': 'pie'}], \
           'layout': {'title': 'Graph of seven dangerous days in ' + str(int(year)-543)}}
    url = py.plot(fig, filename='Seven dangerous days graph '+year+' '+province)

def graph_sex(sex_dict, age_dict, year, province):
    """Creat graph of sex depends on values incame."""
    data = []
    for text in sorted(sex_dict[year]):
        horizontal = ["เพศ", "ช่วงอายุ 1-20", "ช่วงอายุ 21-40", "ช่วงอายุ 41-60", "ช่วงอายุ 61-100"]
        vertical = [sex_dict[year][text], age_dict[year]['1-20'][text], \
                    age_dict[year]['21-40'][text], age_dict[year]['41-60'][text], \
                    age_dict[year]['61-100'][text]]
        if age_dict[year]['ไม่ทราบ']['ชาย'] != 0 or age_dict[year]['ไม่ทราบ']['หญิง'] != 0:
            horizontal.append("ไม่ทราบอายุ")
            vertical.append(age_dict[year]['ไม่ทราบ'][text])
        data.append(go.Bar(x = horizontal, y = vertical, name = text))
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Sex graph '+year+' '+province)

def graph_drink_status(drink_status, year, province):
    """Creat graph of drink status depends on values incame."""
    drink_list, num_people = [], []
    for text in sorted(drink_status[year]):
        if drink_status[year][text] != 0:
            drink_list.append(text)
            num_people.append(drink_status[year][text])
    fig = {'data': [{'labels': drink_list, 'values': num_people, 'type': 'pie'}], \
           'layout': {'title': 'Graph of drink status'}}
    url = py.plot(fig, filename='Drink status graph '+year+' '+province)

main()
