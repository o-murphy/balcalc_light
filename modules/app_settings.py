from dataclasses import dataclass, asdict


@dataclass
class Units:
    twist_units: int = 10
    velocity_units: int = 60
    pressure_units: int = 40
    sight_height_units: int = 15
    temp_units: int = 51
    drop_units: int = 16
    energy_units: int = 30
    distance_units: int = 17
    angular_units: int = 1
    length_units: int = 10
    diameter_units: int = 10
    weight_units: int = 70
    path_units: int = 3

