"""Show accident."""
import csv
def main():
    """"""
    file = open('database.txt')
    data = csv.reader(file)
    table = [row for row in data]
    print("แสดงจำนวนการเกิดอุบัติเหตุในช่วงเทศกาลสงกรานต์ระหว่างวันที่ 11-17")
    year, day, age = False, False, False
    while year == False:
        year = to_range(input("ช่วงเวลา(Ex. 2554-2557) : "), list(range(2551, 2558)))
        if year == False:
            print("Please input year between 2551-2557")
    province = input("จังหวัด(Ex. กรุงเทพมหานคร) : ")
    while day == False:
        day = to_range(input("วันที่เกิดเหตุ(Ex. 11-15) : "), list(range(11, 18)))
        if day == False:
            print("Please input day between 11-17")
    sex = fix_sex([input("เพศ(ถ้าต้องการดูทั้งหมดพิมพ์ All) : ").lower()])
    while age == False:
        age = to_range(input('ช่วงอายุ(Ex. 15-27) : '), list(range(1000)))
        if age == False:
            print("Please input age more than zero")
    print("Processing...")
    show = {}
    for i in year: # create dict
        show[i] = 0
    for row in table:
        if row[0] in year:
            show[row[0]] += 1 if row[1] == province and row[2] in day and row[3] in sex \
                            and row[4] in age else 0
    for i in sorted(show):
        print(i+" : "+str(show[i])+" คน")

def to_range(text, period):
    """"""
    if text[0] == '-':
        return False
    if "-" in text:
        text = [int(num) for num in text.split("-")]
    else:
        text = [int(text), int(text)]
    if text[0] not in period or text[1] not in period: # Fix period
        return False
    return [str(num) for num in list(range(text[0], text[1]+1))]

def fix_sex(sex):
    """"""
    sex = ['ชาย', 'หญิง'] if sex == ["all"] else sex
    sex = ['ชาย'] if sex == ['boy'] or sex == ['man'] or sex == ['men'] or sex == ['male'] else sex
    sex = ['หญิง'] if sex == ['girl'] or sex == ['woman'] or sex == ['female'] else sex
    return sex
main()
