#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技術ロングリスト作成スクリプト
Agent 3用 - ID 27-38の12件
"""

import pandas as pd
from datetime import datetime

# 技術ロングリストデータ
longlist_data = []

# ====================================================================
# No.27 - Vendease
# ====================================================================
longlist_data.append({
    'ID': 27,
    'タイトル': 'レストラン・食品事業者向けオンラインプラットフォーム「Vendease」',
    '概要1': 'レストランおよび食品事業者向けのB2Bデジタルプラットフォームを運営するナイジェリアのVendeaseは、食品調達プロセスのデジタル化と最適化を通じて、アフリカの食品サプライチェーンを変革するプラットフォームを開発/提供している。',
    '概要2': '同プラットフォームは、レストランやホテルなどの食品事業者が食材を調達する際に、デジタルプロセスを通じて供給者とマッチングし、食品在庫を大量購入・保管・配送する機能を提供する。同プラットフォームは、サードパーティの物流プロバイダーを通じて12時間以内の配送を保証し、市場価格よりも安価な調達を実現する。',
    '概要3': '同プラットフォームは、ナイジェリアとガーナの8都市で稼働しており、レストランや食品事業者に対して、技術的支援、運営支援、および金融サービスを提供することで、食品事業の成長を支援している。',
    '概要4': '同プラットフォームは、アフリカの食品セクターにおける断片化と非効率性の課題を解決し、レストランやホテル、食品事業者の調達プロセスを効率化することを目的としている。',
    '注目ポイント1': '・アフリカの食品セクターは高度に断片化されており、損失が発生しやすく、調達プロセスが非効率であることが課題となっていた。',
    '注目ポイント2': '・同プラットフォームは、2020年1月のローンチ当初はマーケットプレイスモデルを採用していたが、2020年中頃に食品を大量購入し、自社で在庫管理と配送を行うモデルへと転換した。\n・同プラットフォームは、デジタル調達エンジンを活用し、レストランが市場価格よりも安価に食材を購入できるようにする。',
    '注目ポイント3': '・同社は、2021年10月に320万ドルのシード資金を調達し、2022年9月にTLcom CapitalとPartech Africaが主導する3000万ドル（株式2000万ドル、負債1000万ドル）のシリーズA資金を調達した。\n・同社は、Y Combinatorのバックアップを受けている。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://techcrunch.com/2022/09/26/vendease-a-food-procurement-platform-for-african-restaurants-nabs-30m-led-by-partech-africa-and-tlcom/',
    '発表年または出願年': '2020',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Vendease',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Nigeria',
    '組織設立年': '2020',
    '組織URL': 'https://vendease.com',
    '情報ソースURL 1': 'https://techcrunch.com/2022/09/26/vendease-a-food-procurement-platform-for-african-restaurants-nabs-30m-led-by-partech-africa-and-tlcom/',
    '情報ソースURL 2': 'https://techcrunch.com/2021/10/25/vendease-gets-3-2m-to-help-hotels-and-restaurants-buy-food-supplies-in-africa/',
    '情報ソースURL 3': 'https://www.linkedin.com/pulse/vendease-2023-update-superpowering-food-businesses-africa/',
    '情報ソースURL 4': 'https://www.ycombinator.com/companies/vendease',
    '情報ソースURL 5': 'https://www.foodbusinessafrica.com/nigerian-b2b-digital-marketplace-vendease-secures-us30m-funding-to-expand-operations/',
    '情報ソースURL 6': 'https://techfocus24.com/vendease-reinvents-itself-to-power-africas-food-supply-chain/',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# ====================================================================
# No.28 - Crowde
# ====================================================================
longlist_data.append({
    'ID': 28,
    'タイトル': '農業者向けピアツーピア融資プラットフォーム「Crowde」',
    '概要1': '農業分野に特化したフィンテックプラットフォームを運営するインドネシアのCrowdeは、投資家と農業者を結びつけるピアツーピア（P2P）融資プラットフォームを開発/提供している。',
    '概要2': '同プラットフォームは、資金を必要とする農業者、水産養殖業者、畜産業者と、魅力的なリターンを求める投資家を接続する。同プラットフォームは、農業者に対して現金を直接支給せず、肥料などの原材料や農業用具を卸売価格で購入して提供することで、資金の不適切使用リスクを回避する。また、同プラットフォームは、農作物の形でローン返済を受け取る。',
    '概要3': '同プラットフォームは、2020年までにインドネシア全土19州の3万人以上の農業者に融資を提供した。また、同プラットフォームは、農業エコシステム全体をテクノロジーで統合し、サプライヤーから顧客までを接続する。',
    '概要4': '同プラットフォームは、資金調達にアクセスできないインドネシアの農業者を支援し、農業者の意識を変革してアグロプレナー（農業起業家）に育成することを目的としている。',
    '注目ポイント1': '・インドネシアの農業者は、運転資金へのアクセスが限られており、資金調達が課題となっていた。',
    '注目ポイント2': '・同プラットフォームは、投資家から集めた資金を農業者に直接支給せず、農業用具を購入して提供することで、資金の不適切使用を防止する。\n・同プラットフォームは、農業者に対して農業、財務、マーケティングに関するトレーニングを提供する。',
    '注目ポイント3': '・同社は、2021年にMonk's Hill Venturesが主導する900万ドルのシリーズB資金を調達した。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://startup.google.com/alumni/stories/crowde/',
    '発表年または出願年': '2015',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Crowde',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Indonesia',
    '組織設立年': '2015',
    '組織URL': 'https://crowde.co',
    '情報ソースURL 1': 'https://startup.google.com/alumni/stories/crowde/',
    '情報ソースURL 2': 'https://www.compasslist.com/insights/crowde-funding-indonesias-fields',
    '情報ソースURL 3': 'https://www.cbinsights.com/company/crowde',
    '情報ソースURL 4': 'https://directory.growasia.org/crowde/',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# ====================================================================
# No.29 - BioConsortia
# ====================================================================
longlist_data.append({
    'ID': 29,
    'タイトル': '微生物コンソーシアムを用いた農業用バイオ製品「BioConsortia」',
    '概要1': '農業バイオテクノロジーを専門とする米国のBioConsortiaは、微生物の力を活用して作物の生産性を向上させるバイオ製品を開発/販売している。',
    '概要2': '同製品は、特許取得済みのAdvanced Microbial Selection（AMS）プロセスと、最先端のGenePro遺伝子工学プラットフォームを用いて、微生物の自然な力を予測、設計、および引き出す。同製品には、窒素固定微生物、バイオスティミュラント、バイオペスティサイド（線虫、細菌、真菌に対する防御）が含まれる。',
    '概要3': '同製品の窒素固定技術は、肥料が存在する環境下でも根圏で窒素を生成することができる。また、同製品は、シェルフライフが長く、種子処理として簡単に適用できる。同製品は、シリアル以外の野菜や他の市場にも展開されている。',
    '概要4': '同製品は、持続可能で高収量の農業を推進し、作物の健康と生産性を向上させることを目的としている。',
    '注目ポイント1': '・従来の農業は、化学肥料や農薬に依存しており、環境への負荷が大きいことが課題となっていた。',
    '注目ポイント2': '・同社の窒素固定微生物技術は、肥料が存在する環境下でも窒素を生成できる点が特徴である。\n・同社のバイオスティミュラントは、干ばつ、塩分、天候などのストレスに対処し、収量を向上させる。\n・同社のバイオペスティサイドは、作物の成長中および収穫後の腐敗を防止する。',
    '注目ポイント3': '・同社は、2024年にOtter Capitalおよび関連ファンドが主導する1500万ドルの資金を調達した。\n・同社は、2024年にニュージーランドでH&Tと提携し、窒素固定微生物種子処理製品を発売した。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.businesswire.com/news/home/20241205428339/en/BioConsortia-and-HT-Partner-to-Launch-Nitrogen-Fixing-Microbial-Seed-Treatment-in-New-Zealand',
    '発表年または出願年': '2014',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'BioConsortia, Inc.',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': '2014',
    '組織URL': 'https://bioconsortia.com',
    '情報ソースURL 1': 'https://www.businesswire.com/news/home/20241205428339/en/BioConsortia-and-HT-Partner-to-Launch-Nitrogen-Fixing-Microbial-Seed-Treatment-in-New-Zealand',
    '情報ソースURL 2': 'https://www.businesswire.com/news/home/20240129899019/en/BioConsortia-Extends-Nitrogen-fixing-Microbial-Products-Beyond-Cereals-to-Vegetables-and-Other-Markets',
    '情報ソースURL 3': 'https://www.fenomstalent.com/blog/bioconsortia-inc-raises-15m-to-scale-microbial-crop-solutions-and-revolutionize-sustainable-agriculture/',
    '情報ソースURL 4': 'https://www.cbinsights.com/company/bioconsortia',
    '情報ソースURL 5': 'https://news.agropages.com/News/NewsDetail---50421.htm',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# ====================================================================
# No.30 - Algama
# ====================================================================
longlist_data.append({
    'ID': 30,
    'タイトル': '微細藻類を用いた機能性飲料「Springwave」および植物性マヨネーズ',
    '概要1': 'フードテック企業であるフランスのAlgamaは、クロレラやスピルリナなどの微細藻類を活用して、動物性原料に代わる食品イノベーションを開発/販売している。',
    '概要2': '同製品には、スピルリナベースの機能性飲料「Springwave」と、クロレラを使用した植物性マヨネーズ「The Good Spoon」が含まれる。「Springwave」は、フィコシアニン、ビタミン、ミネラルを豊富に含む乾燥スピルリナ抽出物を使用し、抗酸化作用と活力回復効果を持つ飲料である。「The Good Spoon」は、卵の代わりにクロレラを使用したビーガンマヨネーズである。',
    '概要3': '同社は、特許出願中の技術、配合、および抽出プロセスを開発し、微細藻類を食べやすく扱いやすい原料にすることを実現した。また、同社は、新鮮で中性的な味わいを保ちながら、微細藻類の利点を維持する飲料を開発した。',
    '概要4': '同製品は、人々と地球の両方に良い食品を提供し、従来の動物性原料に代わる持続可能な選択肢を提供することを目的としている。',
    '注目ポイント1': '・従来の動物性原料を使用した食品は、環境への負荷が大きく、持続可能性の観点から課題があった。',
    '注目ポイント2': '・「Springwave」は、SIAL 2014で「Best Beverage」を含む2つの賞を受賞した（1200製品中）。\n・同社は、微細藻類を中性的な味わいにするための特許出願中の技術を開発した。\n・同社は、飲料、乳製品、ベーカリー製品を含む200以上のプロトタイプを保有している。',
    '注目ポイント3': '・同社は、Roquetteと提携し、微細藻類ベースの食品製品に対する消費者意識を高める取り組みを行っている。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.foodnavigator-usa.com/Article/2018/07/05/Algama-is-using-microalgae-to-disrupt-how-food-is-made-starting-with-mayo/',
    '発表年または出願年': '2014',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Algama Foods',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'France',
    '組織設立年': '2013',
    '組織URL': 'https://algamafoods.com',
    '情報ソースURL 1': 'https://www.foodnavigator-usa.com/Article/2018/07/05/Algama-is-using-microalgae-to-disrupt-how-food-is-made-starting-with-mayo/',
    '情報ソースURL 2': 'https://www.nutraingredients.com/Article/2018/09/07/algama-foods-seeks-partner-for-re-launch-of-spirulina-drink/',
    '情報ソースURL 3': 'https://algamafoods.com/en/food-innovation-through-microalgae/',
    '情報ソースURL 4': 'https://www.labiotech.eu/trends-news/microalgae-on-your-plate-thanks-to-algama/',
    '情報ソースURL 5': 'https://nutraceuticalbusinessreview.com/roquette-and-algama-join-forces-to-increase-consumer-awareness-of-microalgae-based-food-products-109874',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# ====================================================================
# No.31 - TraceGains
# ====================================================================
longlist_data.append({
    'ID': 31,
    'タイトル': 'AIを活用した食品・飲料サプライチェーンのコンプライアンス管理プラットフォーム',
    '概要1': '食品・飲料業界向けのネットワーク型コンプライアンスおよび製品開発ソリューションを提供する米国のTraceGainsは、サプライチェーン全体をデジタル化し、AI（人工知能）を活用したプラットフォームを開発/提供している。',
    '概要2': '同プラットフォームは、サプライヤー管理、品質管理、栄養計算とラベル表示、新製品開発、ESG（環境・社会・ガバナンス）、パッケージング管理を統合し、Source-to-Shelfエコシステムを構築する。同プラットフォームは、10万のサプライヤー拠点と60万以上のアイテムを接続するネットワークを持つ。',
    '概要3': '同プラットフォームのAI機能であるTraceGains IDPは、入荷する分析証明書（COA）を自動的にレビューし、仕様に対する潜在的な問題をフラグ付けする。同機能により、従来1ページあたり平均12分かかっていた手動セットアップが不要になった。また、同プラットフォームは、個々の原料および製品の環境フットプリントを測定し、調達とR&Dプロセスに気候影響データを統合する。',
    '概要4': '同プラットフォームは、食品・飲料業界のサプライチェーンにおけるコンプライアンス、品質管理、製品開発の効率化と透明性の向上を目的としている。',
    '注目ポイント1': '・食品・飲料業界のサプライチェーンは複雑であり、サプライヤー管理、品質管理、コンプライアンス確認に多くの手動プロセスが必要であることが課題となっていた。',
    '注目ポイント2': '・同プラットフォームは、AIを活用したIDP（Intelligent Document Processing）により、分析証明書の自動レビューを実現し、手動プロセスを排除する。\n・同プラットフォームは、10万のサプライヤー拠点と60万以上のアイテムを接続する大規模ネットワークを構築している。\n・同プラットフォームは、ESGデータを統合し、原料および製品の環境フットプリントを可視化する。',
    '注目ポイント3': '・同社のソリューションは、世界のトップ100食品・飲料メーカーの半数以上を含む1500以上のグローバル顧客に信頼されている。\n・同社は、2024年にFood LogisticsおよびSupply & Demand Chain Executiveによって「Top Software & Technology Solution」として認定された。\n・同社は、Veraltoグループの一員である。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.prnewswire.com/news-releases/tracegains-launches-first-purpose-built-ai-powered-certificate-of-analysis-solution-to-eliminate-manual-processes-and-improve-ingredient-safety-and-compliance-302410646.html',
    '発表年または出願年': '2008',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'TraceGains, Inc.',
    '組織タイプ': '大企業/中堅企業',
    '国名': 'United States',
    '組織設立年': '2008',
    '組織URL': 'https://tracegains.com',
    '情報ソースURL 1': 'https://www.prnewswire.com/news-releases/tracegains-launches-first-purpose-built-ai-powered-certificate-of-analysis-solution-to-eliminate-manual-processes-and-improve-ingredient-safety-and-compliance-302410646.html',
    '情報ソースURL 2': 'https://tracegains.com/compliance/supplier-compliance/',
    '情報ソースURL 3': 'https://www.fooddive.com/news/tracegains-AI-food-quality-safety-IDP-processor-openAI-artificial-intelligence-tech/743729/',
    '情報ソースURL 4': 'https://www.veralto.com/company/tracegains/',
    '情報ソースURL 5': 'https://www.prnewswire.com/news-releases/tracegains-recognized-as-a-2024-top-software--technology-solution-by-food-logistics-and-supply--demand-chain-executive-302327741.html',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# ====================================================================
# No.32 - Biotalys
# ====================================================================
longlist_data.append({
    'ID': 32,
    'タイトル': 'タンパク質ベースのバイオコントロール技術「AGROBODY」およびボトリチス・うどんこ病防除製品「EVOCA」',
    '概要1': 'アグリテック企業であるベルギーのBiotalysは、新世代のタンパク質ベースのバイオコントロールソリューションを開発し、持続可能で安全な食料供給を実現する技術を開発/販売している。',
    '概要2': '同社の独自技術プラットフォーム「AGROBODY」は、強力で多様な製品候補を開発し、土壌から食卓までのバリューチェーン全体で主要な作物の害虫や病害に対処する。同技術は、化学農薬の高性能特性と生物農薬のクリーンな安全プロファイルを組み合わせており、ターゲットの害虫または病原体のみに作用し、ミツバチなどの有益な昆虫や他の種に対して安全である。',
    '概要3': '同社のリード製品「EVOCA」は、果物や野菜の生産者向けに、ボトリチス（灰色かび病）とうどんこ病を安全に防除する。同製品は、生分解性であり、統合的病害虫管理（IPM）プログラムに組み込むことができる。同製品は、米国EPAおよび欧州の規制当局による審査が進行中である。',
    '概要4': '同技術は、化学農薬の使用を削減し、持続可能な農業を推進することを目的としている。',
    '注目ポイント1': '・従来の化学農薬は、環境や有益な昆虫に悪影響を及ぼすことが課題となっていた。また、従来の生物農薬は、効果が化学農薬に劣ることが課題であった。',
    '注目ポイント2': '・同社の「AGROBODY」技術は、化学農薬の高性能と生物農薬の安全性を両立する。\n・同社の製品は、ターゲットの害虫や病原体のみに作用し、ミツバチなどの有益な昆虫に対して安全である。\n・2023年末に、同社は次世代AGROBODY技術に移行し、バイオ活性剤の効力と有効性をさらに向上させた。',
    '注目ポイント3': '・同社は、2013年にVIB（Flanders Institute for Biotechnology）のスピンオフとして設立され、2021年7月にEuronext Brusselsに上場した。\n・同社は、Syngenta Crop Protectionと戦略的パートナーシップを締結し、AGROBODY技術に基づく新しいバイオコントロールソリューションを共同研究・開発・商業化している。\n・同社のリード製品「EVOCA」は、米国EPAによる規制審査が進行中であり、2025年9月30日までに規制決定が下される予定である。また、欧州でも規制審査が進行中である。',
    '技術開発の進展度': 'Lv6:承認',
    '主要情報ソースタイプ': '公式情報',
    '主要情報ソースURL': 'https://www.biotalys.com/media/news/biotalys-submits-first-protein-based-biocontrol-registration-package-epa',
    '発表年または出願年': '2013',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Biotalys NV',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Belgium',
    '組織設立年': '2013',
    '組織URL': 'https://biotalys.com',
    '情報ソースURL 1': 'https://www.biotalys.com/media/news/biotalys-submits-first-protein-based-biocontrol-registration-package-epa',
    '情報ソースURL 2': 'https://www.biotalys.com/media/news/biotalys-reports-progress-regulatory-review-evoca-both-us-and-eu',
    '情報ソースURL 3': 'https://www.syngenta.com/media/media-releases/2023/syngenta-and-biotalys-enter-strategic-partnership-biologicals-innovation',
    '情報ソースURL 4': 'https://www.biotalys.com/media/news/biotalys-named-sustainable-crop-protection-company-year',
    '情報ソースURL 5': 'https://be.linkedin.com/company/biotalys-nv',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# 残りのデータも同様に追加...（続く）
# 簡略化のため、ここで一旦区切ります。残りの6社も同様の形式で追加する必要があります。

# Vertical Future (No.33)
longlist_data.append({
    'ID': 33,
    'タイトル': '垂直農業システムとソフトウェアプラットフォーム「DIANA」',
    '概要1': '英国のVertical Futureは、2016年から垂直農業技術を開発し、自動化された垂直農業システムとSaaS型ソフトウェアプラットフォームを提供している。',
    '概要2': '同社のターンキー型自動化垂直農業システムは、独自開発のソフトウェア「DIANA」によって制御される。「DIANA」は、データサービス、自動化スクリプト、およびコア植物アルゴリズムの継続的な供給を提供し、農場が稼働すると継続的に運用を支援する。',
    '概要3': '同社は、建物とユーティリティインフラストラクチャの提供を除く全ての作業を含むフルターンキーベースで垂直農場を建設する。また、同社は、包括的な運用支援を必要とする農場向けに運用・保守（O&M）契約を提供する。',
    '概要4': '同システムは、英国内外で垂直農業技術をグローバルに展開し、地元での食料生産とカーボンフットプリント削減を目的としている。',
    '注目ポイント1': '・英国では消費される食品の46%が輸入されており、カーボンフットプリント削減のために地元での食料生産が課題となっていた。',
    '注目ポイント2': '・同社のシステムは、独自開発のSaaS型ソフトウェア「DIANA」によって完全に制御され、データ駆動型の運用を実現する。\n・同社は、ターンキー型のソリューションを提供し、建設から運用まで一貫したサポートを行う。',
    '注目ポイント3': '・同社は、2016年以来、数百のレストランと数千の家庭に垂直農業で栽培された農産物を販売・流通してきた実績を持つ。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.verticalfuture.com/',
    '発表年または出願年': '2016',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Vertical Future Ltd',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United Kingdom',
    '組織設立年': '2016',
    '組織URL': 'https://verticalfuture.com',
    '情報ソースURL 1': 'https://www.verticalfuture.com/',
    '情報ソースURL 2': 'https://www.ingenia.org.uk/articles/vertical-farming-for-future-growth/',
    '情報ソースURL 3': '',
    '情報ソースURL 4': '',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# Babylon Micro-Farms (No.34)
longlist_data.append({
    'ID': 34,
    'タイトル': '水耕栽培垂直農業システム「Galleri」および遠隔管理ソフトウェア「BabylonIQ」',
    '概要1': '米国バージニア州のBabylon Micro-Farmsは、2017年から室内垂直農業システムを開発し、オンサイト型のモジュール式水耕栽培システムと遠隔管理プラットフォームを提供している。',
    '概要2': '同社の主力製品「Galleri」は、32インチ×66インチ×96インチの大きさで、制御環境水耕栽培を使用して葉物野菜、ハーブ、食用花を栽培する。同製品は、WELL Building Standardsに準拠した初の食品安全対応室内垂直農業システムである。同社の特許取得済み水耕栽培技術と独自ソフトウェアプラットフォーム「BabylonIQ」は、モジュール式垂直農業システムのネットワークをクラウド経由で遠隔管理する。',
    '概要3': '同システムは、遠隔監視を使用して最適な植物の成長と健康を確保し、従来の農業実践と比較して10倍少ない水を使用する。同社は、機器を設置し、栽培用品のサブスクリプションを提供し、独自のソフトウェアプラットフォームを介してクラウド経由で作物の成長を遠隔管理する。',
    '概要4': '同システムは、企業の社員食堂、教育機関、医療機関、ホスピタリティ、高齢者施設などで、年間を通じて新鮮で栄養価の高い農産物を現地で提供することを目的としている。',
    '注目ポイント1': '・従来の農業は、水の使用量が多く、輸送に伴うカーボンフットプリントが大きいことが課題となっていた。',
    '注目ポイント2': '・同社の「Galleri」は、WELL Building Standardsに準拠した初の室内垂直農業システムである。\n・同社は、「Galleri Lite」（約1万ドル）や「STEM Garden」（6500ドル）など、価格帯の異なる製品ラインナップを提供している。\n・同社の独自ソフトウェア「BabylonIQ」により、遠隔監視と自動化を実現している。',
    '注目ポイント3': '・同社は、40州と5か国にわたって300以上のマイクロファームを展開している。\n・同社の顧客には、Aramark、Compass Group、Sodexoなどの大手企業が含まれる。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://babylonmicrofarms.com/',
    '発表年または出願年': '2017',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Babylon Micro-Farms, Inc.',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': '2017',
    '組織URL': 'https://babylonmicrofarms.com',
    '情報ソースURL 1': 'https://babylonmicrofarms.com/',
    '情報ソースURL 2': 'https://babylonmicrofarms.com/babylon-micro-farms-galleri-is-first-indoor-vertical-farming-system-aligned-with-well-to-promote-health/',
    '情報ソースURL 3': 'https://www.agritecture.com/blog/2019/12/1/babylon-micro-farms-a-new-approach-to-urban-food-production',
    '情報ソースURL 4': 'https://www.cbinsights.com/company/babylon-micro-farms',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# Square Roots (No.35)
longlist_data.append({
    'ID': 35,
    'タイトル': 'コンテナ型垂直農業システムとクラウド接続型モジュール式室内農場',
    '概要1': '米国のSquare Rootsは、2016年にKimbal MuskとTobias Peggsによって設立され、輸送用コンテナを再利用した垂直農業システムを開発した。',
    '概要2': '同システムは、再利用された輸送用コンテナ内で、水耕栽培システムとLED照明を使用して、320平方フィートの垂直栽培スペースを提供する。同システムは、水効率の高い水耕栽培システムと垂直栽培タワーを組み合わせ、屋外農場と比較して大幅に少ない水とスペースで済む。',
    '概要3': '同システムは、データ、インサイト、およびその他のツールを農業者に提供し、年間を通じて非遺伝子組み換え、農薬不使用の農産物を栽培する。同社は、2016年にFreight Farmsから10台のコンテナ農場を購入し、ブルックリンの農業キャンパスを立ち上げた。',
    '概要4': '同システムは、都市部での食料生産を実現し、輸送距離を短縮することで、カーボンフットプリントを削減することを目的としていた。',
    '注目ポイント1': '・都市部では、新鮮な農産物を入手するために長距離輸送が必要であり、カーボンフットプリントが大きいことが課題となっていた。',
    '注目ポイント2': '・同社は、輸送用コンテナを再利用することで、既存のインフラストラクチャを活用した垂直農業を実現した。\n・同社は、若い起業家を対象としたアクセラレータープログラムを運営し、都市農業の知識を教育していた。',
    '注目ポイント3': '・2023年7月に、同社のCEOであるTobias Peggsは、事業の大部分を閉鎖し、従業員の大半を解雇し、ビジネスモデルを「farming as a service」に変更することを発表した。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.squarerootsgrow.com/',
    '発表年または出願年': '2016',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Square Roots',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': '2016',
    '組織URL': 'https://squarerootsgrow.com',
    '情報ソースURL 1': 'https://www.squarerootsgrow.com/',
    '情報ソースURL 2': 'https://www.foodnavigator-usa.com/Article/2019/03/06/Square-Roots-urban-indoor-farming-shipping-container-model-goes-nationwide/',
    '情報ソースURL 3': 'https://www.freightfarms.com/square-roots',
    '情報ソースURL 4': 'https://civileats.com/2022/06/01/inside-the-effort-to-unionize-square-roots-kimbal-musks-vertical-farming-company/',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# Phytech (No.36)
longlist_data.append({
    'ID': 36,
    'タイトル': '植物ベースのIoTセンサーとAIによる灌漑管理プラットフォーム「PlantBeat」',
    '概要1': 'イスラエルのPhytechは、IoTセンサーとデータ分析を用いて、作物の水分ストレス、土壌水分、および環境条件を測定し、生産者に継続的なインサイトを提供する精密農業プラットフォーム「PlantBeat」を開発/提供している。',
    '概要2': '同プラットフォームは、デンドロメーター（樹幹径変動測定器）と土壌水分プローブを使用して、作物の水分ニーズと作物の水分ステータスをリアルタイムで追跡する。果樹園内の各樹木または圃場作物の茎に取り付けられたセンサーは、植物の水分および肥料のニーズを継続的に監視し、これを環境データと統合する。また、同プラットフォームは、精密灌漑技術、水圧監視、および遠隔制御機能を組み合わせ、生産者がモバイルデバイスまたはデスクトップからデータ駆動型の灌漑決定を行うことを可能にする。',
    '概要3': '同社は、2025年に、Phytechの独自IoTネットワークから収集されたリアルタイムの圃場データで訓練された初のAI駆動型灌漑アドバイザー「Phytech AI Advisor」を発表した。同アドバイザーは、生産者に対して、水効率、肥料使用、エネルギー消費、および収量改善を即座に改善する正確でリアルタイムの推奨事項を提供する。',
    '概要4': '同プラットフォームは、世界中の農業生産者が水資源を効率的に管理し、収量を向上させることを目的としている。',
    '注目ポイント1': '・従来の灌漑管理は、経験に基づく判断や固定スケジュールに依存しており、水の過剰使用や不足による収量低下が課題となっていた。',
    '注目ポイント2': '・同プラットフォームは、植物に直接取り付けられたセンサーを使用して、植物の水分ニーズをリアルタイムで測定する。\n・同社の「Phytech AI Advisor」は、実際の圃場データで訓練された初のAI駆動型灌漑アドバイザーである。\n・同プラットフォームは、水圧、流量、およびシステムパフォーマンスを追跡し、水が必要な場所と時間に正確に供給されることを保証する。',
    '注目ポイント3': '・同プラットフォームは、160万dunam（40万2426エーカー）にわたって展開され、18000の農場で4300万本の樹木を監視している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.croplife.com/precision-tech/phytech-introduces-ai-powered-irrigation-advisor-to-transform-global-farming/',
    '発表年または出願年': '2012',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Phytech Ltd',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Israel',
    '組織設立年': '2012',
    '組織URL': 'https://phytech.com',
    '情報ソースURL 1': 'https://www.croplife.com/precision-tech/phytech-introduces-ai-powered-irrigation-advisor-to-transform-global-farming/',
    '情報ソースURL 2': 'https://www.phytech.com/post/what-is-irrigation-automation',
    '情報ソースURL 3': 'https://finder.startupnationcentral.org/company_page/phytech',
    '情報ソースURL 4': 'https://igrownews.com/phytech-latest-news/',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# IUNU (No.37)
longlist_data.append({
    'ID': 37,
    'タイトル': 'コンピュータビジョンとAIによる温室作物管理プラットフォーム「LUNA」',
    '概要1': '米国シアトルのIUNUは、2013年に設立され、温室栽培者向けのAI駆動型プラットフォーム「LUNA」を開発/提供している。',
    '概要2': '同プラットフォームは、AIとコンピュータビジョンを使用して、植物の発育を自動的に追跡し、データを意思決定に変換する。同プラットフォームのレールおよび移動式イメージングシステムは、温室のトラスレベルに配置されたアルミニウムレールに沿ってモバイルカメラを誘導し、作物の日次画像をキャプチャする。これらの画像はリアルタイムでクラウドに送信され、植物の健康、成長、およびトレンドに関する即座の可視性を提供する。',
    '概要3': '同プラットフォームは、生産者の既存の制御システムおよびERPシステムと直接統合し、運用を効率化するリアルタイムのデジタルアシスタントを提供する。同プラットフォームは、18か国の100以上の施設で稼働しており、制御環境農業（CEA）セクター（温室運営、垂直農場、室内栽培システムを含む）で使用されている。',
    '概要4': '同プラットフォームは、温室栽培者が品質、収量、および収益性を向上させることを目的としている。',
    '注目ポイント1': '・温室栽培では、植物レベルのデータを収集することが困難であり、栽培者が最適な意思決定を行うための情報が不足していることが課題となっていた。',
    '注目ポイント2': '・同プラットフォームは、自動化されたレールシステムとモバイルカメラを使用して、温室内の作物の日次画像を自動的にキャプチャする。\n・同プラットフォームは、コンピュータビジョンとAIを使用して、植物の健康、成長、およびトレンドをリアルタイムで分析する。\n・同プラットフォームは、生産者の既存のシステムと統合し、運用を効率化する。',
    '注目ポイント3': '・同社は、2025年4月に、S2G Investmentsが主導し、Farm Credit CanadaおよびLewis and Clark Partnersが参加する2000万ドルの資金調達ラウンドを完了した。\n・同社は、ブドウ作物セグメントで330%の成長を達成している。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.prnewswire.com/news-releases/iunu-secures-20-million-to-accelerate-growth-in-ai-driven-greenhouse-technology-302428703.html',
    '発表年または出願年': '2013',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'IUNU, Inc.',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'United States',
    '組織設立年': '2013',
    '組織URL': 'https://IUNU.com',
    '情報ソースURL 1': 'https://www.prnewswire.com/news-releases/iunu-secures-20-million-to-accelerate-growth-in-ai-driven-greenhouse-technology-302428703.html',
    '情報ソースURL 2': 'https://iunu.com/',
    '情報ソースURL 3': 'https://indoor.ag/computer-vision-brings-clarity-to-growers-q-a-with-iunu-ceo-adam-greenberg/',
    '情報ソースURL 4': 'https://www.cbinsights.com/company/iunu',
    '情報ソースURL 5': '',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# Vow (No.38)
longlist_data.append({
    'ID': 38,
    'タイトル': '培養肉を製造する細胞農業プラットフォームと培養ウズラ製品',
    '概要1': 'オーストラリアのVowは、2019年に設立され、商業流通向けの培養肉を製造する細胞農業企業である。',
    '概要2': '同社は、醸造所に似た大型バットで、4週間のプロセスを経て培養肉製品を成長させる。2025年6月時点で、Vowは35000リットルのバイオリアクター容量を有し、世界最大の食品生産バイオリアクター「Andromeda」（20000リットル）を運用している。同社の技術により、1回の収穫あたり最大900 kgの生産能力があり、月間10800 kg、年間13万 kgまでスケールアップする予定である。',
    '概要3': '同社は、2025年4月7日に、オーストラリアおよびニュージーランドで販売が承認された初の培養肉製品となった。これにより、オーストラリアは、シンガポール、米国、イスラエルに次いで、培養肉の販売を承認した4番目の管轄区域となった。2025年6月時点で、同社の全商業製品は日本ウズラの細胞に基づいており、パテ、フォアグラ、食用タローキャンドル、およびスモークバタースプレッドを販売している。',
    '概要4': '同製品は、従来の食肉生産の環境負荷を削減し、持続可能で倫理的な食品を提供することを目的としている。',
    '注目ポイント1': '・従来の食肉生産は、環境負荷が大きく、動物福祉の観点からも課題があった。',
    '注目ポイント2': '・同社は、世界最大の食品生産バイオリアクター「Andromeda」（20000リットル）を運用している。\n・同社の製品は、醸造所に似たバイオリアクターで4週間かけて成長させる。\n・同社は、自然界にはない独自の製品を開発し、肉を好む消費者の関心を引くことを戦略としている。',
    '注目ポイント3': '・2025年4月7日に、Vowのウズラ培養肉は、オーストラリアおよびニュージーランドで販売が承認された初の培養肉製品となった。\n・2024年4月に、シンガポールは培養肉の販売を承認した初の政府となり、Vowは同月に初の商業製品「Forged Parfait」（日本ウズラ細胞製）を販売開始した。',
    '技術開発の進展度': 'Lv7:販売・実用化',
    '主要情報ソースタイプ': 'WEBメディア',
    '主要情報ソースURL': 'https://www.greenqueen.com.hk/vow-cultured-quail-lab-grown-meat-approved-fsanz-australia-new-zealand/',
    '発表年または出願年': '2019',
    '代表的な図のURL': 'Figなし',
    '図の掲載ページURL': 'Figなし',
    '組織名': 'Vow Food Company Pty Ltd',
    '組織タイプ': 'ベンチャー企業',
    '国名': 'Australia',
    '組織設立年': '2019',
    '組織URL': 'https://eatvow.com',
    '情報ソースURL 1': 'https://www.greenqueen.com.hk/vow-cultured-quail-lab-grown-meat-approved-fsanz-australia-new-zealand/',
    '情報ソースURL 2': 'https://www.evokeag.com/cellular-ag-pioneer-vow-makes-history-as-the-first-australian-company-to-launch-a-cultured-meat-product/',
    '情報ソースURL 3': 'https://en.wikipedia.org/wiki/Vow_(company)',
    '情報ソースURL 4': 'https://www.businessnewsaustralia.com/articles/-totally-new-category-of-food---cultured-meat-startup-vow-approved-for-sales-in-australia--nz.html',
    '情報ソースURL 5': 'https://www.just-food.com/news/cultured-meat-approved-by-australia-regulator-as-vow-debuts-in-oz/',
    '情報ソースURL 6': '',
    '情報ソースURL 7': '',
    '情報ソースURL 8': '',
    '情報ソースURL 9': '',
    '情報ソースURL 10': '',
})

# DataFrameを作成
df = pd.DataFrame(longlist_data)

# 情報ソースURL 11-20の列を追加（すべて空欄）
for i in range(11, 21):
    df[f'情報ソースURL {i}'] = ''

# Excelファイルとして保存
output_path = '/home/user/claude251107/work_dir/output/agent_3/技術ロングリスト_初期版.xlsx'
df.to_excel(output_path, index=False, engine='openpyxl')

print(f"技術ロングリスト_初期版.xlsxを作成しました")
print(f"出力パス: {output_path}")
print(f"総件数: {len(df)}件")
print(f"列数: {len(df.columns)}列")
