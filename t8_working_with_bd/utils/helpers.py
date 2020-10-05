from tabulate import tabulate
from t8_working_with_bd.logger.logger import log


def create_table(result):
    rows = [x.values() for x in result]
    tab = tabulate(rows, headers=result[0].keys())
    log.info('\n{}'.format(tab))