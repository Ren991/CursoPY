import logging

log = logging

log.basicConfig(level=log.DEBUG)

if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel info")
    log.error("Mensaje a nivel de error")
    log.critical("Mensaje a nivel critico")