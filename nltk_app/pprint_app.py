import pprint

student_dict = {'Name': 'Tusar', 'Class': 'XII',
                'Address': {'FLAT ': 1308, 'BLOCK ': 'A', 'LANE ': 2, 'CITY ': 'HYD'}}
json = {"Name": ["Rick", "Dan", "Michelle", "Ryan", "Gary", "Nina", "Simon", "Guru"],
        "Salary": ["623.3", "515.2", "611", "729", "843.25", "578", "632.8", "722.5"],
        "StartDate": ["1/1/2012", "9/23/2013", "11/15/2014", "5/11/2014", "3/27/2015", "5/21/2013",
                      "7/30/2013", "6/17/2014"],
        "Dept": ["IT", "Operations", "IT", "HR", "Finance", "IT", "Operations", "Finance"]}

print(student_dict)
pprint.pprint(student_dict, width=-1)

print(json)
print(pprint.pformat(json, indent=2))
