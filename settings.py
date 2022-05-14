# version — ключ указывает версию конфига, рекомендуется наличие этого ключа со значением 1, нужно для обратной совместимости в случае, если в будущем появятся новые версии конфигов.
# disable_existing_loggers — запрещает или разрешает настройки для существующих логеров (на момент запуска), по умолчанию равен True
# formatters — настройки форматов логов
# handlers — настройки для обработчиков логов
# loggers — настройки существующих логеров

def get_logging_config():
    return {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default_formatter': {
                'format': '%(asctime)s %(levelname)s - %(message)s'
            },
        },

        'handlers': {
            'stream_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'default_formatter',
            },
        },

        'loggers': {
            'main': {
                'handlers': ['stream_handler'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
