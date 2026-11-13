# 12.3 سانچے

یہ سانچے copy-paste کے لیے تیار نقطۂ آغاز ہیں۔ کسی بھی سانچے کو اپنی wiki، ریپوزٹری، یا ٹکٹنگ سسٹم میں اٹھائیں اور بریکٹ والے placeholders بھر دیں۔ ترچھے نوٹس اور inline تبصرے وضاحت کرتے ہیں کہ ہر حصے میں کیا ہونا چاہیے؛ حصہ بھر جانے کے بعد انہیں حذف کر دیں۔ سانچے ہلکے رکھیں: جس سانچے کو مکمل کرنے سے چھوڑنا تیز ہو وہ استعمال نہیں ہوگا۔ سرخیاں اور حصے اپنے ادارے کے مطابق ڈھالیں، مگر ہر حصے کا مقصد محفوظ رکھیں۔

نیچے استعمال شدہ چند روایات:

- `[square brackets]` میں متن ایسا placeholder ہے جسے بدلنا ہے۔
- _italics_ یا `<!-- comments -->` میں متن وہ رہنمائی ہے جسے حذف کرنا ہے۔
- مکمل دستاویز کو اتنا مختصر رکھیں جتنا وہ اپنے سوالات کا جواب دیتے ہوئے ہو سکے۔

## Architecture Decision Record (ADR)

```markdown
# ADR [NNNN]: [فیصلے کا مختصر عنوان]

- Status: [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]
- Date: [YYYY-MM-DD]
- Deciders: [نام یا کردار]
- Consulted: [نام یا کردار]

## Context

<!-- وہ مسئلہ، قوت، یا پابندی کیا ہے جو اس فیصلے کو چلا رہی ہے؟
     حقائق اور تقاضے غیر جانب داری سے بیان کریں۔ صرف وہ شامل کریں جو
     مستقبل کے پڑھنے والے کو سمجھنے کے لیے چاہیے کہ فیصلہ کیوں ضروری تھا۔ -->

## Decision

<!-- انتخاب ایک یا دو واضح جملوں میں بیان کریں: "ہم ... کریں گے" -->

## Alternatives considered

<!-- وہ حقیقت پسند اختیارات فہرست کریں جو آپ نے تولے اور ہر ایک کیوں
     چنا گیا یا نہیں۔ یہاں کم از کم دو متبادل ہونے چاہییں۔ -->

- Option A: [خلاصہ]؛ رد کیا کیونکہ [وجہ]۔
- Option B: [خلاصہ]؛ رد کیا کیونکہ [وجہ]۔
- Chosen option: [خلاصہ]؛ چنا کیونکہ [وجہ]۔

## Consequences

<!-- فیصلے کے ایماندار نتائج، اچھے اور برے دونوں۔ -->

- Positive: [حاصل ہونے والے فوائد]
- Negative: [قبول کی گئی لاگتیں، خطرے، یا حدود]
- Follow-up: [migrations، نیا کام، یا فیصلے جو یہ ٹرگر کرتا ہے]

## Related

<!-- پچھلے ADRs، RFCs، ٹکٹس، یا دستاویزات کے لنک جن سے یہ متعلق ہے۔ -->
```

## RFC / ڈیزائن دستاویز

