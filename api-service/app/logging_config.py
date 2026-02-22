import logging
import sys

def setup_logging(log_level):
    """Configure logging with the specified log level."""
    logger = logging.getLogger()

    # Clear existing handlers
    logger.handlers.clear()

    # Convert string level to logging constant
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)

    # Create stream handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # Set format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Attach handler
    logger.addHandler(handler)

    return logger