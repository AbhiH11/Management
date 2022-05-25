import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Goodlooking@92",
    database = "Abhi"
)
# class management:
#     manage = []
def employee():
    d = mydb.cursor()
    e = input("Enter employee name: ")
    f = input("Enter Basic: ")
    g = input("Enter HRA: ")
    h = input("Enter allowance: ")
    i = "Y"
    j = input("Enter date of joining (YYYY-MM-DD): ")
    sql = "insert into employee(emp_name,basic,hra,other_allowance,status,doj) values(%s,%s,%s,%s,%s,%s)"
    data = (e,f,g,h,i,j)
    d.execute(sql,data)
    mydb.commit()
    # for i in d:
    #     print(i)
    print("Data entered sucessfully..!!")


def terminate_emp():
    d = mydb.cursor()
    d.execute("select emp_id,emp_name, DATE_FORMAT(doj, '%d,%b,%y'),(case when status = 'Y' then 'ACTIVE' else 'INACTIVE' end) as status from employee")
    q = d.fetchall()
    # print(q)
    print(3* " ", 'emp_id', 6* " ", 'emp_name', 12* " ", 'doj', 10* " ",'status')
    for i in q:
        print(3*" ",i[0], 12* " ", i[1], 12* " ", i[2], 10* " ",i[3])

    s = input("Enter emp_id: ")
    # print(s)
    id = (s,)
    # print(id)
    t = "select count(*) from employee where emp_id = %s"
    t2 = d.execute(t,id)
    myrow = d.fetchall()

    for i in myrow:
        if i == (0,):
            print("Enter emp_id:")
        else:
            c = input("Enter 'Y' if Active or 'N' if Inactive:")
            if c == 'Y':
                c1 = c.upper()
                print(c1)
            elif c == 'y':
                c1 = c.upper()
                print(c1)
            elif c == 'N':
                c1 = c.upper()
                print(c1)
            elif c == 'n':
                c1 = c.upper()
                print(c1)
            else:
                print("Enter 'Y' if Active or 'N' if Inactive:")


    r = "update employee set status = '{}' where emp_id ={}".format(c,s)
    print(c,s)
    d.execute(r)
    mydb.commit()
    print("Data edited successfully..!!")
terminate_emp()
    # k = input("Enter emp_id:")
    # k2 = (k,)

    # sql = "delete from employee where emp_id = 'k'"
    #
    # d.execute(sql,k)
    # l = input("Enter 'Y' if Active or 'N' if Inactive: " )




# if __name__ == "__main__":
# # f = management()
#
#     print("please choose option : 1. Employee_details 2.Emp_details")
#     choice = int(input("Enter option:"))
#     while True:
#         if choice == 1:
#             employee()
#
#         if choice == 2:
#             terminate_emp()

