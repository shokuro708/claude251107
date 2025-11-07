#!/usr/bin/env python3
"""
Excel統合スクリプト - tech-longlist-orchestrator用

複数エージェントが生成した技術ロングリストExcelファイルを統合する。
"""

import pandas as pd
import glob
import os
from pathlib import Path
from datetime import datetime


def merge_agent_results(output_dir='work_dir/output', output_file='技術ロングリスト_最終統合版.xlsx'):
    """
    各エージェントの結果を統合

    Args:
        output_dir (str): エージェント出力ディレクトリ
        output_file (str): 統合後のファイル名

    Returns:
        pd.DataFrame: 統合データフレーム
        dict: 統合統計情報
    """
    print(f"\n{'='*60}")
    print(f"Excel統合処理開始")
    print(f"{'='*60}")

    # 各エージェントの修正版ファイルを検索
    pattern = os.path.join(output_dir, 'agent_*', '技術ロングリスト_修正版.xlsx')
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"❌ エラー: 統合対象ファイルが見つかりません")
        print(f"検索パターン: {pattern}")
        raise FileNotFoundError(f"統合対象ファイルが見つかりません: {pattern}")

    print(f"統合対象ファイル数: {len(files)}件")
    print(f"{'='*60}\n")

    # データフレーム読み込み
    dfs = []
    agent_stats = []

    for file in files:
        # エージェント番号を抽出
        agent_num = file.split('agent_')[1].split(os.sep)[0]

        try:
            df = pd.read_excel(file)
            dfs.append(df)

            # 統計情報記録
            agent_stats.append({
                'agent_id': agent_num,
                'file': file,
                'row_count': len(df),
                'columns': df.columns.tolist()
            })

            print(f"Agent {agent_num}: {len(df):3d}件 | {file}")

        except Exception as e:
            print(f"❌ エラー: Agent {agent_num}のファイル読み込み失敗 - {e}")
            raise

    if not dfs:
        print(f"❌ エラー: 読み込み可能なファイルがありません")
        raise ValueError("読み込み可能なファイルがありません")

    print(f"\n{'='*60}")
    print(f"データ統合中...")
    print(f"{'='*60}\n")

    # 統合
    merged_df = pd.concat(dfs, ignore_index=True)

    # ID列でソート（存在する場合）
    if 'ID' in merged_df.columns:
        merged_df = merged_df.sort_values('ID').reset_index(drop=True)
        print(f"✅ ID列でソート完了")

    # 重複チェック
    duplicate_info = check_duplicates(merged_df)

    # ファイル出力
    try:
        merged_df.to_excel(output_file, index=False)
        print(f"\n✅ 統合ファイル出力完了: {output_file}")
    except Exception as e:
        print(f"❌ エラー: ファイル出力失敗 - {e}")
        raise

    # 統計情報作成
    stats = {
        'total_rows': len(merged_df),
        'total_agents': len(files),
        'agent_stats': agent_stats,
        'duplicate_info': duplicate_info,
        'timestamp': datetime.now().isoformat(),
        'output_file': output_file
    }

    print(f"{'='*60}")
    print(f"統合完了サマリー")
    print(f"{'='*60}")
    print(f"総件数: {stats['total_rows']}件")
    print(f"エージェント数: {stats['total_agents']}個")

    if duplicate_info['has_duplicates']:
        print(f"⚠️  重複ID: {duplicate_info['duplicate_count']}件")
    else:
        print(f"✅ 重複なし")

    print(f"{'='*60}\n")

    return merged_df, stats


def check_duplicates(df):
    """
    重複IDをチェック

    Args:
        df (pd.DataFrame): 統合データフレーム

    Returns:
        dict: 重複情報
    """
    duplicate_info = {
        'has_duplicates': False,
        'duplicate_count': 0,
        'duplicate_ids': []
    }

    if 'ID' not in df.columns:
        return duplicate_info

    # 重複検出
    duplicates = df[df.duplicated('ID', keep=False)]

    if not duplicates.empty:
        duplicate_info['has_duplicates'] = True
        duplicate_info['duplicate_count'] = len(duplicates)

        # 重複IDリスト取得
        duplicate_ids = duplicates['ID'].unique().tolist()
        duplicate_info['duplicate_ids'] = duplicate_ids

        print(f"\n⚠️  警告: 重複ID検出 - {len(duplicates)}件")
        print(f"{'='*60}")

        for dup_id in duplicate_ids[:10]:  # 最初の10件のみ表示
            dup_rows = duplicates[duplicates['ID'] == dup_id]
            print(f"ID: {dup_id} | 重複数: {len(dup_rows)}件")
            if 'タイトル' in dup_rows.columns:
                for _, row in dup_rows.iterrows():
                    print(f"  - {row['タイトル'][:50]}...")

        if len(duplicate_ids) > 10:
            print(f"... 他 {len(duplicate_ids) - 10}件の重複ID")

        print(f"{'='*60}\n")

    return duplicate_info


