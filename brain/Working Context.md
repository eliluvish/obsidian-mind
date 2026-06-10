---
description: "Eli's operating context — solo Rails dev and own DevOps, PI stakeholders instead of a product team, hospital IT constraints"
tags:
  - brain
---

# Working Context

How Eli works, for calibrating suggestions. The role itself (solo Rails dev at a research hospital, 5–7 concurrent projects) is in [[CLAUDE]]; this note holds the operating constraints that follow from it.

- **Solo means own DevOps.** There is no ops team — deploys, servers, monitoring, and incident response are all Eli. Suggestions that assume "hand this to ops" don't apply; runbooks in `reference/ops/` are the substitute.
- **The core challenge is context switching**, not depth — maintaining working knowledge of 5–7 codebases at once. This is why `/context-switch` matters and why the vault exists. See [[North Star]] for what currently has focus.
- **Stakeholders are PIs (Principal Investigators), not a product team.** No PM, no roadmap process — priorities arrive as requests from PIs and compliance officers. See [[People & Context]].
- **Hospital IT constraints apply everywhere**: VPN, SSO, firewall rules. Anything involving external services, webhooks, or new network paths needs to account for them. HIPAA/IRB context lives in `reference/compliance/`.

## Related

- [[Memories]]
- [[North Star]]
- [[People & Context]]
