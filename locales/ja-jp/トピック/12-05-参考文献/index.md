# 12.5 参考文献

このセクションは、ガイドブックの参照の仕組みを統合します。SWEBOK知識体系への対応表、全体で引用される標準と枠組みの索引、推奨される読み物の選り抜きの文献一覧です。各章ごとの情報源も、各章末の*参考文献とさらなる読み物*のセクションに現れます。

---

# SWEBOK対応表

このガイドブックは、IEEEコンピュータ協会の**SWEBOK V4.0**(ソフトウェアエンジニアリング知識体系)に沿っています。18の知識領域すべてが扱われます。表は各領域を、それを扱う章に対応づけ、ガイドブックはその後、SWEBOKをはるかに超えて、AI、データ、UX、DevOps、持続可能性、フロー、公共の利益のための技術にまで及びます。

| SWEBOK V4.0の知識領域 | 主な章 |
|---|---|
| 1. ソフトウェア要求 | 2.8, 11.1, 5.1 |
| 2. ソフトウェアアーキテクチャ | 3.1, 3.2, 3.3 |
| 3. ソフトウェア設計 | 2.2, 3.1 |
| 4. ソフトウェア構築 | 2.9, 2.1 |
| 5. ソフトウェアテスト | 2.4, 8.5 |
| 6. ソフトウェアエンジニアリング運用 | 9.1, 9.2, 9.3, 8.1 |
| 7. ソフトウェア保守 | 3.7, 3.6, 10.4 |
| 8. ソフトウェア構成管理 | 2.10, 2.6, 8.2 |
| 9. ソフトウェアエンジニアリング管理 | 10.1, 10.6, 10.2 |
| 10. ソフトウェアエンジニアリングプロセス | 1.4, 10.7, 10.8 |
| 11. ソフトウェアエンジニアリングのモデルと方法 | 2.12, 3.1, 2.2 |
| 12. ソフトウェア品質 | 2.11, 2.4, 3.1 |
| 13. ソフトウェアセキュリティ | 4.1, 4.2, 4.3, 4.4 |
| 14. ソフトウェアエンジニアリングの専門的実践 | 10.5, 1.1, 1.3 |
| 15. ソフトウェアエンジニアリング経済学 | 10.10, 10.1, 9.4 |
| 16. コンピューティングの基礎 | 2.13, 3.3, 3.4 |
| 17. 数学の基礎 | 2.13, 11.3 |
| 18. エンジニアリングの基礎 | 2.13, 3.1 |

---

# 標準と枠組み

この付録は、ガイドブック全体で参照される実在の標準、枠組み、規制を整理した索引です。コンプライアンスの手引きではなく、道案内の助けです。現在の本文と、自分の文脈への適用可能性については、常に権威ある情報源を参照し、必要に応じて資格のある法務あるいは監査の助言者に相談してください。

項目は領域ごとにまとめられています。それぞれ、標準あるいは枠組みの名前、発行する団体、一行の範囲、それが最も関連する章あるいは領域を示します。一般に略称で呼ばれる名前には、略称が示されます。文書番号とタイトルは、よく確立されている場合にだけ示され、URLは含まれません。

## この付録の使い方

- **規制**(たとえばGDPR、HIPAA)は、その管轄とセクターで法的に拘束力があります。単なる良い実践ではなく、義務を定めます。
- **標準**(たとえばISO/IEC 27001、WCAG)は、正式で、しばしば認証可能な仕様です。任意のものもあれば、法律や契約で義務づけられるものもあります。
- **枠組み**(たとえばNIST CSF、NIST AI RMF)は、構造化された、通常は任意の指針で、自分のリスクプロファイルに合わせて調整します。
- 適用可能性は、管轄、セクター、データの種類、契約の条件に依存します。多くの組織は、これらのうち複数を同時に満たさなければなりません。

## セキュリティとプライバシー

