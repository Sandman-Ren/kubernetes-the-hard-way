# Two Point Hospital — Items Reference

Items are everything you place in a hospital that is not a wall, door, or window: room machines and required furniture, decorative objects, vending machines, seating, hygiene fixtures, and temperature control. This document covers how items work mechanically, the Kudosh unlock economy, a catalog of functional items, and placement strategy. (Two Point Hospital, Two Point Studios, 2018.)

---

## 1. How items work

### Placement: rooms vs corridors

- Any part of the hospital plot that is not a room counts as **Corridor**. The main item list in build mode pertains to corridors, and several items are corridor-exclusive (most notably the **Reception Desk**).
- When editing a room, you get a filtered item list of what that room accepts. Most decorative items can go in nearly any room; some are restricted (e.g. the Gold Star Award can be placed in any room that allows wall items **except** Reception and the Café).
- Items divide roughly into:
  - **Required items** — the room won't function without them (Office Desk in GP's Office, Bed + Screen in Ward, Researcher's Desk in Research, Nurse Station in Ward/Fracture Ward, Console for several machines, Medical Sink in Surgery).
  - **Functional optional items** — stat boosts, need-servicing, hygiene, temperature.
  - **Pure decoration** — attractiveness and/or prestige only.

### Room prestige

- Every room has a **Prestige level from 1 to 5**. It rises two ways: adding items (windows, decorations — even mundane required items like beds and toilets contribute) and making the room physically bigger.
- Being in a high-prestige room gives staff and patients a positive Feeling that increases Happiness; low prestige does the opposite. Staff will complain about (and eventually threaten to quit over) low-prestige workplaces.
- Items tagged "Increases Room Prestige" contribute more prestige per tile than generic clutter. The **Gold Star Award** is the community-standard prestige stuffer: a cheap wall item famous for letting even minimal 3x3 rooms reach Prestige 5.
- Some items give outsized prestige: the Golden Bathroom Suite pieces (Golden Toilet, Golden Sink, Golden Hand Dryer) each grant roughly **three times** the prestige of their normal counterparts.

### Hospital attractiveness

- Separate from prestige: **attractiveness** is a per-area environmental stat visible on the Attractiveness heat map.
- Positive attractiveness comes from plants and decorative items, each radiating a green glow in a small/medium/large radius depending on the item (e.g. Plant = small radius, Sunflower/Palm Tree = medium, Rosebush/Shrubbery = large).
- Negative attractiveness comes from **full bins, clogged toilets, litter, vomit, Monobeast infestations, and machine-explosion debris** (brown glow).
- Patients and staff in an ugly environment get a negative Feeling that reduces Happiness; attractive environments do the reverse and feed the hospital's overall rating.

### Functional % boosts

Certain decor items carry a percentage boost that applies to the **room they are placed in**:

| Boost type | What it does | Range per item |
|---|---|---|
| **+% Diagnosis Power** | Diagnosis rooms produce a bigger diagnosis-certainty gain per visit | +1% to +3% |
| **+% Treatment Power** | Treatment rooms get a higher cure chance | +1% to +3% |
| **+% Research Power** | Research room generates research points faster | +1% to +3% |
| **+% Training Speed** | Training room courses complete faster | +1% to +5% |

Boost items stack — filling a Training Room's spare tiles with bookcases and anatomy posters, or a GP's Office with Wall Monitors and Medicine Cabinets, gives a meaningful cumulative bonus on top of staff skill and room prestige.

### Patient/staff need items

Patients and staff have needs that decay over time: **Thirst, Hunger, Toilet, Boredom (entertainment), Comfort, Hygiene, Energy (staff only), Happiness** overall. Items service them:

