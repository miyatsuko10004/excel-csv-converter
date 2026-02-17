from pathlib import Path
from excel_csv_converter.converter import start_watching

if __name__ == "__main__":
    input_dir = Path("excel")
    output_dir = Path("csv")
    
    # 既存のファイルを一度全て変換
    from excel_csv_converter.converter import ExcelToCsvConverter
    converter = ExcelToCsvConverter(input_dir, output_dir)
    converter.convert_all()
    
    # 監視を開始
    start_watching(input_dir, output_dir)