| 標準/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | 情報セキュリティマネジメントシステム(ISMS)の要件。 | 4.1–4.6 セキュリティとコンプライアンス |
| ISO/IEC 27002 | ISO / IEC | ISO/IEC 27001を支える指針と統制の集合。 | 4.1–4.4 セキュリティ |
| ISO/IEC 27017 / 27018 | ISO / IEC | クラウド固有のセキュリティ統制(27017)とクラウド内のPIIの保護(27018)。 | 4.3 インフラストラクチャとクラウドのセキュリティ、4.5 プライバシー |
| NISTサイバーセキュリティフレームワーク(CSF) | 米国国立標準技術研究所 | ガバナンス、識別、防御、検知、対応、復旧を軸に構成された任意の枠組み。 | 4.1, 4.4 セキュリティの基礎と運用 |
| NIST SP 800-53 | 米国国立標準技術研究所 | 情報システムのセキュリティとプライバシーの統制のカタログ。 | 4.3, 4.6 クラウドセキュリティとコンプライアンス |
| NIST SP 800-63 | 米国国立標準技術研究所 | デジタルアイデンティティと認証の保証の指針。 | 4.2, 4.3 アプリケーションとインフラストラクチャのセキュリティ |
| OWASP Top Ten | Open Worldwide Application Security Project | 最も重大なWebアプリケーションのセキュリティリスクで、定期的に更新される。 | 4.2 アプリケーションセキュリティ |
| OWASP ASVS | Open Worldwide Application Security Project | アプリケーションのセキュリティを検証するための段階づけられた要件とテスト。 | 2.4, 4.2 テストとアプリケーションセキュリティ |
| OWASP SAMM | Open Worldwide Application Security Project | ソフトウェアセキュリティのプログラムを築き評価するための成熟度モデル。 | 4.1 セキュリティの基礎と文化 |
| STRIDE | Microsoftで考案 | 脅威を分類するための脅威モデリングの分類法。 | 4.2 アプリケーションセキュリティ |
| MITRE ATT&CK | MITRE | 検知と防御のための敵対者の戦術と技法の知識ベース。 | 4.4 セキュリティ運用 |
| SLSA | Open Source Security Foundation (OpenSSF) | ソフトウェアサプライチェーンの完全性と出所についての段階的な枠組み。 | 4.2, 8.1, 10.3 サプライチェーンとデリバリー |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX)、OWASP (CycloneDX) | ソフトウェア部品表の標準形式。 | 4.2, 10.3 アプリケーションセキュリティとライセンス |
| PCI DSS | PCI Security Standards Council | ペイメントカードのデータを扱うためのセキュリティ要件。 | 4.2, 4.5, 4.6 セキュリティ、プライバシー、コンプライアンス |

## コンプライアンスと政府

### 米国

| 規制/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| HIPAA | 米国保健福祉省 | 保護対象保健情報(PHI)の保護措置。 | 4.5, 4.6 プライバシーとコンプライアンス |
| SOX(サーベンス・オクスリー法) | 米国議会 / SEC | 上場企業の財務報告と内部統制の要件。 | 4.6, 10.2 コンプライアンスと監査 |
| FISMA | 米国議会 | 連邦機関の情報セキュリティプログラムの要件。 | 4.3, 4.6 クラウドセキュリティとコンプライアンス |
| FedRAMP | 米国一般調達局 / FedRAMP PMO | 連邦機関が使うクラウドサービスの標準化されたセキュリティ認可。 | 4.3, 4.6 クラウドセキュリティとコンプライアンス |
| NIST SP 800-171 | 米国国立標準技術研究所 | 連邦以外のシステムにおける管理対象非機密情報(CUI)の保護。 | 4.6 コンプライアンス(防衛のサプライチェーン) |
| CMMC | 米国国防総省 | 防衛請負業者のサイバーセキュリティ成熟度の認証。 | 4.6 コンプライアンス(防衛) |
| FIPS 140-3 | 米国国立標準技術研究所 | 暗号モジュールのセキュリティ要件。 | 4.3 インフラストラクチャとクラウドのセキュリティ |
| CCPA / CPRA | カリフォルニア州 | カリフォルニアにおける消費者のプライバシーの権利と事業者の義務。 | 4.5 プライバシーとデータ保護 |