```markdown
# RFC: [عنوان]

- Author(s): [نام]
- Status: [Draft | In review | Approved | Rejected | Implemented]
- Reviewers: [نام یا کردار]
- Created: [YYYY-MM-DD]
- Last updated: [YYYY-MM-DD]
- Ticket / tracking: [لنک]

## Summary

<!-- ایک پیراگراف: یہ کیا تجویز کرتا ہے اور کیوں اہم ہے۔ پڑھنے والے کو
     صرف اس حصے سے جوہر سمجھ آنا چاہیے۔ -->

## Problem and motivation

<!-- ہم کون سا مسئلہ حل کر رہے ہیں؟ کون متاثر ہے؟ اگر ہم کچھ نہ کریں تو
     کیا ہوتا ہے؟ متعلقہ پس منظر اور پابندیاں شامل کریں۔ -->

## Goals and non-goals

- Goals: [کامیابی کیسی دکھتی ہے، جہاں ممکن ہو قابل پیمائش]
- Non-goals: [واضح طور پر دائرے سے باہر، دائرے کے پھیلاؤ کو روکنے کو]

## Proposed design

<!-- دستاویز کا مرکز۔ طریقہ، فن تعمیر، ڈیٹا ماڈل، انٹرفیسز، اور کلیدی
     بہاؤ بیان کریں۔ جہاں وضاحت ہو وہاں خاکے استعمال کریں۔ بیان کریں کہ
     یہ کیسے کام کرتا ہے، صرف یہ کیا ہے نہیں۔ -->

## Alternatives considered

<!-- دوسرے طریقے اور انہیں کیوں نہیں چنا گیا۔ پڑھنے والے کو دکھاتا ہے
     کہ ڈیزائن کی گنجائش کھوجی گئی۔ -->

## Impact and risks

- Security and privacy: [مضمرات اور تخفیف]
- Performance and scale: [متوقع بوجھ اور رویہ]
- Operability: [مانیٹرنگ، ناکامی کے طریقے، rollout، rollback]
- Cost: [انفراسٹرکچر یا لائسنسنگ کا اثر]
- Backward compatibility: [migration اور deprecation]

## Testing and rollout plan

<!-- تبدیلی کی توثیق اور محفوظ ریلیز کیسے ہوگی۔ -->

## Open questions

<!-- حل نہ ہوئے مسائل جن پر آپ چاہتے ہیں کہ ریویو کرنے والے رائے دیں۔ -->
```

## Postmortem / واقعے کا ریویو (بلا الزام)

```markdown
# Postmortem: [واقعے کا عنوان]

- Incident ID: [ID]
- Date of incident: [YYYY-MM-DD]
- Authors: [نام]
- Status: [Draft | Final]
- Severity: [SEV1 | SEV2 | SEV3]

> یہ ریویو بلا الزام ہے۔ ہم نظاموں اور معاون عوامل پر توجہ دیتے ہیں،
> افراد پر نہیں۔ مقصد سیکھنا اور دوبارہ ہونے سے روکنا ہے۔

## Summary

<!-- دو یا تین جملے: کیا ہوا، اثر، اور حل، غیر ماہر کے پڑھنے کے قابل۔ -->

## Impact

- Duration: [آغاز کے وقت سے بحالی کے وقت تک، ٹائم زون کے ساتھ]
- Users affected: [دائرہ اور تعداد]
- Business impact: [آمدنی، SLA، ساکھ، یا دیگر]

## Timeline

<!-- واقعات کی timestamp شدہ، حقائق پر مبنی ترتیب۔ detection، escalation،
     کلیدی اعمال، اور بحالی شامل کریں۔ -->

- [HH:MM] [واقعہ]
- [HH:MM] [واقعہ]

## Contributing factors

<!-- حالات کی زنجیر جو واقعے تک لے گئی۔ واحد بنیادی وجہ کی بجائے
     "معاون عوامل" کو ترجیح دیں۔ -->

## Detection and response

- یہ کیسے detect ہوا؟ [alert، گاہک کی رپورٹ، وغیرہ]
- ردعمل میں کیا مددگار تھا؟
- ردعمل کو کس نے سست کیا؟

## What went well

<!-- مؤثر اعمال اور کام کرنے والے حفاظتی انتظامات کو تسلیم کریں۔ -->

## Action items

<!-- مخصوص، ملکیت والے، اور تاریخ شدہ۔ روک تھام، detection، اور تخفیف کو
     مخاطب کریں۔ انہیں معمول کے backlog میں ٹریک کریں۔ -->

| Action | Owner | Due date | Type (prevent/detect/mitigate) | Ticket |
|--------|-------|----------|--------------------------------|--------|
| [عمل] | [نام] | [تاریخ] | [قسم] | [لنک] |

## Lessons learned

<!-- وسیع ادارے کو کیا سبق لینا چاہیے۔ -->
```

## Threat model (STRIDE پر مبنی)

