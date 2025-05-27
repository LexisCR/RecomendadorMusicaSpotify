import unittest
import sys
import subprocess

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('test')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

if __name__ == "__main__":
    print("Ejecutando testeos...")
    tests_passed = run_tests()
    if not tests_passed:
        print("Una o varias prueban contienen errores. El archivo main no se ejecutará.")
        sys.exit(1)
    print("Todas las pruebas se han pasado. El archivo main se ejecutara...\n")
    subprocess.run([sys.executable, "main.py"])