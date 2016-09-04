import athletemodel
import yate
import glob

data_file = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_file)

print(yate.state_response())
print(yate.include_header("Coach kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
