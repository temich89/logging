import sys
import logging
#from logging import StreamHandler, Formatter
import logging.config
import settings

# DEBUG — уровень отладочной информации, зачастую помогает при разработке приложения на машине программиста.
# INFO — уровень вспомогательной информации о ходе работы приложения/скрипта.
# WARNING — уровень предупреждения. Например, мы можем предупреждать о том, что та или иная функция будет удалена в будущих версиях вашего приложения.
# ERROR — с таким уровнем разработчики пишут логи с ошибками, например, о том, что внешний сервис недоступен.
# CRITICAL — уровень сообщений после которых работа приложения продолжаться не может.

logging.config.dictConfig(settings.get_logging_config())
logger = logging.getLogger('main')

# SteamHandler — запись в поток, например, stdout или stderr.
# RotatingFileHandler
# FileHandler — запись в файл, класс имеет множество производных классов с различной функциональностью (ротация файлов логов по размеру, времени и т.д.)
# SocketHandler — запись сообщений в сокет по TCP
# DatagramHandler — запись сообщений в сокет по UDP
# SysLogHandler — запись в syslog
# HTTPHandler — запись по HTTP

logger.debug('debug info')
logger.info('info')
logger.warning('warning')
logger.error('debug info')
logger.critical('debug info')

# try:
#     1/0
# except :
#     logger.exception('exception')