### 欧州連合と英国

| 規制/標準 | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| GDPR | 欧州連合 | 個人データの処理に関する包括的な規制。 | 4.5, 4.6 プライバシーとコンプライアンス |
| UK GDPR / Data Protection Act 2018 | 英国 | 英国のEU離脱後のデータ保護制度。 | 4.5, 4.6 プライバシーとコンプライアンス |
| eIDAS | 欧州連合 | 電子的な識別とトラストサービスの枠組み。 | 4.2, 4.3 セキュリティ |
| NIS2指令 | 欧州連合 | 必須および重要な事業体のサイバーセキュリティの義務。 | 4.4, 4.6 セキュリティ運用とコンプライアンス |
| DORA(デジタル・オペレーショナル・レジリエンス法) | 欧州連合 | 金融セクターの運用レジリエンスの要件。 | 9.1, 10.2 信頼性と監査 |
| EU AI法 | 欧州連合 | AIシステムのリスクベースの規制(下のAIガバナンスを参照)。 | 6.1, 6.5 AI戦略と責任あるAI |

## アクセシビリティ

| 標準 | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | アクセシブルなWebコンテンツの指針で、A/AA/AAAの適合水準がある。 | 5.3 アクセシビリティ、5.1–5.6 UXとフロントエンド |
| WAI-ARIA | World Wide Web Consortium (W3C) | アクセシブルなリッチインターネットアプリケーションのためのロール、状態、プロパティ。 | 5.3, 5.6 アクセシビリティとフロントエンド |
| セクション508 | 米国アクセスボード / 米国連邦法 | WCAGに沿った、米国連邦のICTのアクセシビリティ要件。 | 5.3 アクセシビリティ(米国政府) |
| EN 301 549 | ETSI / CEN / CENELEC | ICT調達のためのWCAGに沿った欧州のアクセシビリティ要件。 | 5.3 アクセシビリティ(EUの公共部門) |
| ADA(障害を持つアメリカ人法) | 米国議会 | 障害による差別を禁じ、デジタルサービスにも適用される公民権法。 | 5.3 アクセシビリティ |
| ISO/IEC 40500 | ISO / IEC | WCAG 2.0を正式な標準として国際的に採用したもの。 | 5.3 アクセシビリティ |

## AIガバナンス

| 枠組み/規制 | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| NIST AIリスク管理フレームワーク(AI RMF) | 米国国立標準技術研究所 | AIのリスクを統治し、対応づけ、測定し、管理するための任意の枠組み。 | 6.1, 6.5 AI戦略と責任あるAI |
| ISO/IEC 42001 | ISO / IEC | AIマネジメントシステム(AIMS)の要件。 | 6.1, 6.5 AIガバナンス |
| ISO/IEC 23894 | ISO / IEC | AI固有のリスク管理の指針。 | 6.5 責任ある信頼できるAI |
| EU AI法 | 欧州連合 | AIシステムの提供者と展開者に対する、リスク階層別の法的義務。 | 6.1, 6.3, 6.5 AIアプリケーションとガバナンス |
| OECD AI原則 | 経済協力開発機構 | 信頼できるAIのための価値に基づく原則で、政策に影響力がある。 | 6.5, 10.5 責任あるAIと倫理 |

## 品質とプロセス

