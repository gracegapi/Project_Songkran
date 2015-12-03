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
    show, status = {}, {"ผู้ขับขี่": 0, "ผู้โดยสาร": 0, "คนเดินเท้า": 0, "ไม่ทราบ": 0, "จักรยานยนต์": 0}
    for num in year: ## Create dict.
        show[num] = 0
    for row in table:
        if row[0] in year:
            if row[1] == province and row[2] in day and row[3] in sex and row[4] in age:
                show[row[0]] += 1
                status[row[5]] += 1
    for num in sorted(show):
        print(num+" : "+str(show[num])+" คน")
        for number in sorted(status):
            print(number+" : "+str(status[number])+" คน")

def to_range(text, period):
    """Return list each number in this period depends on input entered."""
    if text[0] == '-':
        return False
    for i in text:
        if i.isalpha():
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
