def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

# BUG SECURITY: Command Injection (Bandit akan detect B602)
import subprocess

def run_command(cmd):
    """DANGEROUS: shell=True memungkinkan command injection"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
