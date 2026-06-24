def mostrar_producto (producto):
    print(producto)

def buscar_producto(producto,codigo):
    for producto in productos:
        if producto["codigo"]==codigo:
            mostrar_producto(producto)
            return
    print("Producto no encontrado")
   
productos=[]

producto_1={ "codigo": "C001",
        "nombre": "Producto uno",
        "precio": 10900,
        "stock": 15 
        }
producto_2={ "codigo": "C002",
        "nombre": "Producto dos",
        "precio": 15000,
        "stock": 20 
        }
producto_3={ "codigo": "C003",
        "nombre": "Producto tres",
        "precio": 25000,
        "stock": 45 
        }
producto_4={ "codigo": "C0024",
        "nombre": "Producto cuatro",
        "precio": 9990,
        "stock": 35
        }
productos.append(producto_1)
productos.append(producto_2)
productos.append(producto_3)
productos.append(producto_4)

codigo=input("Ingrese un código: ")
buscar_producto(productos,codigo)