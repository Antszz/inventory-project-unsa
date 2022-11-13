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
```json
abort(404, message="inventory {} doesn't exist".format(inventory_id))
```

### Crear Inventario
> **Agrega un nuevo inventario a la base de datos**

**Method:** ``` POST```
**URL:** ``` '/inventory'```
**Returns:** 
*	Nuevo objeto de tipo *Inventory*

### Listar Inventarios
> **Muestra los inventarios de la base de datos**

**Method:** ``` GET```
**URL:**  ``` /inventories ```

**Returns** 
* Objetos de tipo *Inventory*

---
### Inventarios
**URL:** ``` /inventory/<inventory_id>```


```json
get(self, inventory_id)
```
* **Parameters** 
	* *inventory_id*: ID del inventario
* **Returns** 
	*	Objeto de tipo *Inventory*

```json
delete (self, inventory_id)
```
* **Parameters** 
	* *inventory_id*: ID del inventario
* **Returns**
	*	Inventory -> 'delete': True
	*	Error Response -> Si el inventario no existe

```json
put(self, inventory_id)
```

* **Parameters** 
	* *inventory_id*: ID del inventario
* **Returns**
	*	Inventory -> update(args)
	*	Error Response -> Si el inventario no existe

#### Data constraints *(InventorySchema)*
* **id** *(Autoincrement/Required)*
	* > ID del inventario
* **recorder** *(Integer/Required)*
	* > ID de la persona encargada de ingresar el  inventario.
* **receiver** *(Integer/Required)*
	* > ID de la persona la cual recibe el inventario.
* **location** *(String/Required)*
	* > Localización del inventario, por ejemplo "26.2-205-Aula"
* **assets** *(List of Integers/Required)*
	* > ID de los assets en el inventario
* **type** *(Inventory/Required)* 
	* > Tipo Inventory(InventorySchema)

### Resources:
```json
api.add_resource(Inventory, '/inventory/<inventory_id>')
api.add_resource(CreateInventory, '/inventory')
api.add_resource(ListInventories, '/inventories')
```

## Gestionar assets

:triangular_flag_on_post: **Error Responses:** 
```json
abort(404, message="Asset {} doesn't exist".format(asset_id))
```

### Crear Asset
> **Agrega un nuevo asset a la base de datos**

**Method:** ``` POST```
**URL:** ``` '/asset'```
**Returns:** 
*	Nuevo objeto de tipo *Asset*

### Listar Assets
> **Muestra los assets de la base de datos**

**Method:** ``` GET```
**URL:**  ``` /assets ```
**Returns** 
* Objetos de tipo *Asset*

---
### Assets

**URL:** ``` /asset/<asset_id>```

```json
get(self, asset_id)
```
* **Parameters** 
	* *asset_id*: ID del Asset
* **Returns** 
	*	Objeto de tipo *Asset*

```json
delete(self, asset_id)
```
* **Parameters** 
	* *asset_id*: ID del asset
* **Returns**
	*	Asset-> 'delete': True
	*	Error Response -> Si el asset no existe

```json
put(self, asset_id)
```

* **Parameters** 
	* *asset_id*: ID del asset
* **Returns**
	*	Asset -> update(args)
	*	Error Response -> Si el inventario no existe

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
	* > Numero de serie del asset
* **gp** *(String/Optional)* 
	* > 
* **detail** *(String/Required)* 
	* > Una breve descripción del asset
* **dimensions** *(String/Required)* 
	* > Dimensiones del asset en mts, por ejemplo "Dimensiones: H = 0.85MTS"
* **inventory** *(String/Required)* 
	* > ID del inventario donde se encuentra el asset
* **type** *(String/Required)* 
	* > Tipo Asset(AssetSchema)

### Resources:
```json
api.add_resource(Asset, '/asset/<asset_id>')
api.add_resource(CreateAsset, '/asset')
api.add_resource(ListAssets, '/assets')
```

## Gestionar usuarios

:triangular_flag_on_post: **Error Responses:** 
```json
abort(404, message="user {} doesn't exist".format(user_id))
```

### Crear Usuario
> **Agrega un nuevo usuario a la base de datos**

**Method:** ``` POST```
**URL:** ``` /user ```
**Returns:** 
*	Nuevo objeto de tipo *User*

### Listar Usuarios
> **Muestra los usuarios de la base de datos**

**Method:** ``` GET```
**URL:**  ``` /users ```
**Returns** 
* Objetos de tipo *Usuario*

---
### Usuarios

**URL:** ``` /user/<user_id>```

```json
get(self, user_id)
```
* **Parameters** 
	* *user_id*: ID del usuario
* **Returns** 
	*	Objeto de tipo *User*

```json
delete(self, user_id)
```
* **Parameters** 
	* *user_id*: ID del User
* **Returns**
	*	User-> 'delete': True
	*	Error Response -> Si el usuario no existe

```json
put(self, user_id)
```

* **Parameters** 
	* *user_id*: ID del User
* **Returns**
	*	User-> update(args)
	*	Error Response -> Si el usuario no existe

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
* **type** *(String/Required)* 
	* > Tipo User(UserSchema)

### Resources:
```json
api.add_resource(User, '/user/<user_id>')
api.add_resource(CreateUser, '/user')
api.add_resource(ListUsers, '/users')
```

