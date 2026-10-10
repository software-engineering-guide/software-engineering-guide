# 12.5 참고 문헌

이 절은 가이드북의 참고 장치를 통합합니다. SWEBOK 지식 체계와의 대응표, 책 전반에서
인용한 표준과 프레임워크의 색인, 추천 도서의 엄선된 참고 문헌입니다. 장별 출처는
각 장 끝의 *참고 문헌과 더 읽을거리* 절에도 나옵니다.

---

# SWEBOK 대응표

이 가이드북은 IEEE 컴퓨터 학회의 **SWEBOK V4.0**(소프트웨어 엔지니어링 지식
체계)에 맞춰져 있습니다. 18개 지식 영역을 모두 다루며, 표는 각각을 그것을 다루는
장에 매핑합니다. 가이드북은 이어서 SWEBOK을 훨씬 넘어 AI, 데이터, UX, DevOps,
지속가능성, 흐름, 공익 기술까지 나아갑니다.

| SWEBOK V4.0 지식 영역 | 주요 장 |
|---|---|
| 1. 소프트웨어 요구 사항 | 2.8, 11.1, 5.1 |
| 2. 소프트웨어 아키텍처 | 3.1, 3.2, 3.3 |
| 3. 소프트웨어 설계 | 2.2, 3.1 |
| 4. 소프트웨어 구축 | 2.9, 2.1 |
| 5. 소프트웨어 테스트 | 2.4, 8.5 |
| 6. 소프트웨어 엔지니어링 운영 | 9.1, 9.2, 9.3, 8.1 |
| 7. 소프트웨어 유지 보수 | 3.7, 3.6, 10.4 |
| 8. 소프트웨어 형상 관리 | 2.10, 2.6, 8.2 |
| 9. 소프트웨어 엔지니어링 관리 | 10.1, 10.6, 10.2 |
| 10. 소프트웨어 엔지니어링 프로세스 | 1.4, 10.7, 10.8 |
| 11. 소프트웨어 엔지니어링 모델과 방법 | 2.12, 3.1, 2.2 |
| 12. 소프트웨어 품질 | 2.11, 2.4, 3.1 |
| 13. 소프트웨어 보안 | 4.1, 4.2, 4.3, 4.4 |
| 14. 소프트웨어 엔지니어링 전문 실무 | 10.5, 1.1, 1.3 |
| 15. 소프트웨어 엔지니어링 경제학 | 10.10, 10.1, 9.4 |
| 16. 컴퓨팅 기초 | 2.13, 3.3, 3.4 |
| 17. 수학적 기초 | 2.13, 11.3 |
| 18. 엔지니어링 기초 | 2.13, 3.1 |

---

# 표준과 프레임워크

이 부록은 가이드북 전반에서 참조한 실제 표준, 프레임워크, 규정의 정리된 색인입니다.
컴플라이언스 안내서가 아니라 길 찾기 도구입니다. 항상 권위 있는 출처를 참고하고,
해당하는 경우 현재 본문과 여러분의 맥락에 대한 적용 가능성은 자격 있는 법률이나
감사 자문을 구하십시오.

항목은 영역별로 묶었습니다. 각각 표준이나 프레임워크의 이름, 발행 기관, 한 줄
범위, 가장 관련 있는 장이나 영역을 적었습니다. 이름이 흔히 약어로 쓰이는 곳에는
약어를 보였습니다. 문서 번호와 제목은 잘 확립된 경우에만 적었고 URL은 포함하지
않았습니다.

## 이 부록을 사용하는 방법

- **규정**(예: GDPR, HIPAA)은 관할권과 부문 안에서 법적 구속력이 있습니다. 좋은
  실천만이 아니라 의무를 정합니다.
- **표준**(예: ISO/IEC 27001, WCAG)은 공식적이고 흔히 인증 가능한 명세입니다.
  일부는 자발적이고, 일부는 법이나 계약으로 의무화됩니다.
- **프레임워크**(예: NIST CSF, NIST AI RMF)는 위험 프로필에 맞춰 조정하는 구조화된,
  보통 자발적인 안내입니다.
