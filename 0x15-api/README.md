API This project was further practice in working with API's. I collected data from the JSONPlaceholder REST API, and learned how to export it to either CSV or JSON format.

Tasks ��� 0. Gather data from an API

0-gather_data_from_an_API.py: Python script that returns information on the to-do list progress of a given employee ID. Usage: python3 0-gather_data_from_an_API.py . Output: Employee is done with tasks(<# completed tasks>/<total # tasks>):

Export to CSV
1-export_to_CSV.py: Python script exports to-do list information of a given employee ID to CSV format. Usage: python3 1-export_to_CSV.py File name: .csv. Format: "","","","". 2. Export to JSON

2-export_to_JSON.py: Python script that exports to-do list information of a given employee ID to JSON format. Usage: python3 2-export_to_JSON.py File name: .json Format: { "": [ {"task": "", "completed": , "username": ""}}, ... ]} 3. Dictionary of list of dictionaries

3-dictionary_of_list_of_dictionaries.py: Python script that exports to-do list information for all employees to JSON format. Usage: python3 3-dictionary_of_list_of_dictionaries.py File name: todo_all_employees.json Format: { "": [ {"username": "", "task": "", "completed": }, {"username": "", "task": "", "completed": }, ... ], "": [ {"username": "", "task": "", "completed": }, {"username": "", "task": "", "completed": }, ... ]}
