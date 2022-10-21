FAKE_DB = [
    # Users
    {
        "type": "User",
        "id": 1,
        "rol": "admin",
        "first_name": "Eduardo Antonio",
        "last_name": "Sanchez Hincho",
    },
    {
        "type": "User",
        "id": 2,
        "rol": "recorder",
        "first_name": "Brian Emanuel",
        "last_name": "Silva Corrales",
    },
    {
        "type": "User",
        "id": 3,
        "rol": "recorder",
        "first_name": "Luis Guillermo",
        "last_name": "Villanueva Flores",
    },
    {
        "type": "User",
        "id": 4,
        "rol": "visualizer",
        "first_name": "Andy Geanpiero",
        "last_name": "Ñaca Rodriguez",
    },
    {
        "type": "User",
        "id": 5,
        "rol": "visualizer",
        "first_name": "Juan Carlos",
        "last_name": "Gutierrez Caceres",
    },
    {
        "type": "User",
        "id": 6,
        "rol": "recorder",
        "first_name": "Alex",
        "last_name": "Olanda Saavedra",
    },

    # Inventories
    {
        "type": "Inventory",
        "id": 1,
        "recorder": 6,      # Recorder ID
        "receiver": 5,      # Recorder ID
        "location": "26.2-205-Aula",
        "assets": [        # Assets IDs
            1, 2, 3
        ]
    },

    # Assets
    {
        "type": "Asset",
        "id": 1,
        "code": "74642491B924",
        "denomination": "Carpeta de metal multiple",
        "brand": "-",
        "model": "-",
        "color": "plomo",
        "serie": "9",
        "e": "B",
        "gp": "-",
        "detail": "Con tablero de melamina blanco y 01 espacio de rejillas",
        "dimensions": "1.18 X 0.50 X 0.81 Mts",
        "inventory": 1      # Inventory ID
    },
    {
        "type": "Asset",
        "id": 2,
        "code": "46224785",
        "denomination": "Equipo de iluminacion",
        "brand": "OPALUX",
        "model": "-",
        "color": "blanco",
        "serie": "-",
        "e": "N",
        "gp": "-",
        "detail": "Con tablero de melamina blanco y 01 espacio de rejillas",
        "dimensions": "1.18 X 0.50 X 0.81 Mts",
        "inventory": 1      # Inventory ID
    },
    {
        "type": "Asset",
        "id": 3,
        "code": "46228659",
        "denomination": "Regulador de voltaje",
        "brand": "FORZA",
        "model": "FUR-1221B",
        "color": "negro",
        "serie": "1342565154",
        "e": "B",
        "gp": "-",
        "detail": "-",
        "dimensions": "-",
        "inventory": 1      # Inventory ID
    },
]
