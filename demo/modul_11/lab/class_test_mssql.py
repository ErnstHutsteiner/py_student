
from solution import Mssql

def execute_query(query_or_procedure):
    with Mssql() as sql_client:
        result = sql_client.query(query_or_procedure)
    return result


def select_as_data_frame(query):
    with Mssql() as sql_client:
        result = sql_client.pandas_query(query)
    return result

my_query = "select top 10 FirstName, LastName, EmailPromotion from person.person"

# retval = execute_query(my_query)
# print(retval)

retval = select_as_data_frame(my_query)
# print(retval)
# print(type(retval))

print(retval.index)
print(retval.dtypes)
print(retval.columns)
print(retval.values)

# sort
print(retval.sort_values('LastName', ascending=True))

# filter
print(retval[retval.EmailPromotion == 2])

# iterate
for index, row in retval.iterrows():
    print(index, row["FirstName"], row["LastName"])

# write the stuff to csv
retval.to_csv('mycsv.csv')

# or convert to dictionary
my_dict = retval.astype(str).to_dict(orient='records')
