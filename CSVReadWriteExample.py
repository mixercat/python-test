import csv

def write_csv():
    # ส่วนการสร้างไฟล์ CSV ที่ชื่อ employee_birthday.txt
    # แนะนำให้ใส่ newline='' เพื่อป้องกันไม่ให้เกิดบรรทัดว่างตอนเขียนไฟล์ใน Windows
    with open('employee_birthday.txt', mode='w', newline='') as csv_file:
        # สร้างตัวแปรที่ทำหน้าที่ในการเขียนข้อมูล CSV ชื่อ csv_writer
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # ส่วนในการเขียนข้อมูลลงในไฟล์ CSV
        csv_writer.writerow(['Adirut', 'Accounting', 'November'])
        csv_writer.writerow(['Erica Meyers', 'IT', 'March'])
        csv_writer.writerow(['Aum', 'IT', 'March'])
        csv_writer.writerow(['Mark', 'CMO', 'June'])

# 1. เรียกใช้งานฟังก์ชันเพื่อสร้างและเขียนไฟล์ก่อน
write_csv()

# 2. เมื่อสร้างไฟล์เสร็จแล้ว ค่อยทำการเปิดอ่านไฟล์
# ส่วนการเปิดไฟล์ CSV ที่ชื่อ employee_birthday.txt
with open('employee_birthday.txt') as csv_file:
    # สร้างตัวแปรที่ทำหน้าที่อ่านข้อมูล CSV ชื่อ csv_reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        # ป้องกัน Error: IndexError จากบรรทัดที่ว่างเปล่า
        if len(row) < 3:
            continue

        # ส่วนในการแสดงชื่อ column
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        # ส่วนในการแสดงข้อมูล
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
            
    print(f'Processed {line_count} lines.')