| 標準/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | ソフトウェア製品の品質モデル(機能適合性、信頼性、セキュリティなど)。 | 2.2, 2.4 設計とテスト |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | ソフトウェアライフサイクルのプロセス。 | 1.4, 10.1 働き方とプログラム管理 |
| ISO 9001 | ISO | 一般的な品質マネジメントシステムの要件。 | 10.2 リスク、監査、保証 |
| CMMI | ISACA / CMMI Institute | プロセス能力と改善のための成熟度モデル。 | 10.1, 10.2 プログラム管理と保証 |
| DORA指標 | DevOps Research and Assessment (Google Cloud) | ソフトウェアチームのための四つの主要なデリバリー性能の指標。 | 8.1, 8.4, 9.1 デリバリー、プラットフォーム、信頼性 |
| SPACEフレームワーク | Microsoft / GitHubの研究者 | 開発者の生産性を測定する多次元のモデル。 | 1.3, 8.4 成長と開発者体験 |
| ITIL | AXELOS / PeopleCert | ITサービスマネジメントの実践の枠組み。 | 9.1, 9.3 信頼性とインシデント管理 |

## アーキテクチャ

| 標準/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | アーキテクチャ記述とビューポイントの標準。 | 2.7, 3.1 ドキュメンテーションとアーキテクチャの基礎 |
| TOGAF | The Open Group | エンタープライズアーキテクチャの枠組みと開発手法。 | 3.1, 10.1 アーキテクチャとポートフォリオ管理 |
| C4モデル | コミュニティ(Simon Brown) | ソフトウェアアーキテクチャを可視化する4段階のアプローチ。 | 2.7, 3.1 ドキュメンテーションとアーキテクチャ |
| arc42 | コミュニティ(Starke / Hruschka) | アーキテクチャのドキュメントを構造化するテンプレート。 | 2.7, 3.1 ドキュメンテーションとアーキテクチャ |
| ADR | コミュニティの実践 | 重要なアーキテクチャ決定の軽量な記録。 | 1.5, 2.7, 3.1 意思決定とドキュメンテーション |

## クラウドとDevOps

| 標準/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| CISベンチマーク | Center for Internet Security | システムとクラウドの、合意に基づく安全な構成のベースライン。 | 4.3, 8.2 インフラストラクチャのセキュリティとIaC |
| CNCFランドスケープとプロジェクト | Cloud Native Computing Foundation | クラウドネイティブコンピューティング(たとえばKubernetes)のエコシステムと標準。 | 8.3 コンテナとクラウドネイティブ |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | コンテナイメージとランタイム形式のオープンな標準。 | 8.3 コンテナとクラウドネイティブ |
| OpenTelemetry | Cloud Native Computing Foundation | テレメトリ(トレース、メトリクス、ログ)のためのベンダー中立の標準。 | 9.2 オブザーバビリティと監視 |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | ポリシー・アズ・コードのための汎用ポリシーエンジン。 | 4.6, 8.2, 8.3 コンプライアンス、IaC、オーケストレーション |
| SREの実践 | Google(広く採用) | 信頼できるサービスを運用するための、SLI/SLO/エラーバジェットに基づくアプローチ。 | 9.1 サイトリライアビリティエンジニアリング |
| FinOpsフレームワーク | FinOps Foundation | クラウドの財務管理とコストの説明責任の実践。 | 9.4 コスト、持続可能性、グリーンソフトウェア |

## データ

| 標準/枠組み | 発行団体 | 範囲(一行) | 主な章/領域 |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | データ管理の規律を整理した知識体系。 | 7.1 データ戦略とガバナンス |
| ISO/IEC 38505 | ISO / IEC | 組織の資産としてのデータのガバナンス。 | 7.1 データガバナンス |
| ISO 8000 | ISO | データ品質とマスターデータの標準。 | 7.1, 7.2 データガバナンスとエンジニアリング |
| データメッシュ | コミュニティ(Zhamak Dehghani) | プロダクトとしてのデータへの、分散型でドメイン指向のアプローチ。 | 7.1, 7.2 データ戦略とエンジニアリング |
| DCAM | EDM Council | データ管理の能力を評価するモデル。 | 7.1 データ戦略とガバナンス |

## 範囲と変化についての注記