def validate_merge(stats):
    """
    統合結果の検証

    Args:
        stats (dict): 統合統計情報

    Returns:
        bool: 検証成功ならTrue
    """
    print(f"\n{'='*60}")
    print(f"統合結果検証")
    print(f"{'='*60}")

    # 出力ファイル存在確認
    if not os.path.exists(stats['output_file']):
        print(f"❌ エラー: 出力ファイルが存在しません - {stats['output_file']}")
        return False

    # 行数検証
    expected_rows = sum(agent['row_count'] for agent in stats['agent_stats'])
    actual_rows = stats['total_rows']

    print(f"期待行数: {expected_rows}件")
    print(f"実際行数: {actual_rows}件")

    if expected_rows != actual_rows:
        print(f"❌ エラー: 行数が一致しません")
        return False

    # 重複警告
    if stats['duplicate_info']['has_duplicates']:
        print(f"⚠️  警告: 重複IDが存在します（検証は継続）")

    print(f"✅ 検証成功: ファイル生成完了、行数一致")
    print(f"{'='*60}\n")

    return True


def generate_merge_report(stats, report_file='統合レポート.md'):
    """
    統合レポート生成

    Args:
        stats (dict): 統合統計情報
        report_file (str): レポートファイル名

    Returns:
        str: レポートファイルパス
    """
    print(f"統合レポート生成中: {report_file}")

    report_content = f"""# 技術ロングリスト統合レポート

## 統合サマリー

- **統合日時**: {stats['timestamp']}
- **総件数**: {stats['total_rows']}件
- **エージェント数**: {stats['total_agents']}個
- **出力ファイル**: {stats['output_file']}

## エージェント別統計

| Agent | 件数 | ファイルパス |
|-------|------|------------|
"""

    for agent in stats['agent_stats']:
        report_content += f"| Agent {agent['agent_id']} | {agent['row_count']}件 | {agent['file']} |\n"

    # 重複情報
    if stats['duplicate_info']['has_duplicates']:
        report_content += f"\n## ⚠️ 重複ID検出\n\n"
        report_content += f"- **重複件数**: {stats['duplicate_info']['duplicate_count']}件\n"
        report_content += f"- **重複ID数**: {len(stats['duplicate_info']['duplicate_ids'])}個\n\n"

        report_content += "### 重複IDリスト\n\n"
        for dup_id in stats['duplicate_info']['duplicate_ids'][:20]:
            report_content += f"- ID: {dup_id}\n"

        if len(stats['duplicate_info']['duplicate_ids']) > 20:
            report_content += f"\n... 他 {len(stats['duplicate_info']['duplicate_ids']) - 20}件\n"

    else:
        report_content += f"\n## ✅ 重複チェック\n\n重複IDなし\n"

    report_content += f"\n## 推奨次ステップ\n\n"
    report_content += f"1. 統合ファイル確認: {stats['output_file']}\n"

    if stats['duplicate_info']['has_duplicates']:
        report_content += f"2. 重複ID調査: 上記の重複IDリストを確認\n"
        report_content += f"3. 必要に応じて手動調整または再実行\n"

    report_content += f"\n---\n生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    # ファイル出力
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"✅ レポート生成完了: {report_file}\n")

    return report_file


def main():
    """メイン処理"""
    import sys

    if len(sys.argv) < 2:
        output_dir = 'work_dir/output'
        output_file = '技術ロングリスト_最終統合版.xlsx'
    elif len(sys.argv) == 2:
        output_dir = sys.argv[1]
        output_file = '技術ロングリスト_最終統合版.xlsx'
    else:
        output_dir = sys.argv[1]
        output_file = sys.argv[2]

    print(f"使用方法: python merge_results.py [output_dir] [output_file]")
    print(f"\n現在の設定:")
    print(f"  出力ディレクトリ: {output_dir}")
    print(f"  統合ファイル名: {output_file}\n")

    try:
        # 統合実行
        merged_df, stats = merge_agent_results(output_dir, output_file)

        # 検証
        if validate_merge(stats):
            # レポート生成
            report_file = generate_merge_report(stats)

            print("✅ 統合処理が正常に完了しました\n")
            return 0
        else:
            print("❌ 統合処理でエラーが発生しました\n")
            return 1

    except Exception as e:
        print(f"\n❌ 致命的エラー: {e}\n")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
