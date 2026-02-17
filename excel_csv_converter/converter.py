from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FileConverter(ABC):
    @abstractmethod
    def convert(self, input_path: Path, output_path: Path):
        pass

class ExcelToCsv(FileConverter):
    def convert(self, input_path: Path, output_path: Path):
        df = pd.read_excel(input_path)
        # フォルダパスが存在しない場合は作成
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Converted: {input_path} -> {output_path}")

class ExcelToCsvConverter:
    def __init__(self, input_dir: Path, output_dir: Path, converter: FileConverter = ExcelToCsv()):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.converter = converter

    def convert_all(self):
        for excel_file in self.input_dir.glob("*.xlsx"):
            csv_filename = excel_file.stem + ".csv"
            output_path = self.output_dir / csv_filename
            self.converter.convert(excel_file, output_path)

class ExcelHandler(FileSystemEventHandler):
    def __init__(self, converter: ExcelToCsvConverter):
        self.converter = converter

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".xlsx"):
            self.converter.convert_all()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".xlsx"):
            self.converter.convert_all()

def start_watching(input_dir: Path, output_dir: Path):
    converter = ExcelToCsvConverter(input_dir, output_dir)
    handler = ExcelHandler(converter)
    observer = Observer()
    observer.schedule(handler, str(input_dir), recursive=False)
    observer.start()
    print(f"Watching {input_dir} for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
