/* Sailor demo data — extracted from the prototype, 2026-09-24.
   The two companies are fictional. Real companies appear only in the
   track record, and only through publicly reported facts. */

const LV = {
  1: { name:"Normal",   fg:"#1F7A4D", bg:"#E6F6EE", bar:"#7FC4A0", means:"Within its usual range. Sailor keeps watching." },
  2: { name:"Watch",    fg:"#8A5A00", bg:"#FFF1CC", bar:"#F2C14E", means:"Off its usual range. Review weekly." },
  3: { name:"Alert",    fg:"#B54708", bg:"#FFE6D5", bar:"#F38744", means:"Several signals moving together. Brief leaders, prepare options." },
  4: { name:"Critical", fg:"#B42318", bg:"#FDE2DF", bar:"#E5484D", means:"Business impact likely or underway. Response team on." }
};

const CO = {
  yuki:{ company:{
  name:"YUKI Electronics", short:"YUKI",
  tagline:"Seoul · chips, phones, appliances · ~$200B revenue",
  prof:{ ind:"mfg", indName:"Manufacturing & Tech", rev:"~$200B", staff:"~270,000",
         sites:"9 countries, 5 with plants", entity:"Listed, Korea", fx:"KRW, USD, VND" },
  lines:[{name:"Semiconductors (memory, foundry)", share:"~40% of revenue"}, {name:"Smartphones & networks", share:"~30%"}, {name:"Appliances & TV", share:"~20%"}, {name:"Displays", share:"~10%"}]
},
    teams:[
  { key:"gr",  label:"Compliance · Legal · GR", tab:"Compliance · Legal · GR", desc:"Export controls, tariffs, sanctions and bills in each market." },
  { key:"hr",  label:"Risk · HR · Ops",          tab:"Risk · HR · Ops", desc:"Military tension, unrest, expat safety and site continuity." },
  { key:"mkt", label:"Brand · Marketing",        tab:"Brand · Marketing", desc:"Boycotts, nationalist sentiment and campaign timing." },
  { key:"str", label:"Strategy · Corp Dev",      tab:"Strategy · Corp Dev", desc:"Footprint, capex timing, sourcing shifts and deal risk." }
],
    exposure:[
  { name:"South Korea", role:"HQ, memory fabs, R&D", detail:"Most employees and fabs", lv:2 },
  { name:"China", role:"NAND fab, packaging, sales", detail:"~20% of revenue; US rules apply to the fab", lv:3 },
  { name:"Taiwan", role:"Foundry partners, logistics", detail:"Key parts and sea lanes", lv:3 },
  { name:"Vietnam", role:"Phone assembly", detail:"~50% of phone output, exports to US", lv:1 },
  { name:"Japan", role:"Materials supply", detail:"Photoresist, high-purity chemicals", lv:1 },
  { name:"United States", role:"Largest market, new fab", detail:"Tariffs and export rules", lv:2 },
  { name:"India", role:"Phone plant, growth market", detail:"Second phone hub", lv:1 },
  { name:"Middle East routes", role:"Shipping and energy", detail:"Red Sea and Hormuz lanes", lv:2 }
],
    changes:[
  { sit:"tw", lv:3, where:"Taiwan Strait", kind:"Military activity",
    title:"PLA air and naval activity near Taiwan is running at 3× its usual level",
    what:"Daily flights and ships around Taiwan have been above normal for three weeks, and Beijing's statements have sharpened ahead of Taiwan's 28 Nov local elections.",
    hit:"A week of closed sea lanes stops phone assembly in Vietnam.",
    why:"Your foundry partners and the sea lanes for Taiwan-made parts sit inside the likely drill zones. A week-long disruption would hit phone output in Vietnam.",
    cta:"Should we escalate? See the Taiwan Strait →", view:"esc" },
  { sit:"ec", lv:3, where:"United States → China", kind:"Regulation",
    title:"Draft US rule would tighten servicing of chip tools inside China",
    what:"A proposed update to US export controls would require licences to maintain some chipmaking equipment in China. Comments close in 30 days.",
    hit:"Your China NAND fab could lose tool servicing within a quarter.",
    why:"Your China NAND fab depends on US-made tools. If servicing needs a licence, maintenance could stall within a quarter.",
    cta:"See the triggers for this rule →", view:"esc" },
  { sit:"nk", lv:2, where:"Korean Peninsula", kind:"Military activity",
    title:"North Korean missile launches doubled this month",
    what:"Four short-range launches in three weeks, up from a usual one or two. No long-range test yet.",
    hit:"Nothing to do yet — HQ and the main fabs sit inside it.",
    why:"Your HQ and main fabs are in Korea. At this level no action is needed beyond checking staff alert lists.",
    cta:"See North Korea's level →", view:"esc" }
],
    plan:{
  gr: { act:[{t:"Map which China-fab tools need US servicing licences", sit:"ec", o:"Trade compliance", by:"Oct 3", pr:"Cargill · Glencore — worked out what the sanctions regime still allowed before deciding what to stop."}, {t:"File comments on the draft rule with the industry association", sit:"ec", o:"GR", by:"Oct 17", pr:"Walmart — settled classification and origin internally before saying anything in public."}],
        prep:[{t:"Draft licence applications for the top 10 tools", sit:"ec", o:"Legal", by:"Oct 24"}, {t:"Check force-majeure terms with Taiwan partners", sit:"tw", o:"Legal", by:"Oct 31", pr:"IKEA — contract termination and force-majeure review came before the exit decision, not after."}],
        watch:[{t:"Korea supply-chain bill subcommittee vote", sit:"nk", o:"GR", by:"Oct 14"}, {t:"Japan's matching export rules", sit:"ec", o:"Trade compliance", by:"Ongoing"}],
        alloc:[["tw",30],["ec",60],["nk",10]] },
  hr: { act:[{t:"Refresh the Taiwan expat and traveller list", sit:"tw", o:"Security", by:"Oct 2", pr:"Heineken · Carlsberg — several thousand local staff were the centre of the decision."}, {t:"Test the Taiwan staff alert chain", sit:"tw", o:"HR", by:"Oct 6", pr:"Lufthansa — crew willingness decided the resumption, not the risk assessment."}],
        prep:[{t:"Pre-book alternative routes for Taiwan-made parts", sit:"tw", o:"Supply chain", by:"Oct 10", pr:"Singapore Airlines — had 86 days and used them to reroute quietly, with no announcement."}, {t:"Brief the crisis team on drill scenarios", sit:"tw", o:"Risk", by:"Oct 9"}],
        watch:[{t:"Korea shelter and alert lists", sit:"nk", o:"Security", by:"Ongoing"}, {t:"China fab staffing if servicing stalls", sit:"ec", o:"HR", by:"Nov", pr:"Microsoft — relocation and severance took longer than the decision to close the office."}],
        alloc:[["tw",65],["ec",15],["nk",20]] },
  mkt: { act:[{t:"Hold Taiwan-themed campaigns in mainland China", sit:"tw", o:"Brand", by:"Oct 1", pr:"Muji — the product\u2019s Japanese origin was the brand story and became the liability."}],
        prep:[{t:"Prepare neutral holding statements (China, Taiwan)", sit:"tw", o:"Comms", by:"Oct 8", pr:"IKEA — one statement, no marketing, written for criticism from both directions."}, {t:"Set up boycott-mention alerts on Weibo", sit:"tw", o:"Digital", by:"Oct 8"}],
        watch:[{t:"Nationalist sentiment around Oct 10 speech", sit:"tw", o:"Brand", by:"Oct 10", pr:"McDonald\u2019s · Coca-Cola · Starbucks — peer timing mattered more than the decision itself."}, {t:"US media framing of chip rules", sit:"ec", o:"Comms", by:"Ongoing", pr:"Walmart — announced the price rise without owning the reason, and drew a political response."}],
        alloc:[["tw",70],["ec",20],["nk",10]] },
  str: { act:[{t:"Re-run the China NAND capex case with a servicing-licence delay", sit:"ec", o:"Corp Dev", by:"Oct 7", pr:"Samsung \u00b7 SK hynix \u2014 the China fab decision was reopened each time the licence terms moved, not once."},{t:"Put a number on a four-week Taiwan foundry outage", sit:"tw", o:"Strategy", by:"Oct 10", pr:"Apple \u2014 sized the single-source exposure before choosing where to dual-source."}],
        prep:[{t:"Refresh the India-vs-Vietnam phone capacity split", sit:"tw", o:"Strategy", by:"Oct 21", pr:"Foxconn \u2014 the India build-out started two years before it was needed, and that was the point."},{t:"Screen second-source foundries outside Taiwan", sit:"tw", o:"Corp Dev", by:"Nov 7"}],
        watch:[{t:"US fab subsidy conditions and the China clause", sit:"ec", o:"Strategy", by:"Ongoing", pr:"Intel \u00b7 TSMC \u2014 the subsidy terms decided the footprint more than the demand forecast did."},{t:"Japan equipment-maker earnings for demand signals", sit:"ec", o:"Strategy", by:"Oct 28"}],
        alloc:[["tw",45],["ec",45],["nk",10]] }
} },
  trent:{ company:{
    name:"Forest Inc.", short:"Forest",
    tagline:"Seattle · marketplace, cloud, logistics · ~$450B revenue",
    prof:{ ind:"ret", indName:"Retail & Consumer", rev:"~$450B", staff:"~1,500,000",
           sites:"18 countries, 6 in APAC", entity:"Listed, United States", fx:"USD, JPY, INR" },
    lines:[{name:"Marketplace & retail", share:"~55% of revenue"}, {name:"Forest Cloud", share:"~20%"}, {name:"Advertising", share:"~12%"}, {name:"Devices & subscriptions", share:"~13%"}] },
    teams:[
      { key:"gr",  label:"Legal / Public Policy",     tab:"Legal · Public Policy", desc:"Data rules, platform liability, tariffs and export controls." },
      { key:"hr",  label:"Infrastructure / Capacity", tab:"Infrastructure · Capacity", desc:"Data centres, subsea routes, region capacity and site continuity." },
      { key:"mkt", label:"Seller Ops / Trust & Safety", tab:"Seller Ops · Trust & Safety", desc:"Cross-border sellers, listings, tariffs and buyer trust." },
      { key:"str", label:"Strategy / Corp Dev",         tab:"Strategy · Corp Dev", desc:"Region investment, capacity siting, M&A and market entry." }
    ],
    exposure:[
      { name:"Japan", role:"Marketplace, 2 cloud regions", detail:"Largest APAC market", lv:1 },
      { name:"Singapore", role:"APAC HQ, cloud region", detail:"Regional decisions made here", lv:1 },
      { name:"China", role:"Seller base, hardware sourcing", detail:"Most cross-border sellers", lv:3 },
      { name:"Taiwan", role:"Server and accelerator supply", detail:"Cloud capacity depends on it", lv:3 },
      { name:"India", role:"Marketplace, 3 fulfilment hubs", detail:"Data-localisation exposure", lv:2 },
      { name:"United States", role:"HQ, largest market", detail:"Tariffs and de minimis rules", lv:2 },
      { name:"Australia", role:"Marketplace, cloud region", detail:"Stable", lv:1 },
      { name:"Subsea routes", role:"Asia–US cable capacity", detail:"Two cables pass the strait", lv:2 }
    ],
    changes:[
      { sit:"tw", lv:3, where:"Taiwan Strait", kind:"Military activity",
        title:"PLA air and naval activity near Taiwan is running at 3\u00d7 its usual level",
        what:"Daily flights and ships around Taiwan have been above normal for three weeks, and Beijing's statements have sharpened ahead of Taiwan's 28 Nov local elections.",
        hit:"Cloud capacity and Asia\u2013US latency, not a headline.",
        why:"Your server and accelerator supply runs through Taiwan, and two of the subsea cables carrying Asia\u2013US traffic pass the likely drill zones. A week of disruption shows up as cloud latency and capacity, not as a headline.",
        cta:"Should we escalate? See the Taiwan Strait \u2192", view:"esc" },
      { sit:"ec", lv:3, where:"United States \u2192 China", kind:"Regulation",
        title:"Draft US rule would tighten servicing of chip tools inside China",
        what:"A proposed update to US export controls would require licences to maintain some chipmaking equipment in China. Comments close in 30 days.",
        hit:"Singapore and Japan region expansion slips a quarter.",
        why:"Accelerators in your Asian cloud regions sit in scope. If servicing needs a licence, capacity expansion in Singapore and Japan slips by about a quarter.",
        cta:"See the triggers for this rule \u2192", view:"esc" },
      { sit:"nk", lv:2, where:"Korean Peninsula", kind:"Military activity",
        title:"North Korean missile launches doubled this month",
        what:"Four short-range launches in three weeks, up from a usual one or two. No long-range test yet.",
        hit:"A J-Alert breaks same-day delivery in Japan for a day.",
        why:"Your Japan fulfilment network sits inside the alert area. A J-Alert stops trains and breaks same-day delivery windows for a day.",
        cta:"See North Korea's level \u2192", view:"esc" }
    ],
    plan:{
      gr: { act:[{t:"Map which accelerators in Asian regions fall under the draft rule", sit:"ec", o:"Trade compliance", by:"Oct 3", pr:"Cargill · Glencore — established what was still permitted before halting anything."}, {t:"File comments through the cloud industry group", sit:"ec", o:"Public Policy", by:"Oct 17"}],
            prep:[{t:"Draft position on India data-localisation rules", sit:"ec", o:"Legal", by:"Oct 24"}, {t:"Review seller terms for tariff pass-through", sit:"ec", o:"Legal", by:"Oct 31", pr:"Walmart — the pass-through decision was legal and political before it was commercial."}],
            watch:[{t:"Korea platform-liability bill", sit:"nk", o:"Public Policy", by:"Oct 14"}, {t:"EU CBAM reporting scope for marketplace sellers", sit:"ec", o:"Legal", by:"Ongoing"}],
            alloc:[["tw",20],["ec",65],["nk",15]] },
      hr: { act:[{t:"Confirm subsea cable diversity for Asia\u2013US traffic", sit:"tw", o:"Network", by:"Oct 2", pr:"Singapore Airlines — rerouted early and quietly rather than waiting for the corridor to close."}, {t:"Re-test Japan region failover", sit:"nk", o:"Infrastructure", by:"Oct 6", pr:"Lufthansa — resuming is the harder call; the failover has to be proven before it is needed."}],
            prep:[{t:"Pre-position server inventory outside Taiwan lead times", sit:"tw", o:"Supply", by:"Oct 10", pr:"Cargill · Glencore — cargo already in transit was the exposure nobody had modelled."}, {t:"Model capacity if Taiwan shipments pause two weeks", sit:"tw", o:"Capacity", by:"Oct 9"}],
            watch:[{t:"J-Alert impact on Japan same-day delivery", sit:"nk", o:"Operations", by:"Ongoing"}, {t:"Servicing delays on accelerator supply", sit:"ec", o:"Supply", by:"Nov"}],
            alloc:[["tw",60],["ec",25],["nk",15]] },
      mkt: { act:[{t:"Pause Taiwan-linked merchandising in mainland storefronts", sit:"tw", o:"Category", by:"Oct 1", pr:"McDonald\u2019s · Coca-Cola · Starbucks — none of the three could afford to be last."}],
            prep:[{t:"Prepare seller notice on tariff-driven price changes", sit:"ec", o:"Seller Ops", by:"Oct 8", pr:"Walmart — said prices were rising without owning the reason, and paid for it publicly."}, {t:"Set up boycott-mention monitoring on Weibo and Xiaohongshu", sit:"tw", o:"Trust & Safety", by:"Oct 8", pr:"Muji — consumer hostility reached store staff before it reached the results statement."}],
            watch:[{t:"Nationalist sentiment around the Oct 10 speech", sit:"tw", o:"Brand", by:"Oct 10"}, {t:"Cross-border de minimis changes", sit:"ec", o:"Seller Ops", by:"Ongoing"}],
            alloc:[["tw",45],["ec",45],["nk",10]] },
      str: { act:[{t:"Re-time the Singapore and Japan region capacity plan against the licence risk", sit:"ec", o:"Strategy", by:"Oct 7", pr:"Microsoft \u00b7 Google \u2014 region launches slipped quietly rather than being announced and then delayed."},{t:"Size a two-week subsea cable outage in revenue, not latency", sit:"tw", o:"Corp Dev", by:"Oct 13", pr:"Meta \u2014 the 2023 cable cuts were costed after the fact; the number changed the routing budget."}],
            prep:[{t:"Review the India data-centre investment case under localisation rules", sit:"ec", o:"Corp Dev", by:"Oct 24", pr:"Amazon \u00b7 Microsoft \u2014 local-partner structures were chosen before the rules were final, not after."},{t:"Map which cross-border seller categories break at 30% tariffs", sit:"ec", o:"Strategy", by:"Nov 4"}],
            watch:[{t:"Platform liability bills in India and Indonesia", sit:"ec", o:"Public Policy", by:"Ongoing"},{t:"Accelerator lead times from Taiwan suppliers", sit:"tw", o:"Strategy", by:"Oct 28", pr:"Nvidia customers \u2014 lead time, not price, was what forced the allocation decisions."}],
            alloc:[["tw",40],["ec",50],["nk",10]] }
    } }
};