標準と規制は進化します。バージョン番号(たとえばWCAG 2.1対2.2、あるいはISOの改訂年)と統制のカタログは時間とともに変わり、新しい法(セクター固有のAIやレジリエンスの規制など)は現れ続けます。この付録を出発点の地図として扱ってください。コンプライアンスや調達の決定のためにどの項目に頼る前にも、現在のバージョン、管轄、適用可能性を確認してください。ガイドブックの章とこの付録が細部で異なる場合は、常に権威ある原典が優先します。


---

# 推奨される読み物

この付録は、ガイドブックのあらゆる領域にわたる、注釈付きの選り抜きの読書一覧です。大規模な実践を形づくった著作を好みます。認められた古典、厳密な参考書、そして大規模なチーム、企業、政府のチームが照らし合わされる標準と報告書です。

各項目は、題名と著者に続き、それが重要な理由を一文で示します。一覧は本書の10の部ごとに整理されています。選んで読んでください。棚全体ではなく、今の痛みに最も近い二、三冊を選びます。ある著作が領域にまたがる場合は、最も役立つ所に置かれています。多くは複数の部に属します。

標準についての注記: NIST、OWASP、W3C/WCAG、ISO、DORAプログラムなどの団体は、定期的に改訂される生きた文書を公表します。現在のバージョンを引用し、読んでください。以下の注釈は、それらの変わらない目的を述べています。

## 基礎: 文化、人、プロセス

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. デリバリー性能が組織の性能を予測することを示し、それを測る指標(今ではDORAと呼ばれる)を定義した研究の基礎。
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. フロー、仕掛かりの仕事、DevOpsの「三つの道」を、リーダーにも懐疑派にも直感的にするビジネス小説。
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. 良いソフトウェアを生む組織を設計するための実践的な語彙(ストリームに揃ったチーム、プラットフォームチーム、支援チーム、複雑なサブシステムのチーム)。
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. チームの規模決定、組織の成長の管理、エンジニアリングのリーダーシップの繰り返し現れる決定を行うための、現場で試された枠組み。
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. スタッフ以上の類型と、マネージャーにならずに影響力を望む人のための技術的リーダーシップの道を定義する。
- **The Manager's Path**. Camille Fournier. テックリードから経営幹部までの段階ごとの手引きで、キャリアの梯子とマネジメントへの移行の錨となる。
- **The Staff Engineer's Path**. Tanya Reilly. 技術的リーダーシップ、影響力、権限なしに舵を取る日々の仕事に焦点を当てた、スタッフ以上の文献の相棒。
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. ソフトウェアの中心的な問題は技術的ではなく社会学的だという、変わらない主張。
- **The Mythical Man-Month**. Frederick P. Brooks Jr. ブルックスの法則と、本質的複雑さと偶有的複雑さの区別の源で、今も人員配置とスケジューリングを支配している。
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. 責めない文化と、失敗から学ぶことを可能にする安全性の研究の基礎。
- **Thinking, Fast and Slow**. Daniel Kahneman. 認知バイアスの決定的な解説で、構造化された面接、較正、誠実な意思決定に欠かせない。

## プログラミングの技巧とコード品質

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. 職人技が何を意味するかを定義する、プロの習慣(DRY、直交性、トレーサー弾)の基礎的なカタログ。
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. 挙動を保つ変換の標準的なカタログと、テストに支えられた継続的なコード改善の規律。
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. 命名、関数、可読性についての、広く使われる(そして議論される)標準で、多くのチームのレビューの期待を形づくっている。
- **Code Complete**. Steve McConnell. 構築の実践についての、包括的で証拠を参照する手引きで、プログラミングの品質の徹底した基準であり続けている。
- **Test-Driven Development: By Example**. Kent Beck. レッド・グリーン・リファクターのサイクルとテストファーストの設計への、原典となる実践的な入門。
- **Working Effectively with Legacy Code**. Michael Feathers. テストのないコードにテストを加え、安全に変更するための決定的な道具箱で、長寿命のシステムに欠かせない。
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. 外側から内側へのTDD、モック、テストを通じた設計の進化の、実演つきの解説。
- **A Philosophy of Software Design**. John Ousterhout. 複雑さ、深いモジュール、情報隠蔽についての、鋭く意見のはっきりした扱いで、「クリーンコード」の正統派の一部に実りある形で挑む。

