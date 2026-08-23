# Sample input

upstream digest/editorial pipeline이 생성한 `core_data`를 Today in 30 Seconds 표현으로 변환하는 입력 샘플.

```json
{
  "core_data": {
    "input_date": "2026-08-23",
    "topic": "Daily Market Issue — 2026-08-23",
    "summary": "Geopolitical tension in the Middle East pushed energy prices higher and kept inflation concerns in focus, while large-scale AI-related corporate borrowing added pressure to credit markets. U.S. equities finished lower across major indices as investors weighed commodity-driven inflation risk against still-strong AI investment narratives.",
    "highlights": [
      {
        "title": "Middle East Escalation Raises Energy and Inflation Risk",
        "summary": "Rising geopolitical tension in the Middle East lifted Brent crude above $93 and raised concerns that higher energy costs could keep inflation expectations sticky.",
        "why_it_matters": "Energy shocks can feed directly into goods inflation and limit central-bank policy flexibility, keeping rate-sensitive assets under pressure."
      },
      {
        "title": "Big Tech AI Borrowing Adds Credit-Market Pressure",
        "summary": "Reports highlighted a wave of large AI-related bond issuance from major technology companies, with one hyperscaler reportedly raising about $60 billion in new debt.",
        "why_it_matters": "Heavy AI capex funded through debt can widen credit spreads and make investors more selective about duration and issuer quality."
      },
      {
        "title": "U.S. Equities Slide as Macro Risks Outweigh AI Optimism",
        "summary": "Major U.S. indices closed lower as higher oil prices, firmer long-term yields, and geopolitical uncertainty outweighed continued enthusiasm for AI infrastructure demand.",
        "why_it_matters": "When macro and geopolitical risks rise together, equity markets may become more headline-sensitive even if structural AI demand remains intact."
      }
    ],
    "items": [
      {
        "title": "Dow Jones Industrial Average",
        "summary": "The Dow fell 1.32% on the session as energy and macro concerns weighed on sentiment."
      },
      {
        "title": "S&P 500",
        "summary": "The S&P 500 declined 0.87%, with broad participation in the move lower."
      },
      {
        "title": "Nasdaq Composite",
        "summary": "The Nasdaq closed down 1.00% as tech and growth names gave back recent gains."
      },
      {
        "title": "Brent Crude",
        "summary": "Brent crude settled at $93.78, up 2.4%, after Middle East tensions intensified."
      },
      {
        "title": "U.S. 30-Year Treasury Yield",
        "summary": "The U.S. 30-year yield rose to 5.24% as inflation concerns resurfaced."
      },
      {
        "title": "U.S. Investment-Grade Credit Spreads",
        "summary": "Investment-grade spreads widened modestly as investors priced higher issuance from AI-related borrowers."
      },
      {
        "title": "Bitcoin",
        "summary": "Bitcoin traded lower alongside broader risk assets, though the move was smaller than in equities."
      }
    ],
    "more_items": [
      {
        "title": "Shipping Insurance Premiums",
        "summary": "War-risk premiums for key shipping routes edged higher, adding a secondary cost channel for energy markets."
      },
      {
        "title": "Semiconductor Equipment Orders",
        "summary": "Order commentary remained constructive for advanced packaging tools, supporting the longer-term AI infrastructure thesis."
      }
    ],
    "ending": "Today's market action suggests a chain where geopolitical pressure is lifting commodities, commodity strength is reviving inflation concerns, and those macro pressures are now competing with AI-driven growth optimism for investor attention."
  },
  "output_lang": "ko"
}
```