const SIT = {
  tw: { label:"Taiwan Strait", short:"Taiwan", color:"#FFE6D5", level:3 },
  ec: { label:"US chip export controls", short:"Export controls", color:"#FFF1CC", level:3 },
  nk: { label:"North Korea", short:"N. Korea", color:"#E8EEF9", level:2 }
};

const TR_TYPES = [
  { k:"Build-up", n:"6 of 7", r:86, med:"34 days", fg:"#1F7A4D", bg:"#E6F6EE",
    p:"Troop movements, launch preparations, navigation warnings. The preparation itself is the signal, so it shows up in news and official records alike." },
  { k:"Trigger-response", n:"7 of 10", r:70, med:"44 days", fg:"#B54708", bg:"#FFF0E6",
    p:"Exercises, boycotts, retaliation. The event is a reaction, so the trigger has to be watched, not the event. Longest lead times, and most of the misses." },
  { k:"Rulemaking", n:"2 of 4", r:50, med:"26 days", fg:"#B42318", bg:"#FEE9E7",
    p:"Export controls, tariffs, licensing. Our weakest category, and we know why: rules appear in official gazettes before they appear in news. We are not reading gazettes yet." }
];

const TR_EVENTS = [
  ["bld","2022-02-24","Russia invades Ukraine",1,125],["bld","2022-03-24","North Korea: Hwasong-17 ICBM",1,34],
  ["bld","2022-10-04","North Korea: missile over Japan",1,49],["bld","2022-11-02","North Korea: record missile barrage",0,null],
  ["bld","2024-10-18","North Korean troops sent to Russia",1,34],["bld","2025-06-13","Israel strikes Iran",1,11],
  ["bld","2025-07-24","Thailand\u2013Cambodia border fighting",1,3],
  ["trg","2022-08-04","PLA live-fire drills after the Pelosi visit",0,null],["trg","2023-04-08","Joint Sword drills",1,25],
  ["trg","2023-08-24","China bans all Japanese seafood",1,44],["trg","2023-12-10","China coast guard water-cannons Philippine boats",1,50],
  ["trg","2024-05-23","Joint Sword-2024A",1,45],["trg","2024-06-17","Violent boarding at Second Thomas Shoal",0,null],
  ["trg","2024-10-14","Joint Sword-2024B",0,null],["trg","2025-04-01","Strait Thunder-2025A",1,24],
  ["trg","2025-05-07","Operation Sindoor strikes on Pakistan",1,45],["trg","2025-11-14","China advises citizens against travel to Japan",1,11],
  ["reg","2022-10-07","US BIS export controls on advanced chips",0,null],["reg","2025-04-02","US reciprocal tariffs",1,25],
  ["reg","2025-04-04","China retaliates with rare-earth controls",1,27],["reg","2025-10-09","China expands rare-earth controls",0,null]
];