- **Thirst** — drinks machines, drinking fountains, coffee/hot chocolate makers (staff), Café.
- **Hunger** — snack/food machines, kiosks, Café.
- **Toilet** — Toilet Cubicles placed inside a Toilets room. Some food/drink items *raise* toilet need (Laxative Drink Machine drastically so).
- **Boredom** — arcade machines (full boredom clear), bookcases (~85%), magazine racks/leaflet stands (~80%), and many decor-entertainment hybrids (statues, jukebox, boom box, grandfather clock — typically 5–30% per interaction). Bored patients lose happiness and may leave.
- **Comfort** — benches and chairs in corridors/queues; sofas and armchairs for staff. Sitting slows happiness (and staff energy) loss.
- **Hygiene** — sinks and hand dryers in Toilets, hand sanitiser dispensers anywhere; low hygiene spreads unhappiness and mess.
- **Staff Energy/recuperation** — Staff Room furnishings: sofas, coffee maker, TV, arcade, dart board, punching bag, exercise frame. Better staff rooms = faster energy recovery = shorter breaks.

### Temperature items

- Three plot climates: **Temperate** (no adjustment needed), **Cold** (needs radiators), **Hot** (needs air-con). Wrong temperature makes everyone unhappy ("boiling"/"freezing" feelings) and hot patients buy more drinks.
- Heaters and coolers have small/medium/large radii; use the Temperature visualisation mode when placing.
- Watch for hidden heat sources: the **Super Computer, Server, and Deep Thing 1/2 emit heat** as a side effect, and damaged machines (e.g. a smoking EZ-Scan) heat their surroundings until repaired.

---

## 2. Kudosh

**Kudosh (K)** is the game's persistent meta-currency, shared across all hospitals on the save. Earned from career goals, completing hospital levels and star ratings, award ceremonies, staff challenges, good VIP-visit reports, and (late-game) researching Kudosh in the Research Room.

- **What it buys:** one-time unlocks of items (and room wall/floor customisation patterns, K50–K200 each). Once unlocked, the item becomes purchasable **with money** in every hospital.
- **Money-only items:** the basic functional set never needs Kudosh — Bin, Bench, Chair, Drinks Machine, Snack Machine, Toilet Cubicle, Sink, Hand Dryer, Plant, Extinguisher, Radiator (level-unlocked), reception desks, all required room items, plus several items unlocked automatically by reaching specific levels/star ratings (e.g. Encyclopedia Bookcases via Mitton University stars, Salty Snacks Machine via Hogsport 2 stars).
- **Typical Kudosh prices:** trinkets 5–50 K; standard decor and utility upgrades 75–300 K; premium functional items 400–800 K; showpieces 900–1,800 K (Fir Tree 1,100, Gift Shop 1,200, Hologram 1,200, Hotdog Kiosk/Kiosk Hut 1,500, Horatio Statue 1,800).
- **Spending priorities (community consensus):**
  1. **Gold Star Award (K200)** — the single best purchase; trivialises room prestige.
  2. **Hand Sanitiser (K150)** — hygiene coverage without toilet trips.
  3. **Air Con Unit (K75)** — mandatory before hot-climate regions.
  4. **Energy Drinks Machine (K200)** — the speed buff also works on staff.
  5. **% boost items**: Wall Monitor (K125), Medicine Cabinet (K400), Diagnostic Bookcase (K175), Treatment Bookcase (K200), Operation Monitor (K300), Anatomy Model (K200).
  6. Quality-of-life: Luxury Drinks/Snacks Machines (K300 each), Arcade Machine (K500), better bins.
  - Low priority: cosmetic statues, rugs, and themed variants that duplicate cheaper items' effects.

---

## 3. Item catalog by function

Prices are the wiki-listed base purchase price; "K" is the one-time Kudosh unlock ("—" = no Kudosh needed / unlocked by level progress or DLC ownership). Effect percentages per the Two Point Hospital wiki.

### 3.1 Stat-boost items (the important ones)

