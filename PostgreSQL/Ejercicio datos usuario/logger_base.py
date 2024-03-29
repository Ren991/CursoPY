import logging

log = logging

log.basicConfig(level=log.INFO,
                format = "%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt='%I:%M:S %p',
                handlers=[
                    log.FileHandler("capa_datos.log"),
                    log.StreamHandler()
                ])#=> Configuracion basica manejo de logging.
 

if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel info")
    log.error("Mensaje a nivel de error")
    log.critical("Mensaje a nivel critico")
    
