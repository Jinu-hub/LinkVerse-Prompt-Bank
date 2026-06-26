# Sample input — thesis-summarizer v2

`thesis-reinterpretation/v2` downstream 출력을 `core_data`로 전달하는 형태.
아래는 `thesis-reinterpretation/v2/examples/expected_01.json`에서 핵심 필드만 추린 샘플이다.

```json
{
  "output_lang": "en",
  "core_data": {
    "core_message": {
      "primary_thesis": "As hyperscalers build custom AI ASIC stacks to escape 'the Nvidia tax', a distinct class of specialist suppliers—the 'shadow winners' (design/IP houses, connectivity providers, power/cooling vendors, and advanced packagers/foundries)—will capture outsized, durable value.",
      "secondary_messages": [
        "The market is shifting from model training dominance to a much larger inference-driven economy, which favors purpose-built silicon and distributed specialist ecosystems.",
        "'Structural independence' by hyperscalers does not eliminate third parties; it reallocates where and how value accrues—away from general-purpose GPU vendors toward firms that enable custom chip design, interconnect, power delivery, cooling, and packaging.",
        "Hyperscalers will not do all hardware tasks in-house; the modern ASIC value chain is highly segmented, and the firms that provide IP blocks, physical design, retimers/CXL, optical interconnects, PMICs, liquid cooling, substrates and foundry capacity become essential beneficiaries.",
        "Investor strategy should rotate from a singular focus on leading accelerator vendors to owners of the underlying blueprint and supply chain that scale with hyperscaler capex."
      ],
      "reader_implication": "Investors should prioritize exposure to infrastructure suppliers that are causally linked to hyperscaler ASIC deployments (design/IP partners, connectivity vendors, power/cooling specialists, advanced packagers and TSMC) because these firms mechanically monetize hyperscaler moves to bespoke silicon and offer differentiated risk/reward profiles."
    },
    "signature_framing": [
      "Post-NVIDIA: The Hyperscaler Counterattack and the 'Shadow Winners'",
      "Nvidia Tax → Structural Independence",
      "Big tech refuse to remain mere customers—they become chip designers; who then profits from that transition?",
      "Buy the blueprint, not the frontline soldier"
    ],
    "narrative_map": {
      "opening_frame": "NVIDIA's dominance (H100, Blackwell) has defined AI infrastructure investment through 2023–H1 2024, but a deeper structural shift is underway as hyperscalers move to custom ASICs.",
      "problem_definition": "NVIDIA-centric, general-purpose GPUs impose a high TCO ('Nvidia tax') for hyperscalers whose workloads are inference-heavy and highly repetitive.",
      "structural_shift": "Hyperscalers are pursuing 'structural independence' by designing ASICs (TPU, Trainium, Inferentia, MTIA) to lower TCO, creating demand for specialized suppliers across a segmented value chain.",
      "why_now": "Inference market growth, compiler/portability progress, hyperscaler scale economics, and mounting TCO pressure make ASIC adoption timely; hyperscalers have announced large capex cycles (2025–2026) and concrete programs (e.g., Project Rainier).",
      "development_flow": [
        "Define the inefficiency of general-purpose GPUs (Nvidia Tax) → show economics motivating ASICs",
        "Explain the shift from training to inference and resulting demand dynamics",
        "Map the segmented ecosystem required to realize bespoke ASIC deployments (design/IP, interconnect, power & cooling, packaging & foundry)",
        "Profile companies in each segment that are positioned to capture value",
        "Use Project Rainier and hyperscaler programs as connective tissue to show mechanical revenue flows",
        "Conclude with investment guidance to rotate toward infrastructure suppliers"
      ],
      "closing_logic": "As hyperscalers scale custom ASIC deployments, value will reflow to a repeatable set of specialist vendors. The investment case is to own the suppliers of design IP, interconnect, power/thermal systems, and packaging/foundry capacity—i.e., the shadow winners that monetize every increment of hyperscaler ASIC adoption."
    },
    "hierarchical_structure": {
      "theme": "Hyperscalers' move to custom AI ASICs creates enduring winners among specialist suppliers across the ASIC value chain.",
      "sectors": [
        {
          "name": "ASIC Design & IP (The Architects & Tailors)",
          "companies": ["Broadcom", "Marvell Technology", "Alchip Technologies"]
        },
        {
          "name": "Connectivity & Interconnect (The Veins)",
          "companies": ["Astera Labs", "Credo Technology", "Coherent"]
        },
        {
          "name": "Power & Thermal (The Energy)",
          "companies": ["Monolithic Power Systems", "Vicor", "Vertiv Holdings"]
        },
        {
          "name": "Manufacturing & Advanced Packaging (The Builders)",
          "companies": ["TSMC", "Amkor Technology", "Ibiden"]
        }
      ]
    },
    "case_studies": [
      {
        "name": "Project Rainier",
        "type": "Hyperscaler deployment program",
        "strategic_role": "Concrete embodiment of AWS's strategy to build a large-scale Trainium-based supercluster to achieve Nvidia independence and dramatically lower TCO via bespoke ASIC scale",
        "linked_sectors": [
          "ASIC Design & IP",
          "Connectivity & Interconnect",
          "Manufacturing & Advanced Packaging",
          "Power & Thermal"
        ],
        "linked_companies": [
          "Alchip Technologies",
          "Astera Labs",
          "TSMC",
          "Monolithic Power Systems",
          "Credo Technology"
        ],
        "value_flow": [
          "AWS increases Trainium server count → Alchip receives turnkey physical design and packaging revenue",
          "AWS standardizes interconnect choices → Astera Labs retimer/CXL chips and Credo AEC see per-server content growth",
          "Large-scale server deployment → TSMC and advanced packagers see wafer and CoWoS/2.5D demand",
          "Higher power density per rack → MPS/Vicor/Vertiv see increased equipment and module sales"
        ]
      }
    ],
    "rewrite_critical_takeaways": [
      "Hyperscalers' shift to custom ASICs is driven by TCO incentives (inference-heavy workloads) and compiler/portability improvements that lower the barriers to move off GPUs.",
      "The ASIC value chain is highly segmented; hyperscalers will outsource or license critical IP and physical design functions to specialist partners rather than vertically integrate every component.",
      "Design/IP houses (Broadcom, Marvell, Alchip) capture content-per-chip and NRE fees as hyperscalers scale bespoke silicon.",
      "Connectivity (Astera Labs, Credo, optical vendors) and advanced packaging/foundry (TSMC, Amkor, substrate makers) are structural chokepoints that translate hyperscaler capex into supplier revenue.",
      "Project Rainier (AWS Trainium scale-out) is a concrete example connecting hyperscaler announcements to mechanical revenue paths for specific suppliers."
    ],
    "action_framework": {
      "what_to_avoid": [
        "Over-simplifying into a binary 'Nvidia vs hyperscalers' narrative—preserve nuance that hyperscalers still rely on third parties.",
        "Diluting causal links by adding extraneous companies or unreferenced risks."
      ],
      "what_to_focus": [
        "Clear causal chains from hyperscaler decisions → technical requirements → supplier content growth → revenue/valuation impact.",
        "Concrete program-level examples (Project Rainier, TPU/Trainium lines) to illustrate mechanical demand."
      ],
      "selection_criteria": [
        "Direct revenue linkage to hyperscaler ASIC deployments.",
        "Technology indispensability (SerDes leadership, CXL retimers, advanced packaging capacity).",
        "Supply-side scarcity or chokepoint status (TSMC node capacity, CoWoS/2.5D packaging)."
      ]
    },
    "risk_points": [
      "Concentration risk: several beneficiaries (e.g., Alchip) have high revenue exposure to a single hyperscaler (AWS) leading to client-concentration risk.",
      "Geopolitical / supply-chain risk: Taiwan-based design and substrate firms and TSMC exposure create geopolitical vulnerability.",
      "Dual-sourcing and competition: hyperscalers may adopt dual-sourcing which can cap pricing power.",
      "Packaging/foundry bottlenecks: constrained advanced-packaging or node capacity can delay revenue realization.",
      "Technology-adoption timing: CXL, silicon photonics and ecosystem standards may take longer to mature."
    ]
  }
}
```
