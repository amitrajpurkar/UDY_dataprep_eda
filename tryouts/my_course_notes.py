from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Section", "Topic(s)", "take-away's"]
table.add_row(["1. Getting Started", "few","course intro and materials"])
table.add_row(["2. Intro to Data Science", "few","what parts encompasses data science; expand notes"])
table.add_row(["3. Scoping a Project", "few","SDLC style outlook on a data science project"])
table.add_row(["4. Jupyter Notebook", "few","installation, know-how of jupyter notebook; i choose to use PyCharm"])
table.add_row(["5. Gathering data", "44-47","basics on data sources"])
print(table)




