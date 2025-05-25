import os

def create_dummy_file(filename, size_mb):
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

if __name__ == "__main__":
    create_dummy_file('10MB.txt', 10)
    create_dummy_file('50MB.txt', 50)
    create_dummy_file('100MB.txt', 100)
