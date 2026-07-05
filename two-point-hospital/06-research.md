# Research (In-Hospital Research System)

Research is Two Point Hospital's tech tree. It is performed in the **Research Room**, unlocked during the introductory section of **Mitton University** (level 4, the first hospital of the Cold region). Completing research projects permanently unlocks new rooms, machine upgrades and higher Research qualifications **for every hospital in your Foundation**, and repeatable projects convert researcher time into cash and Kudosh.

## The Research Room

| Property | Value |
|---|---|
| Room type | Facility room |
| Unlocked | Mitton University (intro challenge: reach Hospital Level 3 + upgrade a machine) |
| Minimum size | 3x4 |
| Base build price | $35,100 |
| Required items | Door, Research Pod ($20,000), Researcher's Desk ($10,000) |
| Staff | Doctor with a **Research** qualification (any level) |
| Max staff | 1 by default; the Room Inspector setting allows up to **4 additional** researchers (5 total, like a Ward) |

Mechanics:

- Start a project by clicking the **Research Pod** (or dropping a Research-qualified doctor into an idle Research Room) and picking a project from the list.
- Every project has a **Research Points (RP)** target and a **Green Light Fee** (usually $1,000) paid when the project is (re)started.
- Projects can be paused and resumed with **no progress lost** — even resumed in a *different hospital* — but the Green Light Fee is paid again on every resume.
- Multiple Research Rooms can run in one hospital, on different projects or all pooled onto the same one.
- Once complete, the unlock (room / machine upgrade / qualification level) is permanent and Foundation-wide; researched cash goes to the current hospital, Kudosh to the Foundation.

## Research Points and speed

RP generation scales with the researchers working and the room's items:

**Staff.** A doctor's contribution is based on their Research skill. Qualification levels (each must itself be researched before it can be taught, except level I):

| Research qualification | Effect | Training Units needed | Guest trainer cost |
|---|---|---|---|
| I (Increased) | Allows working in Research | 240 TU | $10,000 + $5,000/trainee |
| II (Enhanced) | +50% Research skill | 300 TU | $10,000 + $10,000/trainee |
| III (Advanced) | +50% | 360 TU | $10,000 + $15,000/trainee |
| IV (Elite) | +50% | 420 TU | $10,000 + $20,000/trainee |
| V (World Class) | +50% | 480 TU | $10,000 + $25,000/trainee |

Doctors also gain experience (Training Units) passively while researching, so long-serving researchers level up on the job.

**Items.** Research Boost items are small individual boosts but stack cumulatively:

| Item | Research boost | Cost | Unlock |
|---|---|---|---|
| Researcher's Desk (required item) | +1% | $10,000 | Mitton University |
| Research Monitors (wall item) | +1% | $8,000 (K200 to unlock) | Mitton University |
| Server | +1% | $5,000 (K500) | Mitton University 3 stars |
| Super Computer | +2% | $20,000 | Melt Downs 3 stars |
| Science Station | +1% | $600 | Chasm 24 1 star (Close Encounters DLC) |
| Deep Thing 1 | +2% (also +3% Diagnosis) | $25,000 (K300) | Superbug project "Learning Machine Learning" |
| Deep Thing 2 | +3% (also +3% Treatment) | $30,000 (K600) | Superbug project "Learning Machine Learning" |

Note: the Server's research boost only applies in the Research Room (it can also be placed in DNA Lab, Fluid Analysis, M.E.G.A Scan etc., where it does not boost research).

