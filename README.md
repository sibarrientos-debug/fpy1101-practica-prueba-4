# FPY1101 - Práctica Prueba 4

## Fundamentos de Programación

Repositorio de práctica para reforzar:

- Fork de repositorios en GitHub.
- Clonación de repositorios.
- Trabajo local con Python.
- Uso de listas.
- Uso de diccionarios.
- Uso de funciones.
- Desarrollo de ejercicios en archivos separados.
- Subida de cambios a GitHub.

---

# Objetivo de la actividad

El objetivo de esta práctica es que cada estudiante aprenda a trabajar con el flujo:

```text
Fork → Clone → Desarrollo local → Commit → Push
```

Además, se busca reforzar contenidos importantes para la Prueba 4 de FPY1101:

- Funciones.
- Listas.
- Diccionarios.
- Ciclos.
- Condicionales.
- Validaciones básicas.
- Organización de código.

---

# Instrucciones generales

Este repositorio contiene 5 archivos Python:

```text
ejercicio1.py
ejercicio2.py
ejercicio3.py
ejercicio4.py
ejercicio5.py
```

Cada archivo está vacío intencionalmente.

Debes desarrollar cada ejercicio en el archivo correspondiente.

---

# Paso a paso para trabajar con Fork

## 1. Realizar Fork del repositorio

Desde GitHub, presiona el botón:

```text
Fork
```

Esto creará una copia del repositorio en tu propia cuenta de GitHub.

---

## 2. Clonar tu repositorio fork

Copia la URL de tu fork y ejecuta en tu computador:

```bash
git clone URL_DE_TU_FORK
```

Ejemplo:

```bash
git clone https://github.com/tu-usuario/fpy1101-practica-prueba-4.git
```

---

## 3. Entrar a la carpeta del proyecto

```bash
cd fpy1101-practica-prueba-4
```

---

## 4. Abrir el proyecto en Visual Studio Code

```bash
code .
```

---

## 5. Desarrollar los ejercicios

Debes completar:

```text
ejercicio1.py
ejercicio2.py
ejercicio3.py
ejercicio4.py
ejercicio5.py
```

---

## 6. Probar cada ejercicio

Ejecuta cada archivo por separado:

```bash
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
python ejercicio4.py
python ejercicio5.py
```

En algunos computadores puede ser necesario usar:

```bash
python3 ejercicio1.py
```

---

## 7. Guardar cambios con Git

Cuando termines o avances en los ejercicios:

```bash
git status
git add .
git commit -m "Desarrollo ejercicios practica prueba 4"
```

---

## 8. Subir los cambios a tu fork

```bash
git push origin main
```

---

# Reglas de desarrollo

- Cada ejercicio debe desarrollarse en su archivo correspondiente.
- Se deben utilizar funciones obligatoriamente.
- Se deben utilizar listas y/o diccionarios según corresponda.
- El código debe ejecutarse sin errores.
- Los nombres de variables deben ser claros.
- Se recomienda comentar partes importantes del código.
- No se permite resolver todos los ejercicios en un solo archivo.

---

# Ejercicio 1 - Registro de estudiantes

## Archivo

```text
ejercicio1.py
```

## Enunciado

Crea un programa en Python que permita registrar estudiantes de una asignatura.

Cada estudiante debe tener:

- RUT
- Nombre
- Edad
- Carrera

El programa debe permitir registrar 3 estudiantes y guardarlos en una lista.

Cada estudiante debe representarse mediante un diccionario.

Al finalizar, mostrar todos los estudiantes registrados.

## Requisitos técnicos

Debes crear al menos las siguientes funciones:

```python
registrar_estudiante()
mostrar_estudiantes(estudiantes)
```

## Pistas

- Usa una lista llamada `estudiantes`.
- Cada estudiante puede ser un diccionario.
- Puedes usar un ciclo `for` para registrar los 3 estudiantes.
- La función `registrar_estudiante()` puede retornar un diccionario.
- La función `mostrar_estudiantes()` puede recorrer la lista e imprimir los datos.

## Ejemplo de estructura esperada

```python
estudiante = {
    "rut": "11111111-1",
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Informática"
}
```

---

# Ejercicio 2 - Buscar productos por código

## Archivo

```text
ejercicio2.py
```

## Enunciado

Crea un programa que administre una lista de productos.

Cada producto debe tener:

- Código
- Nombre
- Precio
- Stock

El programa debe iniciar con al menos 4 productos precargados.

Luego debe solicitar al usuario un código y buscar si el producto existe.

Si existe, mostrar todos sus datos.

Si no existe, mostrar un mensaje indicando que no fue encontrado.

## Requisitos técnicos

Debes crear al menos las siguientes funciones:

```python
buscar_producto(productos, codigo)
mostrar_producto(producto)
```

## Pistas

- Usa una lista de diccionarios.
- La función `buscar_producto()` puede retornar el producto encontrado o `None`.
- Recorre la lista usando `for`.
- Compara el código ingresado con el código del diccionario.
- Recuerda que los códigos pueden manejarse como texto.

