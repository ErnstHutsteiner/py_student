from class_test_alchemy import Myalc

this_q = Myalc()
my_query = "select top 10 FirstName, LastName, EmailPromotion from person.person"
retval = this_q.query(my_query)
print(retval)

