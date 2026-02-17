import os
import pandas as pd
import pytest
from excel_csv_converter.converter import ExcelToCsvConverter

def test_convert_single_file(tmp_path):
    # Setup
    excel_dir = tmp_path / "excel"
    csv_dir = tmp_path / "csv"
    excel_dir.mkdir()
    csv_dir.mkdir()
    
    excel_file = excel_dir / "test.xlsx"
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [30, 25]})
    df.to_excel(excel_file, index=False)
    
    converter = ExcelToCsvConverter(excel_dir, csv_dir)
    
    # Execute
    converter.convert_all()
    
    # Verify
    csv_file = csv_dir / "test.csv"
    assert csv_file.exists()
    df_csv = pd.read_csv(csv_file)
    pd.testing.assert_frame_equal(df, df_csv)

def test_convert_multiple_files(tmp_path):
    # Setup
    excel_dir = tmp_path / "excel"
    csv_dir = tmp_path / "csv"
    excel_dir.mkdir()
    csv_dir.mkdir()
    
    excel_files = ["test1.xlsx", "test2.xlsx"]
    for name in excel_files:
        pd.DataFrame({"Name": [name]}).to_excel(excel_dir / name, index=False)
    
    converter = ExcelToCsvConverter(excel_dir, csv_dir)
    
    # Execute
    converter.convert_all()
    
    # Verify
    for name in excel_files:
        csv_file = csv_dir / name.replace(".xlsx", ".csv")
        assert csv_file.exists()