## Ejemplo de producto

```python
{
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 15000,
    "stock": 10
}
```

---

# Ejercicio 3 - Actualizar stock de productos

## Archivo

```text
ejercicio3.py
```

## Enunciado

Crea un programa que permita actualizar el stock de un producto existente.

El sistema debe tener una lista inicial de productos.

El usuario debe ingresar el código del producto que desea actualizar.

Si el producto existe, debe pedir el nuevo stock y actualizarlo.

Si el producto no existe, debe mostrar un mensaje de error.

## Requisitos técnicos

Debes crear al menos las siguientes funciones:

```python
buscar_producto(productos, codigo)
actualizar_stock(productos, codigo, nuevo_stock)
mostrar_productos(productos)
```

## Validaciones

- El nuevo stock debe ser un número entero igual o mayor a 0.
- Si el usuario ingresa un valor inválido, debe volver a solicitar el dato.

## Pistas

- Puedes reutilizar la lógica del ejercicio 2.
- Usa `try/except` para validar el ingreso del stock.
- Recuerda que los diccionarios se pueden modificar directamente.
- Puedes usar `while` para repetir la solicitud hasta que el dato sea válido.

---

# Ejercicio 4 - CRUD simple de cursos

## Archivo

```text
ejercicio4.py
```

## Enunciado

Crea un sistema CRUD simple para administrar cursos.

Cada curso debe tener:

- Código
- Nombre
- Docente
- Cantidad de estudiantes

El sistema debe mostrar un menú con las siguientes opciones:

```text
1. Agregar curso
2. Listar cursos
3. Buscar curso
4. Eliminar curso
5. Salir
```

## Requisitos técnicos

Debes crear funciones para cada acción:

```python
agregar_curso(cursos)
listar_cursos(cursos)
buscar_curso(cursos, codigo)
eliminar_curso(cursos, codigo)
```

## Validaciones

- El código del curso no debe repetirse.
- La cantidad de estudiantes debe ser un entero positivo.
- Si no existen cursos, se debe mostrar un mensaje adecuado.
- El menú debe repetirse hasta seleccionar la opción 5.

## Pistas

- Usa una lista llamada `cursos`.
- Cada curso debe ser un diccionario.
- Para eliminar, puedes usar `remove()`.
- Para evitar códigos repetidos, busca primero si el curso ya existe.
- El menú puede controlarse con un `while`.

---

# Ejercicio 5 - Sistema de notas por estudiante

## Archivo

```text
ejercicio5.py
```

## Enunciado

Crea un programa que permita registrar estudiantes y calcular su promedio.

Cada estudiante debe tener:

- Nombre
- Nota 1
- Nota 2
- Nota 3
- Promedio
- Estado

El programa debe permitir registrar varios estudiantes hasta que el usuario indique que no desea continuar.

El promedio se calcula con las 3 notas.

El estado será:

- `Aprobado` si el promedio es mayor o igual a 4.0.
- `Reprobado` si el promedio es menor a 4.0.

Al finalizar, mostrar todos los estudiantes con su promedio y estado.

## Requisitos técnicos

Debes crear al menos las siguientes funciones:

```python
validar_nota(mensaje)
calcular_promedio(n1, n2, n3)
determinar_estado(promedio)
registrar_estudiante()
mostrar_resumen(estudiantes)
```

## Validaciones

- Cada nota debe estar entre 1.0 y 7.0.
- Si la nota no es válida, se debe volver a solicitar.
- El usuario debe poder registrar más de un estudiante.
- Cada estudiante debe almacenarse como diccionario dentro de una lista.

## Pistas

- Usa `while` para permitir varios registros.
- Usa `try/except` para validar notas.
- La función `validar_nota()` puede recibir el texto del input.
- La función `calcular_promedio()` debe retornar un número.
- La función `determinar_estado()` debe retornar un string.
- Guarda el promedio dentro del diccionario del estudiante.

---

# Entrega esperada

Cada estudiante debe entregar la URL de su repositorio fork con los 5 ejercicios desarrollados.

El repositorio debe contener:

```text
README.md
ejercicio1.py
ejercicio2.py
ejercicio3.py
ejercicio4.py
ejercicio5.py
```

---

# Criterios sugeridos de revisión

| Criterio | Descripción |
|---|---|
| Uso de funciones | El estudiante separa correctamente la lógica en funciones. |
| Uso de listas | Usa listas para almacenar varios elementos. |
| Uso de diccionarios | Representa correctamente registros mediante diccionarios. |
| Validaciones | Valida datos importantes del usuario. |
| Ejecución | Los archivos se ejecutan sin errores. |
| GitHub | El estudiante realiza fork, commits y push correctamente. |
| Organización | Cada ejercicio está en su archivo correspondiente. |

---

# Recomendación final

Antes de subir los cambios a GitHub, prueba cada archivo de manera individual.

No basta con que el código esté escrito: debe ejecutarse correctamente.
