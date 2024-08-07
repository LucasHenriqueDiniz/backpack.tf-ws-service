import logging
import coloredlogs
from datetime import datetime


def configure_logging(print_events=0):
    """
    Configura o logging com base no valor de print_events.

    Args:
        filename (str, optional): Nome do arquivo de log. Padrão: "logfile.txt".
        print_events (int, optional): Nível de detalhe dos logs. Padrão: 0 (nenhum).
    """
    # Mapeamento de valores para níveis de log
    log_levels = {
        0: logging.CRITICAL,
        1: logging.ERROR,
        2: logging.WARNING,
        3: logging.INFO,
        4: logging.DEBUG,
    }

    # Obtém o nível de log correspondente ao valor de print_events
    log_level = log_levels.get(
        print_events, logging.INFO
    )  # Nível padrão se não encontrado

    filename = f"logs/ERROR_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    coloredlogs.install(level=log_level)

    formatter = logging.Formatter(
        f"%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Configura o logger
    logging.basicConfig(
        filename=filename,
        level=log_level,
        datefmt="%Y-%m-%d %H:%M:%S",
        formatter=formatter,
    )