- 적용 가능성은 관할권, 부문, 데이터 유형, 계약 조건에 달려 있습니다. 많은 조직이
  이 중 여럿을 동시에 충족해야 합니다.

## 보안과 프라이버시

| 표준 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | 정보 보안 관리 시스템(ISMS)의 요구 사항. | 4.1–4.6 보안과 컴플라이언스 |
| ISO/IEC 27002 | ISO / IEC | ISO/IEC 27001을 뒷받침하는 안내와 통제 집합. | 4.1–4.4 보안 |
| ISO/IEC 27017 / 27018 | ISO / IEC | 클라우드 특화 보안 통제(27017)와 클라우드의 PII 보호(27018). | 4.3 인프라와 클라우드 보안, 4.5 프라이버시 |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | 거버닝, 식별, 보호, 탐지, 대응, 복구를 중심으로 조직된 자발적 프레임워크. | 4.1, 4.4 보안 기초와 운영 |
| NIST SP 800-53 | National Institute of Standards and Technology | 정보 시스템의 보안 및 프라이버시 통제 카탈로그. | 4.3, 4.6 클라우드 보안과 컴플라이언스 |
| NIST SP 800-63 | National Institute of Standards and Technology | 디지털 신원과 인증 보증 지침. | 4.2, 4.3 애플리케이션 및 인프라 보안 |
| OWASP Top Ten | Open Worldwide Application Security Project | 주기적으로 갱신되는, 가장 중대한 웹 애플리케이션 보안 위험. | 4.2 애플리케이션 보안 |
| OWASP ASVS | Open Worldwide Application Security Project | 애플리케이션 보안을 검증하기 위한 등급별 요구 사항과 테스트. | 2.4, 4.2 테스트와 애플리케이션 보안 |
| OWASP SAMM | Open Worldwide Application Security Project | 소프트웨어 보안 프로그램을 구축하고 평가하는 성숙도 모델. | 4.1 보안 기초와 문화 |
| STRIDE | Microsoft에서 유래 | 위협을 분류하는 위협 모델링 분류 체계. | 4.2 애플리케이션 보안 |
| MITRE ATT&CK | MITRE | 탐지와 방어를 위한 공격자 전술과 기법의 지식 베이스. | 4.4 보안 운영 |
| SLSA | Open Source Security Foundation (OpenSSF) | 소프트웨어 공급망 무결성과 출처를 위한 단계별 프레임워크. | 4.2, 8.1, 10.3 공급망과 전달 |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX), OWASP (CycloneDX) | 소프트웨어 자재 명세서의 표준 형식. | 4.2, 10.3 애플리케이션 보안과 라이선스 |
| PCI DSS | PCI Security Standards Council | 결제 카드 데이터 취급의 보안 요구 사항. | 4.2, 4.5, 4.6 보안, 프라이버시, 컴플라이언스 |

## 컴플라이언스와 정부

### 미국

| 규정 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | 보호 대상 건강 정보(PHI)의 보호 장치. | 4.5, 4.6 프라이버시와 컴플라이언스 |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | 상장 기업의 재무 보고와 내부 통제 요구 사항. | 4.6, 10.2 컴플라이언스와 감사 |
| FISMA | US Congress | 연방 기관의 정보 보안 프로그램 요구 사항. | 4.3, 4.6 클라우드 보안과 컴플라이언스 |
| FedRAMP | US General Services Administration / FedRAMP PMO | 연방 기관이 쓰는 클라우드 서비스의 표준화된 보안 인가. | 4.3, 4.6 클라우드 보안과 컴플라이언스 |
| NIST SP 800-171 | National Institute of Standards and Technology | 비연방 시스템에서 비기밀 통제 정보(CUI)의 보호. | 4.6 컴플라이언스 (국방 공급망) |
| CMMC | US Department of Defence | 국방 계약자 사이버보안 성숙도 인증. | 4.6 컴플라이언스 (국방) |
| FIPS 140-3 | National Institute of Standards and Technology | 암호 모듈의 보안 요구 사항. | 4.3 인프라와 클라우드 보안 |
| CCPA / CPRA | State of California | 캘리포니아의 소비자 프라이버시 권리와 기업 의무. | 4.5 프라이버시와 데이터 보호 |