## アーキテクチャとシステム

- **Designing Data-Intensive Applications**. Martin Kleppmann. 規模におけるストレージ、レプリケーション、パーティショニング、一貫性、ストリーム処理のトレードオフについての、現代で最良の唯一の参考書。
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. アーキテクチャのスタイル、特性、アーキテクトの役割と意思決定についての、広く現代的な概観。
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. 分散アーキテクチャのトレードオフ、サービスの粒度、データの所有についての、決定に焦点を当てた扱い。
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. フィットネス関数と、時間とともに安全に変わるよう設計されたアーキテクチャを紹介する。
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. 境界づけられたコンテキスト、ユビキタス言語、集約の源で、現代のサービス設計の語彙。
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. 分解、サービスの境界、デプロイ、マイクロサービスの組織的な含意についての参考書。
- **Monolith to Microservices**. Sam Newman. 危険な一斉の書き直しなしに、ストラングラーフィグやブランチ・バイ・アブストラクションなどで段階的に分解するためのパターンのカタログ。
- **Patterns of Enterprise Application Architecture**. Martin Fowler. 企業システムに共有の言語を与えた、名前付きパターンの参考書(リポジトリ、ユニット・オブ・ワークなど)。
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. イベント駆動で非同期のアーキテクチャを支えるメッセージングパターンの決定的なカタログ。
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. 実際の本番を生き延びるシステムのための、サーキットブレーカー、バルクヘッドなどの安定性パターンの源。
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (「Gang of Four」). オブジェクト指向パターンの歴史的に決定的なカタログと、共有の設計の語彙。

## セキュリティ、プライバシー、信頼

- **Threat Modelling: Designing for Security**. Adam Shostack. STRIDEと構造化された脅威モデリングを日常のエンジニアリングの実践とするための、実践的で包括的な手引き。
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. 実際のシステムがどう失敗し、攻撃に抵抗するものをどう築くかについての百科事典的な参考書。
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. ブラウザのセキュリティモデルと、Webプラットフォームが素朴な想定を裏切る微妙な方法についての厳密な案内。
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. 暗号を正しく使い、一般的で危険な間違いを避けるための実務者向けの手引き。
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). セキュリティと信頼性を、最初から設計に組み込まれる絡み合った性質として捉えるGoogleの総合。
- **Zero Trust Networks**. Evan Gilman and Doug Barth. 決して信頼せず常に検証するネットワークアーキテクチャの原則と仕組みの、明快な扱い。
- **OWASP Top 10**. OWASP Foundation. 最も重大なWebアプリケーションのセキュリティリスクの合意に基づくベースラインで、世界中の方針と監査で参照される。
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. 契約と受け入れ基準に適した、段階づけられ、テスト可能なセキュリティ要件のチェックリスト。
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. 米国連邦のセキュリティの中心にある統制のカタログで、FedRAMPとFISMAの認可の基礎。
- **NIST Cybersecurity Framework (CSF)**. NIST. セキュリティプログラムを整理するための、広く採用された識別・防御・検知・対応・復旧の構造。
- **NIST SP 800-207: Zero Trust Architecture**. NIST. ほとんどの企業と政府のゼロトラストプログラムの錨となる、参照の定義と参照アーキテクチャ。

## UX、UI、プロダクトデザイン

