from logging import Logger
import logging


def streamify(batch_func):
    def streamify_wrapper(*args, **kwargs):
        kwargs["page"] = kwargs.get("page", 1)
        batch = batch_func(*args, **kwargs)
        while batch:
            yield from batch
            kwargs["page"] += 1
            batch = batch_func(*args, **kwargs)

    return streamify_wrapper


def get_logger(logger_name) -> Logger:
    logger = logging.getLogger(logger_name)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]")
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    return logger
