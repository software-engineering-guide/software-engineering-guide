# 12.1 용어집

이 용어집은 가이드북 전반에서 쓰는 용어와 약어를 정의합니다. 항목은 영문
알파벳순으로 묶었으며, 표제어는 영어를 유지하고 괄호 안에 한국어 용어를
덧붙였습니다. 항목에 흔한 약어가 있으면 괄호 안에 보입니다. 정의는 의도적으로
간결하게 썼으니, 자세한 설명은 해당 장을 참고하십시오.

## A

**[ABAC (Attribute-Based Access Control, 속성 기반 접근 통제)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: 고정된 역할이 아니라 사용자, 리소스, 행동, 환경의 평가된 속성(예: 부서, 보안 등급, 시간대)에 따라 접근을 허용하는 권한 부여 모델입니다. 세밀한 정책 주도 통제를 제공하지만 RBAC보다 복잡합니다.

**[접근성 (Accessibility, a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: 장애가 있는 사람이 소프트웨어를 인지하고, 이해하고, 탐색하고, 상호작용할 수 있도록 설계하고 만드는 실천입니다. "a11y"는 "a"와 "y" 사이의 11개 글자를 줄인 숫자 약어입니다.

**ADR (Architecture Decision Record, 아키텍처 결정 기록)**: 하나의 중요한 아키텍처 또는 기술 결정, 그 맥락, 검토한 선택지, 결과를 담은 짧고 버전 관리되는 문서입니다. ADR은 시스템이 왜 지금의 모습인지에 대한 지속적이고 검토 가능한 역사를 만듭니다.

**Aggregate (애그리거트)**: 도메인 주도 설계에서 데이터 변경을 위해 하나의 단위로 다루는 도메인 객체의 묶음으로, 불변식을 강제하는 애그리거트 루트 역할을 하는 엔터티가 하나 있습니다. 애그리거트는 일관성과 트랜잭션 경계를 정의합니다.

**[API (Application Programming Interface, 애플리케이션 프로그래밍 인터페이스)](https://en.wikipedia.org/wiki/API)**: 한 소프트웨어가 다른 소프트웨어에 서비스나 데이터를 요청하는 정의된 계약입니다. 잘 설계된 API는 구현 세부 사항을 숨기고 안정적이며 버전이 있는 인터페이스를 제공합니다.

**API-first (API 우선)**: 구현 전에 API 계약을 설계하고 합의해, 소비자와 제공자가 공유된 명세를 두고 병렬로 일할 수 있게 하는 개발 접근입니다.

**arc42**: 소프트웨어 아키텍처를 문서화하는 개방형 템플릿 기반 구조로, 맥락, 제약, 구성 요소, 런타임, 배포, 결정을 다루는 열두 절로 조직됩니다.

**[ARIA (Accessible Rich Internet Applications, 접근 가능한 리치 인터넷 애플리케이션)](https://en.wikipedia.org/wiki/WAI-ARIA)**: 동적이고 맞춤형인 웹 구성 요소를 스크린 리더 같은 보조 기술이 이해할 수 있게 하는 역할, 상태, 속성을 정의한 W3C 명세입니다.

**ASR (Architecturally Significant Requirement, 아키텍처적으로 중요한 요구 사항)**: 성능, 가용성, 보안, 규제 제약처럼 아키텍처에 측정 가능하고 넓은 영향을 미치는 요구 사항입니다. ASR은 가장 중대한 설계 결정을 이끕니다.

**ASVS (Application Security Verification Standard, 애플리케이션 보안 검증 표준)**: 안전한 애플리케이션을 설계, 구축, 검증하기 위한 보안 요구 사항과 테스트의 등급별 체크리스트를 제공하는 OWASP 표준입니다.

**[오토스케일링 (Autoscaling)](https://en.wikipedia.org/wiki/Autoscaling)**: 부하에 따라 실행 중인 컴퓨트 인스턴스의 수(또는 크기)를 자동으로 조정해, 수동 개입 없이 역량이 수요를 따라가게 하는 것입니다. 의도적인 용량 계획을 보완하지만 대체하지는 않습니다.

**[가용성 (Availability)](https://en.wikipedia.org/wiki/Availability)**: 시스템이 동작하고 요청을 처리할 수 있는 시간의 비율로, 흔히 "나인(nines)"(예: 99.9%)으로 표현합니다. SLO와 SLA에 성문화되는 핵심 신뢰성 목표입니다.

## B

**Backpressure (배압)**: 부하를 받는 구성 요소가 상류 생산자에게 속도를 늦추라고 신호해, 무한 대기열과 연쇄 장애를 막는 흐름 제어 메커니즘입니다. 신뢰할 수 있는 스트리밍과 메시지 주도 시스템의 핵심입니다.

**[BDD (Behaviour-Driven Development, 행위 주도 개발)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: 요구 사항을 구체적이고 사람이 읽을 수 있는 행위의 예(흔히 Given/When/Then 형식)로 표현하고, 그것이 자동화된 인수 테스트를 겸하게 하는 협업 실천입니다.

**BFF (Backend for Frontend, 프런트엔드를 위한 백엔드)**: 특정 프런트엔드나 클라이언트 유형을 위한 전용 백엔드 서비스를 만들어, 그 클라이언트의 필요에 맞게 데이터 가공과 집계를 맞추는 아키텍처 패턴입니다.

**[BI (Business Intelligence, 비즈니스 인텔리전스)](https://en.wikipedia.org/wiki/Business_intelligence)**: 보고, 대시보드, 의사 결정을 지원하려고 비즈니스 데이터를 수집하고, 통합하고, 분석하는 도구, 프로세스, 실천입니다.

**Blameless postmortem (비난 없는 사후 검토)**: 사람은 가진 정보와 유인을 고려하면 합리적으로 행동한다는 전제에서, 개인의 잘못이 아니라 체계적 원인과 학습에 초점을 맞추는 인시던트 리뷰입니다.

**[블루-그린 배포 (Blue-green deployment)](https://en.wikipedia.org/wiki/Blue-green_deployment)**: 두 개의 동일한 프로덕션 환경("블루"와 "그린")을 운영하며 한쪽으로 트래픽을 보내는 동안 다른 쪽을 갱신해, 거의 즉각적인 전환과 롤백을 가능하게 하는 릴리스 전략입니다.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: 단어 빈도, 역문서 빈도, 문서 길이를 써서 문서가 질의에 얼마나 잘 맞는지 점수화하는, 전문 검색에 널리 쓰이는 순위 함수입니다. 많은 검색 엔진에서 어휘 순위의 기본값입니다.

**Bounded context (바운디드 컨텍스트)**: 도메인 주도 설계에서 특정 도메인 모델과 그 유비쿼터스 언어가 일관되게 적용되는 명시적 경계입니다. 큰 시스템의 서로 다른 부분에서 개념이 뒤섞이는 것을 막습니다.

**Build cache (빌드 캐시)**: 이전에 계산한 빌드 산출물을 그것을 낳은 입력으로 키를 매겨 저장해, 바뀌지 않은 작업을 다시 빌드하지 않고 재사용하게 하는 저장소입니다. 공유 원격 빌드 캐시는 팀 전체와 CI가 서로의 결과를 재사용하게 합니다.

**[버스 팩터 (Bus factor)](https://en.wikipedia.org/wiki/Bus_factor)**: 필수 지식이 없어 프로젝트가 멈추기 전에 잃어야 하는(비유적으로 "버스에 치이는") 사람의 수입니다. 낮은 버스 팩터는 집중되고 문서화되지 않은 전문성과 조직 위험의 신호입니다.

## C

**[캐시 퇴출 정책 (Cache eviction policy)](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: 캐시가 가득 찼을 때 어느 항목을 제거할지 정하는 규칙으로, 가장 오래 쓰이지 않은 것(LRU)이나 가장 덜 자주 쓰인 것(LFU) 등이 있습니다. 정책이 적중률과 그에 따른 캐시의 가치를 형성합니다.

**[캐시 무효화 (Cache invalidation)](https://en.wikipedia.org/wiki/Cache_invalidation)**: 원천이 바뀌었을 때 캐시된 데이터를 제거하거나 갱신해 독자가 오래된 값을 보지 않게 하는 문제입니다. 컴퓨팅에서 가장 어려운 문제 중 하나로 유명합니다.

**[캐시 스탬피드 (Cache stampede)](https://en.wikipedia.org/wiki/Cache_stampede)**: 많은 클라이언트가 같은 키에 대해 동시에 캐시를 놓치고 모두 원본에 한꺼번에 몰려 압도하는 실패 모드입니다. 요청 병합과 엇갈린 만료가 막아 줍니다. 썬더링 허드라고도 합니다.

**Canary release (카나리 릴리스)**: 새 버전을 먼저 소수의 사용자나 트래픽에 노출하고, 문제를 모니터링한 뒤, 지표가 건강하면 롤아웃을 점진적으로 확장하는 배포 기법입니다.

**[CAP 정리 (CAP theorem)](https://en.wikipedia.org/wiki/CAP_theorem)**: 분산 데이터 저장소가 일관성(Consistency), 가용성(Availability), 분할 허용(Partition tolerance) 중 동시에 최대 둘만 보장할 수 있다는 원리입니다. 분할은 피할 수 없으므로, 설계자는 사실상 분할 중에 일관성과 가용성을 맞바꿉니다.

**[C4 모델 (C4 model)](https://en.wikipedia.org/wiki/C4_model)**: 소프트웨어 아키텍처를 시스템 컨텍스트, 컨테이너, 컴포넌트, 코드의 네 추상화 수준으로 시각화하는 가벼운 접근입니다.

**[CD (Continuous Delivery / Continuous Deployment, 지속적 전달 / 지속적 배포)](https://en.wikipedia.org/wiki/Continuous_delivery)**: 지속적 전달은 소프트웨어를 릴리스 가능한 상태로 유지해 수동 승인으로 언제든 배포할 수 있게 하고, 지속적 배포는 파이프라인을 통과한 모든 변경을 자동으로 릴리스합니다.

**[CDN (Content Delivery Network, 콘텐츠 전송 네트워크)](https://en.wikipedia.org/wiki/Content_delivery_network)**: 콘텐츠를 사용자 가까이에서 캐시하고 제공하는 지리적으로 분산된 에지 서버 네트워크로, 지연을 줄이고 원본 인프라의 부하를 덜어 줍니다.

**Chain-of-thought prompting (사고 사슬 프롬프팅)**: 언어 모델에게 최종 답을 내기 전에 중간 추론 단계를 거치도록 요청해, 더 길고 느린 출력을 대가로 다단계 문제의 성능을 높이는 프롬프팅 기법입니다.

**[CI (Continuous Integration, 지속적 통합)](https://en.wikipedia.org/wiki/Continuous_integration)**: 개발자의 변경을 공유 메인라인에 자주 병합하고, 각 병합을 자동화된 빌드와 테스트 스위트로 검증해 통합 문제를 일찍 탐지하는 실천입니다.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: 소프트웨어 빌드, 테스트, 릴리스를 자동화하는 지속적 통합과 지속적 전달/배포의 결합된 파이프라인입니다.

**CMMC (Cybersecurity Maturity Model Certification, 사이버보안 성숙도 모델 인증)**: 연방 계약 정보와 비기밀 통제 정보를 다루는 계약자의 사이버보안 성숙도를 인증하는 미국 국방부 프로그램입니다.

**[응집도 (Cohesion)](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: 모듈 안의 요소들이 얼마나 함께 속하고 하나의 잘 정의된 목적을 섬기는가의 정도입니다. 낮은 결합도와 짝을 이룬 높은 응집도는 유지 가능한 설계의 특징입니다.

**Context window (컨텍스트 윈도우)**: 언어 모델이 입력과 출력에 걸쳐 한꺼번에 고려할 수 있는 텍스트의 최대량으로, 토큰으로 측정합니다. 프롬프트와 컨텍스트 설계가 의도적으로 관리해야 하는 희소한 예산입니다.

**[콘웨이의 법칙 (Conway's Law)](https://en.wikipedia.org/wiki/Conway's_law)**: 시스템의 구조가 그것을 만드는 조직의 커뮤니케이션 구조를 반영하는 경향이 있다는 관찰입니다. "역 콘웨이 기동"은 원하는 아키텍처를 만들도록 팀을 의도적으로 형성합니다.

**Core Web Vitals (핵심 웹 지표)**: 로딩, 상호작용성, 시각적 안정성을 측정하는, 구글이 정의한 사용자 중심 웹 성능 지표 집합입니다(최대 콘텐츠 렌더링 시간, 다음 페인트까지의 상호작용, 누적 레이아웃 이동 등).

**[지연의 비용 (Cost of delay)](https://en.wikipedia.org/wiki/Cost_of_delay)**: 아직 끝나지 않은 것의 경제적 비용으로, 단위 시간당 잃는 가치로 표현합니다. 명시하면 우선순위가 의견에서 산수로 바뀌며, 가중 최단 작업 우선 같은 순서 규칙의 바탕이 됩니다.

**[결합도 (Coupling)](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: 모듈이나 서비스 사이의 상호 의존 정도입니다. 느슨한 결합은 변경의 파급을 제한하며 좋은 아키텍처의 중심 목표입니다.

**CQRS (Command Query Responsibility Segregation, 명령 조회 책임 분리)**: 상태를 바꾸는 모델(명령)과 상태를 읽는 모델(조회)을 분리해, 각각을 독립적으로 최적화하고 확장하게 하는 패턴입니다.

**[CVE (Common Vulnerabilities and Exposures, 공통 취약점 및 노출)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: 공개된 보안 취약점의 공개 카탈로그로, 각각에 고유 식별자가 부여되어 도구와 팀이 같은 결함을 모호하지 않게 참조할 수 있습니다.

**CWV**: Core Web Vitals를 보십시오.

## D

**[DAST (Dynamic Application Security Testing, 동적 애플리케이션 보안 테스트)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: 소스 코드에 접근하지 않고 실행 중인 애플리케이션을 바깥에서 탐침해 런타임에 나타나는 취약점을 찾는 보안 테스트입니다.

**Data-ink ratio (데이터-잉크 비율)**: 차트가 잉크의 대부분을 데이터 자체에 쓰고 장식에는 적게 써야 하며, 정보를 주지 않는 격자선, 테두리, 차트 장식을 제거해야 한다는 에드워드 터프티의 원칙입니다.

**[데이터 메시 (Data mesh)](https://en.wikipedia.org/wiki/Data_mesh)**: 데이터를 도메인 팀이 소유하는 제품으로 다루며, 셀프서비스 플랫폼 인프라와 연합 거버넌스가 뒷받침하는 분산 데이터 아키텍처이자 운영 모델입니다.

**[데이터 시각화 (Data visualisation)](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: 위치, 길이, 색 등 시각적 형태로 데이터를 인코딩해, 패턴, 비교, 추세가 지각되고 결정이 더 잘 정보를 얻게 하는 실천입니다.

**[DDD (Domain-Driven Design, 도메인 주도 설계)](https://en.wikipedia.org/wiki/Domain-driven_design)**: 공유된 유비쿼터스 언어, 바운디드 컨텍스트, 엔터티, 값 객체, 애그리거트 같은 구성 요소를 써서 모델을 비즈니스 도메인 중심에 두는 소프트웨어 설계 접근입니다.

**Design tokens (디자인 토큰)**: 색, 간격, 타이포그래피 등 디자인 결정을 인코딩해 디자인 시스템과 여러 제품에서 일관되게 공유할 수 있게 하는, 플랫폼에 중립적인 이름 붙은 값입니다.

**DevEx / DevX (Developer Experience, 개발자 경험)**: 마찰, 피드백 속도, 인지 부하를 아우르는, 개발자가 도구, 플랫폼, 프로세스와 일상적으로 상호작용하는 전반적 품질입니다.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: 소프트웨어 개발과 운영을 통합해 전달 주기를 줄이고, 배포 빈도를 높이고, 자동화와 공유 소유권으로 신뢰성을 개선하는 문화와 실천의 집합입니다.

**DORA (DevOps Research and Assessment, DevOps 리서치 및 평가)**: 연구 프로그램과, 소프트웨어 전달 성과를 벤치마크하는 데 널리 쓰이는 네 가지 전달 지표(배포 빈도, 변경 리드 타임, 변경 실패율, 서비스 복원 시간)입니다.

**DPIA (Data Protection Impact Assessment, 데이터 보호 영향 평가)**: GDPR이 고위험 처리에 요구하는, 프로젝트가 진행되기 전에 프라이버시 위험을 식별하고 완화하는 구조화된 평가입니다.

**Drift (configuration, 구성 드리프트)**: 시스템의 실제 상태가 선언되거나 의도한 상태에서 점차 갈라지는 것으로, 흔히 수동 변경이 원인입니다. 코드형 인프라와 GitOps가 이를 탐지하고 바로잡으려 합니다.

**Drift (model, 모델 드리프트)**: 머신러닝에서 입력 데이터의 통계적 속성(데이터 드리프트)이나 모델링하는 관계(개념 드리프트)가 변하면서 시간에 따라 모델 성능이 저하되는 것입니다.

**[DR (Disaster Recovery, 재해 복구)](https://en.wikipedia.org/wiki/Disaster_recovery)**: 큰 중단 사건 뒤에 서비스와 데이터를 복원하기 위한 전략, 절차, 인프라로, 보통 RTO와 RPO 목표가 다스립니다.

**[DRY (Don't Repeat Yourself, 반복하지 마라)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: 모든 지식은 단일하고 권위 있는 표현을 가져야 한다는 설계 원칙으로, 중복과 일관되지 않은 갱신의 위험을 줄입니다.

## E

**East-west traffic (동서 트래픽)**: 시스템과 외부 클라이언트 사이의 남북 트래픽과 달리, 시스템이나 데이터 센터 안의 서비스 사이 네트워크 트래픽입니다. 서비스 메시가 보통 동서 트래픽을 다스립니다.

**[에지 컴퓨팅 (Edge computing)](https://en.wikipedia.org/wiki/Edge_computing)**: 지연과 대역폭을 줄이려고 중앙 위치가 아니라 데이터가 생산되거나 소비되는 곳 가까이에서 연산과 저장을 실행하는 것입니다. 콘텐츠 전송 네트워크는 이른 시기의 널리 퍼진 형태입니다.

**[탄력성 (Elasticity)](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: 변하는 수요에 따라 시스템이 자원을 자동으로 확보하고 반납해, 역량이 부하를 가깝게 따라가는 능력입니다.

**[ELT (Extract, Load, Transform, 추출 적재 변환)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: 원시 데이터를 먼저 대상 저장소에 적재한 뒤 거기서 변환해, 현대 웨어하우스와 레이크하우스의 규모를 활용하는 데이터 통합 패턴입니다.

**[임베딩 (Embedding)](https://en.wikipedia.org/wiki/Word_embedding)**: 텍스트, 이미지, 기타 데이터를 비슷한 항목이 가까이 놓이도록 위치시킨 밀집 수치 벡터로 표현한 것입니다. 임베딩은 시맨틱 및 벡터 검색과 검색 증강 생성을 구동합니다.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: ICT 제품과 서비스의 접근성 요구 사항을 명세하는 유럽 표준으로, EU 전역의 공공 부문 조달이 참조하며 WCAG와 정렬됩니다.

**Error budget (오류 예산)**: SLO가 한 기간에 허용하는 비신뢰성의 허용량입니다. 소진되면 팀은 새 기능보다 신뢰성 작업을 우선합니다. 속도와 안정성 사이의 긴장을 조정합니다.

**[ETL (Extract, Transform, Load, 추출 변환 적재)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: 원천에서 데이터를 추출하고, 대상 형태로 변환하고, 웨어하우스 같은 목적지에 적재하는 데이터 통합 패턴입니다.

**[EU AI Act (EU 인공지능법)](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: AI 시스템을 위험에 따라 분류하고 그에 맞는 의무를 부과하며, 특정 용도를 금지하고 고위험 시스템을 강하게 규제하는 유럽 연합 규정입니다.

**[최종 일관성 (Eventual consistency)](https://en.wikipedia.org/wiki/Eventual_consistency)**: 복제본이 일시적으로 갈라질 수 있지만 갱신 전파가 멈추면 같은 상태로 수렴하는 분산 시스템의 일관성 모델입니다.

## F

**[기능 플래그 / 기능 토글 (Feature flag / feature toggle)](https://en.wikipedia.org/wiki/Feature_toggle)**: 재배포 없이 런타임에 기능을 켜거나 끄는 메커니즘으로, 점진적 롤아웃, 실험, 운영 통제에 쓰입니다.

**Feature store (피처 스토어)**: 큐레이션된 머신러닝 피처를 학습과 추론 모두에서 일관되게 정의, 저장, 제공해 중복과 학습/서빙 편차를 줄이는 중앙 시스템입니다.

**[FedRAMP (Federal Risk and Authorisation Management Program, 연방 위험 및 인가 관리 프로그램)](https://en.wikipedia.org/wiki/FedRAMP)**: 연방 기관이 쓰는 클라우드 서비스의 보안 평가, 인가, 지속적 모니터링을 표준화하는 미국 정부 프로그램입니다.

**Few-shot prompting (퓨샷 프롬프팅)**: 예시 없이 지시만 주는 제로샷 프롬프팅과 달리, 원하는 과업과 출력 형식을 보이는 소수의 예시를 프롬프트에 언어 모델에게 제공하는 것입니다.

**FinOps**: 가변적인 클라우드 지출에 재무적 책임을 가져와, 엔지니어링, 재무, 비즈니스 팀이 비용과 가치를 공동 소유하게 하는 규율이자 문화적 실천입니다.

**[FISMA (Federal Information Security Modernisation Act, 연방 정보 보안 현대화법)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: 연방 기관이 정보 보안 프로그램을 구현하고, 문서화하고, 모니터링하도록 요구하는 미국 법으로, 대부분 NIST 지침을 통해 운영됩니다.

**Flow efficiency (흐름 효율)**: 작업 항목이 기다리지 않고 적극적으로 작업되는 데 쓰는 총 리드 타임의 비율로, 가치 부가 시간을 총 리드 타임으로 나눠 계산합니다. 대부분의 시스템은 놀랄 만큼 낮아 흔히 15% 미만입니다.

**Four-eyes principle (포아이즈 원칙)**: 중요한 행동을 적어도 두 사람이 리뷰하거나 승인하도록 요구해 오류나 비행의 가능성을 줄이는 통제입니다.

**[퍼즈 테스트 (Fuzz testing, fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: 잘못 구성되거나 무작위이거나 예상치 못한 입력을 프로그램에 넣어 충돌, 보안 결함, 경계 사례 결함을 찾는 자동화된 테스트 기법입니다.

## G

**[GDPR (General Data Protection Regulation, 일반 데이터 보호 규정)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: 개인 데이터 처리를 다스리고, 개인에게 권리를 주며, 관리자와 처리자에게 의무를 부과하고, 미준수에 상당한 처벌을 두는 유럽 연합 규정입니다.

**GitOps**: Git을 선언적 인프라와 애플리케이션의 단일 진실 공급원으로 쓰고, 자동화가 라이브 시스템을 커밋된 상태에 지속적으로 맞추는 운영 모델입니다.

**Golden path / paved road (골든 패스 / 포장된 길)**: 안전하고, 준수하고, 신뢰할 수 있는 선택을 가장 쉬운 선택으로 만들도록 설계된, 조직 안에서 소프트웨어를 만들고 출하하는 잘 지원되고 규범적인 기본 방식입니다.

**Golden record (골든 레코드)**: 마스터 데이터 관리에서 매칭과 생존 규칙을 통해 여러 원천 시스템에서 조립한, 고객 같은 비즈니스 엔터티의 단일하고 조정된 권위 있는 버전입니다.

**[점진적 타이핑 (Gradual typing)](https://en.wikipedia.org/wiki/Gradual_typing)**: 정적 타이핑과 동적 타이핑이 한 코드베이스에 공존하게 해, 동적 타입 프로그램에 타입을 점진적으로 추가할 수 있게 하는 타입 시스템 접근입니다. 타입 힌트와 선택적 타입 검사기가 흔한 예입니다.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: 강하게 타입이 있는 스키마를 써서 클라이언트가 필요한 데이터를 정확히 한 번의 호출로 요청하게 하는 API용 질의 언어이자 런타임입니다.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: 효율적인 서비스 간 통신을 위해 HTTP/2와 보통 Protocol Buffers를 쓰는 고성능 계약 우선 원격 프로시저 호출 프레임워크입니다.

## H

**Hermetic build (밀폐 빌드)**: 명시적으로 선언된 입력에만 의존하고 호스트 환경에서 격리되어, 어디서나 같은 출력을 내는 빌드입니다. 밀폐성은 재현 가능한 빌드와 믿을 만한 캐싱의 기반입니다.

**[HSM (Hardware Security Module, 하드웨어 보안 모듈)](https://en.wikipedia.org/wiki/Hardware_security_module)**: 암호화 키를 생성, 저장, 사용하는 변조 방지 하드웨어 장치로, 소프트웨어만의 접근보다 강한 키 보호를 제공합니다.

**[HIPAA (Health Insurance Portability and Accountability Act, 건강보험 이동성 및 책임법)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: 그중에서도 보호 대상 건강 정보(PHI)를 보호하는 요구 사항을 정하고 그 사용과 공개를 다스리는 미국 법입니다.

**Horizontal scaling (수평 확장)**: 단일 노드를 더 강력하게 만드는 대신 더 많은 인스턴스나 노드를 더해("스케일 아웃") 역량을 늘리는 것입니다. 대부분의 대규모 복원력 있는 아키텍처의 바탕입니다.

## I

**[IaC (Infrastructure as Code, 코드형 인프라)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: 수동 프로세스 대신 기계가 읽을 수 있고 버전 관리되는 구성으로 인프라를 정의하고 프로비저닝해 반복 가능성과 리뷰를 가능하게 하는 실천입니다.

**[IAM (Identity and Access Management, 신원 및 접근 관리)](https://en.wikipedia.org/wiki/Identity_management)**: 올바른 신원이 올바른 때에 올바른 리소스에 올바른 접근을 갖도록 보장하는 정책과 기술의 틀입니다.

**IDP / IdP**: "IDP"는 보통 제품 팀을 위해 인프라를 추상화하는 셀프서비스 도구 계층인 내부 개발자 플랫폼(Internal Developer Platform)을, "IdP"는 사용자를 인증하고 단언을 발급하는 서비스인 신원 제공자(Identity Provider)를 가리킵니다. 맥락이 둘을 구별합니다.

**[멱등성 (Idempotency)](https://en.wikipedia.org/wiki/Idempotence)**: 연산을 여러 번 수행해도 한 번 수행한 것과 같은 효과를 내는 속성으로, 분산 시스템과 API에서 안전한 재시도에 필수적입니다.

**[i18n (Internationalisation, 국제화)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: 엔지니어링 변경 없이 다른 언어, 지역, 문화적 관습에 맞출 수 있도록 소프트웨어를 설계하고 만드는 것입니다. 이 숫자 약어는 "i"와 "n" 사이의 18개 글자를 줄인 것입니다.

**Immutable artefact (불변 산출물)**: 일단 만들어지고 버전이 매겨지면 결코 수정되지 않는 빌드 출력으로, 어떤 변경이든 새 버전을 낳습니다. 불변성은 릴리스를 재현 가능하게 하며, 한 번 빌드해 같은 산출물을 환경 사이로 승격하게 합니다.

**InnerSource**: 오픈 소스 개발 실천(투명성, 공유 저장소, 팀 간 기여)을 단일 조직 안에 적용하는 것입니다.

**IaC drift**: Drift (configuration)을 보십시오.

**[역색인 (Inverted index)](https://en.wikipedia.org/wiki/Inverted_index)**: 검색 엔진의 핵심 데이터 구조로, 각 용어를 그것을 포함하는 문서 목록에 매핑해 모든 문서를 훑지 않고 질의에 답할 수 있게 합니다.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: 정보 보안 관리 시스템(ISMS)의 요구 사항을 명세하는 국제 표준으로, 정보 보안 위험을 관리하는 인증 가능한 틀을 제공합니다.

**ISO/IEC 42001**: AI 관리 시스템의 요구 사항을 명세하는 국제 표준으로, 조직이 AI의 개발과 사용을 책임 있게 다스리는 인증 가능한 틀을 제공합니다.

## J

**[JWT (JSON Web Token, JSON 웹 토큰)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: 당사자 사이에 클레임을 전달하는 데 쓰는 간결하고 서명된(선택적으로 암호화된) 토큰 형식으로, 웹과 API 시스템의 인증과 권한 부여에 흔히 쓰입니다.

## K

**[칸반 (Kanban)](https://en.wikipedia.org/wiki/Kanban_(development))**: 일을 보드에 시각화하고, 진행 중인 작업에 한도를 두고, 흐름을 관리해 처리량과 예측 가능성을 개선하는 린 워크플로 방법입니다.

**[KISS (Keep It Simple, Stupid, 단순하게 유지하라)](https://en.wikipedia.org/wiki/KISS_principle)**: 불필요한 복잡성이 비용과 위험을 늘린다는 이유로 필요를 충족하는 가장 단순한 해법을 선호하는 설계 원칙입니다.

**KMS (Key Management Service, 키 관리 서비스)**: 암호화 키를 만들고, 저장하고, 교체하고, 접근을 통제하는 시스템으로, 흔히 하드웨어 보안 모듈이 뒷받침합니다.

**[KPI (Key Performance Indicator, 핵심 성과 지표)](https://en.wikipedia.org/wiki/Performance_indicator)**: 특정 비즈니스나 운영 목표를 향한 진행을 추적하는 데 쓰는 수량화 가능한 척도입니다.

## L

**Lakehouse (레이크하우스)**: 데이터 레이크의 저비용이고 유연한 저장을 데이터 웨어하우스의 관리, 트랜잭션, 성능 기능과 결합한 데이터 아키텍처입니다.

**[리드 타임 (Lead time)](https://en.wikipedia.org/wiki/Lead_time)**: 변경이 요청된(또는 커밋된) 때부터 프로덕션에 전달될 때까지의 경과 시간으로, 핵심 DORA 전달 지표입니다.

**[최소 권한 (Least privilege)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: 각 사용자, 프로세스, 시스템에게 기능을 수행하는 데 필요한 최소한의 접근만 주어 침해나 오류의 피해를 제한하는 보안 원칙입니다.

**[리틀의 법칙 (Little's Law)](https://en.wikipedia.org/wiki/Little's_law)**: 안정된 시스템의 평균 항목 수가 평균 도착률 곱하기 각 항목이 시스템에서 보내는 평균 시간과 같다는 대기행렬 이론의 결과입니다. 진행 중인 작업, 처리량, 리드 타임을 연결합니다.

**[LLM (Large Language Model, 거대 언어 모델)](https://en.wikipedia.org/wiki/Large_language_model)**: 언어를 예측하고 생성하도록 매우 큰 텍스트 말뭉치로 학습한 머신러닝 모델로, 요약, 번역, 코드 생성 같은 과업이 가능합니다.

**[l10n (Localisation, 현지화)](https://en.wikipedia.org/wiki/Language_localisation)**: 국제화된 소프트웨어를 번역, 서식, 문화적 관습을 포함해 특정 로캘에 맞추는 것입니다. 이 숫자 약어는 "l"과 "n" 사이의 10개 글자를 줄인 것입니다.

## M

**[MDM (Master Data Management, 마스터 데이터 관리)](https://en.wikipedia.org/wiki/Master_data_management)**: 고객이나 제품 같은 핵심 비즈니스 엔터티의 시스템 전반에 걸친 단일하고, 권위 있고, 일관된 관점을 만들고 유지하는 규율과 도구입니다.

**MITRE ATT&CK**: 실제 공격자의 전술과 기법을 큐레이션한 공개 지식 베이스로, 레드 팀 연습을 계획하고, 탐지 엔지니어링을 이끌고, 공유된 어휘로 위협을 기술하는 데 널리 쓰입니다.

**Mean Time to Recovery (MTTR, 평균 복구 시간)**: 실패 뒤 서비스를 복원하는 데 걸리는 평균 시간으로, 흔한 신뢰성 및 인시던트 관리 지표입니다.

**[몹 프로그래밍 (Mob programming)](https://en.wikipedia.org/wiki/Mob_programming)**: 팀 전체가 같은 컴퓨터에서 같은 과업을 함께 하며, 타이핑하는 사람을 돌려 가면서 지식을 나누고 집단적으로 결정하는 실천입니다.

**[MLOps (Machine Learning Operations, 머신러닝 운영)](https://en.wikipedia.org/wiki/MLOps)**: DevOps 원칙을 ML 수명 주기로 확장해 머신러닝 모델을 프로덕션에 안정적이고 효율적으로 배포, 모니터링, 유지하는 실천의 집합입니다.

**[모노레포 (Monorepo)](https://en.wikipedia.org/wiki/Monorepo)**: 많은 프로젝트나 조직 전체의 코드를 담은 단일 버전 관리 저장소로, 전문 확장 도구를 대가로 공유 도구와 프로젝트 간 원자적 변경을 가능하게 합니다.

**mTLS (mutual TLS, 상호 TLS)**: 양쪽 당사자가 인증서를 제시하고 검증해 서로를 인증하는 전송 계층 보안 구성입니다. 서비스 메시와 제로 트러스트 네트워크에서 서비스 간 트래픽의 기본값입니다. [상호 인증](https://en.wikipedia.org/wiki/Mutual_authentication)도 보십시오.

**[뮤테이션 테스트 (Mutation testing)](https://en.wikipedia.org/wiki/Mutation_testing)**: 코드에 작은 결함("뮤턴트")을 의도적으로 도입해 테스트 스위트가 그것을 탐지하는지 확인함으로써 스위트의 실제 효과성을 측정하는 기법입니다.

## N

**[NDCG (Normalised Discounted Cumulative Gain, 정규화 할인 누적 이득)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: 매우 관련 있는 결과를 결과 목록 위쪽에 두는 것에 보상하고, 질의 사이에 점수를 비교할 수 있도록 정규화한 순위 품질 지표입니다. 검색 관련성 평가의 기본 도구입니다.

**[NIST (National Institute of Standards and Technology, 미국 국립표준기술연구소)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: 사이버보안, 프라이버시, AI에 대해 널리 참조되는 표준인 특별 간행물과 프레임워크를 내는 미국 연방 기관입니다.

**NIST AI RMF (AI Risk Management Framework, AI 위험 관리 프레임워크)**: 수명 주기 전반에서 AI 시스템과 관련된 위험을 식별, 평가, 관리하기 위한, 거버닝, 매핑, 측정, 관리 기능을 중심으로 조직된 NIST의 자발적 프레임워크입니다.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: 연방 정보 시스템의 보안 및 프라이버시 통제 카탈로그로, 정부를 훨씬 넘어 기준선으로 널리 쓰입니다.

**NIST SP 800-171**: 비연방 시스템에서 비기밀 통제 정보(CUI)를 보호하는 요구 사항을 명세하는 NIST 간행물로, 국방 계약자 컴플라이언스의 핵심입니다.

**[NFR (Non-Functional Requirement, 비기능 요구 사항)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: 시스템이 어떤 기능을 수행하는지가 아니라 어떻게 행동해야 하는지(성능, 보안, 신뢰성, 사용성 같은 품질)를 기술하는 요구 사항입니다.

**North-south traffic (남북 트래픽)**: 내부 서비스 사이의 동서 트래픽과 달리, 시스템과 외부 클라이언트 사이(데이터 센터나 클러스터의 안팎)의 네트워크 트래픽입니다. API 게이트웨이가 보통 남북 트래픽을 다스립니다.

## O

**Observability (관측 가능성)**: 시스템의 내부 상태를 외부 출력에서 추론할 수 있는 정도로, 보통 지표, 로그, 트레이스라는 텔레메트리를 통해 달성합니다.

**[OKR (Objectives and Key Results, 목표와 핵심 결과)](https://en.wikipedia.org/wiki/OKR)**: 정성적 목표를 소수의 측정 가능한 핵심 결과와 짝지워 조직을 정렬하고 집중시키는 목표 설정 프레임워크입니다.

**OpenTelemetry (OTel)**: 소프트웨어에서 텔레메트리 데이터(트레이스, 지표, 로그)를 생성, 수집, 내보내기 위한 벤더 중립의 개방형 표준이자 도구 모음입니다.

**OPA (Open Policy Agent)**: Rego 언어로 쓴 정책을 평가해 스택 전반의 권한 부여와 구성 규칙을 시행하고 코드형 정책을 가능하게 하는 오픈 소스 범용 정책 엔진입니다.

**OSPO (Open Source Program Office, 오픈 소스 프로그램 오피스)**: 소비와 기여를 모두 관리하며 오픈 소스 전략, 거버넌스, 컴플라이언스, 커뮤니티 참여를 조율하는 조직 기능입니다.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: OWASP Top Ten과 ASVS를 포함해 널리 쓰이고 자유롭게 이용할 수 있는 애플리케이션 보안 자료를 만드는 비영리 커뮤니티입니다.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: 분할(Partition)이 있으면 시스템이 가용성(Availability)과 일관성(Consistency)을 맞바꾸고, 그렇지 않으면(Else, 정상 운영에서) 지연(Latency)과 일관성을 맞바꾼다고 말하는 CAP 정리의 확장입니다.

**[PCI DSS (Payment Card Industry Data Security Standard, 결제 카드 산업 데이터 보안 표준)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: 카드 소지자 데이터를 저장, 처리, 전송하는 조직의 요구 사항을 명세하는, 결제 카드 산업이 유지하는 보안 표준입니다.

**[침투 테스트 (Penetration testing)](https://en.wikipedia.org/wiki/Penetration_test)**: 실제 공격자보다 먼저 악용 가능한 취약점을 찾아 시연하려고 숙련된 테스터가 시스템에 하는 승인된 모의 공격으로, 우선순위가 정해진 실행 가능한 발견 사항으로 전달됩니다.

**[PII (Personally Identifiable Information, 개인 식별 정보)](https://en.wikipedia.org/wiki/Personal_data)**: 단독으로나 다른 데이터와 결합해 특정 개인을 식별할 수 있는 정보로, 그 취급은 프라이버시 법과 내부 정책이 다스립니다.

**Platform engineering (플랫폼 엔지니어링)**: 인지 부하를 줄이고 제품 팀을 가속하는 내부 셀프서비스 플랫폼과 골든 패스를 구축하고 운영하는 규율입니다.

**POUR**: 웹 콘텐츠 접근성 지침의 네 가지 지도 원칙입니다. 콘텐츠는 인지 가능(Perceivable)하고, 운용 가능(Operable)하고, 이해 가능(Understandable)하고, 견고(Robust)해야 합니다.

**Production readiness review (프로덕션 준비 리뷰)**: 서비스가 가동되거나 온콜 소유권을 맡기 전에, 관측 가능성, 신뢰성, 보안, 런북, 운영 지원의 표준을 충족하는지 확인하는 구조화된 점검입니다.

**[프롬프트 엔지니어링 (Prompt engineering)](https://en.wikipedia.org/wiki/Prompt_engineering)**: 시행착오가 아니라 버전 관리되고 테스트되는 엔지니어링 규율로 다루어, 신뢰할 수 있는 고품질 출력을 얻도록 언어 모델에게 주는 지시, 컨텍스트, 예시를 설계하고 다듬는 실천입니다.

**[프롬프트 인젝션 (Prompt injection)](https://en.wikipedia.org/wiki/Prompt_injection)**: 조작된 입력이 언어 모델로 하여금 의도된 지시를 무시하고 공격자의 지시를 따르게 하는 공격으로, 인젝션 결함의 AI 시대 대응물입니다. LLM 애플리케이션의 핵심 보안 위험입니다.

**Property-based testing (속성 기반 테스트)**: 직접 고른 예시에만 의존하는 대신, 자동 생성된 많은 입력에 걸쳐 명시된 속성이 성립하는지 점검하는 테스트 기법입니다.

**Pull request (PR) / merge request (MR) (풀 리퀘스트 / 머지 리퀘스트)**: 공유 브랜치에 병합되기 전에 리뷰와 논의를 위해 제출하는 제안된 변경 집합으로, 대부분의 워크플로에서 코드 리뷰의 기본 단위입니다.

**Purple team (퍼플 팀)**: 공격(레드) 보안 팀과 방어(블루) 보안 팀이 실시간으로 함께 일해 공격과 그것을 잡으려는 탐지가 서로에 대해 조정되는 협업 연습입니다.

## Q

**Quality gate (품질 관문)**: 변경이 진행하기 전에 통과해야 하는(예: 커버리지, 보안, 성능 임계값 충족) 파이프라인의 자동화된 점검 지점입니다.

**[쿼럼 (Quorum)](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: 분산 시스템에서 연산(읽기나 쓰기 등)이 성공으로 간주되려면 합의해야 하는 최소 노드 수로, 실패에도 일관성을 유지하는 데 쓰입니다.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: 과업이나 결정의 각 참여자를 실행 책임(Responsible), 최종 책임(Accountable), 자문(Consulted), 통보(Informed)로 표시하는 책임 배정 모델입니다.

**[RAG (Retrieval-Augmented Generation, 검색 증강 생성)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: 먼저 관련 문서나 데이터를 검색해 컨텍스트로 제공함으로써 언어 모델의 출력에 근거를 주어 정확도를 높이고 환각을 줄이는 기법입니다.

**[RBAC (Role-Based Access Control, 역할 기반 접근 통제)](https://en.wikipedia.org/wiki/Role-based_access_control)**: 권한을 역할에 배정하고 역할을 사용자에게 배정해, 역할 수준에서 접근을 관리해 관리를 단순화하는 권한 부여 모델입니다.

**[레드 팀 (Red team)](https://en.wikipedia.org/wiki/Red_team)**: 단지 취약점을 열거하는 것이 아니라 탐지와 대응을 시험하려고, 흔히 방어자에게 경고 없이 조직 전체를 상대로 현실적인 공격자를 모사하는 집단입니다. 블루(방어) 팀과 대비됩니다.

**[참조 데이터 (Reference data)](https://en.wikipedia.org/wiki/Reference_data)**: 국가 코드, 통화, 상태 값처럼 다른 데이터를 분류하는 데 쓰는 통제되고 천천히 바뀌는 코드 목록과 분류입니다. 공유되고 버전이 있는 어휘로 다스리면 시스템이 일관되게 유지됩니다.

**Rego**: 권한 부여와 구성 결정의 규칙을 표현하려고 Open Policy Agent가 쓰는 선언적 정책 언어입니다.

**[REST (Representational State Transfer, 표현 상태 전이)](https://en.wikipedia.org/wiki/REST)**: 주소 지정 가능한 리소스에 대해 HTTP 위의 무상태 연산을 쓰는 네트워크 애플리케이션 아키텍처 스타일로, 단순성과 폭넓은 도구가 장점입니다.

**[리버스 프록시 (Reverse proxy)](https://en.wikipedia.org/wiki/Reverse_proxy)**: 하나 이상의 백엔드 서비스 앞에 놓여 클라이언트 요청을 그쪽으로 전달하는 서버로, 흔히 TLS 종단, 로드 밸런싱, 캐싱, 단일 진입점을 제공합니다.

**[RFC (Request for Comments, 의견 요청)](https://en.wikipedia.org/wiki/Request_for_Comments)**: 중요한 기술 결정이나 변경 전에 피드백을 받으려고 회람하는 서면 제안으로, 투명성과 공유된 소유권을 키웁니다. (이 용어는 인터넷 표준 문서 시리즈의 이름이기도 합니다.)

**[ROI (Return on Investment, 투자수익률)](https://en.wikipedia.org/wiki/Return_on_investment)**: 투자에서 얻은 가치를 비용에 상대적으로 나타낸 척도로, 엔지니어링과 기술 결정을 정당화하고 우선순위를 정하는 데 쓰입니다.

**[RPA (Robotic Process Automation, 로봇 프로세스 자동화)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: 사람이 하듯 기존 사용자 인터페이스와 시스템과 상호작용해 반복적이고 규칙 기반인 과업을 자동화하는 소프트웨어 "로봇"입니다.

**RPO (Recovery Point Objective, 복구 시점 목표)**: 시간으로 측정한 최대 허용 데이터 손실(예: "최대 5분")로, 데이터를 얼마나 자주 보호해야 하는지 정의합니다.

**RTO (Recovery Time Objective, 복구 시간 목표)**: 중단 뒤 서비스를 복원하는 최대 허용 기간으로, 재해 복구 설계와 투자를 이끕니다.

## S

**Saga (사가)**: 로컬 트랜잭션을 순서대로 실행하고 단계가 실패하면 보상 행동을 내는 방식으로, 분산 트랜잭션에서 서비스 간 데이터 일관성을 관리하는 패턴입니다.

**[SAFe (Scaled Agile Framework, 확장형 애자일 프레임워크)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: 많은 팀을 조율하며 큰 기업 전반에 애자일과 린 실천을 적용하는 프레임워크로, 구조는 높이 평가받고 잠재적인 무거움은 비판받습니다.

**[SAST (Static Application Security Testing, 정적 애플리케이션 보안 테스트)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: 소스 코드, 바이트코드, 바이너리를 실행하지 않고 분석해 개발 초기에 취약점을 찾는 보안 테스트입니다.

**SBOM (Software Bill of Materials, 소프트웨어 자재 명세서)**: 공급망과 취약점 위험을 관리하는 데 쓰는, 소프트웨어의 구성 요소와 의존성에 대한 공식적이고 기계가 읽을 수 있는 목록입니다.

**SCA (Software Composition Analysis, 소프트웨어 구성 분석)**: 코드베이스의 오픈 소스와 제3자 구성 요소를 식별하고 알려진 취약점과 라이선스 위험을 표시하는 도구입니다.

**[스크럼 (Scrum)](https://en.wikipedia.org/wiki/Scrum_(software_development))**: 가치의 증분을 전달하려고 정의된 역할, 이벤트, 산출물과 함께 일을 고정 길이 반복(스프린트)으로 조직하는 애자일 프레임워크입니다.

**[Section 508 (재활법 508조)](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: 연방 기관이 전자 및 정보 기술을 장애가 있는 사람이 접근할 수 있게 하도록 요구하는 미국 법으로, 실제로는 WCAG와 정렬됩니다.

**Semantic search (시맨틱 검색)**: 정확한 키워드가 아니라 의미로 매칭하는 검색으로, 보통 질의와 문서의 임베딩을 비교합니다. 하이브리드 접근에서 어휘 검색과 결합하는 경우가 많습니다.

**[서비스 메시 (Service mesh)](https://en.wikipedia.org/wiki/Service_mesh)**: 보통 사이드카 프록시로 구현하며, 상호 TLS, 재시도, 타임아웃, 트래픽 이동, 관측 가능성 같은 서비스 간 통신 관심사를 애플리케이션 코드 밖에서 다루는 전용 인프라 계층입니다.

**Sidecar (사이드카)**: 애플리케이션 자체를 바꾸지 않고 (서비스 메시 프록시 같은) 보조 기능을 제공하려고 주 애플리케이션 인스턴스 옆에 배포하는 도우미 프로세스나 컨테이너입니다.

**[SIEM (Security Information and Event Management, 보안 정보 및 이벤트 관리)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: 환경 전반의 보안 로그와 이벤트를 집계하고 상관 분석해 탐지, 알림, 조사를 가능하게 하는 시스템입니다.

**[SLA (Service Level Agreement, 서비스 수준 협약)](https://en.wikipedia.org/wiki/Service-level_agreement)**: 서비스 제공자와 고객 사이에서 기대되는 서비스 수준과 그것을 놓쳤을 때의 결과를 명시하는 공식 약속입니다.

**SLI (Service Level Indicator, 서비스 수준 지표)**: SLO에 공급되는, 요청 지연이나 오류율 같은 서비스 품질의 어떤 측면에 대한 정량적 척도입니다.

**SLO (Service Level Objective, 서비스 수준 목표)**: 원하는 신뢰성 수준을 정의하는 SLI의 목표 값이나 범위로, 오류 예산의 바탕을 이룹니다.

**SLSA (Supply-chain Levels for Software Artifacts, 소프트웨어 산출물의 공급망 수준)**: 빌드와 릴리스 프로세스를 통해 소프트웨어 산출물의 무결성과 출처를 개선하는 단계별 보안 요구 사항의 프레임워크입니다.

**SOAR (Security Orchestration, Automation, and Response, 보안 오케스트레이션, 자동화, 대응)**: 분류와 대응 플레이북 같은 보안 운영을 자동화하고 조율해 속도와 일관성을 높이는 도구와 실천입니다.

**SOC 2 (System and Organisation Controls 2)**: AICPA 신뢰 서비스 기준에 기반해 서비스 조직의 보안, 가용성, 처리 무결성, 기밀성, 프라이버시 통제를 평가하는 감사 프레임워크이자 보고서입니다.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: 유지 가능하고 유연한 코드를 촉진하는 다섯 객체 지향 설계 원칙(단일 책임, 개방/폐쇄, 리스코프 치환, 인터페이스 분리, 의존성 역전)입니다.

**[SOX (Sarbanes-Oxley Act, 사베인스-옥슬리법)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: 상장 기업의 재무 보고와 내부 통제의 요구 사항을 정립한 미국 법으로, 재무 데이터를 뒷받침하는 IT 시스템에 영향을 줍니다.

**SPACE**: 단일 지표 측정을 경계하며, 개발자 생산성을 다섯 차원에 걸쳐 측정하는 프레임워크입니다. 만족과 웰빙(Satisfaction and well-being), 성과(Performance), 활동(Activity), 커뮤니케이션과 협업(Communication and collaboration), 효율과 흐름(Efficiency and flow)입니다.

**[SRE (Site Reliability Engineering, 사이트 신뢰성 엔지니어링)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: SLO, 오류 예산, 자동화를 써서 소프트웨어 엔지니어링 접근을 운영에 적용해 규모에서 신뢰할 수 있는 시스템을 운영하는 규율입니다.

**SSDF (Secure Software Development Framework, 안전한 소프트웨어 개발 프레임워크)**: 조직 준비, 소프트웨어 보호, 잘 보호된 소프트웨어 생산, 취약점 대응에 걸친 고수준 보안 개발 실천에 대한 NIST의 프레임워크(SP 800-218)입니다.

**[정적 분석 (Static analysis)](https://en.wikipedia.org/wiki/Static_program_analysis)**: 소스 코드, 바이트코드, 바이너리를 실행하지 않고 검사해 결함, 스타일 위반, 보안 결함을 찾는 것으로, 보통 에디터와 파이프라인에 연결된 린터, 타입 검사기, 전용 분석기를 통해 이루어집니다.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: 위협을 위장(Spoofing), 변조(Tampering), 부인(Repudiation), 정보 공개(Information disclosure), 서비스 거부(Denial of service), 권한 상승(Elevation of privilege)으로 분류하는 위협 모델링 분류 체계입니다.

## T

**[TCO (Total Cost of Ownership, 총소유비용)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: 초기 가격만이 아니라 취득, 운영, 유지 보수, 결국의 폐기를 포함한 시스템이나 결정의 전 생애 비용입니다.

**[TDD (Test-Driven Development, 테스트 주도 개발)](https://en.wikipedia.org/wiki/Test-driven_development)**: 설계를 이끌고 커버리지를 보장하려고, 통과시킬 코드 앞에 실패하는 자동화 테스트를 먼저 쓴 뒤 리팩터링하는 짧은 반복 주기의 실천입니다.

**[기술 부채 (Technical debt)](https://en.wikipedia.org/wiki/Technical_debt)**: 더 오래 걸릴 더 나은 해법 대신 지금 편법적인 해법을 택한 데 따른 암묵적인 미래 비용으로, 무의식적으로 쌓는 대신 의도적으로 관리해야 합니다.

**TF-IDF (Term Frequency-Inverse Document Frequency, 단어 빈도-역문서 빈도)**: 용어가 문서에 얼마나 자주 나타나는지로 문서에 대한 중요도를 점수화하되, 전체 말뭉치에서 얼마나 흔한지로 상쇄하는 고전적 가중 방식입니다. 어휘 검색 순위의 상당 부분의 바탕입니다.

**[제약 이론 (Theory of constraints)](https://en.wikipedia.org/wiki/Theory_of_constraints)**: 시스템의 처리량은 언제나 하나의 병목이 제한하므로, 개선 노력은 제약이 다른 곳으로 옮겨 갈 때까지 그 제약에 집중해야 한다는 관리 접근입니다.

**[위협 모델링 (Threat modelling)](https://en.wikipedia.org/wiki/Threat_model)**: 방어를 일찍 설계에 넣을 수 있도록 시스템에 대한 잠재적 위협을 식별하고, 열거하고, 우선순위를 정하는 구조화된 실천입니다.

**Toil (고역)**: SRE에서 서비스와 선형으로 늘어나고 지속적 가치를 주지 않는 수동적이고, 반복적이고, 자동화 가능한 운영 작업으로, 줄이면 엔지니어링 역량이 풀립니다.

**Trunk-based development (트렁크 기반 개발)**: 개발자가 단일 공유 브랜치에 작은 변경을 자주 통합해 오래 사는 브랜치와 병합의 고통을 최소화하는 소스 통제 실천입니다.

**[타입 추론 (Type inference)](https://en.wikipedia.org/wiki/Type_inference)**: 표현식의 타입을 자동으로 추론해, 모든 타입을 손으로 쓰도록 요구하지 않고도 정적 타이핑의 안전성 상당 부분을 주는 언어 기능입니다.

**[타입 시스템 (Type system)](https://en.wikipedia.org/wiki/Type_system)**: 언어가 타입을 배정하고 점검하는 규칙의 집합으로, 프로그램이 실행되기 전에 오류의 부류 전체를 잡고 의도를 문서화합니다. 타입 시스템은 동적에서 정적, 약한 것에서 강한 것까지 범위가 있습니다.

## U

**Ubiquitous language (유비쿼터스 언어)**: 도메인 주도 설계에서 개발자와 도메인 전문가가 일관되게 쓰고 코드와 모델에 직접 반영되는 공유되고 정확한 어휘입니다.

**[UAT (User Acceptance Testing, 사용자 인수 테스트)](https://en.wikipedia.org/wiki/Acceptance_testing)**: 시스템이 릴리스 승인을 받기 전에 비즈니스 필요를 충족하는지 확인하려고 최종 사용자나 그 대표가 수행하는 테스트입니다.

**[UX / UI (User Experience / User Interface, 사용자 경험 / 사용자 인터페이스)](https://en.wikipedia.org/wiki/User_experience)**: 사용자 경험은 사람이 제품과 상호작용하는 전반적 품질이고, 사용자 인터페이스는 그 상호작용이 일어나는 구체적인 시각적, 상호작용적 표면입니다.

## V

**[값 객체 (Value object)](https://en.wikipedia.org/wiki/Value_object)**: 도메인 주도 설계에서 별개의 정체성이 아니라 전적으로 속성으로 정의되는 불변 객체로, 금액이나 날짜 범위 같은 것입니다.

**[가치 흐름 매핑 (Value stream mapping)](https://en.wikipedia.org/wiki/Value-stream_mapping)**: 아이디어에서 전달된 가치까지 모든 단계를 그리고 가치 부가 시간과 대기 시간을 구별해, 병목, 인계, 재작업 루프가 보이고 개선 가능하게 하는 기법입니다.

**[벡터 데이터베이스 (Vector database)](https://en.wikipedia.org/wiki/Vector_database)**: 고차원 임베딩 벡터를 유사도로 색인하고 검색하도록 최적화된 데이터 저장소로, 시맨틱 검색과 검색 증강 생성의 흔한 중추입니다.

**Vertical scaling (수직 확장)**: 단일 노드를 더 강력하게 만들어("스케일 업") 역량을 늘리는 것으로, 단순하지만 결국 가용한 가장 큰 기계에 한계가 있습니다.

**[VCS (Version Control System, 버전 관리 시스템)](https://en.wikipedia.org/wiki/Version_control)**: 이력을 리뷰하고, 브랜치를 유지하고, 작업을 조율할 수 있도록 시간에 따른 파일 변경을 기록하는 Git 같은 도구입니다.

**[취약점 스캔 (Vulnerability scanning)](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: 시스템, 컨테이너, 코드를 알려진 약점과 잘못된 구성의 데이터베이스에 대해 자동으로 검사하는 것입니다. 폭이 넓고 싸며, 수동 침투 테스트의 깊이를 보완합니다.

## W

**[WCAG (Web Content Accessibility Guidelines, 웹 콘텐츠 접근성 지침)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: 웹 콘텐츠를 접근 가능하게 만드는, POUR 원칙과 적합성 수준 A, AA, AAA를 중심으로 조직된 국제적으로 인정받는 W3C의 지침 집합입니다.

**Wardley map (워들리 맵)**: 구축/구매와 투자 결정에 정보를 주려고, 역량을 사용자에 대한 가치와 진화적 성숙도로 위치시키는 시각적 전략 기법입니다.

**Work in progress (WIP) limit (진행 중인 작업 한도)**: 워크플로의 주어진 단계에 한 번에 있을 수 있는 항목 수의 상한으로, 병목을 드러내고 너무 많은 병렬 작업의 오버헤드를 억제해 흐름을 개선하는 핵심 칸반 실천입니다.

**WSJF (Weighted Shortest Job First, 가중 최단 작업 우선)**: 지연의 비용을 추정 기간으로 나눠 일의 순서를 정해, 가장 짧고, 시간에 민감하고, 가치가 가장 높은 항목을 먼저 하는 우선순위 방법입니다.

## X

**[XSS (Cross-Site Scripting, 크로스 사이트 스크립팅)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: 공격자가 다른 사용자의 브라우저에서 실행되는 악성 스크립트를 주입해 데이터를 훔치거나 세션을 가로챌 수 있는 웹 취약점입니다.

## Y

**[YAGNI (You Aren't Gonna Need It, 그건 필요 없을 것이다)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: 예상한 필요는 흔히 실현되지 않고 비용과 복잡성만 더한다는 이유로, 추측에 근거해 기능을 만들지 말라는 원칙입니다.

## Z

**[제로 트러스트 (Zero trust)](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: 네트워크 위치에 근거한 암묵적 신뢰를 가정하지 않고 모든 접근 요청을 신원, 기기, 맥락에 대해 지속적으로 검증하는 보안 모델로, "절대 신뢰하지 말고 항상 검증하라"는 격언을 따릅니다.
