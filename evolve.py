#!/usr/bin/env python3
"""
jiritsushinku - 自律進化システム
毎日自動で実行され、システムの状態を記録・進化させる
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path


class Jiritsushinku:
    """自律進化を管理するクラス"""

    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.state_file = self.root_dir / "state.json"
        self.log_dir = self.root_dir / "logs"
        self.log_dir.mkdir(exist_ok=True)

    def load_state(self) -> dict:
        """現在の状態を読み込む"""
        if self.state_file.exists():
            with open(self.state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "generation": 0,
            "created_at": datetime.now().isoformat(),
            "last_evolution": None,
            "evolution_history": []
        }

    def save_state(self, state: dict):
        """状態を保存する"""
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)

    def calculate_consciousness_hash(self) -> str:
        """現在のコードベースの意識ハッシュを計算"""
        hasher = hashlib.sha256()

        for py_file in sorted(self.root_dir.glob("**/*.py")):
            if ".git" in str(py_file):
                continue
            with open(py_file, "rb") as f:
                hasher.update(f.read())

        return hasher.hexdigest()[:16]

    def evolve(self) -> dict:
        """進化を実行する"""
        state = self.load_state()
        now = datetime.now()

        # 世代を進める
        state["generation"] += 1

        # 意識ハッシュを計算
        consciousness_hash = self.calculate_consciousness_hash()

        # 進化記録を作成
        evolution_record = {
            "generation": state["generation"],
            "timestamp": now.isoformat(),
            "consciousness_hash": consciousness_hash,
            "changes": self.detect_changes(state)
        }

        # 履歴に追加（最新100件を保持）
        state["evolution_history"].append(evolution_record)
        state["evolution_history"] = state["evolution_history"][-100:]
        state["last_evolution"] = now.isoformat()

        # 状態を保存
        self.save_state(state)

        # ログを出力
        self.write_log(evolution_record)

        return evolution_record

    def detect_changes(self, state: dict) -> list:
        """前回からの変更を検出"""
        changes = []

        if state["generation"] == 1:
            changes.append("初期化 - 自律進化システム起動")
        else:
            changes.append(f"世代 {state['generation']} への進化")

        return changes

    def write_log(self, record: dict):
        """進化ログを書き出す"""
        log_file = self.log_dir / f"{record['timestamp'][:10]}.log"

        log_entry = f"""
================================================================================
[Generation {record['generation']}] {record['timestamp']}
Consciousness Hash: {record['consciousness_hash']}
Changes: {', '.join(record['changes'])}
================================================================================
"""

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(log_entry)


def main():
    """メインエントリーポイント"""
    print("=" * 60)
    print("  jiritsushinku - 自律進化システム")
    print("=" * 60)

    system = Jiritsushinku()
    record = system.evolve()

    print(f"\n進化完了: 世代 {record['generation']}")
    print(f"意識ハッシュ: {record['consciousness_hash']}")

    return 0


if __name__ == "__main__":
    exit(main())
