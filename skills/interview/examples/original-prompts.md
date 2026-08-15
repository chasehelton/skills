# Original starter prompts

These prompts are original starting points. During a mock, show only the primary
prompt; keep evaluation targets and follow-ups private until relevant.

## Behavioral

**Primary:** Tell me about a project where the technically cleanest option was
not the best option for the team or customer.

Possible reactive probes: What tradeoff did you personally own? Which
alternative did you reject? How did you measure the result? What would change
your decision now?

**Primary:** Describe a time you discovered that work you owned was headed
off-course.

Possible reactive probes: What was the first observable warning? Who needed to
be influenced? What did you change, and what remained unresolved?

## System design

**Primary:** Design a service that lets teams schedule a large set of
idempotent background jobs and inspect each job's progress.

Clarifications to answer consistently when asked: jobs may run for seconds to
hours; clients can retry submissions; start with one region. Useful pressure:
duplicates become unacceptable, then a region fails.

**Primary:** Design a collaborative status page where organizations publish
incidents and subscribers receive timely updates.

Keep expected scale open until the candidate asks or states an assumption.
Useful pressure: real-time updates and a halved operating budget.

## Coding

**Primary:** Given a stream of event records `(key, timestamp)`, emit an event
only if the same key has not been emitted during the preceding cooldown window.
Events arrive in nondecreasing timestamp order.

Explore boundary semantics, memory cleanup, complexity, and representative
tests. An extension may remove the ordering guarantee.

**Primary:** Given a directed dependency graph and a requested subset of tasks,
return a valid execution order containing each requested task and all of its
transitive prerequisites, or report that no such order exists.

Explore unknown task IDs, cycle detection, deterministic output, complexity,
and disconnected components.