**Diagnosis Power** (place in GP's Office, General Diagnosis, Cardiology, X-Ray, M.E.G.A Scan, Psychiatry, etc.):

| Item | Boost | Kudosh | Price | Notes / source |
|---|---|---|---|---|
| Wall Monitor | +1% Diag, +1% Treat | K125 | $500 | Wall item, also prestige; cheap and stackable |
| Medicine Cabinet | +1% Diag, +1% Treat | K400 | $1,000 | Floor item |
| Weighing Machine | +1% Diag, +1% Treat | — | $400 | Retro Items Pack DLC; no attractiveness |
| Arm-Bot | +1% Diag, entertainment | K500 | $800 | Close Encounters DLC; also reduces boredom 25% |
| Giant Pipette | +1% Diag, prestige | K60 | $900 | Superbug Initiative reward |
| Hologram | +1% Diag, prestige | K1,200 | $1,000 | Superbug Initiative reward |
| Radiation Box | +1% Diag, prestige | K50 | $800 | Superbug Initiative reward |
| Diagnostic Bookcase | +2% Diag, prestige, attractiveness | K175 | $1,000 | Unlocked at Lower Bullocks |
| Deep Thing 1 | +3% Diag, +2% Research | K300 | $25,000 | Superbug Initiative; emits heat |

**Treatment Power** (Pharmacy, Injection Room, Surgery, Ward, treatment clinics):

| Item | Boost | Kudosh | Price | Notes |
|---|---|---|---|---|
| Wall Monitor / Medicine Cabinet / Weighing Machine | +1% | (above) | (above) | Dual diag+treat, see above |
| 3D Printer | +1% Treat (in Identification) | K600 | $1,500 | Pebberley Island DLC; also prestige/attractiveness |
| Treatment Bookcase | +2% Treat, prestige, attractiveness | K200 | $2,000 | Unlocked at Lower Bullocks |
| Operation Monitor | +2% Treat (Surgery), prestige | K300 | $9,000 | Unlocked at Smogley |
| Deep Thing 2 | +3% Treat, +3% Research | K600 | $30,000 | Superbug Initiative; emits heat |

**Research Power** (Research Room only):

| Item | Boost | Kudosh | Price | Notes |
|---|---|---|---|---|
| Researcher's Desk | +1% | — | $10,000 | Required item; each desk adds a researcher slot |
| Research Monitors | +1% | K200 | $8,000 | Wall item |
| Server | +1% | K500 | $5,000 | Emits heat |
| Science Station | +1% | — | $600 | Close Encounters DLC |
| Super Computer | +2% | — | $20,000 | Unlock: Melt Downs 3 stars; emits heat |
| Deep Thing 1 / Deep Thing 2 | +2% / +3% | K300 / K600 | $25,000 / $30,000 | Superbug Initiative; emit heat |

**Training Speed** (Training Room only):

| Item | Boost | Kudosh | Price | Notes |
|---|---|---|---|---|
| Anatomy Poster / Brain Anatomy Poster / Cubism Anatomy Poster | +1% | K80 / K80 / — | $100 | Wall posters; also prestige and a small staff-happiness pulse; Cubism variant unlocks at Grockle Bay 3 stars |
| Anatomy Model | +1–2% | K200 | $800 | Floor decor |
| Display Skeleton | +1–2% | K300 | $1,000 | Floor decor |
| Encyclopedia Bookcase I | +2% | — | $2,000 | Unlock: Mitton University 1 star |
| Knight's Armour | +2%, boredom -25% | — | $5,000 | Also attractiveness |
| Encyclopedia Bookcase II | +4% | — | $4,000 | Unlock: Mitton University 2 stars |
| Wizardry Cauldron | +5%, boredom -25% | — | $3,000 | Best single training item |

### 3.2 Prestige / attractiveness decor (representative)

| Item | Kudosh | Price | Effect |
|---|---|---|---|
| Gold Star Award | K200 | $300 | Wall; attractiveness + big prestige — the standard prestige-5 filler |
| Silver Star Award | K150 | $200 | Wall; attractiveness + prestige |
| Bronze Star Award | K100 | $100 | Wall; attractiveness + prestige |
| Certificate | K25 | $50 | Wall; attractiveness + prestige (cheapest award-type item) |
| Notice Board | K50 | $50 | Wall; attractiveness + prestige |
| Clock | K20 | $100 | Wall; attractiveness |
| Plant | — | $90 | Attractiveness, small radius; the default corridor filler |
| Flowers | K10 | $100 | Attractiveness (unlock: Flottering) |
| Ivy | K25 | $100 | Attractiveness, small radius |
| Cactus | K200 | $90 | Attractiveness, small radius |
| Sunflower | K400 | $200 | Attractiveness, medium radius |
| Rosebush | K500 | $300 | Attractiveness, **large** radius |
| Shrubbery (A Stitch in Time DLC) | K50 | $400 | Attractiveness, **large** radius |
| Palm Tree (Pebberley Island DLC) | K900 | $800 | Attractiveness, medium radius |
| Fir Tree | K1,100 | $1,500 | Attractiveness, medium radius |
| Lamp | K60–125 (per room type) | $300 | Prestige + attractiveness |
| Lava Lamp | K60 | $300 | Prestige + attractiveness (unlock: Flemington) |
| Rug (and themed rug variants) | K150–200 | $300 | Prestige + attractiveness floor coverage |
| Television | K75 | $300 | Prestige |
| Drawing Board | K90 | $300 | Prestige |
| Locker | — | $100 | Prestige (cheap money-only prestige for staff room) |
| Fireplace | K300 | $1,000 | Prestige + attractiveness + **heats area** |
| Horatio Statue | K1,800 | $10,000 | Attractiveness showpiece (Sega/Two Point collection) |
| Gnome (Close Encounters DLC) | K140 | $250 | Attractiveness + prestige |
| Moose Head (Bigfoot DLC) | K600 | $700 | Wall; attractiveness + prestige |

### 3.3 Food & drink

| Item | Kudosh | Price | Serving cost | Effect per serving |
|---|---|---|---|---|
| Drinks Machine | — | $500 | $10 | Thirst -80% |
| Energy Drinks Machine | K200 | $1,000 | $15 | Thirst -80% + Energy Buzz (movement speed up ~30 s; works on staff) |
| Luxury Drinks Machine | K300 | $2,000 | $20 | Thirst -100%, Happiness +10% (unlock: Tumble 3 stars) |
| Chance Drink Machine (Bigfoot DLC) | K500 | $2,000 | $20 | Thirst -80%, random: health ±5%, happiness +5–50% |
| Laxative Drink Machine (Pebberley DLC) | K500 | $2,000 | $20 | Thirst -80%, health up, toilet need drastically up |
| Drinking Fountain | K75 | $300 | free | Thirst -80–100%, hygiene -4%; no income |
| Snack Machine | — | $500 | $20 | Hunger -80% |
| Meaty Snack Machine (Retro pack) | — | $500 | $20 | Hunger -80% |
| Salty Snacks Machine | — | $1,000 | $22 | Hunger -80%, thirst +40% (unlock: Hogsport 2 stars; drives drink sales) |
| Luxury Snacks Machine | K300 | $2,000 | $30 | Hunger -80%, happiness +10% |
| Amusing Snack Machine (Pebberley DLC) | K500 | $2,000 | $30 | Hunger -80%, boredom -50% |
| Absorbent Snack Machine (Bigfoot DLC) | K500 | $2,000 | $30 | Hunger -80%, thirst +10%, toilet need -15% |
| Fancy Food Machine (Culture Shock DLC) | K300 | $2,000 | $35 | Hunger -80%, thirst +70%, happiness +30% |
| Coffee Maker | K200 | $300 | — | Staff: thirst -70% + Caffeine Buzz |
| Hot Chocolate Maker (Bigfoot DLC) | K400 | $300 | — | Staff: thirst -70%, happiness up |
| Café (item, needs Café room + Assistant) | — | $2,000 | $40 | Hunger & thirst -100%, happiness +25% |
| Hotdog Kiosk (staffed) | K1,500 | $2,500 | $80 | Hunger -25%, thirst -15%, happiness +10% |
| Kiosk Hut (Pebberley DLC, staffed) | K1,500 | $2,500 | $100 | Hunger -25%, thirst -15%, happiness +10%, cools customers |
| Cosy Kiosk (staffed) | K750 | $2,500 | $50 | Hunger -80%, happiness +20% |
| Carnival Kiosk (staffed) | — | $1,300 | $40 | Hunger -25%, happiness +10% |

### 3.4 Entertainment (boredom)

| Item | Kudosh | Price | Effect |
|---|---|---|---|
| Arcade Machine | K500 | $1,000 | Boredom -100% per use |
| Endless Arcade Machine (Sega collection) | K550 | $1,200 | Boredom -100% |
| OutRun Arcade (Sega collection) | — | $1,800 | Boredom -80%, $10 per play (income) |
| Pinball Machine (Retro pack) | — | $1,000 | Boredom -100%, $5 per play |
| Bookcase | K75 | $200 | Boredom -85% |
| Leaflet Stand | — | $200 | Boredom -80%; money-only |
| Magazine Rack | K50 | $100 | Boredom reduction (cheap corridor staple) |
| Gift Shop (staffed) | K1,200 | $1,000 | Boredom -100%, happiness +10%, $100 per sale |
| Newsagent (staffed) | — | $1,000 | Boredom -100%, happiness +15%, $60 per sale (unlock: Hogsport 3 stars) |
| Jukebox (Retro pack) | — | $600 | Boredom -5% per interaction |
| Boom Box (Culture Shock DLC) | K450 | $850 | Boredom -30% + prestige/attractiveness |
| Grandfather Clock (Culture Shock DLC) | K400 | $800 | Boredom -30% + prestige/attractiveness |
| Indoor Fountain | K900 | $10,000 | Boredom -30% + attractiveness showpiece |
| Armless Statue (Exhibition pack) | — | $2,000 | Boredom -25% + attractiveness |
| The Statue / Love Statue (Superbug rewards) | K700 / K200 | $10,000 / $8,000 | Boredom -20–25% + attractiveness |
| Bust | — | $850 | Boredom reduction + attractiveness |
| Singing Fish (Pebberley DLC) | K600 | $700 | Wall; boredom -3% + attractiveness |
| Staff-only: Dart Board (K400/$200), Punching Bag (K150/$300), Exercise Frame (K80/$300), TV, consoles | | | Speed up staff recuperation in the Staff Room; Punching Bag also +10% happiness |

### 3.5 Hygiene & sanitation

| Item | Kudosh | Price | Effect |
|---|---|---|---|
| Bin | — | $50 | Litter disposal + vomit receptacle; fills up, janitors empty |
| Big Bin | K20 | $100 | Higher capacity bin |
| Toxic-Waste Bin | K50 | $200 | Bin skin (unlock: Melt Downs 1 star) |
| Recycling Bin (Off the Grid DLC) | — | $50 | Bin variant |
| Elephant Bin (Retro pack) | — | $120 | Bin variant |
| Duck Bin (Speedy Recovery DLC) / Shark Bin (Culture Shock DLC) | K150 / K450 | $350 / $400 | Bin variants |
| Hand Sanitiser | K150 | $200 | Wall; hygiene +75% on use, place anywhere |
| Nice Smelling Sanitiser (Superbug reward) | K150 | $250 | Hygiene +75% + "Nice-Smelling" feeling |
| Sink | — | $400 | Toilets: hygiene +75% after toilet use |
| Hand Dryer | — | $200 | Toilets: hygiene +25% after sink |
| Golden Sink / Golden Hand Dryer (Golden Bathroom Suite) | K60 / K60 | $400 / $800 | Same function + attractiveness + ~3x prestige |
| Medical Sink | — | $500 | Required in Surgery; hygiene +100% for surgical staff |
| Toilet Cubicle | — | $500 | Fully clears toilet need; can clog (janitor fix) |
| Golden Toilet (Golden Bathroom Suite) | K40 | $2,000 | Same + attractiveness + ~3x prestige |

### 3.6 Temperature

| Item | Kudosh | Price | Effect / radius |
|---|---|---|---|
| Small Radiator | — | $100 | Heats, small radius (unlock: Tumble 1 star) |
| Radiator | — | $200 | Heats, medium radius (unlock: Mitton University / Tumble) |
| Mini Radiator (wall) | K75 | $200 | Heats, medium radius; wall-mounted (unlock: Flottering) |
| Large Radiator | — | $300 | Heats, large radius (unlock: Tumble 2 stars) |
| Fireplace | K300 | $1,000 | Heats small radius + prestige + attractiveness |
| Small Air Con Unit | K50 | $100 | Cools, small radius (unlock: Sweaty Palms) |
| Air Con Unit | K75 | $200 | Cools, medium radius (unlock: Sweaty Palms) |
| Ice Sculpture (Pebberley DLC) | K75 | $300 | Cools small radius + attractiveness |
| (Beware) Server / Super Computer / Deep Things | — | — | Unlisted heat emission in a small radius |

### 3.7 Corridor & infrastructure

| Item | Kudosh | Price | Notes |
|---|---|---|---|
| Reception Desk ("Reception" item) | — | $1,000 | Corridor-only; first stop for arriving patients; staffed by an Assistant; multiple desks split the check-in queue |
| Reception Pod | — | $500 | Compact check-in point placed inside a Reception **room**; one Assistant per pod (unlock: Flottering) |
| Bench | — | $100 | Seats 2; queue comfort staple |
| Backless Bench | K100 | $350 | Bench + attractiveness |
| Sophisticated / Bamboo Bench (Bigfoot / Pebberley DLC) | K75 / K75 | $300 | Cosmetic bench variants |
| Chair | K5 | $25 | Cheapest seat; in rooms it also keeps idle staff in-room and boosts their happiness |
| Sofa / Armchair / Luxury Armchair / Egg Chair | varies (staff room free; ~K65–120 for Marketing) | $250–400 | Staff seating: slows happiness/energy loss, speeds staff-room recovery |
| Extinguisher | — | $50 | Wall; lets janitors put out machine fires before the machine explodes — keep one near every machine room |
| Notice Board | K50 | $50 | Cheap wall prestige for corridors |
| Charging Point (Close Encounters DLC) | — | $4,000 | Recharges Robo-Janitors ($1,500 per charge) |
| Nurse Station | — | $500 | Required in Ward/Fracture Ward/Herb Garden; adds prestige |
| Office Desk / Console / Screen / Bed / Filing Cabinet | — | $200–1,500 | Required room furniture (Filing Cabinet is required in GP's Office but purely decorative) |

There is no separate "information kiosk" item — patient direction is handled entirely by Reception desks/pods; the various "Kiosk" items (Hotdog, Cosy, Carnival, Kiosk Hut) are staffed food stalls.

---

## 4. Item strategy

### Minimum-viable prestige-5 rooms

- Build rooms at (or near) minimum size, then wallpaper the interior with **Gold Star Awards** (and Certificates/posters where wall space is short). A 3x3 GP's Office typically reaches Prestige 5 with roughly 6–8 Gold Star Awards plus a window or two — far cheaper in floor space than upsizing the room.
- Windows are free prestige with no floor cost; add them by default.
- Use the room-inspector prestige bar while decorating: stop adding items the moment level 5 is reached.
- For Toilets, the Golden Bathroom Suite items hit prestige caps almost by themselves (3x prestige each).

### Stacking % boosts

- **GP's Office / diagnosis rooms:** 2x Wall Monitor (walls) + Medicine Cabinet(s) + Weighing Machine in spare tiles = +4–5% diagnosis power per room for little money; add Diagnostic Bookcase (+2%) where floor space allows. Combined with high room prestige and trained staff, this measurably cuts repeat-diagnosis loops.
- **Treatment rooms / Surgery:** Wall Monitors + Medicine Cabinets everywhere; Operation Monitor (+2%) specifically in Surgery; Treatment Bookcase in Psychiatry/treatment rooms. Cure chance scales with treatment power, so these items directly reduce deaths on hard illnesses.
- **Training Room:** the king of stacking — Wizardry Cauldron (+5%), Encyclopedia Bookcase II (+4%), Encyclopedia Bookcase I (+2%), Knight's Armour (+2%), plus +1% anatomy posters/models on every wall. A decked-out training room can shave a large fraction off course times, which compounds across every staff member you ever train.
- **Research Room:** every Researcher's Desk, plus Servers/Research Monitors/Super Computer on spare tiles. Remember the heat: pair Server/Super Computer/Deep Things with an Air Con Unit (or exploit them as free heating in cold-climate hospitals like the Bigfoot region).

### Corridor layout for needs

- Cluster a **needs hub** near waiting hotspots (GP queue, diagnostics wing): drinks machine + snack machine + bin + bench + magazine rack/arcade + hand sanitiser, with a Toilets room adjacent.
- Place **bins next to every vending machine** (rubbish is generated where food is consumed) and scatter them along queues for vomit control.
- **Benches along queue lines**, not in distant lounges — patients only use seating near where they wait.
- Use **Salty Snacks / Fancy Food machines deliberately**: they raise thirst, funneling patients into adjacent (profitable) drinks machines.
- One **Extinguisher within reach of every machine room**; one **hand sanitiser near treatment rooms** hit by vomit waves.
- **Energy Drinks Machine in/near the Staff Room** — the movement-speed buzz applies to staff and is one of the cheapest throughput boosts in the game.
- In hot/cold maps, chain Air Con Units/Radiators so radii overlap corridors and room interiors alike; check with the Temperature overlay.

---

## 5. DLC & pack item themes (brief)

| Source | Item theme |
|---|---|
| **Bigfoot** (DLC, 2018) | Winter/cabin items: Hot Chocolate Maker, Moose Head, Chance Drink & Absorbent Snack Machines, Sophisticated Bench, Luxury Armchair, Globe |
| **Pebberley Island** (DLC, 2019) | Tropical: Palm Tree, Bamboo Bench, Ice Sculpture, Kiosk Hut, Singing Fish, Laxative Drink & Amusing Snack Machines, Fridge, 3D Printer |
| **Close Encounters** (DLC, 2019) | Sci-fi/alien: Arm-Bot, Gnome, Database, Science Station, Supply Rack, Charging Point (Robo-Janitor support) |
| **Off the Grid** (DLC, 2020) | Eco/green: Recycling Bin, Big Screen, Hat Rack, Doormat |
| **Culture Shock** (DLC, 2020) | Film-studio/culture: Boom Box, Grandfather Clock, Shark Bin, Fake/False Fan, Golden Statuette, Fancy Food Machine, Mop & Bucket, Book Case Jr. |
| **A Stitch in Time** (DLC, 2021) | Time-travel eras (medieval/prehistoric/future): Shrubbery and era-themed decor |
| **Speedy Recovery** (DLC, 2022) | Ambulance/transport theme: Duck Bin, ambulance-themed decor |
| **Retro Items Pack** | 60s–70s kitsch: Jukebox, Pinball Machine, Weighing Machine, Elephant Bin, Meaty Snack Machine, Retro TV |
| **Exhibition Items Pack** | Museum pieces: Armless Statue and other exhibits |
| **Fancy Dress Pack** | Costume decor: Hat Stand etc. |
| **Golden Bathroom Suite** (pre-order bonus) | Golden Toilet, Golden Sink, Golden Hand Dryer — triple prestige bathroom fixtures |
| **Sega / Two Point Collection (free)** | OutRun Arcade, Space Harrier Mammoth, Endless Arcade Machine, Football Manager Tactics Board, Horatio Statue |
| **Sonic the Hedgehog Pack (free, 2021)** | Sonic Statue, Sonic Rug, Sonic Trees/Totems and costumes |
| **The Superbug Initiative** (free co-op update) | Community-project reward items, many with unique stat boosts: Deep Thing 1/2, Hologram, Radiation Box, Giant Pipette, Nice Smelling Sanitiser, The Statue, Love Statue |

DLC items otherwise follow base-game rules (same Kudosh/money economy); owning the DLC adds them to the catalogue in all hospitals.

---

## Sources

- Two Point Hospital Wiki (Fandom) — item pages retrieved via the MediaWiki API (two-point-hospital.fandom.com/api.php), July 2026 snapshot. Key pages: individual item articles (Gold Star Award, Wall Monitor, Medicine Cabinet, Diagnostic/Treatment/Encyclopedia Bookcases, Deep Thing 1/2, all vending machines, bins, sanitisers, radiators/air-con, benches, kiosks, Reception, Nurse Station, etc.); category listings ("Items", "1–3% Diagnosis/Treatment/Research/Training Boost", "Bins", "Temperature").
- Two Point Hospital Wiki — "Kudosh", "Rooms" (Prestige, Customisation sections), "Hospitals" (Attractiveness, Temperature sections).
- Effect percentages, prices, and Kudosh costs are as listed on the wiki; where the wiki gave no figure, a dash is used. Strategy notes synthesise the wiki's item "Function" descriptions and widely-repeated community guidance (e.g. Gold Star Award prestige stuffing, Energy Drink staff buff).