### 유럽 연합과 영국

| 규정 / 표준 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| GDPR | European Union | 개인 데이터 처리에 관한 포괄적 규정. | 4.5, 4.6 프라이버시와 컴플라이언스 |
| UK GDPR / Data Protection Act 2018 | United Kingdom | 영국의 브렉시트 이후 데이터 보호 체제. | 4.5, 4.6 프라이버시와 컴플라이언스 |
| eIDAS | European Union | 전자 식별과 신뢰 서비스를 위한 프레임워크. | 4.2, 4.3 보안 |
| NIS2 Directive | European Union | 필수 및 중요 주체의 사이버보안 의무. | 4.4, 4.6 보안 운영과 컴플라이언스 |
| DORA (Digital Operational Resilience Act) | European Union | 금융 부문의 운영 복원력 요구 사항. | 9.1, 10.2 신뢰성과 감사 |
| EU AI Act | European Union | AI 시스템의 위험 기반 규제(아래 AI 거버넌스 참조). | 6.1, 6.5 AI 전략과 책임 있는 AI |

## 접근성

| 표준 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | A/AA/AAA 적합성 수준이 있는 접근 가능한 웹 콘텐츠 지침. | 5.3 접근성, 5.1–5.6 UX와 프런트엔드 |
| WAI-ARIA | World Wide Web Consortium (W3C) | 접근 가능한 리치 인터넷 애플리케이션의 역할, 상태, 속성. | 5.3, 5.6 접근성과 프런트엔드 |
| Section 508 | US Access Board / US federal law | WCAG에 정렬된 미국 연방 ICT의 접근성 요구 사항. | 5.3 접근성 (미국 정부) |
| EN 301 549 | ETSI / CEN / CENELEC | WCAG에 정렬된 ICT 조달의 유럽 접근성 요구 사항. | 5.3 접근성 (EU 공공 부문) |
| ADA (Americans with Disabilities Act) | US Congress | 디지털 서비스에도 적용되는, 장애 차별을 금지하는 민권법. | 5.3 접근성 |
| ISO/IEC 40500 | ISO / IEC | WCAG 2.0을 공식 표준으로 국제 채택한 것. | 5.3 접근성 |

## AI 거버넌스

| 프레임워크 / 규정 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | AI 위험을 거버닝, 매핑, 측정, 관리하는 자발적 프레임워크. | 6.1, 6.5 AI 전략과 책임 있는 AI |
| ISO/IEC 42001 | ISO / IEC | AI 관리 시스템(AIMS)의 요구 사항. | 6.1, 6.5 AI 거버넌스 |
| ISO/IEC 23894 | ISO / IEC | AI 특화 위험 관리 안내. | 6.5 책임 있고 신뢰할 수 있는 AI |
| EU AI Act | European Union | AI 시스템 제공자와 배포자에 대한 위험 등급별 법적 의무. | 6.1, 6.3, 6.5 AI 애플리케이션과 거버넌스 |
| OECD AI Principles | Organisation for Economic Co-operation and Development | 정책에 영향력이 큰, 신뢰할 수 있는 AI를 위한 가치 기반 원칙. | 6.5, 10.5 책임 있는 AI와 윤리 |

## 품질과 프로세스

| 표준 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | 소프트웨어 제품 품질 모델(기능 적합성, 신뢰성, 보안 등). | 2.2, 2.4 설계와 테스트 |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | 소프트웨어 수명 주기 프로세스. | 1.4, 10.1 일하는 방식과 프로그램 관리 |
| ISO 9001 | ISO | 일반 품질 관리 시스템의 요구 사항. | 10.2 위험, 감사, 보증 |
| CMMI | ISACA / CMMI Institute | 프로세스 역량과 개선을 위한 성숙도 모델. | 10.1, 10.2 프로그램 관리와 보증 |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | 소프트웨어 팀의 네 가지 핵심 전달 성과 지표. | 8.1, 8.4, 9.1 전달, 플랫폼, 신뢰성 |
| SPACE framework | Microsoft / GitHub researchers | 개발자 생산성을 측정하는 다차원 모델. | 1.3, 8.4 성장과 개발자 경험 |
| ITIL | AXELOS / PeopleCert | IT 서비스 관리 실천의 프레임워크. | 9.1, 9.3 신뢰성과 인시던트 관리 |

