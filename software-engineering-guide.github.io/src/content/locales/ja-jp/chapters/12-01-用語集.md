# 12.1 用語集

この用語集は、ガイドブック全体で使われる用語と略語を定義します。項目は英語の見出し語のアルファベット順にまとめられています。一般的な略語がある項目では、括弧内に示されます。定義は意図して簡潔にしてあります。より詳しい扱いは、関連する章を参照してください。

## A

**[ABAC(属性ベースのアクセス制御、Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: 固定されたロールではなく、ユーザー、リソース、行動、環境について評価された属性(たとえば部署、機密情報取扱資格、時刻)に基づいてアクセスを認める認可モデル。RBACより複雑になる代わりに、きめ細かく、方針駆動の制御を提供します。

**[アクセシビリティ(a11y、Accessibility)](https://en.wikipedia.org/wiki/Computer_accessibility)**: 障害のある人々がソフトウェアを知覚し、理解し、ナビゲートし、操作できるように設計し構築する実践。「a11y」という数字略語(ヌメロニム)は、「a」と「y」の間の11文字を略したものです。

**ADR(アーキテクチャ決定記録、Architecture Decision Record)**: 一つの重要なアーキテクチャ上あるいは技術上の決定、その文脈、検討した選択肢、帰結を捉える、短くバージョン管理された文書。ADRは、システムがなぜ今の姿なのかについての、持続的でレビュー可能な履歴を作ります。

**集約(Aggregate)**: ドメイン駆動設計で、データの変更について単一の単位として扱われるドメインオブジェクトの集まり。一つのエンティティが不変条件を徹底する集約ルートとして働きます。集約は一貫性とトランザクションの境界を定めます。

**[API(アプリケーションプログラミングインターフェース、Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: あるソフトウェアが別のソフトウェアにサービスやデータを要求するための、定義された契約。よく設計されたAPIは実装の詳細を隠し、安定してバージョン管理されたインターフェースを提供します。

**APIファースト(API-first)**: 実装の前にAPIの契約を設計して合意し、利用者と提供者が共有の仕様に対して並行して作業できるようにする開発アプローチ。

**arc42**: ソフトウェアアーキテクチャを文書化するための、オープンでテンプレートベースの構造。文脈、制約、構成要素、実行時、デプロイ、決定をカバーする12のセクションで構成されます。

**[ARIA(Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: 動的でカスタムのWebコンポーネントが、スクリーンリーダーなどの支援技術に理解されるようにするロール、状態、プロパティを定義するW3Cの仕様。

**ASR(アーキテクチャ上重要な要求、Architecturally Significant Requirement)**: 性能、可用性、セキュリティ、規制上の制約など、アーキテクチャに測定可能で広範囲な影響を持つ要求。ASRは、最も影響の大きい設計上の決定を駆動します。

**ASVS(アプリケーションセキュリティ検証標準、Application Security Verification Standard)**: 安全なアプリケーションを設計し、構築し、検証するための、セキュリティ要件とテストの段階づけられたチェックリストを提供するOWASPの標準。

**[オートスケーリング(Autoscaling)](https://en.wikipedia.org/wiki/Autoscaling)**: 負荷に応じて稼働するコンピュートインスタンスの数(あるいはサイズ)を自動的に調整し、手作業の介入なしに容量が需要に追従するようにすること。意図した容量計画を補いますが、置き換えはしません。

**[可用性(Availability)](https://en.wikipedia.org/wiki/Availability)**: システムが稼働してリクエストに応えられる時間の割合で、しばしば「ナイン」(たとえば99.9%)で表される。SLOとSLAに成文化される中核の信頼性の目標です。

## B

**バックプレッシャー(Backpressure)**: 負荷のかかったコンポーネントが上流の生産者に減速を伝え、際限のないキューと連鎖的な失敗を防ぐフロー制御の仕組み。信頼できるストリーミングとメッセージ駆動のシステムの中心です。

**[BDD(振る舞い駆動開発、Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: 要求を、具体的で人間が読める振る舞いの例(しばしばGiven/When/Thenの形式)として表し、自動の受け入れテストを兼ねさせる協働の実践。

**BFF(Backend for Frontend)**: 特定のフロントエンドあるいはクライアントの種類のために専用のバックエンドサービスを築き、そのクライアントのニーズに合わせてデータの整形と集約を行うアーキテクチャパターン。

**[BI(ビジネスインテリジェンス、Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: レポート、ダッシュボード、意思決定を支えるために、事業データを収集し、統合し、分析するための道具、プロセス、実践。

**責めないポストモーテム(Blameless postmortem)**: 人々は持っていた情報とインセンティブのもとで合理的に行動するという前提に立ち、個人の落ち度ではなく、システム的な原因と学びに焦点を当てるインシデントレビュー。

**[ブルーグリーンデプロイ(Blue-green deployment)](https://en.wikipedia.org/wiki/Blue-green_deployment)**: 二つの同一の本番環境(「ブルー」と「グリーン」)を動かし、一方にトラフィックを流している間にもう一方を更新するリリース戦略。ほぼ即時の切り替えとロールバックを可能にします。

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: 語の出現頻度、逆文書頻度、文書の長さを使って、文書がクエリにどれだけ合うかを採点する、全文検索で広く使われるランキング関数。多くの検索エンジンの語彙的ランキングの既定です。

**境界づけられたコンテキスト(Bounded context)**: ドメイン駆動設計で、特定のドメインモデルとそのユビキタス言語が一貫して適用される、明示的な境界。大きなシステムの異なる部分で概念が混同されるのを防ぎます。

**ビルドキャッシュ(Build cache)**: 以前に計算されたビルドの出力を、それを生んだ入力をキーとして保存したもの。変わっていない作業が再構築されず再利用されます。共有のリモートビルドキャッシュにより、チーム全体とそのCIが互いの結果を再利用できます。

**[バスファクター(Bus factor)](https://en.wikipedia.org/wiki/Bus_factor)**: 不可欠な知識の欠如によりプロジェクトが止まるまでに、失われうる(比喩的に「バスにひかれる」)人数。低いバスファクターは、集中して文書化されていない専門知識と組織的なリスクを示します。

## C

**[キャッシュ追い出しポリシー(Cache eviction policy)](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: キャッシュが満杯のときにどのエントリを取り除くかを決めるために使うルールで、最も長く使われていないもの(LRU)や、最も使用頻度の低いもの(LFU)など。ポリシーはヒット率を、ひいてはキャッシュの価値を左右します。

**[キャッシュの無効化(Cache invalidation)](https://en.wikipedia.org/wiki/Cache_invalidation)**: 元のソースが変わったときに、読み手が古い値を見ないよう、キャッシュされたデータを取り除くあるいは更新する問題。コンピューティングで最も難しい問題の一つとして有名です。

**[キャッシュスタンピード(Cache stampede)](https://en.wikipedia.org/wiki/Cache_stampede)**: 多くのクライアントが同じキーで一度にキャッシュをミスし、すべてが同時にオリジンに到達して圧倒する失敗の様式。リクエストの合体とずらした有効期限で防げます。サンダリングハードとも呼ばれます。

**カナリアリリース(Canary release)**: 新しいバージョンをまずユーザーあるいはトラフィックの小さな部分集合に公開し、問題を監視し、指標が健全なままなら展開を段階的に広げるデプロイ技法。

**[CAP定理(CAP theorem)](https://en.wikipedia.org/wiki/CAP_theorem)**: 分散データストアが、一貫性(Consistency)、可用性(Availability)、分断耐性(Partition tolerance)のうち同時に保証できるのは最大で二つだという原則。分断は避けられないので、設計者は事実上、分断の間に一貫性と可用性をトレードオフします。

**[C4モデル(C4 model)](https://en.wikipedia.org/wiki/C4_model)**: システムコンテキスト、コンテナ、コンポーネント、コードの4つの抽象度でソフトウェアアーキテクチャを可視化する、軽量なアプローチ。

**[CD(継続的デリバリー/継続的デプロイ、Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: 継続的デリバリーは、ソフトウェアをリリース可能な状態に保ち、手作業の承認でいつでもデプロイできるようにする。継続的デプロイは、パイプラインを通過したすべての変更を自動的にリリースします。

**[CDN(コンテンツデリバリーネットワーク、Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: ユーザーの近くでコンテンツをキャッシュして配信する、地理的に分散したエッジサーバーのネットワーク。レイテンシを削り、オリジンのインフラストラクチャの負荷を肩代わりします。

**思考の連鎖プロンプト(Chain-of-thought prompting)**: 言語モデルに最終的な答えの前に中間の推論ステップをたどらせるプロンプト技法。出力が長く遅くなる代わりに、多段階の問題での性能が上がります。

**[CI(継続的インテグレーション、Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: 開発者の変更を共有のメインラインに頻繁にマージし、各マージを自動のビルドとテストスイートで検証して、統合の問題を早期に見つける実践。

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: ソフトウェアのビルド、テスト、リリースを自動化する、継続的インテグレーションと継続的デリバリー/デプロイを組み合わせたパイプライン。

**CMMC(サイバーセキュリティ成熟度モデル認証、Cybersecurity Maturity Model Certification)**: 連邦契約情報と管理対象非機密情報を扱う請負業者のサイバーセキュリティ成熟度を認証する、米国国防総省のプログラム。

**[凝集度(Cohesion)](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: モジュール内の要素がどれだけ一緒にあるべきもので、単一の明確に定義された目的に仕えているかの度合い。低い結合度と組み合わさった高い凝集度は、保守しやすい設計の特徴です。

**コンテキストウィンドウ(Context window)**: 言語モデルが一度に考慮できる、入力と出力にまたがるテキストの最大量で、トークンで測られる。プロンプトとコンテキストの設計が意図して管理しなければならない、乏しい予算です。

**[コンウェイの法則(Conway's Law)](https://en.wikipedia.org/wiki/Conway's_law)**: システムの構造は、それを築く組織のコミュニケーション構造を映す傾向があるという観察。「逆コンウェイ戦略」は、望むアーキテクチャを生むために意図してチームを形づくります。

**Core Web Vitals**: 読み込み、インタラクティブ性、視覚的な安定性を測る、Googleが定義したユーザー中心のWebパフォーマンス指標の集合(Largest Contentful Paint、Interaction to Next Paint、Cumulative Layout Shiftなど)。

**[遅延コスト(Cost of delay)](https://en.wikipedia.org/wiki/Cost_of_delay)**: まだ何かが終わっていないことの経済的なコストで、単位時間あたりに失われる価値として表される。明示することで優先順位づけが意見から算術に変わり、重みづけ最短ジョブ優先などの順序づけのルールを支えます。

**[結合度(Coupling)](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: モジュールあるいはサービス間の相互依存の度合い。疎結合は変更の波及を限定し、良いアーキテクチャの中心的な目標です。

**CQRS(コマンドクエリ責務分離、Command Query Responsibility Segregation)**: 状態を変えるために使うモデル(コマンド)と、状態を読むために使うモデル(クエリ)を分け、それぞれを独立に最適化しスケールできるようにするパターン。

**[CVE(共通脆弱性識別子、Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: 公開されたセキュリティ脆弱性の公開カタログ。それぞれに一意の識別子が割り当てられ、ツールとチームが同じ欠陥を曖昧さなく参照できます。

**CWV**: Core Web Vitalsを参照。

## D

**[DAST(動的アプリケーションセキュリティテスト、Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: ソースコードにアクセスせず、稼働中のアプリケーションを外から調べて、実行時に現れる脆弱性を見つけるセキュリティテスト。

**データインク比(Data-ink ratio)**: エドワード・タフティによる、チャートはインクの大半をデータそのものに使い、装飾にはほとんど使うべきでなく、情報を与えない罫線、枠、チャートジャンクを取り除くべきだという原則。

**[データメッシュ(Data mesh)](https://en.wikipedia.org/wiki/Data_mesh)**: データをドメインチームが所有するプロダクトとして扱い、セルフサービスのプラットフォームインフラストラクチャと連合型のガバナンスに支えられる、分散型のデータアーキテクチャと運用モデル。

**[データ可視化(Data visualisation)](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: データを視覚的な形(位置、長さ、色など)で符号化し、パターン、比較、傾向が知覚でき、決定がより情報に基づくようにする実践。

**[DDD(ドメイン駆動設計、Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: モデルを事業ドメインを中心に据え、共有のユビキタス言語、境界づけられたコンテキスト、エンティティ、値オブジェクト、集約などの構成要素を使うソフトウェア設計のアプローチ。

**デザイントークン(Design tokens)**: 設計上の決定を符号化した、名前付きでプラットフォームに依存しない値(色、間隔、タイポグラフィなど)。デザインシステムと複数のプロダクトにわたって一貫して共有できます。

**DevEx / DevX(開発者体験、Developer Experience)**: 摩擦、フィードバックの速さ、認知負荷を含む、開発者の日々のツール、プラットフォーム、プロセスとのやりとりの全体的な質。

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: ソフトウェア開発と運用を結びつけ、デリバリーのサイクルを短くし、デプロイ頻度を上げ、自動化と共有の所有を通じて信頼性を改善する文化と実践の集合。

**DORA(DevOps Research and Assessment)**: ソフトウェアデリバリーの性能をベンチマークするために使われる、研究プログラムと、その広く使われる四つのデリバリー指標(デプロイ頻度、変更のリードタイム、変更失敗率、サービス復旧までの時間)。

**DPIA(データ保護影響評価、Data Protection Impact Assessment)**: GDPRのもとで高リスクの処理に義務づけられ、プロジェクトを進める前にプライバシーのリスクを特定して緩和する、構造化された評価。

**ドリフト(構成、Drift)**: システムの実際の状態が、宣言された、あるいは意図された状態から徐々にずれること。多くは手作業の変更が原因で、インフラストラクチャ・アズ・コードとGitOpsはそれを検知して是正することを目指します。

**ドリフト(モデル、Drift)**: 機械学習で、入力データの統計的性質(データドリフト)あるいはモデル化している関係(コンセプトドリフト)が変わるにつれて、時間とともにモデルの性能が劣化すること。

**[DR(災害復旧、Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: 大きな破壊的出来事の後にサービスとデータを復元するための戦略、手順、インフラストラクチャで、通常はRTOとRPOの目標に支配されます。

**[DRY(Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: あらゆる知識は単一の権威ある表現を持つべきだとする設計原則。重複と、一貫しない更新のリスクを減らします。

## E

**東西トラフィック(East-west traffic)**: システムやデータセンターの内部のサービス間のネットワークトラフィック。システムと外部クライアントの間の南北トラフィックの対です。サービスメッシュは通常、東西トラフィックを統治します。

**[エッジコンピューティング(Edge computing)](https://en.wikipedia.org/wiki/Edge_computing)**: レイテンシと帯域を削るため、中央の場所ではなく、データが生成あるいは消費される場所の近くで計算とストレージを実行すること。コンテンツデリバリーネットワークは、初期で広く普及した形です。

**[弾力性(Elasticity)](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: 変化する需要に応じて資源を自動的に獲得し解放し、容量が負荷に密接に追従するシステムの能力。

**[ELT(Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: 生のデータを先にターゲットのストアにロードし、そこで変換して、現代のウェアハウスとレイクハウスの規模を活かすデータ統合パターン。

**[エンベディング(Embedding)](https://en.wikipedia.org/wiki/Word_embedding)**: テキスト、画像、その他のデータを、似たものが近くに位置するように配置された密な数値ベクトルとして表したもの。エンベディングは、セマンティック検索とベクトル検索、検索拡張生成を支えます。

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: ICT製品とサービスのアクセシビリティ要件を規定する欧州標準。EU全体の公共部門の調達で参照され、WCAGに沿っています。

**エラーバジェット(Error budget)**: ある期間にSLOが許す、許容される不信頼性の量。使い果たされると、チームは新機能より信頼性の仕事を優先します。速度と安定性の緊張を調停します。

**[ETL(Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: ソースからデータを抽出し、ターゲットの形に変換し、ウェアハウスなどの宛先にロードするデータ統合パターン。

**[EU AI法(EU AI Act)](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: AIシステムをリスクで分類してそれに応じた義務を課し、ある種の用途を禁止し、高リスクのシステムを強く規制する欧州連合の規制。

**[結果整合性(Eventual consistency)](https://en.wikipedia.org/wiki/Eventual_consistency)**: レプリカが一時的に乖離しうるが、更新の伝播が止まれば同じ状態に収束する、分散システムの一貫性モデル。

## F

**[フィーチャーフラグ/フィーチャートグル(Feature flag / feature toggle)](https://en.wikipedia.org/wiki/Feature_toggle)**: 再デプロイなしに、実行時に機能を有効あるいは無効にする仕組み。段階的な展開、実験、運用上の制御に使われます。

**フィーチャーストア(Feature store)**: 選り抜きの機械学習の特徴量を、学習と推論の両方で一貫して定義し、保存し、提供する集中化されたシステム。重複と学習/提供のずれを減らします。

**[FedRAMP(連邦リスク認可管理プログラム、Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: 連邦機関が使うクラウドサービスのセキュリティ評価、認可、継続的な監視を標準化する米国政府のプログラム。

**少数例プロンプト(Few-shot prompting)**: 望むタスクと出力形式を示すため、プロンプトに少数の作業済みの例を与えること。例なしで指示を与えるゼロショットプロンプトの対です。

**FinOps**: 変動するクラウド支出に財務上の説明責任を持ち込み、エンジニアリング、財務、事業のチームがコストと価値を共有して所有する、規律と文化的な実践。

**[FISMA(連邦情報セキュリティ近代化法、Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: 連邦機関に情報セキュリティプログラムの実装、文書化、監視を求める米国の法律で、おもにNISTの指針を通じて運用化されます。

**フロー効率(Flow efficiency)**: 作業項目が待つのではなく、積極的に作業されて過ごす、合計のリードタイムの割合。付加価値時間を合計のリードタイムで割って計算されます。ほとんどのシステムは驚くほど低く、しばしば15パーセント未満です。

**四つの目の原則(Four-eyes principle)**: 重要な行動を、少なくとも二人がレビューあるいは承認することを求め、誤りや不正の可能性を減らす統制。

**[ファズテスト(ファジング、Fuzz testing)](https://en.wikipedia.org/wiki/Fuzzing)**: 不正な、ランダムな、あるいは予期しない入力をプログラムに与え、クラッシュ、セキュリティ上の欠陥、エッジケースの欠陥を明らかにする自動テストの技法。

## G

**[GDPR(一般データ保護規則、General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: 個人データの処理を統治し、個人に権利を与え、管理者と処理者に義務を課し、違反に重大な罰則がある欧州連合の規則。

**GitOps**: 宣言的なインフラストラクチャとアプリケーションの唯一の真実の源としてGitを使い、自動化が稼働中のシステムをコミットされた状態に継続的に突き合わせる運用モデル。

**ゴールデンパス/舗装された道(Golden path / paved road)**: 組織内でソフトウェアを築き出荷するための、よく支えられ意見のはっきりした既定の方法で、安全でコンプライアンスに適い信頼できる選択を最も容易にするよう設計されています。

**ゴールデンレコード(Golden record)**: マスターデータ管理で、マッチングと存続のルールを通じて複数のソースシステムから組み立てられた、事業の実体(たとえば顧客)の、単一で突き合わされた権威あるバージョン。

**[段階的型付け(Gradual typing)](https://en.wikipedia.org/wiki/Gradual_typing)**: 静的型付けと動的型付けを一つのコードベースで共存させ、動的に型付けされたプログラムに型を段階的に加えられるようにする型システムのアプローチ。型ヒントと任意の型チェッカーが一般的な例です。

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: 強く型付けされたスキーマを使い、クライアントが必要なデータを正確に一回の呼び出しで要求できるようにする、API向けのクエリ言語とランタイム。

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: HTTP/2と、通常はProtocol Buffersを使い、効率的なサービス間通信を行う、高性能で契約ファーストのリモートプロシージャコールフレームワーク。

## H

**ハーメティックビルド(Hermetic build)**: 明示的に宣言された入力にだけ依存し、ホスト環境から隔離されているので、どこでも同じ出力を生むビルド。ハーメティック性は、再現可能なビルドと信頼できるキャッシュの基礎です。

**[HSM(ハードウェアセキュリティモジュール、Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: 暗号鍵を生成し、保存し、使う、改ざん耐性のあるハードウェアデバイスで、ソフトウェアだけのアプローチより強い鍵の保護を提供します。

**[HIPAA(医療保険の相互運用性と説明責任に関する法律、Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: 保護対象保健情報(PHI)の保護の要件を定め、その使用と開示を統治する、数ある内容の中で米国の法律。

**水平スケーリング(Horizontal scaling)**: 単一のノードをより強力にするのではなく、インスタンスあるいはノードを加えて(「スケールアウト」)容量を増やすこと。大規模でレジリエントなアーキテクチャのほとんどを支えます。

## I

**[IaC(インフラストラクチャ・アズ・コード、Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: 手作業のプロセスではなく、機械可読でバージョン管理された設定を通じてインフラストラクチャを定義しプロビジョニングし、繰り返し可能性とレビューを可能にする実践。

**[IAM(アイデンティティとアクセスの管理、Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: 適切なアイデンティティが、適切な時に、適切なリソースへの適切なアクセスを持つことを保証する、方針と技術の枠組み。

**IDP / IdP**: 「IDP」は一般に内部開発者プラットフォーム(Internal Developer Platform)、つまりプロダクトチームのためにインフラストラクチャを抽象化するセルフサービスのツール層を指す。「IdP」はアイデンティティプロバイダー(Identity Provider)、つまりユーザーを認証してアサーションを発行するサービスを指す。文脈が二つを区別します。

**[冪等性(Idempotency)](https://en.wikipedia.org/wiki/Idempotence)**: 操作を複数回行っても一回行ったのと同じ効果を持つ性質で、分散システムとAPIでの安全な再試行に欠かせません。

**[i18n(国際化、Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: エンジニアリングの変更なしに、異なる言語、地域、文化的な慣習に適応できるようにソフトウェアを設計し構築すること。この数字略語は、「i」と「n」の間の18文字を略したものです。

**不変の成果物(Immutable artefact)**: 一度生成されバージョン管理されたら決して変更されないビルドの出力。どんな変更も新しいバージョンを生みます。不変性によりリリースが再現可能になり、一度築いて同じ成果物を環境にわたって昇格させられます。

**InnerSource**: オープンソース開発の実践(透明性、共有リポジトリ、チーム間の貢献)を、単一の組織の中に適用すること。

**IaCドリフト(IaC drift)**: ドリフト(構成)を参照。

**[転置インデックス(Inverted index)](https://en.wikipedia.org/wiki/Inverted_index)**: 検索エンジンの中核のデータ構造で、各語を、それを含む文書の一覧に対応づけ、すべての文書を走査せずにクエリに答えられるようにします。

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: 情報セキュリティマネジメントシステム(ISMS)の要件を規定し、情報セキュリティのリスクを管理するための認証可能な枠組みを提供する国際標準。

**ISO/IEC 42001**: AIマネジメントシステムの要件を規定し、AIの開発と利用を責任を持って統治するための認証可能な枠組みを組織に与える国際標準。

## J

**[JWT(JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: 当事者間でクレームを伝えるために使われる、コンパクトで署名された(任意で暗号化された)トークン形式で、WebとAPIのシステムでの認証と認可に一般的に使われます。

## K

**[かんばん(Kanban)](https://en.wikipedia.org/wiki/Kanban_(development))**: 作業をボード上で可視化し、仕掛かりの仕事を制限し、スループットと予測可能性を改善するためにフローを管理するリーンのワークフロー手法。

**[KISS(Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: 不要な複雑さはコストとリスクを増やすという理由で、必要を満たす最も単純な解決策を好む設計原則。

**KMS(鍵管理サービス、Key Management Service)**: 暗号鍵を作成し、保存し、ローテーションし、アクセスを制御するシステムで、しばしばハードウェアセキュリティモジュールに支えられます。

**[KPI(重要業績評価指標、Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: 特定の事業あるいは運用上の目標に向かう進捗を追跡するために使う、定量化可能な尺度。

## L

**レイクハウス(Lakehouse)**: データレイクの低コストで柔軟なストレージと、データウェアハウスの管理、トランザクション、性能の機能を組み合わせたデータアーキテクチャ。

**[リードタイム(Lead time)](https://en.wikipedia.org/wiki/Lead_time)**: 変更が要求された(あるいはコミットされた)時から、本番に届けられるまでの経過時間。DORAの中核のデリバリー指標です。

**[最小権限(Least privilege)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: 各ユーザー、プロセス、システムに、その機能を果たすのに必要な最小限のアクセスだけを与え、侵害や誤りによる損害を限定するセキュリティ原則。

**[リトルの法則(Little's Law)](https://en.wikipedia.org/wiki/Little's_law)**: 待ち行列理論の結果で、安定したシステム内の項目の平均数は、平均到着率に、各項目がシステム内で過ごす平均時間を掛けたものに等しいというもの。仕掛かりの仕事、スループット、リードタイムを結びつけます。

**[LLM(大規模言語モデル、Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: 非常に大きなテキストコーパスで学習し、言語を予測し生成する機械学習モデルで、要約、翻訳、コード生成などのタスクができます。

**[l10n(ローカライゼーション、Localisation)](https://en.wikipedia.org/wiki/Language_localisation)**: 国際化されたソフトウェアを、翻訳、書式、文化的な慣習を含め、特定のロケールに適応させること。この数字略語は、「l」と「n」の間の10文字を略したものです。

## M

**[MDM(マスターデータ管理、Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: システムにわたって、中核の事業の実体(顧客や製品など)の、単一で権威があり一貫した視点を作り維持するための規律とツール。

**MITRE ATT&CK**: 現実世界の敵対者の戦術と技法の、選り抜きの公開知識ベースで、レッドチームの演習の計画、検知エンジニアリングの指針、共有の語彙での脅威の記述に広く使われます。

**平均復旧時間(Mean Time to Recovery、MTTR)**: 失敗の後にサービスを復旧するのにかかる平均時間。一般的な信頼性とインシデント管理の指標です。

**[モブプログラミング(Mob programming)](https://en.wikipedia.org/wiki/Mob_programming)**: チーム全体が同じタスクに同じコンピュータで一緒に取り組み、誰がタイプするかを交代して、知識を共有し集合的に決定を行う実践。

**[MLOps(機械学習オペレーション、Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: DevOpsの原則をMLのライフサイクルに広げ、機械学習モデルを本番で確実かつ効率的にデプロイし、監視し、保守する実践の集合。

**[モノレポ(Monorepo)](https://en.wikipedia.org/wiki/Monorepo)**: 多くのプロジェクト、あるいは組織全体のコードを保持する単一のバージョン管理リポジトリ。共有のツールとプロジェクト間のアトミックな変更を可能にする代わりに、専門的なスケーリングのツールが必要になります。

**mTLS(相互TLS、mutual TLS)**: 双方が証明書を提示して検証し、互いを認証するTransport Layer Securityの構成。サービスメッシュとゼロトラストネットワークでのサービス間トラフィックの既定です。[相互認証](https://en.wikipedia.org/wiki/Mutual_authentication)も参照。

**[ミューテーションテスト(Mutation testing)](https://en.wikipedia.org/wiki/Mutation_testing)**: コードに小さな欠陥(「ミュータント」)を意図して入れ、テストスイートがそれらを検知するかを確認して、スイートの本当の有効性を測る技法。

## N

**[NDCG(正規化割引累積利得、Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: 関連性の高い結果を結果リストの上位に置くことに報いる、順位づけの質の指標で、スコアがクエリ間で比較可能になるよう正規化されています。検索の関連性の評価の定番です。

**[NIST(米国国立標準技術研究所、National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: サイバーセキュリティ、プライバシー、AIの広く参照される標準である特別刊行物と枠組みを出す米国連邦機関。

**NIST AI RMF(AIリスク管理フレームワーク、AI Risk Management Framework)**: ガバナンス(Govern)、対応づけ(Map)、測定(Measure)、管理(Manage)の機能を軸に、ライフサイクルにわたってAIシステムに関連するリスクを特定し、評価し、管理するための、NISTの任意の枠組み。

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: 連邦情報システムのセキュリティとプライバシーの統制のNISTのカタログで、政府をはるかに超えて基準線として広く使われます。

**NIST SP 800-171**: 連邦以外のシステムにおける管理対象非機密情報(CUI)の保護の要件を規定するNISTの刊行物で、防衛請負業者のコンプライアンスの中心です。

**[NFR(非機能要求、Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: システムがどのような機能を果たすかではなく、どう振る舞うべきか(性能、セキュリティ、信頼性、使いやすさなどの質)を記述する要求。

**南北トラフィック(North-south traffic)**: システムと外部クライアントの間(データセンターやクラスターの出入り)のネットワークトラフィック。内部サービス間の東西トラフィックの対です。APIゲートウェイは通常、南北トラフィックを統治します。

## O

**オブザーバビリティ(Observability)**: システムの内部状態を、その外部への出力から推測できる度合い。通常はテレメトリ、つまりメトリクス、ログ、トレースを通じて達成されます。

**[OKR(目標と主要な成果、Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: 定性的な目標に、いくつかの測定可能な主要な成果を組み合わせて、組織を揃えて集中させる目標設定の枠組み。

**OpenTelemetry (OTel)**: ソフトウェアからテレメトリのデータ(トレース、メトリクス、ログ)を生成し、収集し、エクスポートするための、ベンダー中立でオープンな標準とツールセット。

**OPA(Open Policy Agent)**: (Rego言語で書かれた)ポリシーを評価して、スタック全体で認可と構成のルールを徹底し、ポリシー・アズ・コードを可能にする、オープンソースの汎用ポリシーエンジン。

**OSPO(オープンソースプログラムオフィス、Open Source Program Office)**: オープンソースの戦略、ガバナンス、コンプライアンス、コミュニティとの関与を調整し、利用と貢献の両方を管理する組織の機能。

**[OWASP(Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: OWASP Top TenやASVSを含む、広く使われ自由に入手できるアプリケーションセキュリティの資源を作る非営利のコミュニティ。

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: CAP定理の拡張で、分断(Partition)があるなら、システムは可用性(Availability)と一貫性(Consistency)をトレードオフし、そうでなければ(通常の運用では、Else)レイテンシ(Latency)と一貫性(Consistency)をトレードオフするというもの。

**[PCI DSS(ペイメントカード業界データセキュリティ基準、Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: カード会員データを保存し、処理し、送信する組織の要件を規定する、ペイメントカード業界が維持するセキュリティ標準。

**[ペネトレーションテスト(Penetration testing)](https://en.wikipedia.org/wiki/Penetration_test)**: 熟練したテスターによる、システムへの認可された模擬攻撃で、本物の攻撃者より先に悪用可能な脆弱性を見つけて示し、優先順位づけされた行動可能な指摘として届けられます。

**[PII(個人を特定できる情報、Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: 単独で、あるいは他のデータと組み合わせて、特定の個人を識別できる情報。その扱いはプライバシー法と内部方針に統治されます。

**プラットフォームエンジニアリング(Platform engineering)**: 認知負荷を減らしプロダクトチームを加速させる、内部のセルフサービスのプラットフォームとゴールデンパスを築き運用する規律。

**POUR**: Web Content Accessibility Guidelinesの四つの導きの原則で、コンテンツは知覚可能(Perceivable)、操作可能(Operable)、理解可能(Understandable)、堅牢(Robust)でなければならない。

**本番準備レビュー(Production readiness review)**: サービスが稼働する前、あるいはオンコールの所有を引き受ける前に行われ、オブザーバビリティ、信頼性、セキュリティ、ランブック、運用サポートの標準を満たしていることを確認する構造化されたチェック。

**[プロンプトエンジニアリング(Prompt engineering)](https://en.wikipedia.org/wiki/Prompt_engineering)**: 信頼できる高品質の出力を得るために、言語モデルに与える指示、文脈、例を設計し洗練する実践で、試行錯誤ではなく、バージョン管理されテストされるエンジニアリングの規律として扱われます。

**[プロンプトインジェクション(Prompt injection)](https://en.wikipedia.org/wiki/Prompt_injection)**: 巧妙に作られた入力により、言語モデルが意図された指示を無視して攻撃者の指示に従う攻撃で、インジェクションの欠陥のAI時代の類似物。LLMアプリケーションの中心的なセキュリティリスクです。

**プロパティベーステスト(Property-based testing)**: 手で選んだ例だけに頼らず、自動生成された多くの入力にわたって、述べられた性質が成り立つことを確認するテスト技法。

**プルリクエスト(PR)/マージリクエスト(MR)**: 共有のブランチにマージされる前に、レビューと議論のために提出される、提案された変更の集合。ほとんどのワークフローでコードレビューの主要な単位です。

**パープルチーム(Purple team)**: 攻撃側(レッド)と防御側(ブルー)のセキュリティチームがリアルタイムで協力し、攻撃とそれを捉えるための検知を互いに対して調整する協働の演習。

## Q

**品質ゲート(Quality gate)**: 変更が先に進む前に通過しなければならない(たとえばカバレッジ、セキュリティ、性能の閾値を満たすなど)パイプラインの自動チェックポイント。

**[クォーラム(Quorum)](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: 分散システムで、操作(読み取りや書き込みなど)が成功と見なされるために合意しなければならないノードの最小数。失敗があっても一貫性を保つために使われます。

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: タスクあるいは決定の各参加者を、実行責任者(Responsible)、説明責任者(Accountable)、協議先(Consulted)、報告先(Informed)として示す責任割り当てのモデル。

**[RAG(検索拡張生成、Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: 関連する文書やデータを先に検索し、文脈として与えることで言語モデルの出力を裏づけ、正確さを高めハルシネーションを減らす技法。

**[RBAC(ロールベースのアクセス制御、Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: 権限をロールに、ロールをユーザーに割り当て、ロールの水準でアクセスを管理して運用を単純にする認可モデル。

**[レッドチーム(Red team)](https://en.wikipedia.org/wiki/Red_team)**: 脆弱性を列挙するだけでなく、検知と対応をテストするために、しばしば防御側に警告せず、組織全体に対して現実的な敵対者を模倣するグループ。ブルー(防御)チームの対です。

**[参照データ(Reference data)](https://en.wikipedia.org/wiki/Reference_data)**: 国コード、通貨、ステータス値など、他のデータを分類するために使われる、管理されゆっくり変わるコード一覧と分類。共有されバージョン管理された語彙として統治することで、システムの一貫性を保ちます。

**Rego**: Open Policy Agentが、認可と構成の決定のルールを表現するために使う宣言型のポリシー言語。

**[REST(Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: アドレス指定可能なリソースへのHTTP上のステートレスな操作を使う、ネットワークアプリケーションのアーキテクチャスタイル。単純さと広いツールが評価されています。

**[リバースプロキシ(Reverse proxy)](https://en.wikipedia.org/wiki/Reverse_proxy)**: 一つ以上のバックエンドサービスの前に立ち、クライアントのリクエストをそれらに転送するサーバーで、一般にTLS終端、負荷分散、キャッシュ、単一の入口を提供します。

**[RFC(コメント募集、Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: 重要な技術上の決定や変更の前に、フィードバックのために回覧される文書化された提案で、透明性と共有の所有を促します。(この用語は、インターネット標準の文書シリーズの名前でもあります。)

**[ROI(投資対効果、Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: 投資から得られる価値をそのコストに対して測る尺度で、エンジニアリングと技術の決定を正当化し優先順位づけするために使われます。

**[RPA(ロボティックプロセスオートメーション、Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: 人がするように既存のユーザーインターフェースとシステムとやりとりして、反復的でルールベースのタスクを自動化するソフトウェアの「ロボット」。

**RPO(目標復旧時点、Recovery Point Objective)**: 時間で測った、許容できるデータ損失の最大量(たとえば「最大5分」)で、データをどれだけ頻繁に保護しなければならないかを定義します。

**RTO(目標復旧時間、Recovery Time Objective)**: 中断の後にサービスを復旧するのに許容できる最大の期間で、災害復旧の設計と投資の指針になります。

## S

**サガ(Saga)**: ローカルトランザクションを順序づけ、ステップが失敗したときに補償の行動を発行することで、分散トランザクションでサービス間のデータの一貫性を管理するパターン。

**[SAFe(Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: 多くのチームを調整しながら、大企業全体にアジャイルとリーンの実践を適用する枠組み。構造が評価される一方、重くなりうると批判もされます。

**[SAST(静的アプリケーションセキュリティテスト、Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: ソースコード、バイトコード、バイナリを実行せずに分析して、開発の早期に脆弱性を見つけるセキュリティテスト。

**SBOM(ソフトウェア部品表、Software Bill of Materials)**: ソフトウェアの構成要素と依存関係の、正式で機械可読な目録で、サプライチェーンと脆弱性のリスクを管理するために使われます。

**SCA(ソフトウェア構成分析、Software Composition Analysis)**: コードベース内のオープンソースとサードパーティのコンポーネントを特定し、既知の脆弱性とライセンスのリスクに旗を立てるツール。

**[スクラム(Scrum)](https://en.wikipedia.org/wiki/Scrum_(software_development))**: 作業を固定長のイテレーション(スプリント)に整理し、定義された役割、イベント、成果物で価値の増分を届けるアジャイルの枠組み。

**[セクション508(Section 508)](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: 連邦機関に、電子・情報技術を障害のある人々がアクセスできるようにすることを求める米国の法律で、実際にはWCAGに沿っています。

**セマンティック検索(Semantic search)**: 正確なキーワードではなく意味で照合する検索で、通常はクエリと文書のエンベディングを比較します。しばしばハイブリッドのアプローチで語彙検索と組み合わされます。

**[サービスメッシュ(Service mesh)](https://en.wikipedia.org/wiki/Service_mesh)**: 通常サイドカープロキシで実装され、相互TLS、再試行、タイムアウト、トラフィックの切り替え、オブザーバビリティなどのサービス間通信の関心事を扱い、アプリケーションコードの外に置く専用のインフラストラクチャ層。

**サイドカー(Sidecar)**: アプリケーション自体を変えずに(サービスメッシュのプロキシなどの)補助的な能力を提供するため、主たるアプリケーションのインスタンスと並べてデプロイされる補助的なプロセスあるいはコンテナ。

**[SIEM(セキュリティ情報イベント管理、Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: 環境全体のセキュリティログとイベントを集約し相関づけて、検知、アラート、調査を可能にするシステム。

**[SLA(サービスレベル合意、Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: サービス提供者とその顧客の間の、期待されるサービスレベルと、それを満たさなかった場合の帰結を規定する正式な約束。

**SLI(サービスレベル指標、Service Level Indicator)**: リクエストのレイテンシやエラー率など、サービス品質の側面の定量的な尺度で、SLOに供給されます。

**SLO(サービスレベル目標、Service Level Objective)**: 望む信頼性の水準を定義するSLIの目標値あるいは範囲で、エラーバジェットの基礎になります。

**SLSA(Supply-chain Levels for Software Artifacts)**: ビルドとリリースのプロセスを通じて、ソフトウェア成果物の完全性と出所を改善するための、段階的なセキュリティ要件の枠組み。

**SOAR(セキュリティオーケストレーション、自動化、対応、Security Orchestration, Automation, and Response)**: トリアージや対応のプレイブックなど、セキュリティ運用を自動化し調整して、速度と一貫性を改善するツールと実践。

**SOC 2(System and Organisation Controls 2)**: AICPAのトラストサービス規準に基づき、サービス組織のセキュリティ、可用性、処理の完全性、機密性、プライバシーの統制を評価する、監査の枠組みと報告書。

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: 保守しやすく柔軟なコードを促す、五つのオブジェクト指向設計の原則(単一責任、開放閉鎖、リスコフの置換、インターフェース分離、依存性逆転)。

**[SOX(サーベンス・オクスリー法、Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: 上場企業の財務報告と内部統制の要件を定め、財務データを支えるITシステムにも含意を持つ米国の法律。

**SPACE**: 満足と幸福(Satisfaction and well-being)、性能(Performance)、活動(Activity)、コミュニケーションと協働(Communication and collaboration)、効率とフロー(Efficiency and flow)の五つの次元にわたって、開発者の生産性を測定し、単一指標の尺度を戒める枠組み。

**[SRE(サイトリライアビリティエンジニアリング、Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: ソフトウェアエンジニアリングのアプローチを運用に適用し、SLO、エラーバジェット、自動化を使って、信頼できるシステムを規模で運用する規律。

**SSDF(Secure Software Development Framework)**: 組織の準備、ソフトウェアの保護、十分に保護されたソフトウェアの生産、脆弱性への対応にわたる、高い水準の安全な開発の実践のNISTの枠組み(SP 800-218)。

**[静的解析(Static analysis)](https://en.wikipedia.org/wiki/Static_program_analysis)**: ソースコード、バイトコード、バイナリを実行せずに調べて、欠陥、スタイル違反、セキュリティ上の欠陥を見つけること。通常、エディタとパイプラインに組み込まれたリンター、型チェッカー、専用の解析器を通じて行われます。

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: 脅威を、なりすまし(Spoofing)、改ざん(Tampering)、否認(Repudiation)、情報漏えい(Information disclosure)、サービス拒否(Denial of service)、権限昇格(Elevation of privilege)に分類する脅威モデリングの分類法。

## T

**[TCO(総所有コスト、Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: 最初の価格だけでなく、取得、運用、保守、最終的な廃止を含む、システムあるいは決定の全生涯のコスト。

**[TDD(テスト駆動開発、Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: 設計を駆動しカバレッジを確保するため、短い繰り返しのサイクルで、通るようにするコードの前に失敗する自動テストを書き、それからリファクタリングする実践。

**[技術的負債(Technical debt)](https://en.wikipedia.org/wiki/Technical_debt)**: 時間のかかる、より良い解決策ではなく、手っ取り早い解決策を今選ぶことの、暗黙の将来のコスト。無意識に積み上げるのではなく、意図して管理しなければなりません。

**TF-IDF(語の出現頻度と逆文書頻度、Term Frequency-Inverse Document Frequency)**: 語がその文書にどれだけ頻繁に現れるかで、その語の文書への重要性を採点し、コーパス全体でどれだけ一般的かで相殺する古典的な重みづけの方式。語彙検索のランキングの多くの基礎です。

**[制約理論(Theory of constraints)](https://en.wikipedia.org/wiki/Theory_of_constraints)**: システムのスループットはいつでも単一のボトルネックに制限されるので、改善の努力はその制約が別の場所に移るまで、そこに集中すべきだとする経営のアプローチ。

**[脅威モデリング(Threat modelling)](https://en.wikipedia.org/wiki/Threat_model)**: 防御を早期に設計に組み込めるよう、システムへの潜在的な脅威を特定し、列挙し、優先順位づけする構造化された実践。

**苦役(Toil)**: SREで、サービスとともに線形に増え、持続的な価値を提供しない、手作業で反復的で自動化可能な運用の仕事。減らすことで、エンジニアリングのための容量が空きます。

**トランクベース開発(Trunk-based development)**: 開発者が小さな変更を単一の共有ブランチに頻繁に統合し、長寿命のブランチとマージの痛みを最小化するソース管理の実践。

**[型推論(Type inference)](https://en.wikipedia.org/wiki/Type_inference)**: 式の型を自動的に導く言語機能で、すべての型を手で書き出すことを求めずに、静的型付けの安全性の多くを与えます。

**[型システム(Type system)](https://en.wikipedia.org/wiki/Type_system)**: 言語が型を割り当てて検査するために使うルールの集合で、プログラムが走る前にエラーの種類全体を捉え、意図を文書化します。型システムは動的から静的、弱いから強いまで幅があります。

## U

**ユビキタス言語(Ubiquitous language)**: ドメイン駆動設計で、開発者とドメインの専門家が一貫して使い、コードとモデルに直接反映される、共有で正確な語彙。

**[UAT(ユーザー受け入れテスト、User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: システムがリリースを受け入れられる前に、事業のニーズを満たしていることを確認するため、エンドユーザーあるいはその代表が行うテスト。

**[UX / UI(ユーザー体験/ユーザーインターフェース、User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: ユーザー体験は、人とプロダクトのやりとりの全体的な質。ユーザーインターフェースは、そのやりとりが起こる、具体的な視覚的で対話的な表面。

## V

**[値オブジェクト(Value object)](https://en.wikipedia.org/wiki/Value_object)**: ドメイン駆動設計で、別個のアイデンティティではなく、その属性によって完全に定義される不変のオブジェクト。金額や日付の範囲など。

**[バリューストリームマッピング(Value stream mapping)](https://en.wikipedia.org/wiki/Value-stream_mapping)**: アイデアから届けられた価値までのすべてのステップを描き、付加価値時間と待ち時間を区別して、ボトルネック、引き継ぎ、手戻りのループが見え改善できるようにする技法。

**[ベクトルデータベース(Vector database)](https://en.wikipedia.org/wiki/Vector_database)**: 高次元のエンベディングベクトルを、類似度でインデックス化し検索するために最適化されたデータストアで、セマンティック検索と検索拡張生成の一般的な土台です。

**垂直スケーリング(Vertical scaling)**: 単一のノードをより強力にして(「スケールアップ」)容量を増やすこと。単純だが、結局は利用可能な最大のマシンに限られます。

**[VCS(バージョン管理システム、Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Gitなど、ファイルへの変更を時間とともに記録し、履歴をレビューでき、ブランチを維持でき、作業を調整できるようにするツール。

**[脆弱性スキャン(Vulnerability scanning)](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: システム、コンテナ、コードを、既知の弱点と設定ミスのデータベースに照らして自動で検査すること。広くて安く、手作業のペネトレーションテストの深さを補います。

## W

**[WCAG(Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Webコンテンツをアクセシブルにするための、POURの原則と適合水準A、AA、AAAを軸に整理された、W3Cによる国際的に認められた指針の集合。

**ウォードリーマップ(Wardley map)**: ユーザーへの価値と進化の成熟度で能力を位置づけ、築くか買うかと投資の決定に情報を与える視覚的な戦略技法。

**仕掛かりの仕事(WIP)の制限(Work in progress limit)**: ワークフローのある段階に一度にあってよい項目の数の上限。ボトルネックを露呈させ、並行作業が多すぎることのオーバーヘッドを抑えてフローを改善する、かんばんの中核の実践です。

**WSJF(重みづけ最短ジョブ優先、Weighted Shortest Job First)**: 遅延コストを見積もられた所要期間で割って作業を順序づけ、最も短く、最も時間に敏感で、最も価値の高い項目を先に行う優先順位づけの方法。

## X

**[XSS(クロスサイトスクリプティング、Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: 攻撃者が悪意のあるスクリプトを注入し、他のユーザーのブラウザで実行されて、データを盗んだりセッションを乗っ取ったりしうるWebの脆弱性。

## Y

**[YAGNI(You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: 予期されたニーズはしばしば実現せず、コストと複雑さを加えるという理由で、憶測で機能を築くことを戒める原則。

## Z

**[ゼロトラスト(Zero trust)](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: ネットワークの場所に基づく暗黙の信頼を想定せず、すべてのアクセス要求をアイデンティティ、デバイス、文脈に照らして継続的に検証する、「決して信頼せず、常に検証する」という格言に従うセキュリティモデル。
