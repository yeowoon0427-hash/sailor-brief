"""Case definitions. Frozen as of 2026-09-23 — see the pre-registration.
Changing anything here invalidates comparison with the backtest."""

MIL = ["conflict_rate", "threat_rate", "military_rate", "neg_tone", "keyword_rate"]
ECON = ["conflict_rate", "threat_rate", "sanction_rate", "neg_tone", "keyword_rate"]

CASES = {
    # ---------------- Military tension / conflict ----------------
    "taiwan_strait": dict(
        group="military", title="PLA pressure on Taiwan: Pelosi → Joint Sword → Strait Thunder (2022–2025)",
        actors=["CHN"], targets=["TWN", "USA"], geo=["TW"], signals=MIL,
        keywords=["taiwan", "pelosi", "joint-sword", "strait-thunder"],
        response_keywords=[["taiwan"], ["reroute", "airline", "flight", "shipping", "supplier", "ban", "suspend", "tsmc"]],
        impacts=[("2022-08-04", "PLA live-fire drills after Pelosi visit"),
                 ("2023-04-08", "Joint Sword drills"),
                 ("2024-05-23", "Joint Sword-2024A"),
                 ("2024-10-14", "Joint Sword-2024B"),
                 ("2025-04-01", "Strait Thunder-2025A")],
        lead_window_days=45,
        events=[("2022-07-19", "Reports: Pelosi plans Taiwan trip"), ("2022-07-28", "Biden–Xi call: 'play with fire'"),
                ("2022-08-02", "Pelosi lands in Taipei"), ("2022-08-04", "PLA drills and missile launches"),
                ("2023-04-05", "Tsai–McCarthy meeting in California"), ("2023-04-08", "Joint Sword"),
                ("2024-05-20", "Lai Ching-te inaugurated"), ("2024-05-23", "Joint Sword-2024A"),
                ("2024-10-10", "Lai National Day speech"), ("2024-10-14", "Joint Sword-2024B"),
                ("2025-03-13", "Lai calls China a 'foreign hostile force'"), ("2025-04-01", "Strait Thunder-2025A")]),
    "north_korea": dict(
        group="military", title="North Korea's provocations against the US and allies (2022–2024)",
        actors=["PRK"], targets=["USA", "KOR", "JPN"], geo=["KN"], signals=MIL,
        keywords=["north-korea", "pyongyang", "kim-jong-un"],
        response_keywords=[["north-korea", "pyongyang"], ["j-alert", "evacuat", "train", "flight", "stock", "market"]],
        impacts=[("2022-03-24", "Hwasong-17 ICBM — first since 2017"),
                 ("2022-10-04", "Missile over Japan — J-Alert"),
                 ("2022-11-02", "Record missile barrage; one lands near South Korean waters"),
                 ("2024-10-18", "Seoul: North Korean troops sent to Russia")],
        lead_window_days=60,
        events=[("2022-01-20", "Politburo signals end of ICBM moratorium"), ("2022-03-24", "Hwasong-17 ICBM"),
                ("2022-09-08", "Law allows pre-emptive nuclear strikes"), ("2022-10-04", "Missile over Japan"),
                ("2022-11-02", "Record barrage; missile crosses NLL"), ("2022-11-18", "ICBM lands in Japan's EEZ"),
                ("2024-06-19", "Russia–North Korea defence treaty"), ("2024-10-18", "Troops to Russia reported")]),
    "south_china_sea_ph": dict(
        group="military", title="China–Philippines clashes in the South China Sea (2023–2024)",
        actors=["CHN"], targets=["PHL"], geo=["RP"], signals=MIL,
        keywords=["south-china-sea", "second-thomas", "ayungin", "scarborough", "west-philippine-sea"],
        response_keywords=[["south-china-sea", "philippine"], ["shipping", "fisher", "supply", "insurance", "oil"]],
        impacts=[("2023-08-05", "China coast guard water-cannons Philippine resupply"),
                 ("2024-06-17", "Violent boarding at Second Thomas Shoal")],
        lead_window_days=60,
        events=[("2023-02-06", "Laser pointed at Philippine vessel"), ("2023-08-05", "Water cannon at Second Thomas Shoal"),
                ("2023-10-22", "Collisions during resupply"), ("2024-03-23", "Water cannon injures crew"),
                ("2024-06-17", "Boarding and axe incident")]),
    "india_pakistan_2025": dict(
        group="military", title="India–Pakistan clash after the Pahalgam attack (2025)",
        actors=["IND", "PAK"], targets=["IND", "PAK"], geo=["IN", "PK"], signals=MIL,
        keywords=["pakistan", "kashmir", "pahalgam", "sindoor"],
        response_keywords=[["india", "pakistan"], ["airspace", "flight", "airline", "stock", "market", "trade", "shipping"]],
        impacts=[("2025-05-07", "Operation Sindoor strikes on Pakistan")], lead_window_days=45,
        events=[("2025-04-22", "Pahalgam terror attack"), ("2025-04-23", "India suspends Indus Waters Treaty"),
                ("2025-04-24", "Pakistan closes airspace to Indian airlines"), ("2025-05-07", "Operation Sindoor"),
                ("2025-05-10", "Ceasefire announced")]),
    "thailand_cambodia_2025": dict(
        group="military", title="Thailand–Cambodia border clashes (2025)",
        actors=["THA", "KHM"], targets=["THA", "KHM"], geo=["TH", "CB"], signals=MIL,
        keywords=["cambodia", "preah-vihear", "border-clash"],
        response_keywords=[["cambodia", "thai"], ["border", "trade", "tourism", "flight", "workers", "factory"]],
        impacts=[("2025-07-24", "Border fighting with artillery and air strikes")], lead_window_days=75,
        events=[("2025-05-28", "Skirmish kills Cambodian soldier"), ("2025-06-23", "Border crossings restricted"),
                ("2025-07-16", "Landmine injures Thai soldiers"), ("2025-07-24", "Fighting erupts"),
                ("2025-07-28", "Ceasefire agreed in Malaysia")]),
    "israel_iran_2025": dict(
        group="military", title="Israel–Iran 12-day war (2025)",
        actors=["ISR", "USA"], targets=["IRN"], geo=["IR", "IS"], signals=MIL,
        keywords=["iran", "fordow", "natanz"],
        response_keywords=[["iran", "israel", "hormuz"], ["oil", "shipping", "tanker", "flight", "airline", "insurance"]],
        impacts=[("2025-06-13", "Israel strikes Iran")], lead_window_days=60,
        events=[("2025-04-12", "US–Iran nuclear talks begin"), ("2025-06-12", "IAEA board finds Iran in breach"),
                ("2025-06-13", "Israeli strikes begin"), ("2025-06-22", "US strikes Fordow, Natanz, Isfahan"),
                ("2025-06-24", "Ceasefire")]),
    "russia_ukraine_2022": dict(
        group="military", title="Russia's escalation before the invasion of Ukraine (2021–22)",
        actors=["RUS"], targets=["UKR", "USA"], geo=["UP"], signals=MIL,
        keywords=["ukraine"],
        response_keywords=[["russia"], ["exit", "suspend", "halt", "withdraw", "pull-out", "pulls-out", "leave", "sanction"]],
        impacts=[("2022-02-24", "Invasion begins")], lead_window_days=150,
        events=[("2021-04-01", "Spring 2021 troop buildup"), ("2021-10-30", "Reports of renewed buildup"),
                ("2021-12-03", "US intel: up to 175,000 troops"), ("2021-12-17", "Russia's security demands"),
                ("2022-01-10", "US–Russia talks in Geneva"), ("2022-02-10", "Russia–Belarus exercises"),
                ("2022-02-21", "Recognition of DPR / LPR"), ("2022-02-24", "Invasion begins"),
                ("2022-03-08", "Wave of Western corporate exits")]),

    # ---------------- Geo-economic / regulatory conflict ----------------
    "us_china_chips_2022": dict(
        group="geoeconomic", title="US semiconductor export controls on China (Oct 2022)",
        actors=["USA"], targets=["CHN"], geo=["CH"], signals=ECON,
        keywords=["export-control", "semiconductor", "chip"],
        response_keywords=[["china"], ["nvidia", "asml", "applied-materials", "lam-research", "samsung", "sk-hynix", "tsmc", "micron"]],
        impacts=[("2022-10-07", "BIS export-control rules on advanced chips and tools")], lead_window_days=75,
        events=[("2022-08-09", "CHIPS and Science Act signed"), ("2022-08-31", "Nvidia discloses A100/H100 China licence requirement"),
                ("2022-10-07", "BIS rules published"), ("2022-10-12", "US staff at Chinese fabs told to stop work (reported)")]),
    "china_japan_seafood_2023": dict(
        group="geoeconomic", title="China bans Japanese seafood over Fukushima water release (2023)",
        actors=["CHN"], targets=["JPN"], geo=["JA", "CH"], signals=ECON,
        keywords=["fukushima", "seafood", "treated-water", "wastewater"],
        response_keywords=[["japan", "japanese"], ["seafood", "boycott", "exporter", "restaurant", "retail"]],
        impacts=[("2023-08-24", "Release begins; China bans all Japanese seafood")], lead_window_days=75,
        events=[("2023-07-04", "IAEA endorses release plan"), ("2023-07-07", "China tightens checks on Japanese seafood"),
                ("2023-08-22", "Japan sets release date"), ("2023-08-24", "Release begins; full ban")]),
    "us_china_tariffs_2025": dict(
        group="geoeconomic", title="US–China tariff war and rare-earth controls (2025)",
        actors=["USA", "CHN"], targets=["USA", "CHN"], geo=["CH", "US"], signals=ECON,
        keywords=["tariff", "rare-earth"],
        response_keywords=[["tariff", "rare-earth"], ["supplier", "supply-chain", "factory", "price", "shipment", "automaker"]],
        impacts=[("2025-04-02", "'Liberation Day' reciprocal tariffs"),
                 ("2025-04-04", "China retaliates; rare-earth export controls"),
                 ("2025-10-09", "China expands rare-earth controls")],
        lead_window_days=60,
        events=[("2025-02-04", "Fentanyl tariffs on China take effect"), ("2025-03-04", "Tariffs raised to 20%"),
                ("2025-04-02", "Reciprocal tariffs announced"), ("2025-04-09", "US raises China tariffs to 125%+"),
                ("2025-05-12", "Geneva truce"), ("2025-10-09", "Rare-earth controls expanded"),
                ("2025-10-30", "Trump–Xi meeting in Busan")]),
    "china_japan_2025": dict(
        group="geoeconomic", title="China–Japan dispute over Takaichi's Taiwan remarks (2025)",
        actors=["CHN"], targets=["JPN"], geo=["JA", "CH"], signals=ECON,
        keywords=["takaichi", "china-japan", "japan-china"],
        response_keywords=[["japan", "japanese"], ["travel", "tourism", "airline", "flight", "seafood", "concert", "film", "retail"]],
        impacts=[("2025-11-14", "China advises citizens against travel to Japan")], lead_window_days=45,
        events=[("2025-10-21", "Takaichi becomes prime minister"), ("2025-11-07", "Takaichi's Taiwan-contingency remarks in the Diet"),
                ("2025-11-14", "China travel advisory against Japan"), ("2025-11-19", "Seafood imports halted again (reported)")]),
}


MILITARY_ROOTS = ["15", "17", "18", "19", "20"]
COLS = {0: "GLOBALEVENTID", 1: "SQLDATE", 7: "A1C", 17: "A2C", 26: "EventCode",
        28: "EventRootCode", 29: "QuadClass", 31: "NumMentions", 34: "AvgTone",
        51: "GeoCountry", 57: "SOURCEURL"}

# Frozen thresholds
BASELINE_WEEKS = 26
COVERAGE_MIN = 0.50
COVERAGE_WINDOW = 12
LEVELS = {1: "Normal", 2: "Watch", 3: "Alert", 4: "Critical"}