## 아키텍처

| 표준 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | 아키텍처 기술과 관점의 표준. | 2.7, 3.1 문서화와 아키텍처 기초 |
| TOGAF | The Open Group | 엔터프라이즈 아키텍처 프레임워크와 개발 방법. | 3.1, 10.1 아키텍처와 포트폴리오 관리 |
| C4 model | Community (Simon Brown) | 소프트웨어 아키텍처를 시각화하는 4단계 접근. | 2.7, 3.1 문서화와 아키텍처 |
| arc42 | Community (Starke / Hruschka) | 아키텍처 문서를 구조화하는 템플릿. | 2.7, 3.1 문서화와 아키텍처 |
| ADRs | Community practice | 중요한 아키텍처 결정의 가벼운 기록. | 1.5, 2.7, 3.1 의사 결정과 문서화 |

## 클라우드와 DevOps

| 표준 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | 시스템과 클라우드를 위한 합의 기반의 안전한 구성 기준선. | 4.3, 8.2 인프라 보안과 IaC |
| CNCF landscape and projects | Cloud Native Computing Foundation | 클라우드 네이티브 컴퓨팅(예: Kubernetes)의 생태계와 표준. | 8.3 컨테이너와 클라우드 네이티브 |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | 컨테이너 이미지와 런타임 형식의 개방형 표준. | 8.3 컨테이너와 클라우드 네이티브 |
| OpenTelemetry | Cloud Native Computing Foundation | 텔레메트리(트레이스, 지표, 로그)의 벤더 중립 표준. | 9.2 관측 가능성과 모니터링 |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | 코드형 정책을 위한 범용 정책 엔진. | 4.6, 8.2, 8.3 컴플라이언스, IaC, 오케스트레이션 |
| SRE practices | Google (widely adopted) | 신뢰할 수 있는 서비스를 운영하는 SLI/SLO/오류 예산 기반 접근. | 9.1 사이트 신뢰성 엔지니어링 |
| FinOps Framework | FinOps Foundation | 클라우드 재무 관리와 비용 책임성의 실천. | 9.4 비용, 지속가능성, 그린 소프트웨어 |

## 데이터

| 표준 / 프레임워크 | 발행 기관 | 범위 (한 줄) | 주요 장 / 영역 |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | 데이터 관리 규율을 조직한 지식 체계. | 7.1 데이터 전략과 거버넌스 |
| ISO/IEC 38505 | ISO / IEC | 조직 자산으로서의 데이터 거버넌스. | 7.1 데이터 거버넌스 |
| ISO 8000 | ISO | 데이터 품질과 마스터 데이터 표준. | 7.1, 7.2 데이터 거버넌스와 엔지니어링 |
| Data mesh | Community (Zhamak Dehghani) | 제품으로서의 데이터에 대한 분산되고 도메인 지향적인 접근. | 7.1, 7.2 데이터 전략과 엔지니어링 |
| DCAM | EDM Council | 데이터 관리 역량 평가 모델. | 7.1 데이터 전략과 거버넌스 |

## 범위와 변화에 관한 메모

표준과 규정은 진화합니다. 버전 번호(예: WCAG 2.1 대 2.2, ISO 개정 연도)와 통제
카탈로그는 시간이 지나며 바뀌고, 새 법(부문별 AI와 복원력 규정 같은)이 계속
나타납니다. 이 부록을 출발점 지도로 다루십시오. 컴플라이언스나 조달 결정에 어떤
항목이든 의존하기 전에 현재 버전, 관할권, 적용 가능성을 확인하십시오. 가이드북의
장과 이 부록이 세부 사항에서 다르면 권위 있는 출처 문서가 언제나 우선합니다.


---

# 추천 도서

