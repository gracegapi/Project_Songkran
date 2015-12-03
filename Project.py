"""Show accident"""
import csv
def main():
    """"""
    file = open('database.txt')
    data = csv.reader(file)
    table = [row for row in data]
    print("แสดงจำนวนการเกิดอุบัติเหตุในช่วงสงกรานต์")
    year = to_range(input("ช่วงเวลา(ex. 2554-2557) : "))
    city = input("จังหวัด : ")
    day = to_range(input("วันที่เกิดเหตุ(ex. 11-15) : "))
    sex = [input("เพศ(ถ้าต้องการดูทั้งหมดพิมพ์ all) : ").lower()]
    sex = ['ชาย', 'หญิง'] if sex == ["all"] else sex
    sex = ['ชาย'] if sex == ['boy'] or sex == ['man'] or sex == ['men'] or sex == ['male'] else sex
    sex = ['หญิง'] if sex == ['girl'] or sex == ['woman'] or sex == ['female'] else sex
    age = to_range(input('ช่วงอายุ(ex. 15-27) : '))
    print("Processing...")
    show = {}
    for i in year:
        show[i] = 0
    for i in table:
        if i[0] in year:
            show[i[0]] += 1 if i[1] == city and i[2] in day and i[3] in sex and i[4] in age else 0
    for i in sorted(show):
        print(i+" : "+str(show[i])+" คน")
def to_range(text):
    if "-" in text:
        text = [int(i) for i in text.split("-")]
    else:
        text = [int(text), int(text)]
    return [str(i) for i in list(range(text[0], text[1]+1))]
main()
