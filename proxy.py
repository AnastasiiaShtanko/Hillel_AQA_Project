import os


class Reader:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:
            self.data = f.read()


class Writer:
    def __init__(self, file_path):
        self.__file_path = file_path

    def write(self, row):
        with open(self.__file_path, 'a') as f:
            f.write(row + '\n')  # Додає рядок в кінець файлу


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None
        self.last_modified = None
        self.last_written = None  # Відстеження останнього записаного рядка

    def read(self):

        current_modified = os.path.getmtime(self.file_path)
        if self.data is None or current_modified != self.last_modified:
            self.reader.read_file()
            self.data = self.reader.data
            self.last_modified = current_modified

    def write(self, row):

        #self.read()  # Забезпечити читання даних перед записом

        if self.data is None or (self.last_written and row == self.last_written):
            return

        self.writer.write(row)  # Використовує клас Writer для запису

        # Оновлюємо час останньої модифікації та останній записаний рядок
        #self.last_modified = os.path.getmtime(self.file_path)
        self.last_written = row


# Приклад використання:
proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')

proxy_rw.read()
proxy_rw.read()
proxy_rw.write('aa')  # запис в файл відбувається
proxy_rw.read()
proxy_rw.write('aa')  # запис в файл НЕ відбувається
proxy_rw.read()
proxy_rw.write('ab')  # запис в файл відбувається
proxy_rw.read()
proxy_rw.write('aa')  # запис в файл відбувається

print(proxy_rw.data)