이 부록은 가이드북의 모든 영역에 걸친 엄선되고 주석이 달린 읽기 목록입니다. 규모에서
실천을 형성한 작품을 선호합니다. 인정받는 고전, 엄밀한 참고서, 큰 팀, 기업, 정부
팀이 그에 대해 평가받는 표준과 보고서입니다.

각 항목은 제목과 저자에 이어 그것이 왜 중요한지 한 문장을 줍니다. 목록은 책의 열
부 아래 조직되어 있습니다. 선택적으로 읽으십시오. 책장 전체가 아니라 지금 겪는 고통에
가장 가까운 두세 권을 고르십시오. 작품이 영역에 걸치면 가장 유용한 곳에 두었으며,
여러 부에 속하는 것도 많습니다.

표준에 관한 메모: NIST, OWASP, W3C/WCAG, ISO, DORA 프로그램 같은 기관은 주기적으로
개정되는 살아 있는 문서를 발행합니다. 현재 버전을 인용하고 읽으십시오. 아래 주석은
그것들의 변치 않는 목적을 기술합니다.

## 기초: 문화, 사람, 프로세스

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. 전달 성과가 조직 성과를 예측함을 보이고 그것을 측정하는 지표(지금의 DORA)를 정의한 연구의 기초.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. 흐름, 진행 중인 작업, DevOps의 "세 가지 길"을 리더와 회의론자 모두에게 직관적으로 만드는 비즈니스 소설.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. 좋은 소프트웨어를 만드는 조직을 설계하는 실용적 어휘(스트림 정렬, 플랫폼, 이네이블링, 복잡한 하위 시스템 팀).
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. 팀 규모 정하기, 조직 성장 관리, 엔지니어링 리더십의 반복되는 결정을 위해 현장에서 검증된 프레임워크.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. 관리자가 되지 않고 영향력을 원하는 사람을 위한 스태프 이상의 원형과 기술 리더십 경로를 정의.
- **The Manager's Path**. Camille Fournier. 커리어 사다리와 관리로의 전환을 닻 내리는, 테크 리드에서 임원까지의 단계별 안내.
- **The Staff Engineer's Path**. Tanya Reilly. 기술 리더십, 영향력, 권위 없는 조타의 일상 업무에 초점을 둔 스태프 이상 문헌의 짝.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. 소프트웨어의 핵심 문제가 기술적이 아니라 사회학적이라는 오래가는 논증.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. 인력 배치와 일정을 여전히 다스리는 브룩스의 법칙과 본질적 복잡성 대 우연적 복잡성 구별의 기원.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. 비난 없는 문화와 실패에서 배우는 것을 가능하게 하는 안전의 연구적 기초.
- **Thinking, Fast and Slow**. Daniel Kahneman. 구조화된 면접, 보정, 정직한 의사 결정에 필수적인 인지 편향의 결정적 설명.

## 프로그래밍 장인 정신과 코드 품질

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. 장인 정신이 무엇을 뜻하는지 정의하는 전문가 습관(DRY, 직교성, 트레이서 불릿)의 기초 카탈로그.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. 행위를 보존하는 변환의 정전적 카탈로그와 지속적이고 테스트가 뒷받침하는 코드 개선의 규율.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. 많은 팀의 리뷰 기대를 형성하는, 이름 짓기, 함수, 가독성에 대한 널리 쓰이는(그리고 논쟁되는) 표준.
- **Code Complete**. Steve McConnell. 프로그래밍 품질의 철저한 기준선으로 남아 있는, 증거를 참조한 구축 실천의 포괄적 핸드북.
- **Test-Driven Development: By Example**. Kent Beck. 레드-그린-리팩터 주기와 테스트 우선 설계에 대한 원조이자 실습형 입문.
- **Working Effectively with Legacy Code**. Michael Feathers. 테스트가 없는 코드에 테스트를 더하고 안전하게 바꾸는 결정적 도구 모음이며 오래 사는 시스템에 필수.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. 외부에서 안으로의 TDD, 모킹, 테스트로 설계를 진화시키는 것의 실제 시연.
- **A Philosophy of Software Design**. John Ousterhout. 일부 "클린 코드" 정통에 생산적으로 도전하는, 복잡성, 깊은 모듈, 정보 은닉에 대한 날카롭고 주관 있는 논의.

