class CSVtoHTMLAdapter:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def convert_to_html(self):
        with open(self.csv_filename, 'r') as file:
            lines = file.readlines()

            # Отримуємо назви колонок з першого рядка
            headers = lines[0].strip().split(',')

            html_output = ""

            # Проходимо по рядках, починаючи з другого (індекс 1)
            for line in lines[1:]:
                values = line.strip().split(',')
                record_html = ""

                # Формуємо HTML-рядок для кожного значення в рядку
                for header, value in zip(headers, values):
                    record_html += f"<{header}>{value}</{header}>\n"

                # Додаємо роздільник між записами
                record_html += ".............\n"

                html_output += record_html

        return html_output


# Приклад використання:
adapter = CSVtoHTMLAdapter("data.csv")
html_output = adapter.convert_to_html()
print(html_output)
