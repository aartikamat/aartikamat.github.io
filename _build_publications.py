"""Builds publications.html: every paper, dataset and software item with links and a copy-ready BibTeX entry.
Plain static HTML (GitHub Pages). Run: python _build_publications.py"""
import html
import json

A = "Kamat, Arati Uday"
ORCID = "https://orcid.org/0009-0000-4781-312X"
HF = "https://huggingface.co/datasets/AratiKamat/"
KG = "https://www.kaggle.com/datasets/aratiudaykamat/"
GH = "https://github.com/aartikamat/"

PAPERS = [
    dict(key="kamat2026houraware", title="Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment",
         year="2026", note="Working paper.", doi="10.5281/zenodo.19670718",
         links=[("arXiv", "https://arxiv.org/abs/2606.08232"), ("SSRN", "https://ssrn.com/abstract=6564803"), ("Zenodo", "https://doi.org/10.5281/zenodo.19670718"),
                ("Companion data", "https://doi.org/10.5281/zenodo.20043301"), ("Pre-registration", "https://doi.org/10.17605/OSF.IO/YVB3M")]),
    dict(key="kamat2026prfs", title="Post-Rejection Follow-up Sampling: Measuring Outcomes of Rejected Decisions in Algorithmic DEX Trading",
         year="2026", note="Working paper.", doi="10.5281/zenodo.19671656",
         links=[("arXiv", "https://arxiv.org/abs/2606.08228"), ("SSRN", "https://ssrn.com/abstract=6607301"), ("Zenodo", "https://doi.org/10.5281/zenodo.19671656"),
                ("Data", "https://doi.org/10.5281/zenodo.20043515"), ("Code (GitHub)", GH + "post-rejection-sampling")]),
    dict(key="kamat2026filterprecision", title="Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading: Evidence from 2,400 Rejection Events",
         year="2026", note="Working paper.", doi="10.5281/zenodo.19720040",
         links=[("arXiv", "https://arxiv.org/abs/2607.02830"), ("SSRN", "https://ssrn.com/abstract=6638259"), ("Zenodo", "https://doi.org/10.5281/zenodo.19720040"),
                ("Companion data", "https://doi.org/10.5281/zenodo.19987695")]),
    dict(key="kamat2026red2400paper", title="RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels",
         year="2026", note="Data paper. The dataset record carries a September 2026 correction notice; a corrected version of the paper is in preparation.", doi="10.5281/zenodo.20011630",
         links=[("arXiv", "https://arxiv.org/abs/2605.12151"), ("SSRN", "https://ssrn.com/abstract=6702198"), ("Zenodo", "https://doi.org/10.5281/zenodo.20011630"),
                ("Dataset", "https://doi.org/10.5281/zenodo.19989074")]),
    dict(key="kamat2026redpump", title="Auditing Collector-Generated Graduation Labels on Pump.fun: Measurement Error and Temporal Non-Generalization",
         year="2026", note="Working paper. The dataset record (version 1.6) carries a September 2026 correction notice; a corrected version is in preparation.", doi=None,
         links=[("arXiv", "https://arxiv.org/abs/2607.02823"), ("SSRN", "https://ssrn.com/abstract=6915560"), ("Dataset", "https://doi.org/10.5281/zenodo.20633486")]),
    dict(key="kamat2026cohorts", title="Coordinated Sniper Cohorts on Pump.fun: Detection of 1,012 Persistent Wallet Rings and a Contamination-Adjusted Estimate of Coordination-Specific First-Hour Buyer-Flow Lift",
         year="2026", note="Working paper. Title as posted on arXiv. Correction (October 2026, arXiv v4): the buyer records include sells and miss many buys, so all numerical results, including the count in the title, are withdrawn; no effect is claimed.", doi=None,
         links=[("arXiv", "https://arxiv.org/abs/2607.02795"), ("Results and code record", "https://doi.org/10.5281/zenodo.20978741")]),
    dict(key="kamat2026crosspipeline", title="Do Two On-Chain Observation Pipelines See the Same Tokens? Cross-Pipeline Coverage on the Solana pump.fun Launchpad",
         year="2026", note="Working paper.", doi=None,
         links=[("arXiv", "https://arxiv.org/abs/2609.18975"), ("SSRN", "https://ssrn.com/abstract=7128818"), ("Reproducibility package", "https://doi.org/10.5281/zenodo.21399918")]),
    dict(key="kamat2026redreject", title="RED-REJECT-2026: A 96-Day Public Corpus of Algorithmic Filter Rejections with Post-Rejection Follow-up Samples",
         year="2026", note="Data paper.", doi="10.5281/zenodo.21402476",
         links=[("SSRN", "https://ssrn.com/abstract=7129798"), ("Dataset", "https://doi.org/10.5281/zenodo.21402476")]),
    dict(key="kamat2026corpus", title="A Multi-Venue Solana/DeFi Microstructure Data Corpus: The RED-2400 Family v2",
         year="2026", note="Working paper. Each companion dataset's version 1.1 (28 September 2026) corrects its documentation.", doi=None,
         links=[("arXiv", "https://arxiv.org/abs/2610.00005"), ("SSRN", "https://ssrn.com/abstract=7062579")]),
]