- **The Design of Everyday Things**. Don Norman. アフォーダンス、シグニファイア、フィードバック、人間中心設計についての基礎的なテキストで、物理的な物をはるかに超えて当てはまる。
- **Don't Make Me Think, Revisited**. Steve Krug. 自明なユーザビリティと、安く頻繁なユーザビリティテストの価値についての、簡潔で変わらない主張。
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. インタラクションデザイン、ペルソナ、目標指向のデザインについての包括的な参考書。
- **Design Systems: A Practical Guide**. Alla Kholmatova. 一貫して再利用可能なコンポーネントシステムと、その背後の共有の言語を築くことについての、地に足のついた解説。
- **Refactoring UI**. Adam Wathan and Steve Schoger. 正式な訓練なしにインターフェースを設計するエンジニアのための、視覚的な洗練の実践的で例中心の手引き。
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. 平易な言葉でタスクに焦点を当てたコンテンツデザインの決定的な手引き。
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering、Laura Kalbag. 人間の能力の全範囲に働くインターフェースを築くための実践的な相棒。
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. アクセシビリティの標準と良いユーザー体験をつなぐ、原則主導の橋。
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. ほとんどのアクセシビリティ法の背後にある、国際的に参照される標準(知覚可能、操作可能、理解可能、堅牢)。
- **U.S. Web Design System (USWDS)**. 米国政府. 公共サービスのために規模で築かれた、アクセシブルで標準に基づくデザインシステムの動く例。

## 人工知能と機械学習

- **Designing Machine Learning Systems**. Chip Huyen. 本番のMLシステムをデータ、特徴量、デプロイ、監視まで端から端まで築くための、先導的な実践的手引き。
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. SREの規律(SLO、監視、インシデント対応)を機械学習システムに広げる。
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. 現代のニューラルネットワークの背後の理論と手法についての標準的な学術的参考書。
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. 大規模な基盤モデルの上に築かれるアプリケーションを設計、評価、運用するための現代的な手引き。
- **Weapons of Maths Destruction**. Cathy O'Neil. アルゴリズムの説明責任と、吟味されないモデルの現実の害についての鮮やかな論で、公共部門のAIに欠かせない。
- **Interpretable Machine Learning**. Christoph Molnar. モデルとその予測の説明可能性の手法についての、包括的で自由に入手できる参考書。
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. AIのリスクを統治し、対応づけ、測定し、管理するための参照の枠組みで、政策と調達でますます引用される。

## データ、分析、洞察

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball and Margy Ross. 分析のためのスタースキーマとディメンショナルモデリングについての標準的な参考書。
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. 規模で信頼でき行動につながる結果を生む実験を行うための、権威ある手引き。
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. 現代のデータライフサイクルとその背後のエンジニアリングの実践の、ベンダー中立の地図。
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. データを規模で整理するための、ドメイン指向でプロダクト中心のアプローチの創設のテキスト。
- **Storytelling with Data**. Cole Nussbaumer Knaflic. 誠実で明快なデータの可視化と、意思決定者に洞察を伝えるための実践的な手引き。
- **The Visual Display of Quantitative Information**. Edward R. Tufte. グラフィカルな完全性、データインク、データを誠実に示す倫理についての基礎的な著作。
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. データガバナンス、スチュワードシップ、品質、カタログ化のための包括的な参照の枠組み。
- **The Book of Why**. Judea Pearl and Dana Mackenzie. 因果推論への読みやすい入門で、相関から擁護できる決定へ移るのに不可欠。

## 自動化、DevOps、プラットフォームエンジニアリング

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. 「三つの道」を、フロー、フィードバック、継続的な学びのための具体的な実践に翻訳する包括的なプレイブック。
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. デプロイメントパイプライン、自動化、ソフトウェアを安全に頻繁にリリースすることについての基礎的なテキスト。
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. インフラストラクチャをソフトウェアとして扱うこと(モジュール、テスト、不変性、ドリフト)についての参考書。
- **Team Topologies**. Matthew Skelton and Manuel Pais. (基礎を参照。)プラットフォームチームと、それが提供する開発者体験を形づくるうえでもここで欠かせない。
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Kubernetes上でクラウドネイティブなアプリケーションを設計するための、再利用可能なパターンのカタログ。
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. テスト、レビュー、ツール、依存関係管理などのエンジニアリングの実践が、数十年にわたって数万人のエンジニアへどうスケールするか。
- **The Twelve-Factor App**. Adam Wiggins (Heroku). 可搬でスケーラブルなクラウドネイティブのサービスを築くための、簡潔で影響力のあるマニフェスト。
- **DORA State of DevOps Report**. DORA / Google Cloud (毎年). 四つの主要なデリバリー指標と、性能を駆動する能力の背後にある継続的な研究プログラム。