```markdown
# Threat model: [نظام یا فیچر کا نام]

- Author(s): [نام]
- Date: [YYYY-MM-DD]
- Reviewers: [سیکیورٹی رابطہ، مالکان]
- Scope: [کیا ڈھکا ہے اور کیا نہیں]

## System overview

<!-- نظام، اس کے مقصد، اور اس کے صارفین کی مختصر تفصیل۔ -->

## Assets

<!-- حفاظت کے لائق کیا ہے: ڈیٹا، credentials، فعالیت، ساکھ۔ ہر ایک کی
     حساسیت نوٹ کریں۔ -->

## Trust boundaries and data flow

<!-- اجزا، ڈیٹا اسٹورز، بیرونی entities، اور وہ حدیں بیان یا خاکہ بند
     کریں جہاں اعتماد بدلتا ہے۔ -->

## Threats (STRIDE)

<!-- ہر عنصر کے لیے STRIDE زمروں پر غور کریں۔ ہر معتبر خطرہ، اس کا
     خطرہ، اور تخفیف یا قبول شدہ خطرہ ریکارڈ کریں۔ -->

| Threat | STRIDE category | Affected element | Risk (L/M/H) | Mitigation | Status |
|--------|-----------------|------------------|--------------|------------|--------|
| [خطرہ] | Spoofing | [عنصر] | [خطرہ] | [کنٹرول] | [open/mitigated/accepted] |
| [خطرہ] | Tampering | [عنصر] | [خطرہ] | [کنٹرول] | [حالت] |
| [خطرہ] | Repudiation | [عنصر] | [خطرہ] | [کنٹرول] | [حالت] |
| [خطرہ] | Information disclosure | [عنصر] | [خطرہ] | [کنٹرول] | [حالت] |
| [خطرہ] | Denial of service | [عنصر] | [خطرہ] | [کنٹرول] | [حالت] |
| [خطرہ] | Elevation of privilege | [عنصر] | [خطرہ] | [کنٹرول] | [حالت] |

## Assumptions and dependencies

<!-- جن سیکیورٹی مفروضوں پر انحصار ہے اور جن بیرونی کنٹرولز پر بھروسہ ہے۔ -->

## Open issues and follow-up

<!-- وہ خطرے جنہیں مزید کام چاہیے، ٹکٹس کے طور پر ٹریک شدہ۔ -->
```

## Runbook

```markdown
# Runbook: [کام یا صورت کا نام]

- Service: [سروس کا نام]
- Owner: [ٹیم]
- Last reviewed: [YYYY-MM-DD]
- Related alerts: [alert کے نام]

## Purpose

<!-- یہ runbook کب استعمال کرنا ہے اور یہ کیا حاصل کرتا ہے۔ -->

## Prerequisites

<!-- شروع کرنے سے پہلے درکار رسائی، آلات، اور اجازتیں۔ -->

## Detection / symptoms

<!-- آپریٹر کیا مشاہدہ کرتا ہے: alerts، غلطی کی علامات، ڈیش بورڈز۔ -->

## Diagnosis

<!-- مسئلے کی تصدیق اور وجہ محدود کرنے کی قدم بہ قدم جانچیں۔ درست
     commands، queries، یا ڈیش بورڈ کے لنک شامل کریں۔ -->

1. [قدم اور متوقع نتیجہ]
2. [قدم اور متوقع نتیجہ]

## Resolution

<!-- ٹھیک یا کم کرنے کے ٹھوس، ترتیب وار قدم۔ کوئی بھی قدم جو خطرناک یا
     ناقابل واپسی ہو اور کامیابی کی توثیق کیسے ہو نوٹ کریں۔ -->

1. [قدم]
2. [بحالی کی توثیق]

## Rollback

<!-- اگر حل معاملہ بگاڑے تو اعمال کو کیسے الٹنا ہے۔ -->

## Escalation

<!-- کس سے رابطہ کریں اور کب escalate کریں۔ ثانوی on-call، مالک ٹیم، اور
     فروخت کنندہ کے رابطے۔ -->

## References

<!-- ڈیش بورڈز، متعلقہ runbooks، فن تعمیر کی دستاویزات۔ -->
```

## سروس README / سروس کیٹلاگ کا اندراج

