# Two Point Hospital — Overview and Core Mechanics

## What the game is

**Two Point Hospital** is a business simulation / hospital management game developed by **Two Point Studios** and published by **Sega**. It was released for PC (Windows, macOS, Linux via Steam) on **30 August 2018**, and later on **PlayStation 4, Xbox One and Nintendo Switch (25 February 2020)**, plus other PC storefronts (Microsoft Store, Origin) and Amazon Luna (November 2020). It runs on the Unity engine, and the PC version sold over one million copies.

The game is the **spiritual successor to Bullfrog's Theme Hospital (1997)**. Two Point Studios was founded in 2016 by Theme Hospital producer **Mark Webley** and lead artist **Gary Carr**, and the game deliberately revives Theme Hospital's formula: build and run hospitals across a fictional region (**Two Point County**), diagnosing and curing patients afflicted with absurd comedy illnesses (Lightheadedness — a light bulb for a head; Pandemic — a pan on the head; Mock Star — Freddie Mercury impersonators; Turtle Head, Verbal Diarrhoea, etc.). The British-humour illness names are intentional puns and official in-game names.

The core loop: place rooms and corridors, hire and train staff (Doctors, Nurses, Assistants, Janitors), keep patients alive, happy and paying as they move through a diagnosis-then-treatment pipeline, and satisfy per-map objectives to earn a 1–3 star rating for each hospital, which unlocks the next hospitals in the county.

---

## The patient lifecycle

### 1. Arrival

Patients arrive at the hospital entrance in a continuous stream. The **arrival rate is driven by hospital Reputation and Hospital Level** (and is subject to a hard cap on many early career maps). Illness Marketing campaigns change the *mix* of arriving patients but not the overall number. Patients enter with **full Health**, which ticks down from the moment they arrive — faster for some illnesses, and faster still if their personal Hygiene is low. If Health reaches zero before treatment begins, they die.

### 2. Reception

Patients queue at a **Reception Desk** (an item, available from the start) or, once unlocked (Flottering, 1 star), a **Reception room** which can hold multiple Reception Pods for higher throughput. Reception is staffed by **Assistants**; Customer Service training speeds up check-in. Patients form a physical queue behind the desk, so leave open floor space.

### 3. GP's Office (the hub of diagnosis)

Every checked-in patient goes first to a **GP's Office** (3x3, staffed by a Doctor). The GP interviews the patient and adds to their **Diagnosis Certainty** percentage. If certainty is still below the required threshold, the GP refers the patient to a dedicated diagnosis room; after each such visit the patient **returns to a GP's Office** for the next referral, ping-ponging until the threshold is met. GP's Offices are therefore the game's #1 bottleneck; experienced players build roughly a 1:1 ratio of GP's Offices to diagnosis rooms.

**Where the GP sends the patient** depends on the doctor's *rank* (not their diagnosis skill): Student Doctors pick diagnosis rooms essentially at random, while each promotion raises the chance of picking the room best suited to that illness; a Senior Consultant always prioritises the best available room.

### 4. How Diagnosis Certainty is calculated

Each visit to a diagnosis room adds Certainty according to two factors:

1. **The illness's diagnosis modifier for that specific room** (a hidden percentage — every illness has a different modifier per room, plus a large first-GP-visit modifier and a tiny return-visit modifier).
2. **The cumulative diagnosis power in the room**: the doctor's/nurse's Diagnosis Skill (base skill from rank, plus General Practice or Diagnostics qualifications) + machine upgrade bonuses + diagnosis-boosting items (e.g. Medicine Cabinet, +2% each).

