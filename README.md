# Namegarage skills

Public agent skills for finding domains in the [Namegarage catalog](https://namegarage.com/).

## Catalog

The catalog skill searches published domains by project description or keywords and checks current USD prices. It also looks up listing details, compares payment options and suggests published alternatives. Search can filter by budget, suffix, length, and tier. No Namegarage account or API key is required.

Install the versioned release with the skills CLI:

```bash
npx skills@1.7.4 add https://github.com/namegarage/skills/tree/v1.2.0 --skill catalog
```

Choose the agent and workspace where you want to use it. The CLI supports agents including Codex, Claude Code, Cursor, and OpenClaw.

For OpenClaw, the same skill is also on [ClawHub](https://clawhub.ai/namegarage/skills/catalog):

```bash
openclaw skills install @namegarage/catalog --version 1.2.0
```

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
before release, plus the central cross-repository check from nikolay/liquidate.

## A2A domain selection

The skill also documents the anonymous [A2A 1.0 concierge](https://namegarage.com/docs/a2a).
Its `select_domains` skill sends one project brief with typed constraints, receives
current catalog matches, and falls back to anonymous HTTP or MCP search when
needed. The service returns direct Messages without a persistent task. It cannot
buy, reserve or register a name. Constraints in prose require clarification.


## Newsletter activation release coordination

The source release record tracks `2026-10-28-blog-newsletter`. Website 1.1.1
connects consented blog signup to confirmed daily delivery and permanent
unsubscribe. API 1.2.1 retains the preceding OpenAPI media-type correction;
MCP, SDK, skill and A2A contracts retain their versions. Source coordination
metadata changes, while published archives and tags remain immutable.
Website deployment and isolated delivery acceptance are pending. The inherited
skills.sh listing-preview acceptance remains explicit in the
[central changelog](https://namegarage.com/developers/changelog/).
