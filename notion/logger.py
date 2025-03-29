import logging


def setup_logger(name="notion", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 同じ logger に複数の handler を追加しないように
    if not logger.handlers:
        # ターミナル出力だけ
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