DATASETS = [
    dict(key="kamat2026redpumpdata", title="RED-PUMP-2026-v1: a public benchmark of 860,213 pump.fun token launches with collector-generated terminal labels", doi="10.5281/zenodo.20633486",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.20633486"), ("Hugging Face", HF + "red-pump-2026"), ("Kaggle", KG + "red-pump-2026-pumpfun-token-launches")]),
    dict(key="kamat2026red2400data", title="RED-2400: A Public Benchmark of Algorithmically-Rejected Trading Events with Outcome Labels (dataset)", doi="10.5281/zenodo.19989074",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.19989074"), ("Hugging Face", HF + "RED-2400"), ("Kaggle", KG + "red-2400-data-rejected-trading-events-solana"),
                ("IEEE DataPort", "https://doi.org/10.21227/c36z-hk34")]),
    dict(key="kamat2026redoracle", title="RED-ORACLE-2026: Pyth Network oracle prices and publication lags for BTC, ETH and SOL with OKX benchmark prices", doi="10.5281/zenodo.21211109",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21211109")]),
    dict(key="kamat2026redarb", title="RED-ARB-2026: Solana decentralized-exchange best quotes against OKX prices for six tokens", doi="10.5281/zenodo.21211186",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21211186")]),
    dict(key="kamat2026redliq", title="RED-LIQ-2026: Aave V3 Ethereum liquidation events and a six-chain lending-utilization panel", doi="10.5281/zenodo.21211302",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21211302")]),
    dict(key="kamat2026redbasis", title="RED-BASIS-2026: OKX spot-perpetual basis and funding observations for BTC, ETH and SOL", doi="10.5281/zenodo.21211414",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21211414")]),
    dict(key="kamat2026redbridge", title="RED-BRIDGE-2026: Wormhole cross-chain messages", doi="10.5281/zenodo.21211497",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21211497")]),
    dict(key="kamat2026redrejectdata", title="RED-REJECT-2026-v2: A 96-Day Public Corpus of Algorithmic Filter Rejections (corrected release)", doi="10.5281/zenodo.21402476",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21402476")]),
    dict(key="kamat2026prfsdata", title="Post-Rejection Follow-up Sampling: Dataset", doi="10.5281/zenodo.20043515",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.20043515")]),
    dict(key="kamat2026ablation", title="REJECTION-ABLATION-2026-v1: A Post-Rejection Follow-up Sampling (PRFS) Corpus and Per-Filter Counterfactual Ablation for Solana Memecoin Trading (June 2026)", doi="10.5281/zenodo.21149175",
         note="The per-filter summaries in this July 2026 deposit are superseded; a revised event-level analysis is in preparation.",
         links=[("Zenodo", "https://doi.org/10.5281/zenodo.21149175")]),
]

SOFTWARE = [
    dict(key="kamat2026prfssoftware", title="Post-Rejection Follow-up Sampling (PRFS): Reference Implementation", doi="10.5281/zenodo.19672363",
         note="The Zenodo record archives v1.0.0; the current source on GitHub is version 2.0.0.",
         links=[("GitHub", GH + "post-rejection-sampling"), ("Zenodo", "https://doi.org/10.5281/zenodo.19672363")]),
    dict(key="kamat2026toolkit", title="RED-2400 Replication Toolkit", doi="10.5281/zenodo.20561397",
         note="The Zenodo record archives v1.0.0, which pooled outcomes by token; its per-filter tables should not be cited as per-event results. The current release on GitHub is v2.0.2.",
         links=[("GitHub", GH + "red2400-replication-toolkit"), ("Zenodo", "https://doi.org/10.5281/zenodo.20561397")]),
    dict(key="kamat2026reader", title="red-2400-reader: a lightweight loader for the RED-2400 files", doi=None,
         links=[("GitHub", GH + "red-2400-reader")]),
]

PREREGS = [
    dict(key="kamat2026slottime", title="Faster blocks, tighter prices? CEX–DEX price gaps across Solana's staged slot-time cuts: a preregistered natural experiment",
         note="Preregistration on OSF, registered 3 October 2026.", doi="10.17605/OSF.IO/YA485",
         links=[("OSF registration", "https://osf.io/ya485/")]),
    dict(key="kamat2026alpenglow", title="Faster finality, faster bridges? Cross-chain message latency across Solana's switch to Alpenglow consensus: a preregistered conditional natural experiment",
         note="Preregistration on OSF, registered 3 October 2026.", doi="10.17605/OSF.IO/2CPSA",
         links=[("OSF registration", "https://osf.io/2cpsa/")]),
    dict(key="kamat2026eventvariance", title="Is US macro-announcement risk priced in 24/7 crypto options? Option-implied event variance from daily-expiry bitcoin and ether options: a preregistered event study",
         note="Preregistration on OSF, registered 3 October 2026.", doi="10.17605/OSF.IO/US2XQ",
         links=[("OSF registration", "https://osf.io/us2xq/")]),
    dict(key="kamat2026macroliquidations", title="Scheduled macro news and forced deleveraging in 24/7 crypto perpetuals: a preregistered event study of exchange-wide liquidations around FOMC, CPI and payroll releases",
         note="Preregistration on OSF, registered 3 October 2026.", doi="10.17605/OSF.IO/QS7HM",
         links=[("OSF registration", "https://osf.io/qs7hm/")]),
    dict(key="kamat2026frozenforecast", title="A frozen forecast: do DeFi fixed rates predict realized yields? Implied fixed rates of Pendle principal tokens versus the realized yields of their underlying assets to maturity, a preregistered forecast test",
         note="Preregistration on OSF, registered 3 October 2026.", doi="10.17605/OSF.IO/7Q3YK",
         links=[("OSF registration", "https://osf.io/7q3yk/")]),
    dict(key="kamat2026hourawareprereg", title="Preregistration (re-registration): Hour-Aware Prospective Deployment Test on the Solana pump.fun Ecosystem, v2.2 redacted with v2.3 implementation amendment",
         note="Preregistration on OSF, registered 5 October 2026. Replaces the withdrawn September 2026 registration.", doi="10.17605/OSF.IO/YVB3M",
         links=[("OSF registration", "https://osf.io/yvb3m/")]),
    dict(key="kamat2026paidpromotion", title="Paying for attention: is paid token promotion a costly signal of quality or a prelude to abandonment? A preregistered test of the 7-day survival of newly promoted Solana tokens on a public DEX screener",
         note="Preregistration on OSF, registered 7 October 2026.", doi="10.17605/OSF.IO/W47YK",
         links=[("OSF registration", "https://osf.io/w47yk/")]),
]

REVIEWS = [
    ("Qeios review of “CryptoPulse: Short-Term Cryptocurrency Forecasting with Dual-Prediction and Cross-Correlated Market Indicators”", "10.32388/MO17NR"),
    ("Qeios review of “Risk-Return Analysis of Select Crypto Currencies: During 2018-2022”", "10.32388/WBHI23"),
    ("Qeios review of “Unpacking the Complexities of Bitcoin Volatility: A Time Series Data with Long-term Memory or Long-range Dependence”", "10.32388/ZMMST8"),
    ("PREreview of “Measuring CEX-DEX Extracted Value and Searcher Profitability: The Darkest of the MEV Dark Forest”", "10.5281/zenodo.21343453"),
    ("PREreview of “RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds”", "10.5281/zenodo.21878877"),
    ("PREreview of “Resisting Manipulative Bots in Meme Coin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning”", "10.5281/zenodo.22679924"),
]


def bib(item, kind):
    lines = [f"@misc{{{item['key']},", f"  author = {{{A}}},", f"  title = {{{item['title']}}},", "  year = {2026},"]
    if kind == "dataset":
        lines.append("  howpublished = {Dataset, Zenodo},")
    elif kind == "software":
        lines.append("  howpublished = {Software},")
    elif kind == "prereg":
        lines.append("  howpublished = {Preregistration, Open Science Framework},")
    if item.get("doi"):
        lines += [f"  doi = {{{item['doi']}}},", f"  url = {{https://doi.org/{item['doi']}}}"]
    else:
        lines.append(f"  url = {{{item['links'][0][1]}}}")
    return "\n".join(lines) + "\n}"


def card(item, kind):
    links = " · ".join(f'<a href="{html.escape(u)}">{html.escape(n)}</a>' for n, u in item["links"])
    note = f'<div class="note">{html.escape(item["note"])}</div>' if item.get("note") else ""
    doi = f' · DOI <a href="https://doi.org/{item["doi"]}">{item["doi"]}</a>' if item.get("doi") else ""
    return (f'<div class="item"><div class="t">{html.escape(item["title"])}</div>'
            f'<div class="m">A. U. Kamat · 2026{doi}</div>{note}<div class="l">{links}</div>'
            f'<details><summary>Cite (BibTeX)</summary><pre>{html.escape(bib(item, kind))}</pre></details></div>')


ld = [{"@context": "https://schema.org", "@type": "Dataset", "name": d["title"], "identifier": f"https://doi.org/{d['doi']}",
       "url": f"https://doi.org/{d['doi']}", "license": "https://creativecommons.org/licenses/by/4.0/",
       "creator": {"@type": "Person", "name": "Arati Uday Kamat", "sameAs": ORCID},
       "isAccessibleForFree": True, "sameAs": [u for _, u in d["links"]]} for d in DATASETS]

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Publications, Datasets and Software – Arati Uday Kamat</title>
<meta name="description" content="Working papers, public datasets and open-source software by Arati Uday Kamat, with DOIs and copy-ready citations.">
<meta name="author" content="Arati Uday Kamat">
<link rel="canonical" href="https://aartikamat.github.io/publications.html">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root {{ --bg:#ffffff; --ink:#1a1a1a; --muted:#555; --card:#f5f7fa; --line:#d6dce4; --accent:#0b5cad; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#121417; --ink:#f0f0f0; --muted:#b8b8b8; --card:#1c2026; --line:#353d48; --accent:#7fb6ff; }} }}
:root[data-theme="dark"] {{ --bg:#121417; --ink:#f0f0f0; --muted:#b8b8b8; --card:#1c2026; --line:#353d48; --accent:#7fb6ff; }}
body {{ background:var(--bg); color:var(--ink); font-family: Georgia, 'Times New Roman', serif; line-height:1.55; margin:0; padding:16px; }}
main {{ max-width:880px; margin:0 auto; }}
h1 {{ font-size:28px; margin:8px 0 2px; }} h2 {{ font-size:22px; margin:28px 0 8px; color:var(--accent); }}
.sub {{ color:var(--muted); margin-bottom:10px; }}
.item {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin:10px 0; }}
.t {{ font-weight:bold; }} .m, .note {{ color:var(--muted); font-size:15px; }} .l {{ margin-top:6px; font-size:16px; }}
a {{ color:var(--accent); }} pre {{ white-space:pre-wrap; word-break:break-word; font-size:13px; background:var(--bg); border:1px solid var(--line); padding:8px; border-radius:6px; }}
summary {{ cursor:pointer; color:var(--accent); font-size:15px; margin-top:6px; }}
</style>
</head>
<body><main>
<p><a href="index.html">← Home</a></p>
<h1>Publications, datasets and software</h1>
<div class="sub">Arati Uday Kamat · Independent Researcher · <a href="{ORCID}">ORCID 0009-0000-4781-312X</a> · <a href="https://scholar.google.com/citations?user=CWpdnloAAAAJ">Google Scholar</a> · <a href="https://github.com/aartikamat">GitHub</a> · <a href="https://huggingface.co/AratiKamat">Hugging Face</a> · <a href="https://www.kaggle.com/aratiudaykamat">Kaggle</a></div>
<p>All datasets are released under CC BY 4.0. Please cite the DOI shown for each item; each "Cite" button gives a ready-to-paste BibTeX entry.</p>
<h2>Working papers and data papers</h2>
{''.join(card(p, 'paper') for p in PAPERS)}
<h2>Preregistrations</h2>
<p>Study plans registered in advance on the Open Science Framework (OSF). Each registration is public, time-stamped and has a DOI.</p>
{''.join(card(r, 'prereg') for r in PREREGS)}
<h2>Datasets</h2>
{''.join(card(d, 'dataset') for d in DATASETS)}
<h2>Software</h2>
{''.join(card(s, 'software') for s in SOFTWARE)}
<h2>Open peer reviews</h2>
<p>Public peer reviews with DOIs. A seventh public review (ResearchHub) and two reviews invited by journal editors are listed on the <a href="index.html">home page</a>.</p>
{''.join(f'<div class="item"><div class="t">{html.escape(t)}</div><div class="l"><a href="https://doi.org/{d}">doi:{d}</a></div></div>' for t, d in REVIEWS)}
<p class="sub">Last updated 7 October 2026.</p>
</main></body></html>
"""
open("publications.html", "w", encoding="utf-8").write(page)
print("publications.html written:", len(PAPERS), "papers,", len(PREREGS), "preregistrations,", len(DATASETS), "datasets,", len(SOFTWARE), "software,", len(REVIEWS), "reviews")
