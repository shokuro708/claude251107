#!/usr/bin/env python3
"""
技術ロングリスト作成スクリプト
Agent 2用: ID 14-26の13件を処理
"""

import pandas as pd
from datetime import datetime
import os

# 出力ディレクトリの確認
output_dir = '/home/user/claude251107/work_dir/output/agent_2'
os.makedirs(output_dir, exist_ok=True)

# 全エントリーのデータ
entries = []

# ===========================================
# ID 14: THIS™
# ===========================================
entries.append({
    'ID': 14,
    'タイトル': 'ファバビーンプロテイン、しいたけ、種子類を組み合わせた植物性高タンパク質食品「Super Superfood」',
    '概要1': '英国のTHIS™は、オリーブオイルを主成分とした植物性脂肪技術FAT 2.0™を開発し、植物由来の肉代替製品を製造・販売している。同社は2017年に設立され、ロンドンに本社を置く。',
    '概要2': '同製品は、ファバビーンプロテインを主要なタンパク源とし、しいたけ、かぼちゃの種、亜麻仁、ヘンプハート、チアシード、ほうれん草を組み合わせた「スーパーフード技術」を使用する。同技術は、豆、種子、きのこの自然な相乗効果を活用して、新しい植物ベースの食感を生み出す。同製品には、Super BlockとMarinated Piecesの2種類があり、Super Blockは高タンパク質ブロック型、Marinated Piecesはレモンとハーブのマリネで事前調理されたキューブ型である。',
    '概要3': '同製品のSuper Blockは、100gあたり18gのタンパク質を含み、同重量の典型的な豆腐ブロックと比較して30%多いタンパク質を提供する。また、オメガ3脂肪酸と鉄分も供給する。',
    '概要4': '同製品は、植物由来の高タンパク質食品を求める消費者をターゲットとし、2025年4月に英国のTesco、Ocado、Waitrose、Sainsburyで発売された。価格は1パックあたり3.95ポンドである。',
    '注目ポイント1': '・従来の植物由来タンパク質製品は、豆腐と比較して十分なタンパク質含有量を提供できないことが課題であった。',
    '注目ポイント2': '・同製品は、ファバビーンプロテイン、しいたけ、種子類を独自に組み合わせて、高タンパク質かつウマミ深度のある食感を実現した。\n・同製品のSuper Blockは、豆腐より30%多いタンパク質（18g/100g）を含み、オメガ3と鉄分を提供する。\n・同社は、オリーブオイルを主成分とする植物性脂肪FAT 2.0™の特許を含む合計3件の特許を保有している。',
    '注目ポイント3': '・同社は、2017年に設立され、2021年に英国小売市場で前年比333%の成長を記録した。\n・同社は、Caffé Nero、Honest Burger、Premier Inn、Prezzoなどの英国主要フードサービスチェーンとパートナーシップを締結している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://retailtimes.co.uk/this-to-the-rescue-this-launches-new-format-plant-based-protein-super-superfood-onto-supermarket-shelves-nationwide/',
    '発表年または出願年': 2025,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'THIS™',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United Kingdom',
    '組織設立年': 2017,
    '組織URL': 'https://this.co',
    '情報ソースURL 1': 'https://retailtimes.co.uk/this-to-the-rescue-this-launches-new-format-plant-based-protein-super-superfood-onto-supermarket-shelves-nationwide/',
    '情報ソースURL 2': 'https://plantbasednews.org/lifestyle/food/this-high-protein-superfood/',
    '情報ソースURL 3': 'https://sifted.eu/articles/this-plant-based-interview-ceo',
    '情報ソースURL 4': 'https://republic.com/this',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 15: Desert Control
# ===========================================
entries.append({
    'ID': 15,
    'タイトル': '砂粒子に粘土層を形成して水分保持能力を向上させる液体天然粘土技術「Liquid Natural Clay」',
    '概要1': 'ノルウェーのDesert Controlは、砂漠化、土壌劣化、水不足に対処する気候スマート農業技術ソリューションを開発している。同社は2015年に設立され、Sandnesに本社を置く。',
    '概要2': '同技術は、粘土と水のみを使用した特許取得済みの混合プロセスで作製される液体天然粘土（Liquid Natural Clay: LNC）である。同技術は、砂に噴霧されると、土壌にスポンジ状の層を形成する。具体的には、砂粒子の表面に1.5ナノメートルの厚さの粘土層を追加し、砂粒子に水分を吸着させることで、水と栄養素が土壌を透過せず、LNC強化層に保持される仕組みである。LNCは、現地で水と粘土のみを混合して作製され、化学添加物は一切使用しない純粋に自然な製品である。',
    '概要3': '同技術は、独立第三者機関による検証により、水消費量を最大50%削減し、作物収量を最大62%増加させることが実証されている。また、作物収量、バイオマス生産、炭素吸収を増加させながら、水と肥料消費を最大50%削減する。',
    '概要4': '同技術は、米国（カリフォルニア州、アリゾナ州）、UAE等における農業作物、ゴルフコース、景観プロジェクトに適用されている。',
    '注目ポイント1': '・砂漠地域における従来の農業は、水と栄養素が砂を透過して失われるため、水使用効率が低いことが課題であった。',
    '注目ポイント2': '・同技術は、化学添加物を一切使用せず、水と粘土のみを現地で混合して使用する純粋に自然な製品である。\n・同技術は、砂粒子に1.5ナノメートルの粘土層を形成し、スポンジ状の層として水分と植物必須栄養素を保持する。\n・同技術は、水使用量を最大50%削減し、収量を最大62%増加させることが第三者機関により検証されている。',
    '注目ポイント3': '・同社は、特許取得済みのLiquid Natural Clay技術を保有している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.cnn.com/2020/08/13/world/desert-control-liquid-nanoclay-spc-intl/index.html',
    '発表年または出願年': 2015,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Desert Control',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Norway',
    '組織設立年': 2015,
    '組織URL': 'https://desertcontrol.com',
    '情報ソースURL 1': 'https://www.cnn.com/2020/08/13/world/desert-control-liquid-nanoclay-spc-intl/index.html',
    '情報ソースURL 2': 'https://www.cleantech.com/agtech-inspiration-from-desert-to-fertile-land-desert-control-makes-the-2020-50-to-watch-list/',
    '情報ソースURL 3': 'https://desertcontrol.com',
    '情報ソースURL 4': 'https://aws.amazon.com/blogs/startups/beewise-combines-iot-and-ai-to-offer-an-automated-beehive/',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 16: Varaha
# ===========================================
entries.append({
    'ID': 16,
    'タイトル': 'リモートセンシングと機械学習を用いて農業における温室効果ガス削減と炭素クレジットを生成するプラットフォーム',
    '概要1': 'インドのVarahaは、発展途上国における意識的な自然ベースの介入を通じて気候変動を逆転させることを目的とした気候テクノロジー企業である。同社は2022年に農業エンジニアのMadhur Jain、Ankita Garg（COO）、Vishal Kuchanur（CTO）によって共同設立された。',
    '概要2': '同社は、リモートセンシング、機械学習、科学研究を組み合わせた測定・報告・検証（MRV）プラットフォームを提供し、再生農業、植林、バイオ炭プロジェクトからの温室効果ガス隔離と削減を定量化する。同プラットフォームは、インド、バングラデシュ、ネパール、ケニアの70万エーカー以上で作物を栽培する数千の小規模農家と協力し、水田における水使用量削減によるメタン排出抑制（世界の総排出量の2%を占める）、作物残渣焼却防止、植林・再植林・植生回復（ARR）、バイオ炭などの実践を支援する。',
    '概要3': '同社は、2025年1月にGoogleに10万クレジットを販売し、これは産業用バイオ炭における世界最大の二酸化炭素除去（CDR）オフテイク契約である。同社は、多様化したプロジェクトポートフォリオ全体で23万以上の炭素クレジットを契約・販売している。',
    '概要4': '同プラットフォームは、アジアおよびアフリカの小規模農家が気候に優しい農法に移行することを支援し、炭素クレジット市場への参加を可能にする。',
    '注目ポイント1': '・従来、小規模農家は炭素クレジット市場に参加する手段が限られており、気候変動対策の恩恵を受けることができなかった。\n・水田は、全世界の排出量の2%を占めるメタン排出源であり、削減が課題であった。',
    '注目ポイント2': '・同社は、リモートセンシングと機械学習を組み合わせた自動化されたMRVプラットフォームを提供し、温室効果ガス削減を定量化する。\n・同社は、小規模農家向けのエンドツーエンドの炭素クレジット開発者として機能する。\n・同社は、水使用削減、作物残渣焼却防止、植林、バイオ炭、岩石風化促進など複数の気候変動対策を支援する。',
    '注目ポイント3': '・同社は、2025年1月にGoogleとの世界最大の産業用バイオ炭CDRオフテイク契約を締結した。\n・同社は、RTP Globalが主導し、日本の農林中央金庫が参加したシリーズA資金調達で870万ドルを調達した（2024年）。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://agfundernews.com/breaking-varaha-signs-landmark-deal-with-google-to-make-smallholders-part-of-the-carbon-removal-solution',
    '発表年または出願年': 2022,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Varaha',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'India',
    '組織設立年': 2022,
    '組織URL': 'https://varaha.earth',
    '情報ソースURL 1': 'https://agfundernews.com/breaking-varaha-signs-landmark-deal-with-google-to-make-smallholders-part-of-the-carbon-removal-solution',
    '情報ソースURL 2': 'https://techcrunch.com/2024/02/21/varaha-india-carbon-credits-farmers/',
    '情報ソースURL 3': 'https://agfundernews.com/varaha-raises-8-7m-to-help-smallholders-in-asia-africa-transition-to-climate-friendly-farming-methods',
    '情報ソースURL 4': 'https://varaha.earth',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 17: LiveKindly Collective
# ===========================================
entries.append({
    'ID': 17,
    'タイトル': '植物由来の肉代替製品ブランドを統合する多ブランドポートフォリオ',
    '概要1': '米国のLIVEKINDLY Collectiveは、植物ベースの食品企業として、複数の植物由来肉代替製品ブランドを買収・統合している。同社は2020年に設立された。',
    '概要2': '同社は、Oumph!（英国・欧州）、The Fry Family Food Co.（米国、英国、オーストラリア、南アフリカ）、LikeMeat（ドイツ）、No Meat（英国）、The Dutch Weed Burger（オランダ）、Alpha Foods（米国）の6つのブランドを保有する。同社は、各ブランドの製造施設を所有し、主に植物由来のチキン代替品とその他の肉代替品に焦点を当てている。',
    '概要3': '同社は、5億ドル以上の資金調達を完了し、2020年の設立以来6件の買収（LikeMeat、Frys、Oumph!、No Meat、Dutch Weedburger、Alpha）を完了している。',
    '概要4': '同社は、世界最大級の植物ベース食品企業になることを目指し、グローバル市場において植物ベースの生活を新しい標準とすることを目標としている。',
    '注目ポイント1': '・植物由来肉代替品市場において、各ブランドが独立して展開することで、規模の経済を実現できないことが課題であった。',
    '注目ポイント2': '・同社は、複数のブランドを統合することで、製造、流通、マーケティングの規模の経済を実現する。\n・同社は、地域ごとに異なるブランドを展開し、各市場に最適化した製品を提供する。\n・同社は、Alpha Foodsの買収により米国市場でのプレゼンスを大幅に拡大した。',
    '注目ポイント3': '・同社は、5億ドル以上の資金調達を完了した（2021年）。\n・同社は、The Rise Fundなどの投資家から支援を受けている。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://vegconomist.com/interviews/livekindly-collective-on-track-to-become-one-of-the-worlds-largest-plant-based-food-companies/',
    '発表年または出願年': 2020,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'LIVEKINDLY Collective',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': 2020,
    '組織URL': 'https://thelivekindlyco.com',
    '情報ソースURL 1': 'https://vegconomist.com/interviews/livekindly-collective-on-track-to-become-one-of-the-worlds-largest-plant-based-food-companies/',
    '情報ソースURL 2': 'https://agfundernews.com/livekindly-collective-expands-global-plant-based-empire-with-acquisition-of-alpha-foods',
    '情報ソースURL 3': 'https://thelivekindlyco.com',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 18: PlantX Life
# ===========================================
entries.append({
    'ID': 18,
    'タイトル': '植物ベース製品の包括的オンラインマーケットプレイスとミール配送サービス',
    '概要1': 'カナダのPlantX Life Inc.（CSE: VEGA, Frankfurt: WNT1, OTCQB: PLTXF）は、植物ベースのライフスタイルを送る人々にとって最も信頼でき便利な目的地となることを目指す電子商取引企業である。同社は、ブリティッシュコロンビア州バンクーバーに本社を置く。',
    '概要2': '同社は、効率的な電子商取引体験、対話型の実店舗、PlantX宅配サービスを通じて、北米の消費者に1万点以上の植物ベース製品を提供する多面的なマーケットプレイスである。同プラットフォームは、植物ベースの食料品、ビタミン、化粧品、ペットフード、ミール配送サービスを含む。また、ブリティッシュコロンビア州Squamishに1,700平方フィートの実店舗を開設し、植物ベースの食料品、健康・ウェルネス製品、植物ベース教育プログラムを提供している。',
    '概要3': '同社は、オンラインショップに5,000以上のヴィーガン製品を収容し、最近追加されたミールサービスは、シェフが作成した料理を西カナダの顧客の玄関先まで配送する。また、Walmart Canada Marketplaceとの提携により、製品販売チャネルを拡大している。',
    '概要4': '同プラットフォームは、植物ベースのライフスタイルを送る消費者に、ワンストップの目的地を提供し、オンラインショップとミール配送サービスを統合している。',
    '注目ポイント1': '・植物ベース製品は、複数の小売業者に分散しており、消費者がすべての製品を一箇所で見つけることが困難であった。',
    '注目ポイント2': '・同プラットフォームは、1万点以上の植物ベース製品を提供し、食料品からペットフードまで包括的な品揃えを実現する。\n・同プラットフォームは、電子商取引、実店舗、ミール配送サービスを統合した多面的なアプローチを採用する。\n・同社は、Walmart Canada Marketplaceと提携し、販売チャネルを拡大した。',
    '注目ポイント3': '・同社は、カナダ証券取引所（CSE: VEGA）に上場している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://plantx.ca/',
    '発表年または出願年': 2019,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'PlantX Life Inc.',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Canada',
    '組織設立年': 2019,
    '組織URL': 'https://plantx.ca',
    '情報ソースURL 1': 'https://plantx.ca/',
    '情報ソースURL 2': 'https://www.proactiveinvestors.com/companies/news/952202/plantx-life-begins-selling-its-first-products-on-walmart-canada-marketplace-952202.html',
    '情報ソースURL 3': 'https://plantx.com/blogs/press/plantx-opens-1st-physical-store-in-canada',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 19: Dole Food Company
# ===========================================
entries.append({
    'ID': 19,
    'タイトル': '再生農業実践を推進する持続可能性フレームワーク「The Dole Way」',
    '概要1': '米国のDole Food Companyは、果物と野菜の生産・販売を行うグローバル企業であり、持続可能性戦略「The Dole Way」を通じて、再生農業実践を推進している。',
    '概要2': '同フレームワークは、For Nature、For People、For Foodの3つの柱と堅固なガバナンスに焦点を当てている。For Natureでは、Science Based Target Initiativeへのコミットメントにより気候変動対策を最前線に置き、水管理、生物多様性、廃棄物管理、包装削減に取り組む。同社は、特定のパイナップル生産サイクル間の耕起回避、バナナ生産における小型機械式掘削機使用による土壌擾乱最小化、15年以上にわたるバナナ栽培における最小耕起維持などの再生農業実践を実施している。また、植生被覆またはカバークロップの実施は土壌健康の鍵であり、複数の多年生作物に土壌被覆を適用して複数の持続可能性効果を生み出している。',
    '概要3': '同社は、Rainforest Allianceと協力して、サプライチェーン全体で再生農業技術を実施している。同社は、20年以上にわたり有機農業を行っており、地域コミュニティ、生物多様性、土壌保全、温室効果ガス排出削減に好影響を与えている。',
    '概要4': '同フレームワークは、自社運営および関連農場における再生農業実践の推進を通じて、気候目標を支援することを目的としている。',
    '注目ポイント1': '・従来の集約農業は、土壌劣化、水質汚染、温室効果ガス排出などの環境問題を引き起こしていた。',
    '注目ポイント2': '・同社は、耕起回避、最小耕起、カバークロップなどの再生農業実践を複数の作物に適用する。\n・同社は、Rainforest Allianceとのパートナーシップにより、サプライチェーン全体で再生農業技術を実施する。\n・同社は、Science Based Target Initiativeにコミットし、気候変動対策を推進する。',
    '注目ポイント3': '・同社は、2022年持続可能性レポートを発表し、2030年までの目標を設定した。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': '公式情報',
    '主要情報ソースURL': 'https://www.dole.com/sustainability/progress-report-on-the-dole-way/for-natures-health',
    '発表年または出願年': 2022,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Dole Food Company',
    '組織タイプ': '大企業/中堅企業',
    '国名': 'United States',
    '組織設立年': 1851,
    '組織URL': 'https://www.dole.com',
    '情報ソースURL 1': 'https://www.dole.com/sustainability/progress-report-on-the-dole-way/for-natures-health',
    '情報ソースURL 2': 'https://www.dole.com/en/farms/improving-agriculture',
    '情報ソースURL 3': 'https://www.businesswire.com/news/home/20221220005564/en/Dole-Releases-2022-Sustainability-Report-Outlining-Its-Sustainability-Strategy-and-2030-Goals',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 20: GoodDot
# ===========================================
entries.append({
    'ID': 20,
    'タイトル': '大豆、エンドウ豆、小麦、じゃがいものタンパク質から作製された植物由来の肉代替製品',
    '概要1': 'インドのGoodDot Enterprisesは、植物由来の肉とヴィーガン食品を製造する企業である。同社は2016年にUdaipurで共同設立され、インド国内および海外で1日あたり120万ユニットを販売している。',
    '概要2': '同社は、Beyond MeatやImpossible Foodsなどの米国企業が普及させたアイデア、すなわちエンドウ豆、小麦、じゃがいもなどの植物から抽出したタンパク質から肉代替品を作製するアイデアに基づいている。同社の製品には、ヴィーガンマトン（羊肉代替品）、脱水植物ベースのチキン製品、卵スクランブルが含まれる。製品は、人工保存料や色素を使用しないクリーンラベルで、動物に対して残酷でない。',
    '概要3': '同社は、植物ベースの肉を主流にするためには実際の肉との価格パリティが重要であると考えており、ヴィーガンマトンは従来の羊肉と価格パリティを実現している。製品は常温保存可能であり、消費者は腐敗を心配することなく長期間（最大1年）保存できる。',
    '概要4': '同社は、Biryani、Meatless Mince、Unmutton Dhaba Curry Kit、Vegicken Chunks in Brineなどの調理済み肉代替品を、125〜500gのパッケージで、95〜379ルピーの価格で提供している。製品は、Dmart、Relianceなどのスーパーマーケットチェーン、レストラン、電子商取引プラットフォームで販売されている。また、ADF Foods Ltd.とのパートナーシップにより、米国市場に参入し、Plant-based Lamb Nihari、Plant-based Butter Chicken、Plant-based Jackfruit Curryなどを販売している。',
    '注目ポイント1': '・インドにおいて、植物ベースの肉代替品は、価格が高く、消費者にとってアクセスしづらいことが課題であった。',
    '注目ポイント2': '・同社の製品は、実際の肉との価格パリティを実現し、消費者にアクセス可能な価格を提供する。\n・同社の製品は、常温保存可能で、最大1年間保存できるため、流通と保存が容易である。\n・同社は、エンドウ豆、小麦、じゃがいもなどの植物タンパク質を使用し、人工保存料や色素を使用しないクリーンラベル製品を提供する。',
    '注目ポイント3': '・同社は、2016年にUdaipurで設立され、ティアIIおよびティアIII都市の店舗を通じて成長した。\n・同社は、ADF Foods Ltd.とのパートナーシップにより米国市場に参入した（2022年）。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://yourstory.com/2022/06/plant-based-meat-startup-gooddot-udaipur-vegan-meat-soybean',
    '発表年または出願年': 2016,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'GoodDot Enterprises',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'India',
    '組織設立年': 2016,
    '組織URL': 'https://gooddot.in',
    '情報ソースURL 1': 'https://yourstory.com/2022/06/plant-based-meat-startup-gooddot-udaipur-vegan-meat-soybean',
    '情報ソースURL 2': 'https://thespoon.tech/good-dot-paves-way-for-plant-based-meats-in-india-with-vegan-mutton/',
    '情報ソースURL 3': 'https://www.veganfirst.com/article/indian-plant-based-meat-company-gooddot-enters-the-us-market',
    '情報ソースURL 4': 'https://gooddot.in',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 21: xFarm Technologies
# ===========================================
entries.append({
    'ID': 21,
    'タイトル': 'IoTセンサーとクラウドベース管理ソフトウェアを統合した農場デジタル化プラットフォーム',
    '概要1': 'イタリアのxFarm Technologiesは、農業食品セクターのデジタル化に焦点を当てた技術企業であり、農家とステークホルダーのビジネス管理を支援する革新的なツールを提供している。同社は、イタリアのデジタル農業プラットフォームxFarmとFarm Technologiesの合併により2021年に設立され、Matteo VanottiがCEOを務める。',
    '概要2': '同プラットフォームは、IoTセンサーベースのシステムであり、作物活動、作物処理、その他の操作に関する農場データを定期的に収集し、作物の健康状態を分析して適切な対策を計画するための洞察を農家に提供するソフトウェアにデータをロードする。同プラットフォームは、フリーミアムビジネスモデルに基づくモジュール式オープンプラットフォームであり、クラウドベースの管理ソフトウェア、フィールドIoTセンサー、灌漑最適化ソリューション、農業気象予測、病害警告、精密農業サービスなどのサービスを統合するマーケットプレイスを提供する。',
    '概要3': '同社は、AIとIoTソリューションを提供する完全なデジタル農場管理プラットフォームであり、8万の農場と100万ヘクタールを管理している。最近では、100か国以上の30以上のサプライチェーンに属する30万の農場の作業を300万ヘクタールでサポートしている。',
    '概要4': '同プラットフォームは、農家が作物の健康状態を監視し、灌漑を最適化し、病害を予測し、精密農業技術を適用することを支援する。',
    '注目ポイント1': '・従来の農業では、作物の健康状態や土壌状態をリアルタイムで監視することが困難であり、最適なタイミングで対策を講じることができなかった。',
    '注目ポイント2': '・同プラットフォームは、IoTセンサーとクラウドソフトウェアを統合し、リアルタイムのデータ収集と分析を可能にする。\n・同プラットフォームは、モジュール式でオープンなフリーミアムモデルを採用し、農家が必要なサービスを選択できる。\n・同プラットフォームは、灌漑最適化、病害警告、精密農業サービスを提供するマーケットプレイスを統合している。',
    '注目ポイント3': '・同社は、Emerald Technology Ventures、United Ventures、Novacapitalなどの投資家から6,030万ドルの資金調達を完了した。\n・同社は、100か国以上で30万の農場と300万ヘクタールをサポートしている（2024年）。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://agfundernews.com/xfarm-and-farm-technologies-merge-to-become-the-spotify-of-agtech',
    '発表年または出願年': 2017,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'xFarm Technologies',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Italy',
    '組織設立年': 2017,
    '組織URL': 'https://xfarm.ag',
    '情報ソースURL 1': 'https://agfundernews.com/xfarm-and-farm-technologies-merge-to-become-the-spotify-of-agtech',
    '情報ソースURL 2': 'https://www.eu-startups.com/2019/12/xfarm-raises-3-million-to-digitalise-farms/',
    '情報ソースURL 3': 'https://xfarm.ag',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 22: GOURMEY
# ===========================================
entries.append({
    'ID': 22,
    'タイトル': 'アヒルの卵細胞から培養された細胞農業フォアグラ',
    '概要1': 'フランスのGOURMEYは、培養肉の喜びを創造する企業である。同社は2019年にNicolas Morin-Forest、Jérôme Caron、Antoine Davydoff、Gemma Lyonsの4人によって設立された。',
    '概要2': '同社は、アヒルの卵から抽出した少数の細胞を使用して、動物に残酷でないフォアグラを開発している。これらの細胞は、最適な温度、栄養素、成長スペースを提供する慎重に制御された培養器に配置され、実際の肉と同じ味、食感、組成を持つ肝臓肉に成長する。少数の細胞だけで、世界のフォアグラ需要を数年間再現するのに十分である。',
    '概要3': '同社は、シリーズA資金調達で4,800万ユーロを確保した。このラウンドは、Earlybird Venture Capitalが主導し、Keen Venture Partners、Omnes Capital、Discoveryなどが参加した。同社は、この資金を使用して、パリに46,000平方フィートのR&D・生産サイトを開設する。これは、ヨーロッパ最大の培養肉施設となる。',
    '概要4': '同社は、2026年までにシェフやレストランに培養フォアグラを提供することを計画している。同社は、シンガポール、米国、英国、スイス、欧州連合の5つの初期グローバル市場で市場アクセスの承認を要請している。',
    '注目ポイント1': '・従来のフォアグラ生産は、アヒルやガチョウに強制給餌を行うため、動物福祉の観点から倫理的な問題があった。',
    '注目ポイント2': '・同社の培養フォアグラは、アヒルの卵から抽出した細胞を培養することで、動物に残酷でない方法で生産される。\n・同社の技術は、少数の細胞から世界のフォアグラ需要を数年間満たすことが可能である。\n・同社は、実際のフォアグラと同じ味、食感、組成を持つ培養肉を生産する。',
    '注目ポイント3': '・同社は、欧州連合における培養肉の規制承認を申請した最初の企業である（2022年）。\n・同社は、シリーズA資金調達で4,800万ユーロを確保し、ヨーロッパ最大の培養肉施設を建設する（2022年）。',
    '技術開発の進展度': 'Lv5:製品検証',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://vegconomist.com/investments-finance/investments-acquisitions/gourmey-cultivated-foie-gras/',
    '発表年または出願年': 2019,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'GOURMEY',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'France',
    '組織設立年': 2019,
    '組織URL': 'https://gourmey.com',
    '情報ソースURL 1': 'https://vegeconomist.com/investments-finance/investments-acquisitions/gourmey-cultivated-foie-gras/',
    '情報ソースURL 2': 'https://techcrunch.com/2021/07/14/gourmey-is-a-cell-based-poultry-startup-working-on-lab-grown-foie-gras/',
    '情報ソースURL 3': 'https://www.greenqueen.com.hk/first-french-startup-gourmey-cultivated-meat-foie-gras-duck-egg-cells/',
    '情報ソースURL 4': 'https://gourmey.com',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 23: Tender Food
# ===========================================
entries.append({
    'ID': 23,
    'タイトル': '植物タンパク質を髪の毛の太さの繊維に紡糸して肉の筋繊維を模倣する技術',
    '概要1': '米国のTender Foodは、ボストン近郊の食品技術企業であり、2020年にハーバード大学のエンジニアによって設立された。同社は、植物タンパク質を繊維に紡糸して肉のホールカットを作製する独自技術を開発している。',
    '概要2': '同技術は、ハーバード大学のKevin Kit Parker博士の研究室で考案された材料とタンパク質繊維製造におけるイノベーションによって実現されている。同技術は、大豆タンパク質、食物繊維、その他の炭水化物を含む植物タンパク質混合物を溶液に混合し、この溶液を高速で紡糸して髪の毛の太さの繊維にする（綿菓子機の高度版を想像してください）。同技術は、高スループット、原料非依存の繊維紡糸技術であり、任意の入力（植物タンパク質、菌類タンパク質、精密発酵由来タンパク質など）を繊維（動物筋肉の構成要素）に変換できる。',
    '概要3': '同技術により作製された製品は、ソーセージやバーガーのような加工肉を模倣する他の植物ベース製品とは対照的に、動物肉と区別できない食感と調理特性を持ち、高タンパク質の栄養プロファイルを持ち、添加物や充填剤を含まない。同社の製品には、プルドポーク、チキンブレスト、ビーフショートリブ、シーフード、ステーキなどのホールカットが含まれる。',
    '概要4': '同技術は、プルドポークからチキンブレスト、シーフード、ステーキまで、任意のフォーマットで超現実的、栄養価の高い、手頃な価格の製品を、シンプルな原料で作製することを可能にする。2024年、同社はボストン地域のベジタリアンファストフードチェーンClover Food Labと契約を締結した。',
    '注目ポイント1': '・従来の植物ベース肉代替品は、ソーセージやバーガーのような加工肉を模倣することはできたが、ステーキやチキンブレストのようなホールカットを再現することが困難であった。',
    '注目ポイント2': '・同技術は、植物タンパク質を髪の毛の太さの繊維に紡糸することで、動物筋肉の構造を模倣する。\n・同技術は、原料非依存であり、植物タンパク質、菌類タンパク質、精密発酵由来タンパク質など、任意の入力を使用できる。\n・同技術により作製された製品は、動物肉と区別できない食感と調理特性を持ち、添加物や充填剤を含まない。',
    '注目ポイント3': '・同技術は、ハーバード大学のKevin Kit Parker博士の研究室で開発され、特許を取得している。\n・同社は、Chris SaccaのLowercarbon Capitalが主導するシード資金調達で1,200万ドルを調達した（2022年）。その後、シリーズA資金調達で1,100万ドルを調達した（2024年）。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://vegconomist.com/interviews/tender-food-technology-breakthroughs-rekindle-growth-alternative-meat-industry/',
    '発表年または出願年': 2020,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Tender Food',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': 2020,
    '組織URL': 'https://tender.com',
    '情報ソースURL 1': 'https://vegconomist.com/interviews/tender-food-technology-breakthroughs-rekindle-growth-alternative-meat-industry/',
    '情報ソースURL 2': 'https://wyss.harvard.edu/news/tender-food-raises-12-million-seed-round-led-by-chris-saccas-lowercarbon-capital-to-scale-production-of-plant-based-whole-muscle-cuts-of-beef-pork-and-chicken/',
    '情報ソースURL 3': 'https://techcrunch.com/2024/06/17/tender-food-plant-based-alternative-protein/',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 24: Miso Robotics
# ===========================================
entries.append({
    'ID': 24,
    'タイトル': 'AIとロボットアームを使用してフライドポテト、オニオンリング、チキンなどを自動調理する「Flippy Fry Station」',
    '概要1': '米国のMiso Roboticsは、レストランをより安全、簡単、フレンドリーにすることを使命とするキッチンAIと自動化の企業である。同社は、「Flippy 2」、「CookRight」、「Sippy」の製造者である。',
    '概要2': '同社は、2025年1月に次世代のFlippy Fry Stationロボットを発表した。同ロボットは、Misoのキッチン AIと25以上の特許によって動力を供給され、フライドポテト、オニオンリング、チキン、タコス、その他の揚げ物を精度と一貫性を持って自動調理する。以前のバージョンと比較して、新しいFlippyは半分のサイズで、2倍の速度で、はるかに信頼性が高く、わずか数時間で既存のキッチンに一晩でインストールできる（75%少ない時間）。新しいFlippyは、1時間あたり100バスケット以上を処理でき、これは人間のほぼ2倍である。',
    '概要3': '同社は、Ecolab（NYSE: ECL）からの投資、NVIDIA（NASDAQ: NVDA）との協力、Rich HullがCEOを務める新しいリーダーシップに支えられている。White Castleは2024年後半に新しいFlippyのパイロットを開始し、Jack in the BoxとWhite Castleは今年初めに追加のFlippyインストールを予定している。2025年時点で、Misoは2つのブランドの13のレストランにのみロボットアームをインストールしていた。',
    '概要4': '同ロボットは、ファストフードレストランにおける労働力不足と一貫した品質の提供を支援する。フライクックの費用は月額5,400ドルである。連邦規制により、18歳未満の従業員がFlippy Fry Stationを操作することが許可されており、クイックサービスレストランの労働力課題を支援する。',
    '注目ポイント1': '・ファストフードレストランにおいて、労働力不足と一貫した品質の提供が課題であった。\n・揚げ物調理は、高温の油を扱うため、18歳未満の従業員には危険な作業であった。',
    '注目ポイント2': '・同ロボットは、AIとロボットアームを使用して、フライドポテト、オニオンリング、チキンなどを自動調理する。\n・新世代のFlippyは、以前のバージョンと比較して、半分のサイズで2倍の速度であり、1時間あたり100バスケット以上を処理できる（人間のほぼ2倍）。\n・連邦規制により、18歳未満の従業員がFlippyを操作することが許可されており、労働力課題を緩和する。',
    '注目ポイント3': '・同社は、Ecolabからの投資とNVIDIAとの協力を受けている（2025年）。\n・同社は、25以上の特許を保有している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://misorobotics.com/newsroom/miso-launches-next-generation-flippy-fry-station-the-most-significant-evolution-of-the-ai-powered-robot-since-its-inception/',
    '発表年または出願年': 2016,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Miso Robotics',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': 2016,
    '組織URL': 'https://misorobotics.com',
    '情報ソースURL 1': 'https://misorobotics.com/newsroom/miso-launches-next-generation-flippy-fry-station-the-most-significant-evolution-of-the-ai-powered-robot-since-its-inception/',
    '情報ソースURL 2': 'https://www.restaurantdive.com/news/miso-robotics-develops-smaller-faster-flippy-white-castle-jack-in-the-box/738567/',
    '情報ソースURL 3': 'https://misorobotics.com',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 25: Beewise
# ===========================================
entries.append({
    'ID': 25,
    'タイトル': 'AIとコンピュータビジョンを使用してミツバチのニーズをリアルタイムで監視・対応する自律型ロボット養蜂箱「BeeHome」',
    '概要1': 'イスラエルのBeewiseは、IoTとAIを活用して最初の自律型養蜂箱を提供する企業である。同社は2018年にBeit Haemekに設立された。',
    '概要2': '同システムは、BeeHomeと呼ばれる太陽光発電の改造コンテナであり、ロボティクス、人工知能、イメージング、ソフトウェアプラットフォーム、モバイルアプリケーションを統合している。BeeHomeは最大24の養蜂箱を収容でき、ミツバチのニーズに対応するロボットシステムを含む。同ロボットは、人工知能とコンピュータビジョンを使用して、ミツバチのニーズをリアルタイムで監視・特定する。同システムは、自動気候・湿度制御、害虫駆除、群れ防止、収穫を可能にし、問題が発生した際に養蜂家に警告する。同ロボットは、食料、水、病気や害虫がある場合は薬を投与し、温度を調整する。',
    '概要3': 'BeeHomeは、年間のコロニー崩壊率が8%にとどまり、全体的なミツバチの死亡率を80%削減する。平均して、養蜂家はBeeHomeから従来の養蜂箱よりも60%多くの蜂蜜を収穫できる。',
    '概要4': '同システムは、ミツバチの健康を改善し、受粉と蜂蜜生産を増加させることを目的とした、AI、コンピュータビジョン、精密ロボティクスに基づく自動養蜂プラットフォームである。',
    '注目ポイント1': '・従来の養蜂は、手作業による定期的な巣箱の検査と管理が必要であり、大規模な養蜂場では労働集約的であった。\n・ミツバチの群れ崩壊症候群（Colony Collapse Disorder）により、世界中でミツバチの個体数が減少していた。',
    '注目ポイント2': '・同システムは、AIとコンピュータビジョンを使用して、ミツバチのニーズをリアルタイムで監視・対応する。\n・同システムは、自動気候制御、害虫駆除、群れ防止、収穫を提供し、養蜂家の労働を大幅に削減する。\n・BeeHomeは、コロニー崩壊率を8%に抑え、全体的なミツバチの死亡率を80%削減し、蜂蜜収穫量を60%増加させる。',
    '注目ポイント3': '・同社は、TIME誌の「ベスト発明」リストに選ばれた（2020年）。\n・同社は、8,000万ドルの投資を獲得した（2022年3月）。\n・同社は、18の特許を確保している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.timesofisrael.com/israeli-bee-tech-startup-beewise-pulls-in-80m-investment-for-robotic-beehives/',
    '発表年または出願年': 2018,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Beewise',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Israel',
    '組織設立年': 2018,
    '組織URL': 'https://beewise.ag',
    '情報ソースURL 1': 'https://www.timesofisrael.com/israeli-bee-tech-startup-beewise-pulls-in-80m-investment-for-robotic-beehives/',
    '情報ソースURL 2': 'https://aws.amazon.com/blogs/startups/beewise-combines-iot-and-ai-to-offer-an-automated-beehive/',
    '情報ソースURL 3': 'https://beewise.ag/about-us',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# ===========================================
# ID 26: KETOS
# ===========================================
entries.append({
    'ID': 26,
    'タイトル': 'IoTセンサーとクラウド分析を使用して水質をリアルタイムで監視するプラットフォーム',
    '概要1': '米国のKETOSは、IoTセンサーシステムを通じて自動水質監視とテストを提供する企業である。同社は2015年に設立され、カリフォルニア州Sunnyvaleに本社を置く。',
    '概要2': '同プラットフォームは、ハードウェア、ソフトウェア、接続性、自動レポート、予測分析、メンテナンスを統合した完全統合プラットフォームであり、水質監視とテストを自動化する。KETOSは、2つの特許取得済みハードウェアデバイス、KETOS SHIELDとKETOS WAVEを製造している。同プラットフォームは、LoRa、WiFi、セルラー、顧客ネットワークなどの複数の接続オプションを通じてクラウド統合を特徴とする。同システムは、温度などの環境要因、鉛とヒ素などの重金属を含む30以上のパラメータを監視する。リアルタイムデータ、履歴トレンド、データモデルの相関により、予防的な洞察を提供する。',
    '概要3': '農業産業は、KETOSを使用して、より優れた栄養ブレンドで作物品質を改善し、オープンフィールドの地下水と制御環境における水の再利用を増加させる、より安全な作物を作成している。同プラットフォームは、酸性度レベルや溶存酸素含有量などの重要なパラメータを測定する継続的な水質監視を提供するInternet of Things（IoT）センサーを使用する。',
    '概要4': '同プラットフォームは、栄養管理、水の利用可能性、水質、一貫性、または製品安全性が不可欠な農業アプリケーションにおいて、水質と保全が重要である産業、農業、市政セクターにサービスを提供する。同ソリューションには、CAPEXは不要であり、ハードウェア、ソフトウェア、接続性、レポート、警告、予測分析を含む包括的な月額料金制である。',
    '注目ポイント1': '・農業において、水質を継続的に監視することが困難であり、栄養素の不均衡や汚染物質による作物品質の低下が課題であった。',
    '注目ポイント2': '・同プラットフォームは、IoTセンサーを使用して、30以上のパラメータ（温度、重金属、栄養素など）をリアルタイムで監視する。\n・同プラットフォームは、ハードウェア、ソフトウェア、接続性、レポート、予測分析を統合した完全統合ソリューションを提供する。\n・同プラットフォームは、CAPEXが不要の包括的な月額料金制を採用し、農家にとってアクセスしやすい。',
    '注目ポイント3': '・同社は、Accentureからの投資を受けた（2022年）。\n・同社は、KETOS SHIELDとKETOS WAVEの2つの特許取得済みデバイスを製造している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': '公式情報',
    '主要情報ソースURL': 'https://ketos.co/',
    '発表年または出願年': 2015,
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'KETOS',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': 2015,
    '組織URL': 'https://ketos.co',
    '情報ソースURL 1': 'https://ketos.co/',
    '情報ソースURL 2': 'https://newsroom.accenture.com/news/2022/accenture-invests-in-ketos-to-advance-water-intelligence-through-real-time-monitoring',
    '情報ソースURL 3': 'https://ketos.co/ketos-for-agriculture',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
})

# DataFrame作成
df = pd.DataFrame(entries)

# 列の順序を指定
columns_order = [
    'ID', 'タイトル',
    '概要1', '概要2', '概要3', '概要4',
    '注目ポイント1', '注目ポイント2', '注目ポイント3',
    '技術開発の進展度', '主要情報ソースタイプ', '主要情報ソースURL',
    '発表年または出願年', '代表的な図のURL', '図の掲載ページURL',
    '組織名', '組織タイプ', '国名', '組織設立年', '組織URL'
]

# 情報ソースURL列を追加
for i in range(1, 21):
    col_name = f'情報ソースURL {i}'
    if col_name not in df.columns:
        df[col_name] = ''
    columns_order.append(col_name)

# 列を並び替え
for col in columns_order:
    if col not in df.columns:
        df[col] = ''
df = df[columns_order]

# Excel出力
output_file = os.path.join(output_dir, '技術ロングリスト_初期版.xlsx')
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"技術ロングリスト初期版を作成しました: {output_file}")
print(f"エントリー数: {len(df)}")
print(f"列数: {len(df.columns)}")
