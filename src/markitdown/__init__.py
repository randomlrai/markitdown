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
- Re-exported all exception types under a single 'exceptions' tuple for convenience
- Added EXCEPTIONS_MAP dict for looking up exception types by name (personal addition)
- Added EXCEPTIONS as a base exception tuple usable directly in except clauses
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

# Convenience tuple of all exception types exported by this package.
# Handy for broad exception catching: `except markitdown.EXCEPTIONS as e:`
# Personal note: I kept tripping over which exceptions to catch, so this helps.
# Note: Python requires a plain tuple (not a variable) in except clauses, so
# use it like: `except tuple(markitdown.EXCEPTIONS) as e:` or unpack manually.
EXCEPTIONS = tuple(
    obj for name in ["UnsupportedFormatException", "FileConversionException"]
    if (obj := globals().get(name)) is not None
)

# Convenience dict mapping exception name -> exception class.
# Personal note: useful when I want to reference an exception type by string,
# e.g. in config-driven error handling or logging utilities.
EXCEPTIONS_MAP = {
    name: globals()[name]
    for name in ["UnsupportedFormatException", "FileConversionException"]
    if name in globals()
}
