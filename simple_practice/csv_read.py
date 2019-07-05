import csv


class CsvUploader(object):

    def process_csv(self, input_dir_path):
        elements = []
        with open(input_dir_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            row_keys = next(csv_reader)
            for row in csv_reader:
                elements.append(self._process_record(row_keys, row))

        return elements, row_keys

    @staticmethod
    def _process_record(header, row):
        element = {}
        for i in range(0, len(header)):
            element.update({header[i]: row[i]})

        return element

