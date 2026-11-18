# Namegarage skills

Version 1.3.2 is the published catalog skill. It belongs to release `2026-11-17-installed-service-packaging`, pins SDK 0.3.2 and serves the installed UCP adapter 1.0.0 contract.

Version 1.3.3 is an upcoming source candidate under release `2026-11-16-ucp-exact-admission`. It changes only the two SDK pins to 0.3.3 and records reserved UCP adapter 1.0.1. It is not published; keep installing 1.3.2 until the [developer changelog](https://namegarage.com/developers/changelog/) shows that release as published.

Public agent skills for finding domains in the [Namegarage catalog](https://namegarage.com/).

## Catalog

The catalog skill searches published domains by project description or keywords and checks current USD prices. It also looks up listing details, compares payment options and suggests published alternatives. Search can filter by budget, suffix, length, and tier. No Namegarage account or API key is required.

Install the versioned release with the skills CLI:

```bash
npx skills@1.7.4 add https://github.com/namegarage/skills/tree/v1.3.2 --skill catalog
```

After the changelog shows release `2026-11-16-ucp-exact-admission` as published, use `tree/v1.3.3` in the same command.

Choose the agent and workspace where you want to use it. The CLI supports agents including Codex, Claude Code, Cursor, and OpenClaw.

For OpenClaw, the same skill is also on [ClawHub](https://clawhub.ai/namegarage/skills/catalog):

```bash
openclaw skills install @namegarage/catalog --version 1.3.2
```

Use `--version 1.3.3` only after the changelog shows that release as published.

Try a prompt:

> Use the Namegarage catalog skill to find up to five domains for a meal-planning app under $3,000 USD. Show current prices and listing links, and explain why each name fits.

Search text is sent to Namegarage, so use general descriptions rather than confidential project details. A missing price means offer-only. A name missing from the catalog says nothing about registration or listings elsewhere. Results do not reserve names; follow the returned links before a purchase decision.

The skill uses only documented public read interfaces. It cannot buy or reserve a domain, make offers, send messages, sign in, or access private portfolio data.

[API quickstart](https://namegarage.com/docs/quickstart) · [MCP connection guide](https://namegarage.com/mcp/) · [Published skill](https://namegarage.com/.well-known/agent-skills/catalog/SKILL.md)

## License

MIT No Attribution (MIT-0). See [LICENSE](LICENSE).

## Coordinated capabilities

The catalog skill documents `search_domains`, `get_domain`, `get_purchase_options`
and `suggest_alternatives`, and their matching public HTTP interfaces. Payment
comparisons use server-provided monthly, final and total amounts; the skill does
not calculate replacement prices, start checkout or reserve a name.

[Developer changelog](https://namegarage.com/developers/changelog/) records the API,
MCP, SDK and skill versions under one release ID. The root `release.json` records
this artifact's compatibility and SHA-256. Run `python3 tools/check_release.py`
before release, plus the central cross-repository coordination check.

## A2A domain selection

The skill also documents the anonymous [A2A 1.0 concierge](https://namegarage.com/docs/a2a).
Its `select_domains` skill sends one project brief with typed constraints, receives
current catalog matches, and falls back to anonymous HTTP or MCP search when
needed. The service returns direct Messages without a persistent task. It cannot
buy, reserve or register a name. Constraints in prose require clarification.


## UCP release coordination

Release `2026-11-10-ucp-catalog` published SDK 0.3.0 and skill 1.3.0, which add
UCP catalog and buyer handoff guidance. The deployed UCP catalog
accepts the configured signed Playground platform. These POST reads need its
reviewed profile and a fresh ES256 HTTP message signature; the anonymous HTTP,
MCP and A2A alternatives remain available without platform enrollment.

Catalog browsing uses the deployed snapshot during transaction-database
outages. Dynamic catalog operations check current prices and availability;
a browsing snapshot never authorizes a purchase. Earlier candidate metadata
and acceptance evidence remain in the central changelog. New registry
verification applies to this version and does not rewrite earlier artifacts.

Published release `2026-11-17-installed-service-packaging` covers skill 1.3.2,
SDK 0.3.2 and the installed UCP adapter 1.0.0 contract. The source release
record now tracks the upcoming `2026-11-16-ucp-exact-admission` release, which
reserves UCP adapter 1.0.1. Skill 1.3.3 updates its two SDK pins to 0.3.3 and
its coordination metadata, with the same public read-only guidance and MIT-0
license. It has not been tagged, published or verified on ClawHub or skills.sh.
Published 1.3.0, 1.3.1 and 1.3.2 bytes remain immutable. Current publication
status and remaining checks are tracked in the central release record and the
developer changelog.
