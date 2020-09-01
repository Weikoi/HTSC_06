from Query import Query

if __name__ == '__main__':

    query1 = Query("Customers", "((companyName=HTSC)or(age<30))")
    query1.to_ast()
    assert ("SELECT * FROM Customers WHERE ((companyName=HTSC)or(age<30))" == query1.to_sql())

    query2 = Query("Customers", "(((companyName=HTSC)or(age<30))and(sex!=male))")
    query2.to_ast()
    assert ("SELECT * FROM Customers WHERE (((companyName=HTSC)or(age<30))and(sex!=male))" == query2.to_sql())
