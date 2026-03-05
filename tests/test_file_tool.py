import os
import sys
import tempfile

# ensure workspace root is on path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.file_tool import find_python_files


def test_find_single_file(tmp_path):
    file = tmp_path / "example.py"
    file.write_text("print('hello')")
    assert find_python_files(str(file)) == [str(file)]


def test_find_in_directory(tmp_path):
    # create nested structure
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    f1 = pkg / "a.py"
    f1.write_text("# a")
    sub = pkg / "sub"
    sub.mkdir()
    f2 = sub / "b.py"
    f2.write_text("# b")

    results = find_python_files(str(tmp_path))
    assert str(f1) in results
    assert str(f2) in results
    assert len(results) == 2


def test_extensions_filter(tmp_path):
    f1 = tmp_path / "a.py"
    f1.write_text("")
    f2 = tmp_path / "c.txt"
    f2.write_text("")
    assert find_python_files(str(tmp_path), extensions=[".txt"]) == [str(f2)]


def test_sorting(tmp_path):
    files = [tmp_path / n for n in ("z.py", "a.py")]
    for f in files:
        f.write_text("")
    ordered = find_python_files(str(tmp_path))
    assert ordered == sorted(str(f) for f in files)
