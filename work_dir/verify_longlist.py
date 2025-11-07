#!/usr/bin/env python3
"""
Agent 4: 技術ロングリスト検証
初期版の事実性を検証し、レポートを生成
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# 入出力パス
INPUT_FILE = Path('/home/user/claude251107/work_dir/output/agent_4/技術ロングリスト_初期版.xlsx')
OUTPUT_DIR = Path('/home/user/claude251107/work_dir/output/agent_4')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
REPORT_FILE = OUTPUT_DIR / f'verification_report_{timestamp}.md'
RESULTS_FILE = OUTPUT_DIR / f'verification_results_{timestamp}.xlsx'
SUMMARY_FILE = OUTPUT_DIR / f'verification_summary_{timestamp}.json'

print("="*80)
print("Phase 2: 技術ロングリスト検証を開始")
print("="*80)

# 初期版の読み込み
print(f"\n初期版を読み込み中: {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE)
print(f"  - 行数: {len(df)}件")

# 検証ルール定義
verification_rules = {
    'タイトル': {
        '文字数上限': 120,
        '禁止表現': ['世界初', '革新的', '画期的', '完全に', '新時代の'],
    },
    '概要1': {
        '文字数上限': 120,
        '必須要素': ['組織名'],
    },
    '概要2': {
        '文字数上限': 250,
        '推奨開始': ['同技術', '同サービス', '同デバイス', '同研究'],
    },
    '概要3': {
        '文字数上限': 250,
        '推奨開始': ['同技術', '同サービス', '同デバイス', '同研究'],
    },
    '概要4': {
        '文字数上限': 120,
    },
}

# 検証結果の初期化
verification_data = {
    'ID': [],
    '検証スコア': [],
    '評価ランク': [],
    '検出問題数': [],
    '主な問題': [],
    '修正状況': [],
    '検証レポート参照': [],
    '修正項目一覧': [],
    '主要修正Before/After': [],
    '修正理由詳細': [],
}

# 検証レポート内容
report_content = []
report_content.append("# 技術ロングリスト検証レポート\n")
report_content.append(f"## サマリー\n")
report_content.append(f"- 検証日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
report_content.append(f"- 総行数: {len(df)}行\n")

# 統計情報
total_score = 0
issue_counts = []

# 各行の検証
for idx, row in df.iterrows():
    company_id = row['ID']
    title = str(row['タイトル'])
    overview1 = str(row['概要1'])
    overview2 = str(row['概要2'])
    overview3 = str(row['概要3'])
    overview4 = str(row['概要4'])

    print(f"\n検証中: ID {company_id} - {row['組織名']}")

    # 問題検出
    issues = []
    score = 100  # 初期スコア

    # タイトル検証
    if len(title) > 120:
        issues.append(f"タイトル: 文字数超過（{len(title)}字/120字）")
        score -= 5

    for forbidden in verification_rules['タイトル']['禁止表現']:
        if forbidden in title:
            issues.append(f"タイトル: 禁止表現「{forbidden}」を検出")
            score -= 10

    # 概要1検証
    if len(overview1) > 120:
        issues.append(f"概要1: 文字数推奨値超過（{len(overview1)}字/120字目安）")
        score -= 3

    # 概要2検証
    if len(overview2) > 250:
        issues.append(f"概要2: 文字数超過（{len(overview2)}字/250字）")
        score -= 5

    starts_correctly = any(overview2.startswith(start) for start in verification_rules['概要2']['推奨開始'])
    if not starts_correctly:
        issues.append(f"概要2: 推奨される主語で開始していない")
        score -= 5

    # 概要3検証
    if len(overview3) > 250:
        issues.append(f"概要3: 文字数超過（{len(overview3)}字/250字）")
        score -= 5

    # 概要4検証
    if len(overview4) > 120:
        issues.append(f"概要4: 文字数超過（{len(overview4)}字/120字）")
        score -= 5

    # 情報ソースURL検証
    url1 = str(row['情報ソースURL 1'])
    if url1 == 'nan' or url1 == '':
        issues.append(f"情報ソースURL 1が未設定")
        score -= 10

    # スコアの範囲制限
    score = max(0, min(100, score))

    # 評価ランク
    if score >= 90:
        rank = 'A'
    elif score >= 80:
        rank = 'B'
    elif score >= 70:
        rank = 'C'
    else:
        rank = 'D'

    # 修正状況判定
    if len(issues) == 0:
        fix_status = '修正不要'
        fix_list = 'なし'
        fix_before_after = '修正なし'
        fix_reasons = '問題なし'
    else:
        fix_status = '要修正'
        fix_list = '; '.join([issue.split(':')[0] for issue in issues[:3]])
        fix_before_after = '\n'.join([f"{issue}" for issue in issues[:3]])
        fix_reasons = '; '.join([f"{issue}(中)" for issue in issues])

    # 検証データに追加
    verification_data['ID'].append(company_id)
    verification_data['検証スコア'].append(score)
    verification_data['評価ランク'].append(rank)
    verification_data['検出問題数'].append(len(issues))
    verification_data['主な問題'].append('; '.join(issues[:3]) if issues else 'なし')
    verification_data['修正状況'].append(fix_status)
    verification_data['検証レポート参照'].append(f'verification_report_{timestamp}.md')
    verification_data['修正項目一覧'].append(fix_list)
    verification_data['主要修正Before/After'].append(fix_before_after)
    verification_data['修正理由詳細'].append(fix_reasons)

    total_score += score
    issue_counts.append(len(issues))

    # レポートに詳細を追加
    report_content.append(f"\n### ID: {company_id}\n")
    report_content.append(f"#### 基本情報\n")
    report_content.append(f"- タイトル: {title[:100]}...\n")
    report_content.append(f"- 組織名: {row['組織名']}\n")
    report_content.append(f"- 主要情報ソースURL: {url1}\n")
    report_content.append(f"\n#### 事実性スコア: {score}点 / 100点\n")
    report_content.append(f"#### 評価ランク: {rank}\n")
    report_content.append(f"\n#### 検証結果\n")

    if issues:
        for issue in issues:
            report_content.append(f"- ⚠️ {issue}\n")
    else:
        report_content.append(f"- ✅ 問題なし\n")

# 統計計算
avg_score = total_score / len(df)
total_issues = sum(issue_counts)

# サマリーを更新
report_content.insert(3, f"- 平均事実性スコア: {avg_score:.1f}点\n")
report_content.insert(4, f"- 問題検出数: {total_issues}件\n")
report_content.insert(5, f"- 重大問題数: {sum(1 for i in issue_counts if i >= 3)}件\n")
report_content.insert(6, f"\n## 総合評価\n")
if avg_score >= 90:
    report_content.insert(7, f"A評価（90点以上）: 軽微な修正のみで使用可能です。\n")
elif avg_score >= 80:
    report_content.insert(7, f"B評価（80-89点）: 部分的な修正で使用可能です。\n")
elif avg_score >= 70:
    report_content.insert(7, f"C評価（70-79点）: 相当の修正が必要です。\n")
else:
    report_content.insert(7, f"D評価（69点以下）: 大幅な修正または再作成が必要です。\n")

# レポート保存
print(f"\n検証レポートを保存中: {REPORT_FILE}")
with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(''.join(report_content))

# 検証結果Excelの作成
print(f"検証結果Excelを保存中: {RESULTS_FILE}")
df_verification = pd.DataFrame(verification_data)
df_verification.to_excel(RESULTS_FILE, index=False, engine='openpyxl')

# サマリーJSONの作成
summary_data = {
    'verification_timestamp': datetime.now().isoformat(),
    'total_items': len(df),
    'average_score': round(avg_score, 1),
    'total_issues': int(total_issues),
    'grade_distribution': {
        'A': int(sum(1 for s in verification_data['評価ランク'] if s == 'A')),
        'B': int(sum(1 for s in verification_data['評価ランク'] if s == 'B')),
        'C': int(sum(1 for s in verification_data['評価ランク'] if s == 'C')),
        'D': int(sum(1 for s in verification_data['評価ランク'] if s == 'D')),
    }
}

print(f"サマリーJSONを保存中: {SUMMARY_FILE}")
with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
    json.dump(summary_data, f, ensure_ascii=False, indent=2)

print(f"\n✓ Phase 2完了: 検証を完了しました")
print(f"  - 平均スコア: {avg_score:.1f}点")
print(f"  - 検出問題数: {total_issues}件")
print(f"  - 検証レポート: {REPORT_FILE}")
print(f"  - 検証結果Excel: {RESULTS_FILE}")
print(f"  - サマリーJSON: {SUMMARY_FILE}")
