from dataclasses import dataclass
import uuid
from random import random

@dataclass
class Street:
    name: str
    location: float
    snow_cover_cm: float

@dataclass
class SnowSweepery:
    id: uuid.uuid4()
    name: str
    location: (str | None)

SS = SnowSweepery(uuid.uuid4(), 'adam', 'Bielsko')

print(SS.id)

def create_city():

    s1 = Street('Cieszyńska', 2.41, snow_cover_cm=0.4)
    s2 = Street('Krakowska', 3.12, snow_cover_cm=0.2)
    s3 = Street('Lupiecka', 2.12, snow_cover_cm=0.1)
    s4 = Street('Lutomierska', 6.42, snow_cover_cm=0.3)
    s5 = Street('Piastowska', 3.44, snow_cover_cm=0.5)


    streets = dict()
    streets['Cieszyńska'] = s1
    streets['Krakowska'] = s2
    streets['Lupiecka'] = s3
    streets['Lutomierska'] = s4
    streets['Piastowska'] = s5

    return streets

# C
# self.current_snow_fall_rate = random()



if __name__ =='__main__':
    city = create_city()


    # ssweeper1 = SnowSweepery(uuid.uuid4(), 'adam', 'Bielsko')
    # async 
    print(random())