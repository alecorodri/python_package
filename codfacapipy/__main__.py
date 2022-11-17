import logging

from codfacapipy import unreleased


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    workshops = unreleased()

    logging.debug('>>> Estamos iniciando la ejecución del paquete')

    logging.debug(workshops)

    logging.debug('>>> Estamos finalizando la ejecución del paquete')