def main():

products = {

    "mobiles": {

        "Apple": [

            {

                "id": 1,

                "name": "iPhone 7",

                "price": 300

            },

            {

                "id": 2,

                "name": "iPhone 8",

                "price": 350

            },

            {

                "id": 3,

                "name": "iPhone Xr",

                "price": 450

            },

            {

                "id": 4,

                "name": "iPhone Xs",

                "price": 460

            },

                {

                    "id": 5,

                    "name": "iPhone 11",

                    "price": 900

                },

                {

                    "id": 6,

                    "name": "iPhone 12",

                    "price": 1100

                },

                {

                    "id": 7,

                    "name": "iPhone 13",

                    "price": 1300

                },

            ],

            "Samsung": [

                {

                    "id": 8,

                    "name": "Samsung Galaxy Beam",

                    "price": 150

                },

                {

                    "id": 9,

                    "name": "Samsung Galaxy S6",

                    "price": 200

                },

                {

                    "id": 10,

                    "name": "Samsung Galaxy S7",

                    "price": 300

                },

            ],

            "Xiaomi": [

                {

                    "id": 11,

                    "name": "Xiaomi Redmi Note 8",

                    "price": 250

                },

                {

                    "id": 12,

                    "name": "Xiaomi Redmi Note 8 Pro",

                    "price": 300

                },

            ]

        },

        "laptops": {

            "DELL": [

                {

                    "id": 13,

                    "name": "Dell Inspiron 15",

                    "price": 600

                },

                {

                    "id": 14,

                    "name": "Dell Latitude 14",

                    "price": 650

                },

            ],

            "MAC": [

                {

                    "id": 15,

                    "name": "MacBook Pro 13",

                    "price": 900

                },

                {

                    "id": 16,

                    "name": "MacBook M1",

                    "price": 1500

                },

            ]

        },

    }
    while True:
        opcion= input('Por favor ingrrseuna opcion valida: \n 1. Ver inventario \n2. Hacer una compra. \n Salir \n')
        if opcion== 1:
            categories= (1:'mobiles',2: 'laptos')
            category= int(input('Ingrese la categoria n\ 1. Mobile n\ 2. Laptos:\n'))
            for tipos, brands in products.items():
                if tipos== categories.get(categories)
                print(brands)
                for brands, list_de_telefonos in brands.items():
                    print(brands)
                    for products in list_de_telefonos:
                        id= products.get('id')
                        name= products.get('name')
                        price= products.get('price')
                        print(products)
        elif opcion== 2:
            
        elif opcion== 3:
        else:
            continue
main()