**Other RP sources:** capturing a **ghost** can grant a small number of RP (assigned to a project relevant to the patient's cause of death), and the Mitton University briefing states that diagnosis and treatment of patients can also contribute research progress.

## Project structure

Room/machine projects follow a fixed **three-stage pattern** (only Training: Research has four stages):

1. **Room project** — unlocks the room and its level-I machine (cheap: 250–2,000 RP).
2. **Upgrade** — unlocks the machine's level II (2,000 RP).
3. **Advanced Upgrade** — unlocks level III (5,000 RP), after which the chain disappears.

Per the GameFAQs guide, upgrade-tier projects only become available after you have actually built (and then upgraded) the machine in one of your hospitals — you can't research level III before owning a level II machine somewhere. (Uncertain: exact gating conditions; the wiki only says each stage appears after its predecessor completes.)

### Machine upgrades: cost and benefit

Upgrades are installed by a **Janitor with the Mechanics qualification**; the machine is unavailable during the work (interruptible without losing progress).

| Upgrade level | Treatment/Diagnosis power | Install cost | Estimated install time |
|---|---|---|---|
| Level II | +25% | $10,000 | 37 days |
| Level III | +50% | $20,000 | 112 days |

(Values from the Colourizer and Jab Master wiki pages; the pattern is uniform across machines. Diagnosis machines gain Diagnosis power instead — e.g. a Heart Racer II contributes 25% diagnosis skill.) Upgrades also raise room prestige and are the single biggest lever on cure rate for machine-based treatment rooms.

## What can be researched

### Training: Research (Mitton University)

| Project | Output | RP | Fee |
|---|---|---|---|
| Training: Research (1) | Research II teachable | 1,000 | $1,000 |
| Training: Research (2) | Research III | 2,000 | $1,000 |
| Training: Research (3) | Research IV | 4,000 | $1,000 |
| Training: Research (4) | Research V | 8,000 | $1,000 |

### Repeatable (income) research

Unlocked after **five completed research projects** (base-game pair); repeatable forever — this is the "income when nothing left to research" outlet:

| Project | Output | RP | Green Light Fee | Source |
|---|---|---|---|---|
| Generate Kudosh | K20 | 1,000 | $1,000 | Base game |
| General Research | $20,000 | 1,000 | $1,000 | Base game |
| Roderick's Plot Hole | $35,000 | 1,500 | $2,000 | Bigfoot DLC (Swelbard, after Urban Mythology research) |
| Cheesier Gubbins | $45,000 | 2,000 | $3,000 | Bigfoot DLC (Swelbard, after Roachburger Scandal) |
| Time Travel | $50,000 | 5,000 | $1,000 | A Stitch In Time DLC (Clockwise-before-Thyme 2 stars) |

### Base-game rooms (research-locked)

Through the base campaign you research 3 diagnostic rooms, 6 treatment rooms and the DNA Lab (both). RP costs are stage 1 / stage 2 (machine II) / stage 3 (machine III); Green Light Fee $1,000 per stage (M.E.G.A Scan stage 1 is $2,000).

| Room (machine) | Type | Project appears at | RP (room / II / III) |
|---|---|---|---|
| Chromatherapy (Colourizer) | Treatment (Grey Anatomy) | Mitton University | 250 / 2,000 / 5,000 |
| Injection Room (Jab Master) | Treatment (multi-illness) | Mitton University — required to treat patients there | 1,000 / 2,000 / 5,000 |
| Fluid Analysis (Fluid Accelerator) | Diagnostic | Mitton University | 1,000 / 2,000 / 5,000 |
| X-Ray (X-Ray Machine) | Diagnostic | Mitton University | 2,000 / 2,000 / 5,000 |
| M.E.G.A Scan (M.E.G.A Scanner) | Diagnostic | Mitton University | 1,000 / 2,000 / 5,000 |
| Pest Control (Ultrasonic Cannon) | Treatment (Animal Magnetism) | Flemington | 1,000 / 2,000 / 5,000 |
| Head Office (Turbo-Plunger) | Treatment (Turtle Head) | **Smogley — must be researched to progress the level** | 1,000 / 2,000 / 5,000 |
| DNA Lab (Healixir) | Diagnostic + Treatment (Denim Genes, etc.) | Melt Downs | 1,000 / 2,000 / 5,000 |
| Shock Clinic (Discharger) | Treatment (Shock Horror) | Melt Downs | 1,000 / 2,000 / 5,000 |
| Resolution Lab (Debugger) | Treatment (8-bitten) | Duckworth-upon-Bilge | 1,000 / 2,000 / 5,000 |
| Cryptology (Decrypter) | Treatment (Premature Mummification) | Sweaty Palms | 1,000 / 2,000 / 5,000 |
| Recurvery Room (Recurvery Unit) | Treatment (Cubism) | Grockle Bay | 1,000 / 2,000 / 5,000 |

Machine-upgrade-only chains also exist for the non-researched starter rooms (unlocked at various levels/star ratings): General Diagnosis (EZ-Scan II/III), Cardiology (Heart Racer), Pharmacy (Drug Mixer), De-Lux Clinic (De-Lux O-Luxe), Pans Lab (Extract-a-Pan) and Clown Clinic (Dehumorfier) — each 2,000 / 5,000 RP.

### DLC rooms (each DLC adds 3 researchable treatment rooms, Off The Grid adds 4)

| DLC | Rooms (level where the project appears) |
|---|---|
| Bigfoot | Doghouse (Underlook Hotel, 500 RP), Urban Mythology (Swelbard, 1,000), Reanimation (Roquefort Castle, 1,000) |
| Pebberley Island | Indentification (Pebberley Reef, 1,000), Escape Room (Overgrowth, 1,000), Correcting Pool (Topless Mountain, 1,000) |
| Close Encounters | Self-Assembly (Goldpan, 1,000), Toad Hall (Camouflage Falls, 1,000), Personification (Chasm 24, 1,000) |
| Off The Grid | Woodwork (Wanderoff, 500), Herb Garden (Old Newpoint, 1,000), Farmacology (Old Newpoint, 1,000), Tech Support (Windsock, 750) |
| Culture Shock | Danger Zone (Plywood Studios, 500), Wash Pit (Mudbury Festival, 500), War Room (Fitzpocket Academy, 750) |
| A Stitch In Time | Time Portal (Clockwise-before-Thyme, 1,000) |
| Speedy Recovery | Cloud Computing (Ailing, 500), Wax Works (Betts Shore, 500), Powder Room (Pointy Pass, 500) + ambulance upgrade chains (Pantomobile, Big Healer, Relicopter, Feather Balloon, Airloovator, Compliant Colin) |

All DLC rooms follow the same II (2,000 RP) / III (5,000 RP) upgrade pattern (Herb Garden gets a single "Power Flower Bed" upgrade at 1,000 RP; War Room's Meltn' Mould appears to have only a II upgrade).

## Levels that REQUIRE research

- **Mitton University** — the research tutorial level. The "Research Licence" challenge requires researching **Chromatherapy, Injection Room, Fluid Analysis, X-Ray and M.E.G.A Scan**. Star goals include: train a doctor in Research + complete the Chromatherapy project (1 star), generate 2,000 RP (2 stars), generate 4,000 RP (3 stars). Its R.E.M.I.X variant asks for a Level 5 Research Room.
- **Smogley** (level 7) — Turtle Head patients cannot be cured until you research the **Head Office**; the level effectively requires an on-site or prior research effort.
- Flemington, Melt Downs, Duckworth-upon-Bilge, Sweaty Palms and Grockle Bay each introduce illnesses whose treatment rooms must be researched (see table above) — but because unlocks are **global**, you can research them once (e.g. at Mitton) and never build a Research Room in those hospitals.

## Strategy

- **Use Mitton University as a dedicated research hospital.** Mitton pays a bonus for every completed research project and every staff member trained (the TechRaptor guide reports **$10,000 per completed research** and **$5,000 per employee trained** — treat exact figures as guide-reported), and it only offers unqualified student doctors, perfect blank slates. A common approach: earn 1 star normally, then restart the level and build only a Research Room (or two), Training Room, Staff Room and Toilets — no reception, no patients. Hire a janitor for maintenance and doctors to train toward Research V.
- **Room setup:** enable all 5 researcher slots, fill walls with Research Monitors (+1% each) and add Super Computer / Servers / Deep Things; boosts are small but cumulative. Keep the room warm (Mitton is a cold map) and drop an item like the Brain Chair/coffee maker nearby for staff happiness.
- **Cash flow:** your only income in a patient-free research hospital is General Research ($20,000 per 1,000 RP) plus training/research bonuses; keep a cash buffer (the guide suggests staying above ~$200,000) and remember losing condition is -$300,000. Loans are available if needed.
- **Priorities:** research rooms needed to progress the current level first; then Training: Research II–V early (it compounds everything else); then machine upgrades for high-traffic rooms — upgrade **diagnostic machines** (X-Ray, M.E.G.A Scan, Fluid Analysis) and problem treatment rooms first, since +25%/+50% machine power directly raises diagnosis and cure rates. Generate Kudosh runs are a decent idle default once the tree is exhausted.
- Yearly **Hospital Awards** include "Best Research Hospital" ($5,000, K5, +3 reputation), and Mitton also hosts an online **Research Challenge**.

## Sources

- Two Point Hospital Wiki (Fandom, via MediaWiki API): "Research", "Research (Room)", "Staff Training", "Mitton University", "Colourizer", "Jab Master", item pages (Server, Super Computer, Science Station, Research Monitors, Researcher's Desk, Deep Thing 1/2), "Hospital Awards Ceremony", "Janitor" — https://two-point-hospital.fandom.com/wiki/Research
- GameFAQs: CityBuilderAK47's Two Point Hospital Strategy Guide (FAQ 76595), "Research Projects" appendix (via Wayback Machine) — https://gamefaqs.gamespot.com/pc/230622-two-point-hospital/faqs/76595/research-projects
- TechRaptor: "The Key to Research in Two Point Hospital" (via Wayback Machine) — https://techraptor.net/gaming/guides/key-to-research-in-two-point-hospital

Uncertainties are marked inline; notably the Mitton per-research/per-training bonus amounts, the exact gating of upgrade-tier projects, and whether stage-1 RP costs vary slightly by patch (GameFAQs lists a few values — e.g. X-Ray III at 4,000 RP — that differ from the wiki's current 5,000 RP standard).