const TR_MISS = [
  { t:"PLA live-fire drills after the Pelosi visit", d:"Aug 2022",
    w:"China\u2013Taiwan activity was pooled with China\u2013US activity, so the Taiwan signal was diluted to 0.0\u03c3. Narrowing the actor pair is the fix, and it needs no new data." },
  { t:"Joint Sword-2024B", d:"Oct 2024", w:"Same pooling problem, on a round with lower news volume than the others." },
  { t:"North Korea: record missile barrage", d:"Nov 2022",
    w:"Came four weeks after the missile over Japan. The rolling baseline had already absorbed the elevated activity, so the barrage looked normal against it." },
  { t:"Violent boarding at Second Thomas Shoal", d:"Jun 2024",
    w:"A single-day confrontation with no public build-up. This is the shock category \u2014 we do not claim to catch these." },
  { t:"US BIS export controls on advanced chips", d:"Oct 2022",
    w:"Published without a prior comment period. The rulemaking record only exists after publication, and we are not reading the Federal Register yet." },
  { t:"China expands rare-earth controls", d:"Oct 2025",
    w:"Chinese ministry notices do not enter the news corpus until they are reported, usually a day or two later. Reading MOFCOM notices directly would close this." }
];

const TR_CURVE = [["Nov 1",0.4],["Nov 15",0.6],["Nov 29",0.9],["Dec 13",1.1],["Dec 20",1.1],["Dec 27",1.1],["Jan 3",1.3],["Jan 10",0.6],["Jan 17",0.7],["Jan 24",0.4],["Jan 31",0.5],["Feb 7",5.4],["Feb 14",-0.1],["Feb 21",0.6],["Feb 28",1.3]];

