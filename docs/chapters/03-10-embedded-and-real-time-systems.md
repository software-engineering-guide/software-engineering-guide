# 3.10 Embedded and real-time systems

## Overview and motivation

An [embedded system](https://en.wikipedia.org/wiki/Embedded_system) is software that runs on a device rather than on a general-purpose computer. It lives inside a car, a pacemaker, a thermostat, a factory robot, or a guidance unit. The software is dedicated to that device, and the device usually has tight limits on memory, processing power, and energy. You cannot always add more resources by clicking a button in a cloud console. What you ship is often what runs for years.

A [real-time system](https://en.wikipedia.org/wiki/Real-time_computing) is one where correctness depends on timing, not just on producing the right answer. An airbag controller that computes a perfect deployment command one second too late has failed completely. Real-time work adds a hard question to every task: will this finish by its deadline, every time, under the worst case? This is a different discipline from the throughput-first thinking common in web and cloud software.

For a large organization, this matters more than it first appears. Enterprises build connected cars, medical devices, industrial controllers, and billions of [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) devices. Governments run defence platforms, avionics, power-grid controllers, and medical regulators. In these domains a software defect can injure people, halt a production line, or compromise national security. The rules here are stricter, the testing is harder, and the standards are legally binding. This chapter helps you build software that is correct, timely, safe, and secure under real constraints. It connects to software construction (chapter 2.9), distributed systems (chapter 3.3), scalability and performance (chapter 3.5), infrastructure and cloud security (chapter 4.3), and software maintenance (chapter 3.7).

## Key principles

- **Timing is a correctness requirement, not a performance nice-to-have.** A late answer can be a wrong answer.
- **Design for the worst case, not the average case.** Real-time guarantees rest on worst-case behaviour, not typical speed.
- **Determinism beats raw speed.** A predictable system that always meets its deadline beats a faster one that sometimes misses.
- **Resources are finite and fixed.** Budget memory, CPU cycles, and energy as deliberately as you budget money.
- **Safety and security are engineered in, not added later.** In regulated domains you must show your work, not just assert quality.
- **The hardware is part of the system.** You cannot reason about the software without reasoning about the chip, the sensors, and the physics.
- **Field updates are a lifecycle capability, not an afterthought.** Devices in the world need a safe way to receive fixes.

## Recommendations

### Classify each timing requirement as hard, firm, or soft

Not all deadlines are equal. A hard real-time deadline must never be missed, because a miss causes system failure or harm: think engine control or flight surfaces. A firm deadline tolerates rare misses, but a late result is useless and is discarded. A soft real-time deadline degrades value gracefully: a video frame that arrives slightly late lowers quality but causes no disaster. Label every timing-sensitive task with its class, because the effort, the testing rigor, and the cost differ enormously. Two properties describe timing behaviour. [Latency](https://en.wikipedia.org/wiki/Latency_%28engineering%29) is the delay between an event and the response. [Jitter](https://en.wikipedia.org/wiki/Jitter) is the variation in that latency from one occurrence to the next. Hard real-time systems care as much about bounding jitter as about lowering latency, because predictability is what lets you prove a deadline is always met.

### Choose your execution foundation deliberately: RTOS or bare metal

You have two main foundations. Bare-metal firmware runs directly on the hardware with no operating system, using a simple loop and interrupt handlers. It is the smallest and most predictable option, and it suits tiny devices with one clear job. A [real-time operating system](https://en.wikipedia.org/wiki/Real-time_operating_system) (RTOS) is a small operating system that schedules tasks by priority and guarantees timing bounds. It gives you multiple tasks, a scheduler, and services like timers and message queues, while keeping timing predictable. Choose an RTOS when you have several concurrent tasks with different deadlines. Choose bare metal when the device is very constrained or the timing must be provably simple. For hard real-time work, prefer a preemptive priority-based scheduler, and analyse it with a method such as rate-monotonic scheduling, which assigns priorities by task frequency and lets you prove the task set is schedulable.

### Budget memory, CPU, and power as first-class resources

Treat each scarce resource as a budget with a hard ceiling. For memory, prefer static allocation over dynamic allocation on the heap, because dynamic memory can fragment and can fail unpredictably at the worst moment. Many safety standards restrict or ban heap use after startup for exactly this reason. For CPU, measure [worst-case execution time](https://en.wikipedia.org/wiki/Worst-case_execution_time) (WCET), the longest time a task can take, and schedule against that number, not the average. For power, remember that many devices run on a battery or harvest energy, so design duty cycles, sleep states, and wake-up events to hit an energy budget that must last months or years. Write these budgets down and review them like any other requirement.

### Handle interrupts and concurrency with strict discipline

An [interrupt](https://en.wikipedia.org/wiki/Interrupt) is a hardware signal that pauses the current work to run a handler immediately. Interrupts are how devices react instantly to the world, and they are a major source of subtle bugs. Keep handlers as short as possible: acknowledge the event, stash minimal data, and defer the real work to a normal task. Because an interrupt can fire between any two instructions, you must protect shared data from [race conditions](https://en.wikipedia.org/wiki/Race_condition) with care. Use lock-free techniques, brief critical sections, or well-understood primitives, and guard against priority inversion, where a low-priority task holding a lock blocks a high-priority one. This concurrency shares the reasoning of chapter 3.3, but with tighter timing and no room for a retry.

### Write device drivers that isolate hardware detail

A [device driver](https://en.wikipedia.org/wiki/Device_driver) is the software layer that talks to a specific piece of hardware: a sensor, a radio, a motor controller. Keep hardware-specific code behind a clean interface, so the rest of your software depends on a stable abstraction rather than on register addresses. This makes the code testable off the target, easier to port when a chip goes out of stock, and simpler to reason about. Document every assumption about timing, byte order, and hardware quirks, because these are the details that cause field failures. This is the construction discipline of chapter 2.9 applied where a wrong bit can stall a motor.

### Adopt the functional-safety standard that governs your domain

If your device can harm people or property, a [functional-safety](https://en.wikipedia.org/wiki/Functional_safety) standard likely applies, and it is often the law. IEC 61508 is the general standard for the safety of electronic systems and the parent of several others. [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) governs road-vehicle safety. [DO-178C](https://en.wikipedia.org/wiki/DO-178C) governs airborne software in civil aviation. IEC 62304 governs medical-device software. For coding, [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) is a widely used set of rules that restricts risky C language features to make code safer and more analysable. These standards demand traceability from requirement to code to test, defined processes, and evidence you can hand to an auditor or a regulator. Adopt the right one early, because retrofitting the paper trail later is painful and sometimes impossible.

### Test with simulation and hardware in the loop

You cannot test embedded software the way you test a web app. Build a layered strategy. Run unit tests on a normal computer against the hardware-abstraction interface. Use simulation to model the device and its environment when real hardware is scarce or dangerous to exercise. Then use [hardware-in-the-loop](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation) (HIL) testing, where the real controller runs against a simulated version of the physical system it controls, so you can safely test fault conditions like a stuck sensor or a sudden load. Automate these tests in your pipeline so every change is checked under realistic conditions before it reaches a device.

### Design over-the-air updates and device security from day one

Devices in the field will need fixes, so plan for over-the-air (OTA) updates: a way to deliver new firmware securely over a network. A safe OTA design signs each update cryptographically, verifies the signature before installing, updates atomically, and can roll back to a known-good image if the new one fails to boot. Pair this with the security principles of chapter 4.3, adapted for constrained hardware. Use a hardware root of trust and secure boot so only signed firmware runs. Encrypt data in transit and at rest. Change default credentials and disable unused interfaces. An IoT fleet is a distributed system with a huge attack surface, and a single weak default password can compromise millions of devices at once.

## Trade-offs: pros and cons

| Choice | Pros | Cons / cost |
|---|---|---|
| RTOS | Multitasking, priority scheduling, timing services | Overhead, larger footprint, learning curve |
| Bare metal | Smallest, most predictable, full control | Hard to scale to many tasks, more manual work |
| Static allocation | Predictable, no fragmentation, safety-friendly | Less flexible, must size everything up front |
| Formal safety certification | Legal market access, rigorous evidence, higher trust | Large time and money cost, slower iteration |
| OTA updates | Fix and improve fielded devices, extend life | Update infrastructure, security burden, rollback risk |

The master trade-off is between predictability and flexibility. Everything that makes a general-purpose system convenient (dynamic memory, background garbage collection, best-effort scheduling, elastic resources) works against the guarantee that a task always finishes on time within a fixed footprint. Embedded and real-time engineering deliberately gives up flexibility to buy determinism and safety. The skill is to spend that trade only where the deadline or the risk truly demands it, and to keep the flexible, faster-moving parts (like a device's cloud back end) on the other side of a clean boundary.

## Questions to discuss with your team

1. **Do you measure jitter, or only average latency, on your timing-critical paths?** Hard real-time correctness rests on bounding the variation in response time (jitter), not just lowering the typical latency, because predictability is what lets you prove a deadline is always met. A control loop with a low average but occasional large spikes can still miss its deadline and cause harm, and the average will hide it. Bring measurements of the spread, worst case included, for each timing-critical task, and label every one as hard, firm, or soft so the testing rigor matches the consequence of a miss. Everything convenient in general-purpose systems (dynamic memory, garbage collection, best-effort scheduling) attacks predictability, so it stays out of the hard path. If you only report averages, you cannot honestly claim a hard deadline is met.

2. **Is your RTOS-or-bare-metal choice still the right one, and can you prove the task set is schedulable?** The execution foundation is a decision to revisit as the device grows: bare metal is smallest and most predictable for one clear job, while an RTOS earns its overhead once you have several concurrent tasks with different deadlines. For hard real-time work the chapter points to a preemptive priority-based scheduler analysed with a method like rate-monotonic scheduling, which lets you prove the tasks fit rather than hope they do. Bring the current task set, their frequencies, and their worst-case execution times, and check whether the schedulability actually holds or whether tasks have quietly accumulated past what the foundation can guarantee. Guard against priority inversion, where a low-priority task holding a lock stalls a high-priority one. Choosing the foundation by habit rather than by the task set is how timing guarantees silently erode.

3. **Where exactly is the boundary between the deterministic device and the flexible cloud backend, and is it clean enough to move fast on one side without endangering the other?** The chapter's master trade-off gives up flexibility to buy determinism and safety, and the skill is spending that trade only where the deadline or the risk truly demands it. A clean boundary lets the safety-critical firmware stay conservative and certified while the cloud back end iterates quickly, so the two evolve at their own safe pace. Bring your architecture and locate that seam: what must be proven deterministic and updated through a signed, verified path, versus what can change weekly on the server. Blurring the line drags cloud-style habits (dynamic allocation, best-effort timing) into the control path, or needlessly slows the back end to the firmware's cadence. Getting the boundary right is what keeps both the safety evidence and the delivery speed intact.

4. **Which functional-safety standard governs each product, and how far is the current evidence from what an auditor would accept?** The standard (IEC 61508, ISO 26262 for road vehicles, DO-178C for airborne software, IEC 62304 for medical devices) is often the law, and it demands traceability from requirement to code to test that you cannot fake at the end. For a large team the risk is that groups adopt the paper trail unevenly, so one product line is audit-ready while another discovers halfway through certification that its requirements were never traced. The competing pull is speed: full traceability and MISRA C enforcement slow day-to-day iteration, and a team under deadline pressure is tempted to defer the evidence until "later". Bring the current traceability matrix, the static-analysis findings still open, and an honest gap analysis against the target assurance level. In enterprise and government contexts, add the certification lead time and the auditor's expectations, because retrofitting evidence after design is slow, costly, and sometimes impossible, and a slipped certification can block market access entirely.

5. **If a serious defect were found in a fielded device tomorrow, how fast could you fix it safely across the whole fleet, and have you rehearsed the rollback?** A device you cannot patch becomes a permanent safety and security liability, and a physical recall costs orders of magnitude more than a signed over-the-air update. The tension is that a careless update mechanism is itself an attack surface and a bricking risk: an OTA path that installs unsigned images, or that cannot roll back a bad boot, can turn one bad release into millions of dead units. Bring your update design (cryptographic signing, signature verification before install, atomic install, automatic rollback to a known-good image), the secure-boot and hardware-root-of-trust status, and the last time anyone actually exercised a rollback on real hardware. For an enterprise or public fleet, add who is accountable for the signing keys and how you would revoke a compromised one, because a leaked key or a shared default credential can compromise the entire fleet at once.

6. **Are your memory, CPU, and power budgets written down with hard ceilings, and does your test strategy exercise both simulation and real hardware?** Real-time guarantees rest on worst-case execution time and a fixed resource footprint, not average behaviour, so an unbudgeted heap allocation or an untested worst-case load is where determinism quietly erodes. For a large team the danger is drift: tasks accumulate, memory creeps up, and nobody owns the budget until a device fails in the field after weeks of uptime. The trade-off is coverage versus cost, because a hardware-in-the-loop rig that injects faults like a stuck sensor is expensive to build, while pure simulation hides timing bugs that only appear on the real chip. Bring the documented budgets, the measured worst-case execution times against them, and evidence that your pipeline runs unit tests on the abstraction layer, simulation, and hardware-in-the-loop before a release. In regulated and government settings, tie this to the structural test coverage the standard requires, since an auditor will want proof that fault conditions were exercised, not an assurance that the average case looked fine.

## Sector lens

**Startup.** Speed and survival dominate, so pick a lightweight RTOS or a simple bare-metal loop, forbid dynamic allocation after startup, and measure the worst-case time of your one critical loop rather than chasing a certification budget you do not have. Skip formal functional-safety processes unless your market forces them, but never skip signed over-the-air updates with automatic rollback: a young company cannot survive a field recall, and a remote fix is the difference between a bad night and a dead product. Keep the device firmware small and conservative so your scarce engineers are not maintaining a pipeline they cannot afford.

**Small business.** With no embedded specialist on staff, lean on proven modules, reference designs, and vendor RTOS distributions rather than rolling your own scheduler or bootloader. Frame the build-versus-buy choice around who will patch the device for the next decade: a bought security and update stack you can rely on beats a bespoke one nobody left can maintain. Treat default passwords, open debug interfaces, and unsigned updates as the failures most likely to hurt you, because they are cheap to prevent and ruinous to discover in the field.

**Enterprise.** The problem is consistency across many product lines and teams: a shared execution-foundation policy, common resource-budget templates, enforced MISRA C and static analysis, and one certified over-the-air update and secure-boot platform so each group does not reinvent it. Budget the functional-safety and hardware-in-the-loop burden explicitly, standardize the hardware-abstraction interface so a chip going out of stock does not strand a product, and manage the fleet's timing evidence, safety artefacts, and security posture as governed assets rather than per-team folklore. A single weak default credential across the fleet is an enterprise-scale liability, so centralize credential and key management.

**Government.** Procurement rules, transparency, and public accountability shape every choice. Require suppliers to develop airborne, medical, or defence software to the governing standard (DO-178C, IEC 62304, IEC 61508) at the assurance level matching the hazard, and to hand over the traceability and structural-coverage evidence auditors will review. Demand secure boot, a hardware root of trust, and a controlled, signed field-update process, because an unverified update to a flight or grid system is unacceptable. Favour contracts that grant rights to source, safety artefacts, and the ability to re-certify with a second supplier, so a vendor going out of business does not strand a system the public depends on for decades.

## Examples

**Startup.** A small hardware startup building a battery-powered air-quality monitor writes its firmware against a lightweight RTOS with a fixed set of tasks and no dynamic allocation after startup, so the device that ships is the device that runs for years on a coin cell. Even without a certification budget, the team measures the worst-case time of its sensor-reading loop and tests the unit against injected fault conditions on a bench rig before every release. Signed over-the-air updates with automatic rollback let them fix a defect across every shipped unit, so a bad reading in the field does not mean a recall the young company could not survive.

**Enterprise.** A connected-vehicle maker builds an electronic braking controller. The hard real-time control loop runs on an RTOS with rate-monotonic scheduling and static memory, and every task carries a measured worst-case execution time. The team develops to ISO 26262 with full traceability from requirement to code to test, and enforces MISRA C with static analysis on every commit. A hardware-in-the-loop rig replays thousands of road scenarios, including injected sensor faults, before any firmware ships. Signed OTA updates let the company fix a defect across the whole fleet without a costly recall, with automatic rollback if a car fails to boot the new image.

**Government.** A national aviation authority certifies a new flight-management computer. The supplier develops the airborne software to DO-178C at the assurance level matching the hazard, producing evidence of requirement coverage and structural test coverage that auditors review. Timing is proven deterministic under worst-case load, with bounded interrupt latency and no dynamic allocation after startup. Secure boot and a hardware root of trust ensure only signed, certified firmware runs. Field updates follow a controlled, signed process, because an unverified update to a flight system is unacceptable.

## Business case: motivations, ROI, and TCO

The business case is dominated by the cost of failure and the cost of access to a market. In regulated domains, you cannot sell the product at all without the safety certification, so the process cost is simply the price of entry. Beyond that, defects in fielded hardware are extraordinarily expensive: a physical recall costs far more than a cloud hotfix, and a safety incident carries liability, regulatory penalty, and reputational harm that can end a product line. Building safety, determinism, and updateability in from the start is cheap compared with discovering their absence in the field.

Frame the return on investment around avoided recalls, faster certification, and longer device life. A robust OTA capability converts many would-be recalls into low-cost remote fixes, and each avoided recall can pay for the whole update programme. Rigorous WCET analysis and resource budgeting let you ship on cheaper hardware with confidence, lowering the per-unit cost across a large fleet. For total cost of ownership, remember these devices live for years or decades: the maintenance, security-patching, and support burden (chapter 3.7) dwarfs the initial build. Designing for updateability, clear hardware abstraction, and documented budgets is what keeps that long tail affordable.

## Anti-patterns and pitfalls

- **Optimizing for the average case.** Meeting the deadline "usually" is failing a hard real-time requirement.
- **Dynamic allocation in the control path.** Heap fragmentation causes a failure that appears only after weeks of uptime.
- **Fat interrupt handlers.** Putting heavy processing inside an interrupt blows your timing budget and creates race conditions.
- **Ignoring the standard until the audit.** Retrofitting traceability and evidence late is slow, costly, and sometimes impossible.
- **Shipping without an update path.** A device you cannot patch becomes a permanent security and safety liability.
- **Default passwords and open interfaces.** One weak credential turns an IoT fleet into a botnet.
- **Testing only on a simulator or only on hardware.** Each hides bugs the other would catch; you need both.
- **Treating the hardware as someone else's problem.** Timing, byte order, and sensor quirks are software concerns here.

## Maturity model

- **Level 1: Initiate.** Timing is hoped for, not analysed. Memory is allocated dynamically at will. No functional-safety standard is followed. Testing is manual and on-device only. Devices cannot be updated once shipped, so a field defect means a recall or a permanent liability.
- **Level 2: Develop.** Some tasks have measured timing and a basic RTOS or structured loop is in place, but practice varies team by team. Coding guidelines exist yet are not enforced. Testing includes some simulation. A manual, risky update path exists on some products and not others. Good habits are present but inconsistent, and nothing guarantees the next product line inherits them.
- **Level 3: Standardize.** Timing requirements are classified as hard, firm, or soft, and analysed with worst-case execution time and a schedulability method, documented and enforced across the organization. Resource budgets for memory, CPU, and power are written down with hard ceilings. The governing functional-safety standard is followed with traceability from requirement to code to test, and MISRA C or an equivalent is enforced by static analysis on every commit. Hardware-in-the-loop testing runs in the pipeline. Signed, atomic over-the-air updates with rollback and secure boot are the required baseline everywhere.
- **Level 4: Manage.** The organization measures and controls its embedded estate against baselines. It tracks worst-case execution time margins, jitter distributions, deadline-miss rates, memory and power headroom, static-analysis findings still open, certification-evidence coverage, and over-the-air update success and rollback rates, and it compares them to agreed targets. Drift against a resource or timing budget triggers action before a device fails in the field, and go or no-go release decisions rest on this data rather than on judgement in the moment. Managers can see which product lines are audit-ready and which are trending toward a missed deadline or a blown budget.
- **Level 5: Orchestrate.** Determinism, safety evidence, and security are continuously verified and automated. Fault injection and hardware-in-the-loop run on every change, and certification artefacts are generated as a byproduct of the process. The fleet is monitored, patched, and updated safely at scale throughout a long service life. The organization adapts its execution foundations, resource budgets, and standard adoption as chips go out of stock, threats evolve, and regulations change, rebalancing the whole portfolio of devices on evidence rather than reacting to each crisis alone.

## Ideas for discussion

1. Which of your device's tasks are truly hard real-time, and can you prove each one always meets its deadline?
2. Do you know the worst-case execution time of your critical control loop, or only its average?
3. Which functional-safety standard governs your product, and how far is your current evidence from what it demands?
4. If a serious defect were found in a fielded device tomorrow, how would you fix it, and how fast?
5. Where does dynamic memory allocation still exist in your control path, and what happens if it fails at hour 1000?
6. How would your IoT fleet withstand an attacker who found one shared default credential?

## Key takeaways

- Embedded software runs on constrained hardware, and real-time correctness depends on timing, not just on the right answer.
- Classify each deadline as hard, firm, or soft, and design for worst-case timing, bounded jitter, and determinism over raw speed.
- Choose an RTOS or bare metal deliberately, and budget memory, CPU, and power as fixed, first-class resources.
- Keep interrupt handlers tiny, guard shared data, and isolate hardware behind clean, testable driver interfaces.
- Adopt the functional-safety standard your domain requires early (IEC 61508, ISO 26262, DO-178C, IEC 62304, MISRA C), with full traceability.
- Test with simulation and hardware in the loop, and build secure, signed, rollback-capable OTA updates and device security from day one.

## References and further reading

- IEC 61508, *Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*
- ISO 26262, *Road Vehicles: Functional Safety*
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*
- IEC 62304, *Medical Device Software: Software Life Cycle Processes*
- MISRA, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Michael Barr and Anthony Massa, *Programming Embedded Systems*
- Elecia White, *Making Embedded Systems*
- Jane W. S. Liu, *Real-Time Systems*
- Giorgio Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*
- Colin Walls, *Embedded Software: The Works*
- Philip Koopman, *Better Embedded System Software*
- OWASP Internet of Things (IoT) security guidance
