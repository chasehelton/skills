# System-design track

Offer only the primary design prompt at first. Let the candidate drive this
flexible path:

1. requirements and scope
2. constraints and scale
3. APIs and data model
4. high-level design
5. bottlenecks and deep dives
6. reliability and operations
7. tradeoff review

Answer candidate clarification questions consistently. When a premise is open,
invite a reasonable assumption rather than hiding a single expected answer.
Reward coherent explicit assumptions, prioritization, and revision—not one
preferred architecture.

## Follow-up pressure

Introduce one pressure at a time, selected to test the observed design:

- traffic increases 100×
- a region fails
- deletion must complete within 24 hours
- the product requires real-time behavior
- the budget is halved
- duplicates are unacceptable

Do not stack surprises merely to make the candidate fail. Probe bottlenecks,
failure modes, migrations, observability, and operational ownership at a depth
appropriate to the contract.

## Dimensions

Score requirements discovery, prioritization, decomposition, data modeling,
scalability, reliability, tradeoff reasoning, communication, and adaptability
using [SCORECARD.md](SCORECARD.md).

Complete conduct when the candidate has defended an end-to-end design and
responded to at least one meaningful tradeoff or pressure, or the timebox ends.
Artifacts may be stored under `.interview/artifacts/system-design/`.
