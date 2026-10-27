# Namegarage skills

Public agent skills for finding domains in the [Namegarage catalog](https://namegarage.com/).

## Catalog

The catalog skill searches published domains by project description or keywords and checks current USD prices. Search can filter by budget, suffix, length, and tier. No Namegarage account or API key is required.

Install the versioned release with the skills CLI:

```bash
npx skills@1.7.4 add https://github.com/namegarage/skills/tree/v1.0.0 --skill catalog
```

Choose the agent and workspace where you want to use it. The CLI supports agents including Codex, Claude Code, Cursor, and OpenClaw.

For OpenClaw, the same skill is also on [ClawHub](https://clawhub.ai/namegarage/skills/catalog):

```bash
openclaw skills install @namegarage/catalog --version 1.0.0
```

Try a prompt:

> Use the Namegarage catalog skill to find up to five domains for a meal-planning app under $3,000 USD. Show current prices and listing links, and explain why each name fits.

Search text is sent to Namegarage, so use general descriptions rather than confidential project details. A missing price means offer-only. A name missing from the catalog says nothing about registration or listings elsewhere. Results do not reserve names; follow the returned links before a purchase decision.

The skill uses only documented public read interfaces. It cannot buy or reserve a domain, make offers, send messages, sign in, or access private portfolio data.

[API quickstart](https://namegarage.com/docs/quickstart) · [MCP connection guide](https://namegarage.com/mcp/) · [Published skill](https://namegarage.com/.well-known/agent-skills/catalog/SKILL.md)

## License

MIT No Attribution (MIT-0). See [LICENSE](LICENSE).
