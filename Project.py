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
    year = 'False'
    while year == 'False':
        year = to_range(input("ช่วงเวลา(Ex. 2554-2557) : "), list(range(2551, 2558)))
        if year == 'False':
            print("Please input year between 2551-2557.")
    province = input("จังหวัด(Ex. กรุงเทพมหานคร) : ")
    print("Processing...")
    total, status, vehicle, parties_vehicle, treatment = {}, {}, {}, {}, {}
    drink_status, days, age, sex = {}, {}, {}, {}
    for num in year:  # Create dict.
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
        days[num] = {'10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}\
            if num == '2552' else {'12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0}\
            if num == '2553' else {'11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0}
        age[num] = {'ไม่ทราบ': {'ชาย': 0, 'หญิง': 0}, '1-20': {'ชาย': 0, 'หญิง': 0}, \
                    '21-40': {'ชาย': 0, 'หญิง': 0}, '41-60': {'ชาย': 0, 'หญิง': 0}, \
                    '61-100': {'ชาย': 0, 'หญิง': 0}}
        sex[num] = {"ชาย": 0, "หญิง": 0}
        treatment[num] = {'heal': 0, 'dead': 0}
    for row in table:
        if row[0] in year and row[1] == province:
            total[row[0]] += 1
            status[row[0]][row[5]] += 1
            vehicle[row[0]][row[6]] += 1
            parties_vehicle[row[0]][row[7]] += 1
            drink_status[row[0]][row[8]] += 1
            days[row[0]][row[2]] += 1
            sex[row[0]][row[3]] += 1
            if int(row[4]) in range(1, 21):
                age[row[0]]['1-20'][row[3]] += 1
            elif int(row[4]) in range(21, 41):
                age[row[0]]['21-40'][row[3]] += 1
            elif int(row[4]) in range(41, 61):
                age[row[0]]['41-60'][row[3]] += 1
            elif int(row[4]) in range(61, 100):
                age[row[0]]['61-100'][row[3]] += 1
            else:
                age[row[0]]['ไม่ทราบ'][row[3]] += 1
            if row[9] == 'ทุเลา/หาย':
                treatment[row[0]]['heal'] += 1
            else:
                treatment[row[0]]['dead'] += 1
    for num in sorted(total):
        print("ผู้ประสบอุบัติเหตุในปี "+num+" : "+str(total[num])+" คน")
        if total[num] != 0:
            print("* จำนวนผู้ประสบอุบัติเหตุในแต่ละวัน *")
            for day in sorted(days[num]):
                print("วันที่ "+day+" จำนวน "+str(days[num][day])+" คน")
            print("* เพศของผู้ประสบอุบัติเหตุ *")
            for text in sorted(sex[num]):
                if sex[num][text] != 0:
                    print(text+" : "+str(sex[num][text])+" คน")
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
            print("* ช่วงอายุของผู้ประสบอุบัติเหตุ *")
            for text in sorted(age[num]):
                print(text+" : ", end="")
                for text2 in sorted(age[num][text]):
                    print(text2+" "+str(age[num][text][text2])+" คน", end=" ")
                print()
            print("* จำนวนรอดชีวิตและเสียชีวิต *")
            print("ผู้รอดชีวิต"+" : "+str(treatment[num]['heal'])+" คน")
            print("ผู้เสียชีวิต"+" : "+str(treatment[num]['dead'])+" คน")
            graph_seven(days, num, province)  # Create graph of seven dangerous days.
            graph_drink_status(drink_status, num, province)  # Create graph of drink status.
            graph_vehicle(vehicle, parties_vehicle, num, province)  # Create graph of vehicles.
            graph_sex(sex, age, num, province)  # Create graph of sex.
            graph_treatment(treatment, num, province)  # Create graph of treatment.
        print()


def to_range(text, period):
    """Return list each number in this period depends on values incame, 'False' otherwise."""
    if text[0] == '-':
        return 'False'
    for char in text:
        if char.isalpha():
            return 'False'
    if "-" in text:
        text = [int(num) for num in text.split("-")]
    else:
        text = [int(text), int(text)]
    if text[0] not in period or text[1] not in period: # Fix period.
        return 'False'
    return [str(num) for num in list(range(text[0], text[1]+1))]


def graph_vehicle(vehicle, parties_vehicle, year, province):
    """Create graph of vehicles depends on values incame."""
    data = []
    for text in sorted(vehicle[year]):
        if vehicle[year][text] == 0 and parties_vehicle[year][text] == 0:
            continue
        data.append(go.Bar(x=["ยานพาหนะของผู้ประสบอุบัติเหตุ", "ยานพาหนะของคู่กรณี"], \
                           y=[vehicle[year][text], parties_vehicle[year][text]], name=text))
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Vehicles graph '+year+' '+province)


def graph_seven(days, year, province):
    """Create graph of seven dangerous days depends on values incame."""
    days_list, num_people = [], []
    for day in sorted(days[year]):
        if days[year][day] != 0:
            days_list.append('วันที่ ' + str(day))
            num_people.append(days[year][day])
    fig = {'data': [{'labels': days_list, 'values': num_people, 'type': 'pie'}], \
           'layout': {'title': 'Graph of seven dangerous days'}}
    url = py.plot(fig, filename='Seven dangerous days graph '+year+' '+province)


def graph_sex(sex, age, year, province):
    """Create graph of sex depends on values incame."""
    data = []
    for text in sorted(sex[year]):
        horizontal = ["เพศ", "ช่วงอายุ 1-20", "ช่วงอายุ 21-40", "ช่วงอายุ 41-60", "ช่วงอายุ 61-100"]
        vertical = [sex[year][text], age[year]['1-20'][text], age[year]['21-40'][text], \
                    age[year]['41-60'][text], age[year]['61-100'][text]]
        if age[year]['ไม่ทราบ']['ชาย'] != 0 or age[year]['ไม่ทราบ']['หญิง'] != 0:
            horizontal.append("ไม่ทราบอายุ")
            vertical.append(age[year]['ไม่ทราบ'][text])
        data.append(go.Bar(x=horizontal, y=vertical, name=text))
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Sex graph '+year+' '+province)


def graph_drink_status(drink_status, year, province):
    """Create graph of drink status depends on values incame."""
    drink_list, num_people = [], []
    for text in sorted(drink_status[year]):
        if drink_status[year][text] != 0:
            drink_list.append(text)
            num_people.append(drink_status[year][text])
    fig = {'data': [{'labels': drink_list, 'values': num_people, 'type': 'pie'}], \
           'layout': {'title': 'Graph of drink status'}}
    url = py.plot(fig, filename='Drink status graph '+year+' '+province)


def graph_treatment(treatment, year, province):
    """Create graph of treatment depends on values incame."""
    data = []
    data.append(go.Bar(x=["จำนวนผู้รอดชีวิตและผู้เสียชีวิต"], y=[treatment[year]['heal']], \
                       name='ผู้รอดชีวิต'))
    data.append(go.Bar(x=["จำนวนผู้รอดชีวิตและผู้เสียชีวิต"], y=[treatment[year]['dead']], \
                       name='ผู้เสียชีวิต'))
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Treatment graph '+year+' '+province)

main()
