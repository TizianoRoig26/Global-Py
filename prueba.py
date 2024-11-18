from Mutador import Mutador
from Radiacion import Radiacion
from Virus import Virus

adn = Virus(["123456","123456","123456","123456","123456","123456"], 'T')
adn_radiacion = Radiacion(["123456","123456","123456","123456","123456","123456"], 'T')
#adn = Radiacion(["123456","123456","123456","123456","123456","123456"], 'T')
adn_radiacion.crear_mutante()

#adn_virus = Virus(["123456","123456","123456","123456","123456","123456"], 'T')
#adn.crear_mutante()