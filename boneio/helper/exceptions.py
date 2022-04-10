"""BoneIO Errors"""


class BoneIOException(Exception):
    """BoneIO standard exception."""


class GPIOInputException(BoneIOException):
    """GPIOInput Exception."""


class I2CError(BoneIOException):
    """I2C Exception."""


class ConfigurationException(BoneIOException):
    """Configuration yaml exception."""


class CoverRelayException(BoneIOException):
    """Cover configuration exception."""
