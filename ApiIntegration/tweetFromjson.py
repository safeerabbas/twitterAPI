import json
import pprint
#
# with open('tweetlist.json', 'r',encoding="utf8") as file:
#     data = json.load(file)
#
# print(data)
# # print(data.get(""))
# printer = pprint.PrettyPrinter()
# data=data.get("data")
# for item in data:
#     entities=item.get("entities")
#     printer.pprint(item.get("entities"))
#     for entity in entities:
#         # hashtags=entity.get("annotations")
#         print(type(entity))
#         # for hashtag in hashtags:
#         #     printer.pprint(hashtag)
#


with open('employees.json', 'r') as file:
    data = json.load(file)


printer = pprint.PrettyPrinter()
# printer.pprint(data)

language = data.get('data')

employees = data.get('employees')

print(language)

for employee in employees:
    print(type(employee))
    print(employee.get('id'), employee.get('fullname'))