## 아키텍처와 시스템

- **Designing Data-Intensive Applications**. Martin Kleppmann. 규모에서의 저장, 복제, 분할, 일관성, 스트림 처리의 상충에 관한 단일 최고의 현대적 참고서.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. 아키텍처 스타일, 특성, 아키텍트의 역할과 의사 결정에 대한 폭넓고 최신의 조망.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. 분산 아키텍처 상충, 서비스 세분성, 데이터 소유권에 대한 결정 중심의 논의.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. 적합성 함수와 시간에 따라 안전하게 변하도록 설계된 아키텍처를 소개.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. 바운디드 컨텍스트, 유비쿼터스 언어, 애그리거트, 곧 현대 서비스 설계 어휘의 기원.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. 분해, 서비스 경계, 배포, 마이크로서비스의 조직적 함의에 대한 참고서.
- **Monolith to Microservices**. Sam Newman. 위험한 일괄 재작성 없이 스트랭글러 피그와 추상화를 통한 브랜치 같은 점진적 분해의 패턴 카탈로그.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. 기업 시스템에 공유 언어를 준 이름 붙은 패턴(리포지터리, 작업 단위 등) 참고서.
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. 이벤트 주도 및 비동기 아키텍처를 받치는 메시징 패턴의 결정적 카탈로그.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. 실제 프로덕션에서 살아남는 시스템을 위한 서킷 브레이커, 벌크헤드 등 안정성 패턴의 출처.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). 객체 지향 패턴의 역사적으로 결정적인 카탈로그이자 공유 설계 어휘.

## 보안, 프라이버시, 신뢰

- **Threat Modelling: Designing for Security**. Adam Shostack. STRIDE와 구조화된 위협 모델링을 일상적 엔지니어링 실천으로 다루는 실용적이고 포괄적인 안내.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. 실제 시스템이 어떻게 실패하고 공격에 저항하는 시스템을 어떻게 만드는지에 대한 백과사전적 참고서.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. 브라우저 보안 모델과 웹 플랫폼이 순진한 가정을 배신하는 미묘한 방식의 엄밀한 안내.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. 암호를 올바르게 쓰고 흔하고 위험한 실수를 피하는 실무자 안내.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). 보안과 신뢰성을 처음부터 설계에 넣는 얽힌 속성으로 보는 구글의 종합.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. 절대 신뢰하지 말고 항상 검증하는 네트워크 아키텍처의 원칙과 메커니즘에 대한 분명한 설명.
- **OWASP Top 10**. OWASP Foundation. 전 세계 정책과 감사가 참조하는, 가장 중대한 웹 애플리케이션 보안 위험의 합의된 기준선.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. 계약과 인수 기준에 적합한 보안 요구 사항의 등급별 시험 가능한 체크리스트.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. 미국 연방 보안의 중심에 있고 FedRAMP와 FISMA 인가의 바탕인 통제 카탈로그.
- **NIST Cybersecurity Framework (CSF)**. NIST. 보안 프로그램을 조직하는 널리 채택된 식별-보호-탐지-대응-복구 구조.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. 대부분의 기업과 정부 제로 트러스트 프로그램을 닻 내리는 참조 정의와 참조 아키텍처.

## UX, UI, 제품 디자인

