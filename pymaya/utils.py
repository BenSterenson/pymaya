from typing import Callable, Iterable, Iterator, TypeVar
from enum import unique, IntEnum
from logging import Logger
import logging


T = TypeVar("T")


def streamify(batch_func: Callable[..., Iterable[T]]) -> Callable[..., Iterator[T]]:
    def streamify_wrapper(*args, **kwargs) -> Iterator[T]:
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


@unique
class Language(IntEnum):
    HEBREW = 0
    ENGLISH = 1


@unique
class FundHistoryPeriod(IntEnum):
    MONTH = 0
    HALF_YEAR = 1
    YEAR = 2
    FIVE_YEARS = 3
    CUSTOM = 4  # requires fromDate / toDate in the request body