## 運用、信頼性、オブザーバビリティ

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). SLI、SLO、エラーバジェット、信頼性をエンジニアリングする規律を定義した基礎的なテキスト。
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). 実践的な例、作業済みのSLO、実装の指針を伴う、実地の相棒。
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. オブザーバビリティ、高カーディナリティのデータ、本番で未知の未知をデバッグすることの現代的な定義。
- **Implementing Service Level Objectives**. Alex Hidalgo. SLOとエラーバジェットを適切に設計し、測定し、使うための、徹底して実践的な手引き。
- **Release It!**. Michael T. Nygard. (アーキテクチャを参照。)本番の安定性パターンと、レジリエントなシステムの運用についてもここで基礎的。
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. 成長するシステムの需要を予測し容量を計画するための、データ駆動のアプローチ。
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. システムのレジリエンスへの信頼を築くために失敗を意図的に注入することの決定的な扱い。
- **Google SRE Book, Chapter on Postmortems**. Google. 責めないポストモーテムとインシデントからの学びの、広く模倣されるモデル。

## 企業、政府、公共の利益

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. オープンソースが実際にどう維持されるか、そして企業が頼る依存関係の背後のメンテナーの負担についての、欠かせない研究。
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. 公共部門の技術がなぜ失敗するか、デリバリーに焦点を当てた改革がどう直せるかについての、冷静な解説。
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. 計画ではなく届けることで公共サービスを変革することについての、英国政府デジタルサービスからの教訓。
- **Project to Product**. Mik Kersten. 大企業をプロジェクトベースの資金から、持続するプロダクトのバリューストリームへと移すフローフレームワーク。
- **Escaping the Build Trap**. Melissa Perri. 組織がアウトプットをアウトカムと取り違える仕方と、プロダクトマネジメントがそれをどう直すか。ポートフォリオとプログラムのガバナンスに直接関連する。
- **U.S. Digital Services Playbook**. U.S. Digital Service. 効果的でユーザー中心の政府のデジタルサービスを届けるための簡潔なプレイ集。
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. 良い公共サービスを築くための、動いて公表された標準で、他の政府に広く模倣されている。
- **NIST SP 800-37: Risk Management Framework**. NIST. 米国連邦システムの運用認可(ATO)と継続的な監視の背後にあるプロセスの枠組み。
- **The FinOps Foundation Framework**. FinOps Foundation. 財務とエンジニアリングにまたがるクラウドコストの可視性、最適化、説明責任の参照モデル。

## このリストの使い方

- **痛みから始める。** デプロイが遅く怖いなら、他の何より先に*Accelerate*、*Continuous Delivery*、*DORA*の報告書を読んでください。
- **スプリントではなく十年のために読む。** 特定のツールのバージョンに結びついたものより、変わらない原則を説明する著作を好みます。
- **標準の現在の版を確認する。** NIST、OWASP、WCAG、ISO、DORAは出版物を改訂します。常に最新のリリースから作業し、自分の方針にバージョンを記してください。
- **共有の棚を築く。** これらの本のうち二、三冊を共通に読んだチームは、語彙と参照点の集合を共有するので、議論が少なく、決定が速くなります。
- 標準と枠組みの参照の完全な索引は**12.5章**を、これらの著作が記述する実践の採用を順序づける方法は**12.6章**を参照してください。