- **The Design of Everyday Things**. Don Norman. 물리적 대상을 훨씬 넘어 적용되는 어포던스, 시그니파이어, 피드백, 인간 중심 설계에 대한 기초 텍스트.
- **Don't Make Me Think, Revisited**. Steve Krug. 자명한 사용성과 싸고 잦은 사용성 테스트의 가치에 대한 간결하고 오래가는 논증.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. 상호작용 설계, 페르소나, 목표 지향 설계에 대한 포괄적 참고서.
- **Design Systems: A Practical Guide**. Alla Kholmatova. 일관되고 재사용 가능한 구성 요소 시스템과 그 뒤의 공유 언어를 만드는 일에 대한 근거 있는 설명.
- **Refactoring UI**. Adam Wathan and Steve Schoger. 정식 교육 없이 인터페이스를 디자인하는 엔지니어를 위한 시각적 완성도의 실용적이고 예시 중심의 안내.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. 쉬운 말과 과업 중심 콘텐츠 설계의 결정적 안내.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. 인간 능력의 전 범위에 동작하는 인터페이스를 만드는 실용적 동반서.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. 접근성 표준과 좋은 사용자 경험 사이의 원칙 중심 다리.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. 대부분의 접근성 법의 바탕인 국제적으로 참조되는 표준(인지 가능, 운용 가능, 이해 가능, 견고).
- **U.S. Web Design System (USWDS)**. U.S. government. 규모에서의 공공 서비스를 위해 만든, 접근 가능하고 표준 기반인 디자인 시스템의 실제 사례.

## 인공지능과 머신러닝

- **Designing Machine Learning Systems**. Chip Huyen. 데이터, 피처, 배포, 모니터링에 걸쳐 프로덕션 ML 시스템을 종단 간 만드는 일에 대한 선도적인 실용 안내.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. SRE 규율(SLO, 모니터링, 인시던트 대응)을 머신러닝 시스템으로 확장.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. 현대 신경망의 바탕이 되는 이론과 방법에 대한 표준 학술 참고서.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. 거대 파운데이션 모델 위에 만든 애플리케이션을 설계, 평가, 운영하는 최신 안내.
- **Weapons of Maths Destruction**. Cathy O'Neil. 알고리즘 책임성과 검토되지 않은 모델의 실제 해악에 대한 생생한 사례로, 공공 부문 AI에 필수.
- **Interpretable Machine Learning**. Christoph Molnar. 모델과 그 예측에 대한 설명 가능성 방법의 포괄적이고 자유롭게 이용할 수 있는 참고서.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. 정책과 조달에서 점점 인용되는, AI 위험을 거버닝, 매핑, 측정, 관리하는 참조 프레임워크.

## 데이터, 분석, 통찰

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball and Margy Ross. 분석을 위한 스타 스키마와 차원 모델링의 정전적 참고서.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. 규모에서 신뢰할 수 있고 행동 가능한 결과를 내는 실험을 운영하는 권위 있는 안내.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. 현대 데이터 수명 주기와 그 뒤의 엔지니어링 실천에 대한 벤더 중립 지도.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. 규모에서 데이터를 조직하는 도메인 지향적이고 제품 중심적인 접근의 창립 텍스트.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. 정직하고 분명한 데이터 시각화와 의사 결정자에게 통찰을 전달하는 실용적 안내.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. 그래픽 무결성, 데이터-잉크, 데이터를 정직하게 보이는 윤리에 대한 기초 저작.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. 데이터 거버넌스, 스튜어드십, 품질, 카탈로깅의 포괄적 참조 프레임워크.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. 상관에서 방어 가능한 결정으로 나아가는 데 필수적인 인과 추론의 읽기 쉬운 입문.

## 자동화, DevOps, 플랫폼 엔지니어링

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. "세 가지 길"을 흐름, 피드백, 지속적 학습의 구체적 실천으로 옮기는 포괄적 플레이북.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. 배포 파이프라인, 자동화, 소프트웨어를 안전하고 자주 릴리스하는 것에 대한 기초 텍스트.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. 인프라를 소프트웨어로 다루는 것(모듈, 테스트, 불변성, 드리프트)에 대한 참고서.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (기초를 보십시오.) 플랫폼 팀과 그들이 제공하는 개발자 경험을 형성하는 데도 필수.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Kubernetes 위에 클라우드 네이티브 애플리케이션을 설계하기 위한 재사용 가능한 패턴 카탈로그.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. 테스트, 리뷰, 도구, 의존성 관리 같은 엔지니어링 실천이 수십 년에 걸쳐 수만 명의 엔지니어로 어떻게 확장되는가.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). 이식 가능하고 확장 가능한 클라우드 네이티브 서비스를 만드는 간결하고 영향력 있는 선언.
- **DORA State of DevOps Report**. DORA / Google Cloud (annual). 네 가지 핵심 전달 지표와 성과를 이끄는 역량 뒤의 지속적인 연구 프로그램.