const BOARD = [
  ["Taiwan Strait", 2.4], ["US export controls", 2.1], ["North Korea", 1.3], ["South China Sea", 0.7],
  ["China – Japan", 0.5], ["US–China tariffs", 0.4], ["India – Pakistan", 0.1],
  ["Russia – Ukraine", -0.2], ["Israel – Iran", -0.5]
];

const GEO = {
  "South Korea":[37.57,126.98], "Korea":[37.57,126.98], "China":[31.23,121.47], "Taiwan":[25.03,121.57],
  "Japan":[35.68,139.69], "Vietnam":[10.82,106.63], "Singapore":[1.35,103.82], "India":[19.08,72.88],
  "Australia":[-33.87,151.21], "Philippines":[14.60,120.98], "Thailand":[13.76,100.50]
};

const ZONES = [
  { lat:24.5, lon:119.5, rx:26, ry:34, label:"Taiwan Strait", below:true },
  { lat:38.5, lon:127.5, rx:20, ry:24, label:"Korean Peninsula", below:false }
];

const UPCOMING = [
  { date:"Oct 10", title:"Taiwan National Day speech", meta:"Big event · past drills followed within days" },
  { date:"Oct 14", title:"Korea: supply-chain security bill, subcommittee vote", meta:"Small event · affects chip subsidies" },
  { date:"Oct 21", title:"US comment period closes on chip-tool rule", meta:"Regulation · final rule can follow in weeks" },
  { date:"Nov 4",  title:"US–ROK combined exercise begins", meta:"Military exercise · North Korea usually responds" },
  { date:"Nov 28", title:"Taiwan local elections", meta:"Big event · watch Beijing's rhetoric" }
];
