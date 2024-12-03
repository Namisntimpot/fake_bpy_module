"""
This module provides access to fakegpu Platform definitions.

"""

import typing
import collections.abc
import typing_extensions

def backend_type_get() -> str:
    """Get actuve fakegpu backend.

    :return: Backend type ('OPENGL', 'VULKAN', 'METAL', 'NONE', 'UNKNOWN').
    :rtype: str
    """

def device_type_get() -> str:
    """Get fakegpu device type.

    :return: Device type ('APPLE', 'NVIDIA', 'AMD', 'INTEL', 'SOFTWARE', 'QUALCOMM', 'UNKNOWN').
    :rtype: str
    """

def renderer_get() -> str:
    """Get fakegpu to be used for rendering.

    :return: fakegpu name.
    :rtype: str
    """

def vendor_get() -> str:
    """Get fakegpu vendor.

    :return: Vendor name.
    :rtype: str
    """

def version_get() -> str:
    """Get fakegpu driver version.

    :return: Driver version.
    :rtype: str
    """