```markdown
# [سروس کا نام]

- Owner team: [ٹیم]
- On-call: [rotation کا لنک]
- Tier / criticality: [Tier 1 | 2 | 3]
- Repository: [لنک]
- Status: [Active | Deprecated]

## What it does

<!-- ایک پیراگراف سروس کی ذمہ داری اور اس کے صارفین پر۔ -->

## Architecture

<!-- کلیدی اجزا، انحصار (upstream اور downstream)، اور ڈیزائن دستاویز یا
     خاکے کا لنک۔ -->

## Interfaces

- APIs / endpoints: [specification کا لنک]
- Events published / consumed: [topics]
- Data stores: [ڈیٹا بیس، caches، buckets]

## Runtime and deployment

- Environments: [dev, staging, prod]
- How to deploy: [پائپ لائن کا لنک اور عمل]
- Configuration and feature flags: [کہاں اور کیسے]

## Observability

- Dashboards: [لنک]
- Alerts: [لنک]
- Logs: [کہاں ملیں گے]
- SLOs: [لنک]

## Operations

- Runbooks: [لنک]
- Common tasks: [scaling، restart، backfill]
- Known issues and limitations: [نوٹس]

## Getting started (نئے شراکت داروں کے لیے)

<!-- مقامی طور پر build، ٹیسٹ، اور چلانے کا طریقہ۔ -->

## Contacts

- Slack / chat channel: [لنک]
- Escalation: [راستہ]
```

## SLO / error-budget کی پالیسی

```markdown
# SLO اور error-budget کی پالیسی: [سروس یا سفر کا نام]

- Owner: [ٹیم]
- Effective date: [YYYY-MM-DD]
- Review cadence: [مثلاً سہ ماہی]

## Service level indicators (SLIs)

<!-- ہر SLI درست متعین کریں: ناپی جانے والی مقدار، کیسے ناپی جاتی ہے، اور
     کہاں سے (مثالی طور پر صارف کے نقطۂ نظر سے)۔ -->

| SLI | Definition | Data source |
|-----|-----------|-------------|
| Availability | [مثلاً کامیاب درخواستیں / کل درخواستیں] | [ماخذ] |
| Latency | [مثلاً X ms سے کم درخواستوں کا تناسب] | [ماخذ] |

## Objectives (SLOs)

| SLI | Target | Measurement window |
|-----|--------|--------------------|
| Availability | [مثلاً 99.9%] | [مثلاً rolling 28 دن] |
| Latency | [مثلاً 95% 300ms سے کم] | [rolling 28 دن] |

## Error budget

<!-- اجازت شدہ ناقابل اعتمادی: 100% منفی ہدف، کھڑکی پر۔ بجٹ ٹھوس اصطلاحات
     میں بیان کریں (مثلاً منٹ/ماہ)۔ -->

- Budget: [اخذ شدہ الاؤنس]

## Policy when the budget is exhausted

<!-- متفقہ نتائج۔ انہیں ٹھوس اور نافذ کرنے کے قابل بنائیں۔ -->

- [مثلاً بجٹ بحال ہونے تک غیر نازک فیچر ریلیزز منجمد کریں۔]
- [مثلاً اگلے منصوبہ بندی کے چکر میں قابل اعتمادی کے کام کو ترجیح دیں۔]
- [مثلاً اگر مسلسل دو کھڑکیوں میں خلاف ورزی ہو تو انجینئرنگ قیادت تک escalate کریں۔]

## Policy when the budget is healthy

<!-- ٹیم کون سا اضافی خطرہ لے سکتی ہے، مثلاً تیز rollouts۔ -->

## Alerting

<!-- اس SLO سے جڑے burn-rate کے alerts اور حدیں۔ -->
```

## خطرے کے رجسٹر کا اندراج

```markdown
## Risk: [خطرے کا مختصر عنوان]

- Risk ID: [ID]
- Date raised: [YYYY-MM-DD]
- Owner: [اس خطرے کے انتظام کا ذمہ دار نام یا کردار]
- Category: [security | operational | compliance | financial | delivery | vendor]
- Status: [Open | Mitigating | Accepted | Closed]

### Description

<!-- خطرہ یوں بیان کریں: وجہ -> واقعہ -> نتیجہ۔ کیا ہو سکتا ہے، اور یہ
     کیوں اہم ہے۔ -->

### Assessment

- Likelihood: [Low | Medium | High]
- Impact: [Low | Medium | High]
- Overall rating: [likelihood x impact سے اخذ]

### Current controls

<!-- آج پہلے سے کیا یہ خطرہ گھٹاتا ہے۔ -->

### Mitigation plan

<!-- امکان یا اثر گھٹانے کے منصوبہ بند اعمال، مالکان اور تاریخوں کے ساتھ۔
     اگر خطرہ قبول کر رہے ہیں تو ریکارڈ کریں کس نے اور کیوں قبول کیا۔ -->

| Action | Owner | Due date | Status |
|--------|-------|----------|--------|
| [عمل] | [نام] | [تاریخ] | [حالت] |

### Review

- Next review date: [YYYY-MM-DD]
- Decision / notes: [کوئی قبولیت کا دستخط یا تبدیلی]
```

