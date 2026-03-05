"""KORE — File Tools
=================

Utility helpers for working with files. Includes the existing read/write
tools for the outputs/ directory and a helper to scan a repository for
Python files.
"""

import os
from crewai.tools import tool
from config.settings import OUTPUTS_DIR
from typing import Iterable, Optional


@tool("Write to File")
def file_write_tool(input: str) -> str:
    """
    Write content to a file in the outputs/ directory.

    Input format (pipe-delimited):
        filename.txt|content to write here

    Example:
        kore_execution_log.txt|Phase 1 complete. Deliverable: ...

    Returns a confirmation message or an error.
    """
    try:
        parts = input.split("|", 1)
        if len(parts) != 2:
            return (
                "❌ Error: use format 'filename.txt|content'\n"
                f"Received: {input[:120]}"
            )
        filename, content = parts[0].strip(), parts[1].strip()

        # Safety: keep files inside outputs/
        safe_name = os.path.basename(filename)
        filepath  = os.path.join(OUTPUTS_DIR, safe_name)

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)

        return f"✅ Saved to {filepath} ({len(content)} chars)"
    except Exception as exc:
        return f"❌ File write failed: {exc}"


# ---------------------------------------------------------------------------
# repository scanning helpers
# ---------------------------------------------------------------------------


from typing import Iterable, Optional

def find_python_files(
    root_path: str,
    extensions: Optional[Iterable[str]] = None,
    sort: bool = True,
) -> list[str]:
    """Recursively scan ``root_path`` and return matching file paths.

    Parameters
    ----------
    root_path:
        A file or directory to search.  If it's a file and matches the
        requested extensions it will be returned as a single-element list.
    extensions:
        Iterable of suffix strings to match (e.g. ``['.py', '.pyw']``).  If
        :data:`None` the function defaults to ``['.py']``.
    sort:
        If ``True`` the resulting list is returned in lexical order.  This
        makes results deterministic for testing.

    Returns
    -------
    List[str]
        Absolute paths to matching files.

    Example::

        >>> find_python_files('src')
        ['/path/to/src/main.py', '/path/to/src/tools/file_tool.py']
    """

    ext_list = tuple(extensions) if extensions is not None else (".py",)

    python_files: list[str] = []

    root_path = os.path.abspath(root_path)
    if os.path.isfile(root_path):
        for ext in ext_list:
            if root_path.endswith(ext):
                return [root_path]
        return []

    for dirpath, dirnames, filenames in os.walk(root_path):
        # skip cache directories
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for fname in filenames:
            if any(fname.endswith(ext) for ext in ext_list):
                python_files.append(os.path.join(dirpath, fname))

    if sort:
        python_files.sort()
    return python_files


@tool("Read from File")
def file_read_tool(filename: str) -> str:
    """
    Read a file from the outputs/ directory.

    Input: filename only (e.g. 'kore_execution_log.txt')
    Returns: file contents as a string, or an error message.
    """
    try:
        safe_name = os.path.basename(filename.strip())
        filepath  = os.path.join(OUTPUTS_DIR, safe_name)

        if not os.path.exists(filepath):
            return f"❌ File not found: {filepath}"

        with open(filepath, "r", encoding="utf-8") as fh:
            content = fh.read()

        return f"📄 Contents of {safe_name}:\n\n{content}"
    except Exception as exc:
        return f"❌ File read failed: {exc}"
