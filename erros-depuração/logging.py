import logging

LOG_FORMAT = "%(levelname)s  %(asctime)s - %(message)s"
logging.basicConfig(filename="app.log", level=logging.DEBUG, filemode="w", format=LOG_FORMAT)

log = logging.getLogger()

log.info("Olá")
log.critical("Erro grave")
log.error("Olá")
log.debug("Erro grave")
log.warning("Erro grave")
log.level