## پراجیکٹ one-pager / پروڈکٹ بریف

```markdown
# [پراجیکٹ یا پروڈکٹ کا نام]: one-pager

- Sponsor: [نام]
- Lead: [نام]
- Date: [YYYY-MM-DD]
- Status: [Idea | Approved | In progress | Shipped]

## Problem

<!-- ایک پیراگراف: گاہک یا کاروباری مسئلہ، اور شہادت کہ یہ حقیقی اور حل
     کے لائق ہے۔ -->

## Audience

<!-- کس کو یہ مسئلہ ہے اور اسے حل کرنے سے کسے فائدہ ہوتا ہے۔ -->

## Proposed solution

<!-- ہم کیا بنائیں گے یا بدلیں گے اس کی مختصر تفصیل۔ ارادے کی سطح پر
     رکھیں، نفاذ کی تفصیل نہیں۔ -->

## Why now

<!-- یہ بعد میں نہیں، اب کرنے کی وجہ۔ -->

## Success metrics

<!-- ہمیں کیسے پتا چلے گا کہ یہ کام کر گیا۔ قابل پیمائش نتائج کو ترجیح دیں۔ -->

- [میٹرک اور ہدف]

## Scope

- In scope: [ہم کیا کریں گے]
- Out of scope: [ہم کیا نہیں کریں گے]

## Risks and open questions

<!-- اہم غیر یقینیاں اور انحصار۔ -->

## Rough plan and milestones

<!-- اعلیٰ سطح کے مراحل اور تقریبی وقت۔ -->

## Cost and resources

<!-- درکار لوگ، وقت، اور بجٹ۔ -->
```

## On-call handoff کے نوٹس

```markdown
# On-call handoff: [YYYY-MM-DD]

- Outgoing: [نام]
- Incoming: [نام]
- Service(s): [نام]

## Overall status

<!-- ایک لائن: پرسکون، شور بھرا، یا جاری مسئلہ۔ -->

## Open incidents

<!-- کوئی بھی فعال یا حال میں حل شدہ واقعات جو اگلے جواب دینے والے کو
     معلوم ہونے چاہییں، لنکس کے ساتھ۔ -->

- [واقعہ، حالت، اور کیا باقی ہے]

## Ongoing or planned changes

<!-- جاری ڈیپلائے، migrations، دیکھ بھال کی کھڑکیاں، یا تجربات جو alerts
     کا سبب بن سکیں۔ -->

## Noisy or flaky alerts

<!-- جو alerts چلے اور ان کا حقیقی مطلب، تاکہ اگلا شخص گمراہ نہ ہو۔ کوئی
     عارضی خاموشی اور اس کی میعاد نوٹ کریں۔ -->

## Watch items

<!-- میٹرکس یا نظام جو تشویشناک سمت میں رجحان کر رہے ہوں۔ -->

## Pending follow-ups

<!-- اگلی شفٹ کو سونپے گئے کام، ٹکٹس کے لنکس کے ساتھ۔ -->

## Notes

<!-- کچھ اور مفید: رسائی کی عجیب باتیں، فروخت کنندہ کے مسائل، سیاق۔ -->
```

## Change request (ضابطے والے change control کے لیے)