## 운영, 신뢰성, 관측 가능성

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). SLI, SLO, 오류 예산, 신뢰성을 엔지니어링하는 규율을 정의한 기초 텍스트.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). 실용적 예시, 실제 SLO, 구현 안내가 있는 실습형 동반서.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. 관측 가능성, 높은 카디널리티 데이터, 프로덕션의 미지의 미지를 디버깅하는 것의 현대적 정의.
- **Implementing Service Level Objectives**. Alex Hidalgo. SLO와 오류 예산을 설계, 측정, 잘 쓰는 것에 대한 철저하고 실용적인 안내.
- **Release It!**. Michael T. Nygard. (아키텍처를 보십시오.) 프로덕션 안정성 패턴과 복원력 있는 시스템 운영에도 기초적.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. 성장하는 시스템의 수요를 예측하고 용량을 계획하는 데이터 주도 접근.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. 시스템 복원력에 대한 확신을 쌓으려고 실패를 의도적으로 주입하는 것의 결정적 논의.
- **Google SRE Book, Chapter on Postmortems**. Google. 비난 없는 사후 검토와 인시던트에서 배우는 것의 널리 모방되는 모델.

## 기업, 정부, 공익

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. 오픈 소스가 실제로 어떻게 지속되는지와, 기업이 의존하는 의존성 뒤의 메인테이너 부담에 대한 필수 연구.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. 공공 부문 기술이 왜 실패하며 전달 중심 개혁이 어떻게 고칠 수 있는지에 대한 냉철한 설명.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. 계획이 아니라 전달함으로써 공공 서비스를 변혁하는 것에 대한 영국 정부 디지털 서비스의 교훈.
- **Project to Product**. Mik Kersten. 큰 기업을 프로젝트 기반 자금에서 지속되는 제품 가치 흐름으로 옮기는 흐름 프레임워크.
- **Escaping the Build Trap**. Melissa Perri. 조직이 산출을 성과로 착각하는 방식과 제품 관리가 그것을 어떻게 고치는지로, 포트폴리오와 프로그램 거버넌스에 직접 관련.
- **U.S. Digital Services Playbook**. U.S. Digital Service. 효과적이고 사용자 중심의 정부 디지털 서비스를 전달하기 위한 간결한 플레이 모음.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. 다른 정부가 널리 모방하는, 좋은 공공 서비스를 만들기 위한 공개된 실제 표준.
- **NIST SP 800-37: Risk Management Framework**. NIST. 미국 연방 시스템의 운영 권한(ATO)과 지속적 모니터링 뒤의 프로세스 프레임워크.
- **The FinOps Foundation Framework**. FinOps Foundation. 재무와 엔지니어링 전반에 걸친 클라우드 비용 가시성, 최적화, 책임성의 참조 모델.

## 이 목록을 사용하는 방법

- **고통에서 시작하십시오.** 배포가 느리고 무섭다면 다른 무엇보다 먼저 *Accelerate*, *Continuous Delivery*, *DORA* 보고서를 읽으십시오.
- **스프린트가 아니라 십 년을 위해 읽으십시오.** 특정 도구 버전에 묶인 것보다 오래가는 원칙을 설명하는 작품을 선호하십시오.
- **표준의 현재 판을 확인하십시오.** NIST, OWASP, WCAG, ISO, DORA는 간행물을 개정합니다. 항상 최신 릴리스로 작업하고 자체 정책에 버전을 적어 두십시오.
- **공유 책장을 만드십시오.** 이 중 두세 권을 함께 읽은 팀은 어휘와 참조점을 공유하므로 덜 다투고 더 빨리 결정합니다.
- **12.5장도 보십시오.** 참조 표준과 프레임워크의 전체 색인이 있고, **12.6장**에는 이 작품들이 기술하는 실천의 도입 순서를 정하는 방법이 있습니다.
