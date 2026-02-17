# Excel to CSV Converter

Excelファイルをディレクトリに配置するだけで、自動的にCSVに変換するツール。

## 特徴

- **自動監視:** `excel/` ディレクトリにファイルが追加・更新されると即座に変換を実行。
- **SOLID原則:** 拡張性を考慮した設計（`FileConverter` インターフェース）。
- **TDD:** `pytest` によるテスト駆動開発で品質を担保。
- **高速な環境管理:** `uv` を使用した高速なパッケージ管理。

## ディレクトリ構成

- `excel/`: 変換したい Excel ファイル (.xlsx) を配置。
- `csv/`: 変換された CSV ファイルが格納される。
- `excel_csv_converter/`: 変換ロジックのコアコード。
- `tests/`: 単体テスト。

## セットアップ

### 必要条件

- [uv](https://github.com/astral-sh/uv) がインストールされていること。

### インストール

```bash
uv sync
```

## 使い方

1. 監視・変換プロセスを開始：
   ```bash
   uv run python main.py
   ```
2. `excel/` ディレクトリに Excel ファイルを配置。
3. `csv/` ディレクトリに変換された CSV ファイルが自動生成される。

## 開発

### テストの実行

```bash
uv run pytest
```

### GitHub Actions

GitHub に push または pull request を送ると、自動的にテストが実行される。