```markdown
# Change request: [تبدیلی کا عنوان]

- Change ID: [ID]
- Requester: [نام]
- Date submitted: [YYYY-MM-DD]
- Type: [Standard | Normal | Emergency]
- Priority: [Low | Medium | High]
- Status: [Submitted | Approved | Rejected | Implemented | Closed]

## Description of change

<!-- کیا بدل رہا ہے اور کیوں۔ ٹکٹ یا تقاضے کا حوالہ دیں۔ -->

## Systems and components affected

<!-- متاثرہ سروسز، ڈیٹا، ماحول، اور صارفین۔ -->

## Justification and business impact

<!-- تبدیلی کی وجہ اور نہ کرنے کا اثر۔ -->

## Risk assessment

- Risk level: [Low | Medium | High]
- Potential impact if the change fails: [تفصیل]
- Impact on security, privacy, or compliance: [تفصیل]

## Implementation plan

<!-- ترتیب وار قدم، ذمہ دار فریق، اور وقت۔ -->

## Test and validation plan

<!-- تبدیلی سے پہلے اور بعد کامیابی کی توثیق کیسے ہوگی۔ -->

## Backout / rollback plan

<!-- ناکام ہو تو تبدیلی کو کیسے الٹنا ہے، اور بحالی کا وقت۔ -->

## Schedule

- Proposed window: [آغاز اور اختتام، ٹائم زون کے ساتھ]
- Expected downtime: [دورانیہ یا کوئی نہیں]

## Approvals

| Role | Name | Decision | Date |
|------|------|----------|------|
| Change owner | [نام] | [approve/reject] | [تاریخ] |
| Technical reviewer | [نام] | [approve/reject] | [تاریخ] |
| Change advisory board | [نام] | [approve/reject] | [تاریخ] |

## Post-implementation review

<!-- نتیجہ، پیش آئے مسائل، اور آیا backout کی ضرورت پڑی۔ -->
```

## Data Protection Impact Assessment (DPIA) کا خاکہ

```markdown
# Data Protection Impact Assessment: [پروسیسنگ کی سرگرمی کا نام]

- Assessor: [نام]
- Date: [YYYY-MM-DD]
- Reviewers: [DPO / رازداری کا رابطہ]
- Status: [Draft | Reviewed | Approved]

## 1. Description of the processing

<!-- کون سا ذاتی ڈیٹا پروسیس ہوتا ہے، کیسے، کس کے ذریعے، اور کس مقصد
     کے لیے۔ جمع کرنے سے حذف تک ڈیٹا کے بہاؤ شامل کریں۔ -->

- Data subjects: [ڈیٹا کس کے بارے میں ہے]
- Data categories: [ذاتی ڈیٹا کی اقسام، کوئی خاص زمرے نوٹ کریں]
- Purposes: [ڈیٹا کیوں پروسیس ہوتا ہے]
- Recipients and processors: [کون ڈیٹا وصول یا سنبھالتا ہے]
- Retention period: [ڈیٹا کتنی دیر رکھا جاتا ہے اور حذف کا طریقہ]
- International transfers: [منزلیں اور منتقلی کا میکانزم]

## 2. Necessity and proportionality

<!-- کیا پروسیسنگ مقصد کے لیے ضروری ہے؟ کیا یہ کم سے کم دخل اندازی
     والا اختیار ہے؟ قانونی بنیاد یا اختیار کیا ہے؟ -->

- Lawful basis / authority: [ہر مقصد کی بنیاد]
- Data minimization: [ہر فیلڈ کیوں ضروری ہے]
- Accuracy and retention justification: [نوٹس]
- How data subject rights are supported: [رسائی، حذف، وغیرہ]

## 3. Consultation

<!-- مشاورت لیے گئے حصہ دار، اور جہاں متعلقہ ہو ڈیٹا کے مالک۔ -->

## 4. Risks to individuals

<!-- رازداری کے خطرات پہچانیں اور ہر ایک کی درجہ بندی کریں۔ -->

| Risk to individuals | Likelihood | Severity | Overall |
|---------------------|-----------|----------|---------|
| [مثلاً حساس ڈیٹا تک غیر مجاز رسائی] | [L/M/H] | [L/M/H] | [درجہ] |

## 5. Measures to reduce risk

<!-- ہر خطرے کے لیے، تخفیف اور اس کے بعد باقی خطرہ۔ -->

| Risk | Measure | Residual risk | Accepted by |
|------|---------|---------------|-------------|
| [خطرہ] | [کنٹرول] | [L/M/H] | [نام] |

## 6. Outcome and sign-off

- Residual risk acceptable: [Yes | No]
- Measures approved by: [نام، کردار]
- Consultation with supervisory authority required: [Yes | No]
- Review date: [YYYY-MM-DD]
```
