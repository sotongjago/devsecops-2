from src.app import add, divide, run_command
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Tidak boleh bagi nol"):
        divide(10, 0)

def test_run_command():
    # Hanya test fungsi dasar (bukan security)
    output = run_command("echo Hello World")
    assert "Hello World" in output
