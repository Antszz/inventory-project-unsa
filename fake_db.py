FAKE_DB = [
    # Users
    {
        "type": "User",
        "id": 1,
        "rol": "admin",
        "first_name": "Eduardo Antonio",
        "last_name": "Sanchez Hincho",
        "dni": "20202021"
    },
    {
        "type": "User",
        "id": 2,
        "rol": "recorder",
        "first_name": "Brian Emanuel",
        "last_name": "Silva Corrales",
        "dni": "20202022"
    },
    {
        "type": "User",
        "id": 3,
        "rol": "recorder",
        "first_name": "Luis Guillermo",
        "last_name": "Villanueva Flores",
        "dni": "20202023"
    },
    {
        "type": "User",
        "id": 4,
        "rol": "visualizer",
        "first_name": "Andy Geanpiero",
        "last_name": "Ñaca Rodriguez",
        "dni": "20202024"
    },
    {
        "type": "User",
        "id": 5,
        "rol": "visualizer",
        "first_name": "Juan Carlos",
        "last_name": "Gutierrez Caceres",
        "dni": "20202025"
    },
    {
        "type": "User",
        "id": 6,
        "rol": "recorder",
        "first_name": "Alex",
        "last_name": "Olanda Saavedra",
        "dni": "20202026"
    },

    # Inventories
    {
        "type": "Inventory",
        "id": 1,
        "recorder": 6,      # Recorder ID
        "receiver": 5,      # Recorder ID
        "location": 1,      # Location ID
        "assets": [         # Assets IDs
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
        "location": 1,      # Location ID
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
        "location": 1,      # Location ID
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
        "location": 1,      # Location ID
        "inventory": 1      # Inventory ID
    },

    # Locations
    {
        "type": "Location",
        "id": 1,
        "code": "26.2-205",
        "location_type": "Aula"
    }
]
