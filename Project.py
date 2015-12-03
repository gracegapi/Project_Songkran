"""Show accident."""
import csv
def main():
    """"""
    file = open('database.txt')
    data = csv.reader(file)
    table = [row for row in data]
    print("แสดงจำนวนการเกิดอุบัติเหตุในช่วงเทศกาลสงกรานต์ระหว่างวันที่ 11-17")
    year = to_range(input("ช่วงเวลา(Ex. 2554-2557) : "))
    province = input("จังหวัด(Ex. กรุงเทพมหานคร) : ")
    day = to_range(input("วันที่เกิดเหตุ(Ex. 11-15) : "))
    sex = [input("เพศ(ถ้าต้องการดูทั้งหมดพิมพ์ All) : ").lower()]
    sex = ['ชาย', 'หญิง'] if sex == ["All"] else sex
    sex = ['ชาย'] if sex == ['boy'] or sex == ['man'] or sex == ['men'] or sex == ['male'] else sex
    sex = ['หญิง'] if sex == ['girl'] or sex == ['woman'] or sex == ['female'] else sex
    age = to_range(input('ช่วงอายุ(Ex. 15-27) : '))
    print("Processing...")
    show = {}
    for num in year:
        show[num] = 0
    for num in table:
        if num[0] in year:
            show[num[0]] += 1 if num[1] == province and num[2] in day and num[3] in sex and\
                            num[4] in age else 0
    for year in sorted(show):
        print(year+" : "+str(show[year])+" คน")
def to_range(text):
    """"""
    if "-" in text:
        text = [int(num) for num in text.split("-")]
    else:
        text = [int(text), int(text)]
    return [str(num) for num in list(range(text[0], text[1]+1))]
main()
