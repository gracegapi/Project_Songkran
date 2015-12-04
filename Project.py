"""Show a number of accidents during songkarn festival between 10-18."""
import csv
def main():
    """"""
    file = open('database.txt')
    data = csv.reader(file)
    table = [row for row in data]
    print("แสดงจำนวนการเกิดอุบัติเหตุในช่วงเทศกาลสงกรานต์ระหว่างวันที่ 10-18")
    year, day, age = False, False, False
    while year == False:
        year = to_range(input("ช่วงเวลา(Ex. 2554-2557) : "), list(range(2551, 2558)))
        if year == False:
            print("Please input year between 2551-2557.")
    province = input("จังหวัด(Ex. กรุงเทพมหานคร) : ")
    while day == False:
        day = to_range(input("วันที่เกิดเหตุ(Ex. 11-15) : "), list(range(10, 19)))
        if day == False:
            print("Please input day between 10-18.")
    sex = fix_sex([input("เพศ(ถ้าต้องการดูทั้งหมดพิมพ์ All) : ").lower()])
    while age == False:
        age = to_range(input('ช่วงอายุ(Ex. 15-27) : '), list(range(1000)))
        if age == False:
            print("Please input age more than zero.")
    print("Processing...")
    show, status, vehicle, parties_vehicle, drink_status = {}, {}, {}, {}, {}
    for num in year: ## Create dict.
        show[num] = 0
        status[num] = {"ผู้ขับขี่": 0, "ผู้โดยสาร": 0, "คนเดินเท้า": 0, "ไม่ทราบ": 0}
        vehicle[num] = {"รถเก๋ง/แท็กซี่": 0, "จักรยานยนต์": 0, "รถจักรยาน": 0, "ไม่ทราบ": 0, \
                        "สามล้อถีบ": 0, "สามล้อเครื่อง": 0, "ไม่มี/ล้มเอง": 0, "ปิคอัพ": 0, \
                        "อื่นๆ": 0, "รถโดยสารใหญ่": 0, "รถโดยสาร4ล้อ": 0, "รถบรรทุก": 0, "รถตู้": 0}
        parties_vehicle[num] = {"รถเก๋ง/แท็กซี่": 0, "จักรยานยนต์": 0, "รถจักรยาน": 0, \
                                "ไม่ทราบ": 0, "สามล้อถีบ": 0, "สามล้อเครื่อง": 0, \
                                "ไม่มี/ล้มเอง": 0, "ปิคอัพ": 0, "อื่นๆ": 0, "รถโดยสารใหญ่": 0, \
                                "รถโดยสาร4ล้อ": 0, "รถบรรทุก": 0, "รถตู้": 0}
        drink_status[num] = {"ดื่ม": 0, "ไม่ดื่ม": 0, "ไม่ทราบ": 0}
    for row in table:
        if row[0] in year:
            if row[1] == province and row[2] in day and row[3] in sex and row[4] in age:
                show[row[0]] += 1
                status[row[0]][row[5]] += 1
                vehicle[row[0]][row[6]] += 1
                parties_vehicle[row[0]][row[7]] += 1
                drink_status[row[0]][row[8]] += 1
    for num in sorted(show):
        print(num+" : "+str(show[num])+" คน")
        if show[num] != 0:
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
        print()

def to_range(text, period):
    """Return list each number in this period depends on input entered, False otherwise."""
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

def fix_sex(sex):
    """Return sex of input entered."""
    sex = ['ชาย', 'หญิง'] if sex == ["all"] else sex
    sex = ['ชาย'] if sex == ['boy'] or sex == ['man'] or sex == ['men'] or sex == ['male'] or \
          sex == ['gentle'] or sex == ['masculine'] else sex
    sex = ['หญิง'] if sex == ['girl'] or sex == ['woman'] or sex == ['female'] or sex == ['women'] or \
          sex == ['lady'] else sex
    return sex

main()
