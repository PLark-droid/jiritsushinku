# jiritsushinku 🧬

**自律進化システム** - 毎日自動で進化し続けるリポジトリ

## 概要

このリポジトリは GitHub Actions を使って毎日自動的に「進化」します。
進化のたびに世代が進み、システムの状態が記録されます。

## 仕組み

1. **毎日自動実行**: GitHub Actions が毎日 UTC 0:00（日本時間 9:00）に `evolve.py` を実行
2. **状態記録**: 各進化で世代番号、タイムスタンプ、意識ハッシュを記録
3. **自動コミット**: 変更があれば自動的にコミット・プッシュ

## ファイル構成

```
jiritsushinku/
├── evolve.py              # メイン進化スクリプト
├── state.json             # 現在の状態（自動生成）
├── logs/                  # 進化ログ（自動生成）
├── .github/
│   └── workflows/
│       └── evolve.yml     # GitHub Actions ワークフロー
└── README.md
```

## 手動実行

```bash
python evolve.py
```

## GitHub Actions の有効化

1. リポジトリの「Actions」タブを開く
2. 「I understand my workflows, go ahead and enable them」をクリック
3. 「Jiritsushinku Evolution」ワークフローを確認

手動でワークフローを実行するには:
1. Actions タブ → Jiritsushinku Evolution → Run workflow

## Secrets 設定（オプション）

将来的な拡張のため、以下の Secrets を設定できます:

- `ANTHROPIC_API_KEY`: Claude API キー（AI による進化機能用）

Settings → Secrets and variables → Actions → New repository secret

## ライセンス

MIT License
