# Language scope and mechanical control — design

Three changes inside the unpublished 2.0.0. No version bump.

## Problem

The acceptance run surfaced two honest limits:

1. **The control query is composed by judgment and I got it wrong.** I mixed three
   `site:` operators with a year token; the search returned the hosts' marketing pages
   instead of their forums, scored 1 qualifying post against a threshold of 3, and landed
   in PATH-B BLIND. The verdict machinery was correct; the input was not.
2. **The method is verified on one product, one market, one search path, one agent.** The
   skill's architecture is market-neutral, but its evidence is not.

Shipping a market-neutral claim on that evidence would repeat the exact failure this
project has been correcting: output that looks more certain than the run behind it.

## Decisions

**Supported languages are Arabic and English. Enforced, not documented.** The market
profile derives the language as before; if the result is neither, the run states the
derived language, states the verified scope, and stops for the user to choose. Soft
warnings were rejected — a caveat inside a polished report is skimmed past.

**The control query becomes mechanical.** Micro-tests verify whether prose binds an
agent's judgment. The better fix is to remove the judgment. With two supported languages
the control can be a checked-in query per language rather than a composition task, so
run-to-run variance goes to zero by construction rather than by measurement.

## Changes

### 1. Language gate — `references/market-profile.md`, "Market and language"

After the language is derived, one gate:

- Arabic or English → continue.
- Anything else → state the derived language and the page it was read from, state that
  the skill is verified only for Arabic and English, and stop. Offer the user the choice
  to proceed knowingly, and record that choice in the report if they do.
- A market with two writing languages where one is Arabic or English → continue on the
  supported one and record the other as unsearched scope.

The gate is stated once, here. SKILL.md, fit-check.md and the README reference it.

### 2. Mechanical control — `references/fit-check.md`, Step 2

Replace the composition instruction with a fixed control query per supported language,
plus two construction rules that encode the observed failure:

- **Exactly one platform per control query.** No OR'd `site:` operators.
- **No date or year tokens** — they bias the index toward SEO pages that carry the year
  in the title.

The four qualifying conditions and the 3-or-more threshold are unchanged. If a control
returns 0-2 on a correctly-formed query, the PATH-B BLIND verdict stands as before.

### 3. Honest surfaces

- SKILL.md: a hard rule naming the supported languages and pointing at the gate; the
  frontmatter description gains the scope as a trigger qualifier, not a workflow summary.
- README: a supported-languages statement replacing any implication of universal reach.
  The "how it handles a market it has never seen" section stays, describing the
  architecture, and states the verified scope alongside it.
- `docs/superpowers/acceptance-2026-08-17.md`: a header noting German is now outside
  supported scope. The findings stay — they are the evidence that justifies the
  architecture, and deleting them would hide why the design is what it is.

## Verification

- Re-derive output 1 for sevdesk.de. Expected: stop at the gate, naming German.
- Read-through: the gate is stated once and referenced elsewhere, never restated.
- The Arabic control query is the one that returned three real permalinks in the earlier
  run, so it is known-good rather than newly invented.
- Tests stay green.

## Not doing

- No micro-test reps. The judgment that needed testing has been removed rather than
  measured; what remains judgment-heavy (local-phrasing derivation) is unchanged from the
  version the acceptance run exercised.
- No revert of the generalization. The architecture stays; only the claim narrows.
