"""MarkItDown - A utility for converting various file formats to Markdown.

This package provides tools to convert documents, spreadsheets, presentations,
and other file formats into clean, readable Markdown text.

Note: Forked from microsoft/markitdown for personal use and experimentation.

Personal fork notes:
- Tracking upstream at microsoft/markitdown
- Added StreamInfo to top-level exports for easier programmatic usage
- Pinned __version__ to track local changes separately from upstream releases
- Added __all__ export for UnsupportedFormatException for cleaner error handling
- Exposed FileConversionException at top level alongside UnsupportedFormatException
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

# Upstream version this fork is based on, plus a local suffix to distinguish
# personal changes from official releases.
__version__ = "0.1.0.post1+personal"
__author__ = "MarkItDown Contributors"
__license__ = "MIT"

# Expose StreamInfo if available, as it's useful for programmatic usage
try:
    from markitdown._markitdown import StreamInfo
    __all__ = [
        "MarkItDown",
        "DocumentConverter",
        "ConversionResult",
        "StreamInfo",
        "__version__",
    ]
except ImportError:
    __all__ = [
        "MarkItDown",
        "DocumentConverter",
        "ConversionResult",
        "__version__",
    ]

# Also expose UnsupportedFormatException if available, so callers can catch it
# without digging into the private _markitdown module.
try:
    from markitdown._markitdown import UnsupportedFormatException
    __all__ = __all__ + ["UnsupportedFormatException"]
except ImportError:
    pass

# Expose FileConversionException for callers who want to catch conversion errors
# separately from unsupported format errors. Useful when you want to distinguish
# between "we don't support this format" vs "we tried but something went wrong".
try:
    from markitdown._markitdown import FileConversionException
    __all__ = __all__ + ["FileConversionException"]
except ImportError:
    pass