Certainty gained = (illness's room modifier) × (cumulative diagnosis power). Worked example from the wiki, for Lycanthropy (first GP visit modifier 30%; Cardiology/Fluid Analysis modifier 41%): a Senior Consultant (120% skill) with General Practice V (+75%) in a GP's Office with two Medicine Cabinets gives ~197% total power → 30% × 197% ≈ **59%** certainty from the first GP visit; a Student Nurse (80%) with a Level II Heart Racer (+25%) in Cardiology then adds 41% × 105% ≈ **43%**, reaching 100%.

**Diagnosis rooms** (base game): GP's Office and General Diagnosis, Ward (Hogsport); Psychiatry and Cardiology (Lower Bullocks); Fluid Analysis, X-Ray, M.E.G.A Scan (Mitton University, via Research); DNA Lab (Melt Downs). Ward, Psychiatry and DNA Lab double as treatment rooms.

### 5. Thresholds and the treat / send home / keep diagnosing decision

- The **Policy screen** (Finance → Overview → Policy) has a **diagnosis threshold slider, default 90%**. Once a patient reaches the threshold they are sent for treatment. The **Fast-Track Decision** toggle (off by default) lets any diagnosis doctor/nurse dispatch the patient to treatment directly; with it off, only a GP can sign the patient off (one extra GP visit). *Note:* older guides describe the pre-patch behaviour as "100% required unless fast-track is enabled"; the current behaviour is the configurable threshold + fast-track toggle described above.
- **Send for Treatment (manual):** once a patient has at least **50% certainty**, their inspector panel shows a button to skip further diagnosis. Risky, because certainty feeds directly into treatment success chance.
- **Send Home:** available whenever the patient isn't inside a room. The patient leaves untreated — a small Reputation penalty, but often better than letting an incurable or nearly-dead patient die in your building. Veteran players periodically "purge" hopeless patients this way.
- If neither happens, the patient just keeps cycling GP ↔ diagnosis rooms, losing Health and Happiness in every queue.

### 6. Treatment and cure chance

Once dispatched, the patient queues for the treatment room matching their illness (each illness maps to exactly one room; multi-illness rooms include Pharmacy, Ward, Psychiatry, Injection Room, Fracture Ward, Surgery, DNA Lab). The displayed **Chance of Cure (Treatment Score, capped at 99% — never 100%)** combines four factors:

1. **Base illness difficulty** (a 1–10-ish scale; Grout is easy, Jumbo DNA or Shattered are hard).
2. **Diagnosis Certainty** at the moment of treatment — under-diagnosed patients are markedly more likely to have treatment fail.
3. **Staff Treatment Skill** — the treating doctor's/nurse's rank plus Treatment qualifications (Treatment I–V give +10% treatment skill each) and room-specific qualifications (Surgery, Psychiatry etc.).
4. **Machine level / room gear** — treatment machines can be upgraded to Level II and III via Research, each upgrade filling more of this bar; in machine-less rooms (Psychiatry, Surgery, Ward) in-room items (e.g. Treatment Bookcase, Operation Monitor) add percentage boosts. **Room Prestige itself does not directly raise cure chance** — its effect is on the happiness of the people in the room (see Prestige below); the "room quality" contribution to cures comes from upgrades and score-boosting items.

### 7. Outcomes

- **Cured:** patient pays the treatment fee and leaves happy; +1 Reputation; counts toward the hospital **Cure Rate** statistic (cures ÷ patients processed), which many star objectives target.
- **Treatment failed (ineffective):** each illness has its own probability that a failed treatment **kills** the patient; survivors leave unhappy. −1 Reputation for an ineffective treatment. You are **paid for treatment even if it fails or kills** the patient.
- **Death:** −2 Reputation, and possibly a ghost (see Death mechanics).
- **Sent home:** −0.25 Reputation.
- **Rage quit** (Happiness hits zero): the patient storms out; −0.5 Reputation.
- **Waited too long:** patients who give up in queues cost −0.25 Reputation.

---

## Patient needs and happiness

Patients (and staff) have a **Happiness** mood driven by stacking positive/negative **Feelings**. A patient whose happiness hits 0% rage-quits. The needs to manage:

| Need | Served by | Notes |
|---|---|---|
| **Thirst** | Drinks Machine, Drinking Fountain, Energy/Luxury drinks machines | "Very Thirsty" ≈ −10–12% happiness |
| **Hunger** | Snack Machine, Sweet Dispenser, Luxury/Amusing Snack Machines, Café | "Very Hungry" ≈ −10–12% happiness |
| **Toilet** | Toilets rooms with cubicles; patients refuse clogged cubicles and may go on the floor | Sinks/hand dryers/sanitiser also restore Hygiene |
| **Boredom / Entertainment** | Magazine racks, bookcases, arcade machines (also earn money), TVs, Newsagent/Gift Shop stalls, Giggle Pump | "Very Bored" ≈ −12% happiness |
| **Comfort / Seating** | Benches, sofas near queues | Patients want to sit while waiting |
| **Hygiene (personal)** | Sinks, Hand Dryers, Hand Sanitiser; clean environment | Low hygiene lowers happiness **and speeds up Health loss** |
| **Health** | Not a need per se; Laxative Drinks Machine (Pebberley Island DLC item) restores some health | Reaches 0 → death |

Other happiness modifiers: environment attractiveness, temperature comfort, room prestige, queue lengths, treatment events (cured +, treatment failed −7%, witnessing death, scared of ghosts, earthquakes/fires), and prices perceived as too high. Distribute amenities along the patient flow — a distant toilet block wastes patient lifetime on walking.

Staff have parallel needs (energy/breaks, toilet, food/drink, being paid fairly, prestige of their rooms, training and promotion aspirations); unhappy staff work worse ("I hate my job": −20% speed/diagnosis/treatment skill) and eventually threaten to quit.

---

## Hospital-level systems

### Reputation

A 0–100% score shown per hospital; it rises with each cure and publicity, and falls with failures (values above under Outcomes). Bands are roughly Very Poor / Poor / Fine (~50–60%) / Good (~73%) / Great (86–100%). Higher reputation = **more patients and better job applicants**. General Marketing campaigns and good VIP visits raise it; deaths, rage quits, failed epidemics and over-pricing lower it. High reputation early can be a trap — it floods an immature hospital with patients.

### Hospital Level

A measure of hospital size/quality (max **level 30**), driven by number of rooms, staff employed and room prestige/items (buying plots alone doesn't raise it; it can decrease if you remove things). Effects:

- More patients arrive at higher levels (with harder illnesses appearing).
- Better and more numerous job applicants: every 5 levels adds one applicant slot per staff type (3 slots at level 1 → 6 at level 15+).
- Many star objectives and loan criteria require minimum levels.

### Attractiveness

Items project a radius of environmental effect. Plants and decorative items add attractiveness (green on the heat-map); litter, full bins, clogged toilets, explosion debris and Monobeast infestations subtract (brown). Ugly surroundings apply a negative feeling to everyone nearby. Janitors keep it up by sweeping, emptying bins and watering plants.

### Hygiene (environmental)

Clogged toilets, full bins and litter create low-hygiene zones; people walking through them lose personal hygiene. Janitors are essential; sinks/hand dryers/sanitisers let people recover (staff only use sanitisers when idle).

### Temperature

Three map climates: **Temperate** (no action needed — e.g. all of World 1), **Cold** (needs Radiators, Fireplaces, heating — e.g. World 2, industrial/urban worlds), **Hot** (needs Air Con Units, ice sculptures — e.g. World 4 beach maps and DLC deserts/tropics). The temperature visualisation shows blue (too cold), yellow (comfortable), red (too hot). Too hot/cold applies a happiness-draining feeling; cold patients don winter hats. Machines emit heat — some always (Super Computer), some increasingly as they degrade toward catching fire — and plants near heat need more watering.

### Room Prestige

Each room has a Prestige level 1–5 determined by **room size plus the items inside it** (some items, like the Gold Star Award, give large prestige boosts and are famously "spammed" on walls). Effects on occupants' happiness: **Level 3 +10%, Level 4 +20%, Level 5 +30%**. Staff frequently raise "I want a more prestigious room" requests; low-prestige rooms sap staff morale. Prestige also feeds Hospital Level. It is distinct from corridor Attractiveness.

---

## Death, ghosts and the cure rate

Patients die when (a) Health hits zero before treatment, or (b) treatment fails and the illness's death roll comes up. A dying patient shows a "Close to Death!" then "Dying!" icon with a tolling bell. On death:

- **50% chance a Ghost spawns** and haunts the hospital, scaring patients and staff (negative "Scared of Ghost" feeling, people flee) and dripping ectoplasm that Janitors must mop.
- Only a **Janitor with the Ghost Capture qualification** can vacuum ghosts up. Each capture grants 10 research points toward the illness that killed the patient (a death itself also generates 1 RP). Mousing over a ghost tells you how the patient died.
- In the Close Encounters DLC, captured ghosts can be deposited in the **Ectovat**, which staff can then use to recharge 50% of their energy.

**Cure Rate** is a tracked hospital statistic (successful cures as a proportion of patients handled) and a common 2/3-star objective (e.g. sustain 70–90%). Send-homes prevent deaths but do not count as cures.

---

## Events

### Epidemics

Contagious outbreaks, mostly in Worlds 4–5 (Duckworth-upon-Bilge onwards; also Chasm 24 in Close Encounters). Two base-game contagions: **Abominable Curse** (victims walk like mummies — confusable with genuine Premature Mummification patients) and **Jogger's Ripple** (victims jog and stretch athletically — confusable with happy staff or freshly-cured patients). Infection spreads by proximity/sneezing and **can infect staff**, who then quietly keep spreading it inside rooms.

When detected, the Two Point Centre for Disease Control (TPCDC) issues a challenge: a **limited stock of vaccines** (commonly 20) and a time limit. You must visually spot infected people ("pixel hunt" — slow the game speed to see gaits) and click the **Vaccinate** button on each one's panel. Containing the outbreak brings cash, Kudosh and reputation, with bonuses reported per successful vaccination and per unused dose; letting it spread beyond your vaccine supply or the timer means a reputation hit (~−10) — and some sources also report a monetary fine. Exact reward/penalty numbers vary between sources, so treat specific figures as approximate.

### Emergencies

Periodic letters offer a batch of **4–12 pre-diagnosed patients** with one illness (some illnesses are emergency-only on a given map). You may delay accepting until ready. Accepted patients arrive with flashing lights and "(VIP)" names, skip diagnosis entirely, and jump queues to the treatment room. Typical terms: **cure the quota within 90 days** (Surgery emergencies 150 days). Typical rewards: **+10 Reputation, 10 Kudosh, $10,000**, roughly **+15 Rep / 15 Kudosh / $20,000 for a perfect (all-cured) result**, plus normal treatment fees for every patient. Curing fewer than half instead costs reputation. Survivors past the deadline remain as normal patients — except the classic Lightheadedness/Headcrabedness emergency, where (as a Theme Hospital homage) untreated patients die at the deadline. Tip: multiple treatment rooms split the batch automatically; machines often break under the load.

### VIP visits

Named characters periodically tour the hospital ("Impress the VIP with a nice hospital"); results are good/neutral/bad. Good visits award reputation, Kudosh and sometimes cash (e.g. Health Inspector Henry Jobsworth: $5,000, +8 Rep, 10 Kudosh; Health Minister Tarquin Foxbridge up to +20 Rep, $20,000, 20 Kudosh); bad visits cost reputation. VIPs include Henry Jobsworth, reporter Sally Figblanket, mayor Tabitha Windsock, Health Minister Tarquin Foxbridge, singer Jasmine Odyssey, actor Roderick Cushion (may donate), rival CEOs Augustus Lavender (Holistix — vomits, poisons plants, distracts staff), Sophie Nova (Bungle), cult leader Agatha Sphere (brainwashes patients into rage-quitting, tempts staff to resign) and saboteur Jumbo McNally (litters, wrecks machines left unattended). VIP visits can be toggled off in Sandbox.

### Awards

At the end of each in-game year, the **Hospital Awards Ceremony** hands out up to **eight awards per hospital** (the selection varies by map): Doctor/Nurse/Assistant/Janitor of the Year, Employer of the Year, Most Prestigious Hospital, Patients' Choice, No Deaths, Best Research/Teaching Hospital, Hospital of the Year, Rising Star. Each win pays **$5,000 + 5 Kudosh + 3 Reputation**. Some award trophies are placeable prestige items.

### Disasters

Map-specific hazards, all mitigated by Janitors (maintenance + extinguishers): **fires** (neglected machines ignite, then explode), **earthquakes** (three intensities, damage machines), **electrical storms** (lightning strikes, scorch marks), **volcanic eruptions** (quakes + flaming rocks); DLC adds avalanches, hailstorms and more. Disasters can be disabled in Sandbox.

---

## Marketing, loans and money

### Marketing

Unlocked with the **Marketing room** in Flemington; run by an **Assistant with the Marketing qualification** (up to 4 extra staff make campaigns more effective). Campaigns run per hospital for a chosen **3–12 months** (longer runs are more cost-effective; most cost ~$5,000/month plus a flat fee):

- **General Marketing** (Small/Medium/Large; $10,000 up to $130,000): boosts hospital **Reputation** — bigger campaign, bigger boost.
- **Illness Marketing** (~$16,000–$61,000): raises the **proportion** of arriving patients needing a specific room (Pharmacy, Ward, Psychiatry, Injection, Fracture, Surgery, DNA, plus single-illness rooms like the De-Lux Clinic or Clown Clinic). Total patient volume is unchanged — that's still governed by reputation/level and map caps. Ideal for grinding "cure N of illness X" objectives.
- **Recruitment Marketing** (from ~$2,000/month): increases the rate and/or qualification quality of job applicants of a chosen type.

### Loans

From the Finance tab, three lenders offer escalating tiers (repaid automatically monthly; can be repaid in full any time):

| Lender | Amount | Interest | Term |
|---|---|---|---|
| Two Point Bank | $25,000–$50,000 | 5% p.a. | 24 months |
| Swindles | $75,000–$100,000 | 10% p.a. | 24 months |
| $MC ("Smell My Cash") | $150,000–$250,000 | 15% p.a. | 36 months (requires $500k hospital value, 25 rep, level 2 — some guides cite a hospital-level gate on the top tier) |

**Insurance:** there is **no player-facing insurance mechanic** in Two Point Hospital (unlike some other hospital sims). Insurance exists only as radio flavour (Swindles "also runs an insurance business" per Two Point Radio).

### Income and costs

- **Income:** per-visit fees for every diagnosis step and treatment (treatments pay more; you're paid even for failed treatments); vending machines, arcades and stalls (Newsagent, Gift Shop take a cut); emergency/VIP/award/epidemic rewards; research contract payouts and the "Generate Kudosh"/money research projects; star-objective completion bonuses. Some special maps (Duckworth-upon-Bilge, Underlook Hotel, Wanderoff) replace fee income partly or wholly with **target-based public funding / monthly performance bonuses**.
- **Costs:** staff salaries (the big one — and pay-rise demands as staff level up), room construction and items, machine repairs/replacement, plot purchases, training (external lecturers cost more than in-house trainers), marketing, loan interest; Off the Grid adds energy generation management on its maps.
- **Price adjustment:** the Prices panel lets you tune the fee of **every individual diagnosis/treatment** by percentage. Higher prices earn more per patient but **affect reputation and patient willingness/happiness** — patients feel ripped off if prices are far above base (and marked-up hospitals attract fewer patients), while discounts can buy goodwill at revenue cost. Community consensus (Steam beginner's guide): a blanket **+10%** is essentially free money; much beyond that starts generating unhappiness ("Cost Too Much"-type feelings) and reputation drag. Exact tolerance thresholds aren't officially documented — treat specifics as folk knowledge.

**Hospital Value / Organisation Value:** the summed value of your buildings, rooms, items and cash appears in star objectives ("Hospital Value of $750,000") and career goals ($10M/$20M/$50M organisation value).

---

## Star ratings, hospital level and progression gates

Every hospital has its own **Star Objectives** list for 1, 2 and 3 stars, set by the Two Point Health Ministry and *different on every map* (e.g. Hogsport 1-star: cure 3 Lightheadedness patients; Hogsport 3-star: cure 30 patients, earn $400k, reach $750k hospital value; later maps demand cure rates, reputation levels, staff morale, vaccinations, training counts, etc.). Each star awards **cash + Kudosh + unlocks** (items, machine upgrades, new rooms) — and the **1-star rating is what unlocks the next hospital(s)** on the county map. You never need 3 stars to advance; you can move on at 1 star and return any time, and hospitals keep running while you're away. Star ratings sit on top of the separate, dynamic **Hospital Level** (see above) — objectives frequently reference both.

---

## Kudosh

**Kudosh (K)** is the organisation-wide premium currency — earned anywhere, spendable in every hospital. Earned from: **Career Goals** (lifetime milestones — cures, promotions, training, upgrades, marketing campaigns, stars — paying K100–K1,000 each), **hospital/star objectives**, **award ceremony wins** (K5 each), **VIP visit good reports** (~K10), **emergencies** (K10–15), **staff challenges** (periodic timed challenges such as "cure N patients in X days"), **research projects** that generate Kudosh, and **Superbug Initiative** project nodes. Its sole use: **unlocking new items** in the build catalogue (one-time unlock, then available in all hospitals and purchasable with cash). See the progression file for spending priorities.

---

## Game modes

- **Career mode** — the main campaign across Two Point County's 15 base hospitals (plus DLC regions). No difficulty selector exists; difficulty is baked into each map (climate, funding model, illness roster, disasters). The **Policy screen** (diagnosis threshold, fast-track, staff break rules) and per-treatment pricing are the player's main "tuning knobs".
- **Challenge variants inside career:** some maps change the rules — *Target/funding* modes (Duckworth-upon-Bilge, Underlook Hotel), *Horde/wave* modes (Topless Mountain, Camouflage Falls, Mudbury Festival and all R.E.M.I.X maps — patients arrive in waves that must be fully processed before the next 12-day countdown), *Index* modes (Wellness Index / VIBE meters), *Energy* mode (Windsock), *Marketing* mode (Flemington R.E.M.I.X), *Ambulance* mode (Speedy Recovery).
- **Sandbox / Freeplay** (free update, October 2018; expanded since) — pick any owned map and customise: starting cash (−$20k to $10M) and Kudosh (0–20,000), income multiplier (x0–x2), patient arrival rate (x0.25–x2), illness set (all-over-time / easy / medium / hard / visible-symptoms-only / all-from-start / per-DLC sets), objectives preset (none, cure, cure & expand, moneymaker, research & training, staff development), staff hiring pool, climate, rooms/items/upgrades all-unlocked vs. earned, plots owned, and **on/off toggles for Staff Challenges, Patient Emergencies, VIP Visits, Disasters and Epidemics** (most settings re-adjustable mid-game). Sandbox hospitals can be shared via Steam Workshop.
- **R.E.M.I.X mode** (free updates, Feb & May 2020) — wave-based "digital recreation" remixes of the first six career maps with their own single star to earn.
- **The Superbug Initiative** (free update, April 2019) — online co-operative community research projects: team up with friends to feed research/ghost-capture/activity points into shared project trees that unlock exclusive items (e.g. Brain Chair) for everyone.
- **Room Templates / copy-paste** (free update 1.21) — save any built room (layout + items) as a template and stamp it into any hospital, including cross-save; earlier free updates added the **Interior Designer** (custom wall/floor/item skins, Steam Workshop sharing, Feb 2019).

---

## Sources

- https://two-point-hospital.fandom.com/ — pages: Two Point Hospital, Patients, Diagnosis, Treatment, GP's Office, Hospitals, Illnesses, Death, Ghosts, Epidemics, Emergencies, Marketing, Loans, Kudosh, Career Goals, Hospital Awards Ceremony, Feelings, Boredom, Energy, Complaints, Sandbox Mode, Disasters, Reception, Rooms, Staff (via MediaWiki API)
- https://en.wikipedia.org/wiki/Two_Point_Hospital
- https://steamcommunity.com/sharedfiles/filedetails/?id=1632044281 (Beginner's guide: how not to kill your patients)
- https://gamefaqs.gamespot.com/pc/230622-two-point-hospital/faqs/76595 — sections: Chance of Cure, The Patient Process, Room Prestige, Important Game Concepts, Epidemics, Emergencies, VIP Visits, Which Kudosh Items Do You Recommend First (via Wayback Machine)
- https://www.gamepressure.com/two-point-hospital/ — Finances, Epidemics sections
- https://store.steampowered.com/news/app/535930/ — R.E.M.I.X and Room Templates free-update announcements (via search)
