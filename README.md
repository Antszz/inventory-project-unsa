
# Modulo de Inventario UNSA


Todos los años en la Escuela Profesional de Ciencia de Computación de la Universidad Nacional de San Agustín se realiza el inventariado de las diferentes adquisiciones de la escuela. Esto envuelve a personal administrativo tanto de la escuela como de las autoridades correspondientes donde se define al registro documental los bienes y demás cosas pertenecientes.

Se realiza este proyecto para que el inventario de la escuela pueda ser visualizado por las personas interesadas.

## Instalacion
Este proyecto usa **python 3.8**

Tienes que crear un entorno virtual, asegúrate de tener virtualenv instalado.

```bash
python3 -m venv venv
source venv/bin/activate
```
Ahora instala requirements.txt

```bash
python3 -m pip install -r requirements.txt
```

## Ejecutar el proyecto
Run
```bash
python3 main.py
```

Y visita [localhost:5000/inventories](http://localhost:5000/inventories)


## Gestionar inventarios

:triangular_flag_on_post: **Error Responses:** 
```
Code: 404 NOT FOUND
{Error: "inventory {inventory_id} doesn't exist"}
```

### Crear Inventario
> **Agrega un nuevo inventario a la base de datos**

**Method:** ``` POST```

**URL:** ``` '/inventory'```

**Returns:** 
*	Nuevo objeto de tipo *Inventory*

#### Data constraints *(InventorySchema)*
* **id** *(Autoincrement/Required)*
	* > ID del inventario
* **recorder** *(Integer/Required)*
	* > ID de la persona encargada de ingresar el  inventario.
* **receiver** *(Integer/Required)*
	* > ID de la persona la cual recibe el inventario.
* **location** *(String/Required)*
	* > Localización del inventario, por ejemplo "26.2-205-Aula"
	
### Listar Inventarios
> **Muestra los inventarios de la base de datos**

**Method:** ``` GET```

**URL:**  ``` /inventories ```

**Returns** 
* Objetos de tipo *Inventory*

---
### Inventarios
**Method:** ``` GET```
**URL:** ``` /inventory/<inventory_id>```

**Success Response:**
``` 
Code: 200 OK
{"type": "Inventory", 
"id": [Integer], 
"recorder": [Integer], 
"receiver": [Integer], 
"location": [String], 
"assets": [List of Integers]}
``` 
**Error Responses:**
``` 
{"message": "inventory <inventory_id> doesn't exist"}
``` 





## Gestionar assets

:triangular_flag_on_post: **Error Responses:** 
```
Code: 404 NOT FOUND
{Error: "Asset {asset_id} doesn't exist"}
```

### Crear Asset
> **Agrega un nuevo asset a la base de datos**

**Method:** ``` POST```

**URL:** ``` '/asset'```

**Returns:** 

*	Nuevo objeto de tipo *Asset*
#### Data constraints *(AssetSchema)*
* **id** *(Autoincrement/Required)*
	* > ID del Asset
* **code** *(String/Required)*
	* > Codigo registrado del asset.
* **denomination** *(String/Required)*
	* > Denominacion del asset, por ejemplo "Silla fija de metal".
* **brand** *(String/Optional)*
	* > Marca del asset
* **color** *(String/Required)*
	* > Color del asset
* **serie** *(String/Optional)* 
	* > Número de serie del asset
* **gp** *(String/Optional)* 
	* > 
* **detail** *(String/Required)* 
	* > Una breve descripción del asset
* **dimensions** *(String/Required)* 
	* > Dimensiones del asset en mts, por ejemplo "Dimensiones: H = 0.85MTS"
* **inventory** *(String/Required)* 
	* > ID del inventario donde se encuentra el asset

### Listar Assets
> **Muestra los assets de la base de datos**

**Method:** ``` GET```

**URL:**  ``` /assets ```

**Returns** 
* Objetos de tipo *Asset*

---
### Assets

**Method:** ``` GET```

**URL:** ``` /asset/<asset_id>```

**Success Response:**
``` 
Code: 200 OK
{"type": "Asset", 
"id": [Integer], 
"code": [String], 
"denomination": [String], 
"brand": [String], 
"model": [String], 
"color": [String], 
"serie": [String], 
"e": [String], 
"gp": [String], 
"detail": [String], 
"dimensions": [String], 
"inventory": [String]}
``` 
**Error Responses:**
``` 
{"message": "Asset <asset_id> doesn't exist"}
``` 




## Gestionar usuarios

:triangular_flag_on_post: **Error Responses:** 
```
Code: 404 NOT FOUND
{Error: "user {user_id} doesn't exist"}
```

### Crear Usuario
> **Agrega un nuevo usuario a la base de datos**

**Method:** ``` POST```

**URL:** ``` /user ```

**Returns:** 
*	Nuevo objeto de tipo *User*

#### Data constraints *(UserSchema)*
* **id** *(Autoincrement/Required)*
	* > ID del Usuario
* **rol** *(String/Required)*
	* > Rol designado (Admin, Recorder, Visualizer)
* **first_name** *(String/Required)*
	* > Nombres del usuario.
* **last_name** *(String/Required)*
	* > Apellidos del usuario.
* **dni** *(String/Required)*
	* > DNI del usuario
### Listar Usuarios
> **Muestra los usuarios de la base de datos**

**Method:** ``` GET```

**URL:**  ``` /users ```

**Returns** 
* Objetos de tipo *Usuario*

---
### Usuarios

**Method:**  `GET`

**URL:** ``` /user/<user_id>```

**Success Response:**
``` 
Code: 200 OK
{"type": "User", 
"id": [Integer], 
"rol": [String], 
"first_name": [String], 
"last_name": [String], 
"dni": [Integer]}
``` 
**Error Responses:**
``` 
{"message": "user <user_id> doesn't exist"}
``` 
