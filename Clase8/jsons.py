import json  #Importar las funciones de json en la 
#clase 15 entenderemos mejor el IMPORT

# data = {}

# data['clients'] = []
# data['locations'] = []



# data['clients'].append({
#     'first_name': 'Sigrid',
#     'last_name': 'Mannock',
#     'age': 27,
#     'amount': 7.17})

# data['clients'].append({
#     'first_name': 'Joe',
#     'last_name': 'Hinners',
#     'age': 31,
#     'amount': [1.90, 5.50]})

# data['clients'].append({
#     'first_name': 'Theodoric',
#     'last_name': 'Rivers',
#     'age': 36,
#     'amount': 1.11})

# with open('Clase8' + "/primerJson.json", 'w') as file:
#   json.dump(data, file, indent=4)

with open('Clase8' + '/primerJson.json') as file:
    dato_lectura = json.load(file)
    for client in dato_lectura['clients']:
        print('first name: ',client['first_name'])
        print('last name: ',client['last_name'])
        print('age ', client['age'])
        print('amount ', client['amount'])
        print("")