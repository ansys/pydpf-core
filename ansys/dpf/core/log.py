import logging


def setup_logger(loglevel="INFO"):
    """Set up the logger.

    Parameters
    ----------
    loglevel : str, optional
        The level of the logger to set up. The default is ``"INFO"``.
    """

    # return existing log if this function has already been called
    if hasattr(setup_logger, "log"):
        setup_logger.log.setLevel(loglevel)
        ch = setup_logger.log.handlers[0]
        ch.setLevel(loglevel)
        return setup_logger.log

    # create logger
    log = logging.getLogger(__name__)
    log.setLevel(loglevel)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)

    # create formatter
    formatstr = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    formatter = logging.Formatter(formatstr)

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    log.addHandler(ch)

    # make persistent
    setup_logger.log = log

    return log
