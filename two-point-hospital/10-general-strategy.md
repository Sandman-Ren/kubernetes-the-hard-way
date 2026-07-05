# Two Point Hospital — General Strategy & Meta Guide

The distilled playbook for the base game (2018, Two Point Studios), synthesized from the
GameFAQs CityBuilderAK47 strategy guide (FAQ of the Month, Oct 2018; v1.9, 2023), the Two Point
Hospital Fandom wiki (mechanics/math), the top-rated Steam Community beginner guide, and several
community tip compilations (Basically Average, TheGamer, Steam forum threads). Opinionated on
purpose; conflicting opinions between sources are flagged inline.

---

## 1. Core principles

### GP throughput is the master bottleneck

Every patient starts at a GP's Office, and — unless you change policy — returns to a GP after
*every* diagnosis room visit for "sign-off". The GP's Office is therefore visited 2–4x more than
any other room, and GP queues are the first thing that collapses when a hospital scales. All
sources agree on this; the Steam beginner guide calls the GP "the biggest, most powerful cog in
the diagnosis system" and estimates a mature 250-patient hospital needs **about 8 GP's Offices**.

How diagnosis actually works (Fandom wiki math):

- Each visit adds Diagnosis Certainty = (illness's per-room modifier %) × (staff member's
  cumulative diagnosis skill).
- Cumulative skill = base skill from rank (a Senior Consultant has 120%) + qualifications
  (**General Practice = +15% per level, so GP V = +75%**; generic Diagnostics = +10%/level)
  + room items (each Medicine Cabinet = +1% diagnosis power; machine upgrades add more).
- Worked example: Senior Consultant (120%) + GP V (+75%) + 2 Medicine Cabinets (+2%) = 197%
  cumulative; against an illness with a 30% first-visit GP modifier that's a **~59% certainty
  gain in one visit** — near "one-shot" territory. An untrained junior doctor manages ~10%.
- Critical subtlety: **only the doctor's rank (Student → Senior Consultant) determines how
  intelligently they route patients** to the next diagnosis room; a Senior Consultant always
  picks the room best suited to the illness. Diagnosis skill doesn't affect routing.

Scaling rules of thumb (GameFAQs):

- Queue "magic number" is **6** — when any room's queue consistently exceeds 6, build another
  of that room. For GP's Offices, build more *and* train GPs.
- Keep a **1:1 ratio of GP's Offices to diagnosis rooms** as you expand.
- Train the bulk of your GPs to **General Practice III** (the guide's "magic number"
  qualification level); a few GP IV/V doctors for one-shotting, but IV→V gains are marginal.
  50–66% of your doctors should be on the GP track.
- Enable **Fast Track / "Fast-Track Treatment Decision"** in Finances → Overview → Policy. It
  lets patients above the threshold (default ~85–90% depending on level) skip the final GP
  sign-off — removing one GP visit per patient across the whole hospital. It is *off* by
  default; turning it on is the single biggest GP-queue fix in the game. Tradeoff: sub-100%
  certainty slightly reduces cure chance, so gate it on having Level-III+ staff and upgraded
  machines when a cure-rate goal is active.

### Diagnosis-chain efficiency

Room economics (Fandom wiki; build cost / default diagnosis fee):

| Room | Staff | Cost | Fee | Verdict |
|---|---|---|---|---|
| GP's Office | Doctor | $5,800 | $500 | Build many; the workhorse |
| General Diagnosis | Nurse | $7,100 | $750 | Cheap, nurse-staffed workhorse |
| Cardiology | Nurse | $7,600 | $1,000 | Best value-per-dollar early |
| Ward | Nurse | $7,500 | $2,000 | Dual diagnosis+treatment; excellent |
| Psychiatry | Doctor | $6,100 | $1,000 | Dual-duty; needed for psych illnesses anyway |
| Fluid Analysis | Nurse | $20,100 | $1,200 | Mid-tier; fine when needed |
| X-Ray | Doctor + Radiology | $31,100 | $2,000 | **Commonly skipped** — see below |
| M.E.G.A Scan | Doctor + Radiology | $60,100 | $5,500 | Late-game money printer |
| DNA Lab | Doctor + Genetics | $50,100 | $5,000 | Better used as treatment room |

- **General Diagnosis + Ward are the workhorses**: nurse-staffed (cheaper wages than doctors),
  cheap to build, and many illnesses actually *prefer* basic rooms — advanced machines are not
  universally better. Steam-forum consensus: "most illnesses can be diagnosed with just GP,
  Psychiatry, Ward, General Diagnosis and Cardiology."
- **Why players skip X-Ray**: it costs 4x a Cardiology, requires a doctor with Radiology (an
  expensive, scarce staffing line) rather than a nurse, is slow, and the M.E.G.A Scan (same
  Radiology doctor) outclasses it. The Steam beginner guide explicitly discourages X-Rays for
  slowness/queues. Counterpoint from Steam forums: in the hardest late levels even a GP V only
  gets ~50% on tough illnesses, and basic rooms add only ~12–20% more per visit, so 2–3
  X-Rays/M.E.G.A Scans *do* earn their keep there. Skip X-Ray until roughly the Tropical/Urban
  regions, then go straight to M.E.G.A Scans if you can afford them.
- Set hybrid rooms (Ward, Psychiatry, DNA Lab) to diagnosis-only or treatment-only via the room
  panel when queues tangle; build them in pairs.
- DNA Lab: treat it as a treatment room (its illnesses are among the hardest in the game and pay
  well); only add diagnosis duty once you have multiple labs and the Healixer III upgrade.

### Treat-anyway thresholds and sending home

- Cure chance = illness base difficulty + **diagnosis certainty** + staff treatment skill +
  machine upgrade level. Caps at 99%.
- You can manually "Send for Treatment" at **≥50% certainty**, but certainty feeds directly
  into cure chance. GameFAQs' operating rule: **aim for >90% before treating; 85% is doable;
  80% only if cure rate isn't a level goal.**
- Default policy threshold is 90–100% depending on level; Basically Average recommends keeping
  it at 100% early, dropping to ~85% mid/late game when your staff skill can absorb the risk.
- **Send home** any patient whose treatment chance is poor or whose health is low: community
  rule of thumb (GameFAQs "Great Patient Purge" + TheGamer) — sort the Patients list by health,
  **send home everyone under ~30% health**, case-by-case for 30–50%. A death hurts reputation
  (and cure rate) more than a discharge does.

---

## 2. Layout doctrine

GameFAQs' "9 General Rules of Hospital Layout", condensed and cross-checked:

1. **GP's Offices as close to the entrance/reception as possible** — the heart of the hospital
   stays tied to GPs and diagnosis; everything else gets pushed outward as you grow.
2. **Diagnosis rooms cluster around the GPs.** When you buy new plots, move treatment and
   admin rooms out, then backfill the vacated central space with more GP/diagnosis rooms.
3. **1:1 GP:diagnosis ratio** as you scale.
4. If you must build diagnosis far away, give that wing its own **GP "field office"** (and
   ideally its own reception later).
5. **Hybrid rooms (Ward/Psychiatry/DNA Lab) sit in the middle ring**; psychiatry patients
   deplete health slowly, so psych can sit further out.
6. **Level-specific/emergency treatment rooms near the helipad** and main block — half of an
   emergency is travel time.
7. Rare treatment rooms go further afield.
8. **Administration (Training, Research, Marketing) goes furthest of all** — patients never use
   them. Staff Rooms are the exception: 2–3 spread across the map, near building doors; even a
   2x3 closet with a couch and vending machine works.
9. **Every building gets amenities**: a toilet block (a 4x4 block is a good standard), several
   vending machines, one entertainment item (the Arcade Machine actually turns a profit), bins,
   and radiators/air-con from the Cold Region (level 4) onward. Otherwise patients trek across
   the campus mid-queue and lose 10–20% health.

Other doctrine, agreed across sources:

- **Corridors at least 2 tiles wide; 3 tiles in busy areas** (especially around GP clusters and
  reception). One-tile corridors are a pathing death trap.
- **Build minimum-size rooms** (most are 3x3). Smaller rooms = shorter walks, more rooms per
  building, cheaper. GameFAQs: "build smaller, not larger" is tip #1. Exception: multi-staff
  rooms — Wards run well at **8–9 beds split between 3 nurses** (GameFAQs) or 6 beds / 2 nurses
  (Steam guide); Fracture Wards want two plaster machines; cafes max ~2 assistants.
- **Prestige is decoupled from size**: the community's standard trick is to build the minimum
  footprint and **spam Gold Star Award wall items** (cheap Kudosh unlock) — even a 3x3 room
  reaches Prestige Level 5 this way (myPotatoGames, Basically Average, Steam forums). Prestige
  L3/L4/L5 gives **+10%/+20%/+30% happiness** to occupants, which feeds diagnosis/treatment
  skill via the Happy buff (+10% skill).
- **Reception**: expand from one desk to a multi-pod Reception room (unlocked at Flottering).
  Watch assistant load — one assistant per ~5–6 queued patients; expect a full redesign of the
  reception area at each new star, and a **second reception area at ~175–200 patients**.
  Surround it with vending machines and entertainment — happiness starts draining at check-in.
- **Re-audit the whole layout every +50 patients** (0–50, 50–100, …): follow an actual patient
  from reception and remove unnecessary walking.
- **Room templates**: once you've built a good min-size/max-prestige room, save it as a template
  and stamp it into every subsequent hospital — this trivializes mid-campaign starts.
- Expansion order: don't buy a plot just because you can afford it. Shrink/reorganize first;
  buy when monthly profit is stable at **$10k–20k+**, ideally paying cash. New buildings take
  **~16 in-game days** to construct — time loans accordingly.

---

## 3. Economy

- **Wages are the enemy.** Salaries are the dominant recurring cost. The two biggest early-game
  mistakes are hiring $50k+ senior consultants with scattershot skills, and building too much
  too soon. Be picky but cheap at hire time (see §4). Leave reception unbuilt (hospital stays
  closed, bills stay near zero) until good candidates appear.
- **The 3-strikes build rule** (GameFAQs): don't build a new treatment room the first time you
  see an incurable disease — build it when you've seen the need **three times in one month**.
- **Loans**: three tiers, the **$250,000** tier unlocking at hospital level 5. Interest is a
  drag but loans are the correct answer to expansion crunches and near-bankruptcy; GameFAQs
  calls "not taking a loan when prudent" a classic 2-star failure mode.
- **Price tuning**: raise all prices **+10% across the board** at level start (Steam guide);
  patients rarely refuse at that level. Higher reputation supports higher prices. Diminishing
  returns: as prices climb, "Refuse to Pay" events rise and reputation drips down — but a small
  marketing campaign costs a fraction of the extra revenue and cancels the rep hit (Steam
  forums). GameFAQs case study: stuck at $2.5M hospital value, a +20% price rise blew past a
  $4M goal in half an hour. Keep *amenity* prices at or below default to protect happiness.
- **Marketing ROI**: campaign months cost ~$5,000 (small general $2,500/mo, large general
  $10,000/mo, staff recruitment $2,000/mo) with a ~$1,000 green-light fee; **longer campaigns
  are more cost-effective per month** (Fandom). A 3–4 month general campaign is the standard
  reputation patch. Illness campaigns skew the patient *mix* (Fandom notes they don't raise
  total volume beyond your rep/level cap — GameFAQs' observed "double or triple the patients
  for that room" is the proportion shifting). Room cost is only $15–20k; build it in every
  hospital from Flemington on.
- **Research** is a money tap: once projects are done, park qualified doctors on cash research
  permanently (Steam guide: "General Research should run continuously").
- **Hospital value levers** (for "reach $X value" goals): (a) hard assets — buildings, machines,
  even décor count permanently, so buying and decorating raises the floor; (b) the volatile
  driver is **month-over-month profit** — steady, slightly-rising profits push value up, spiky
  profits whipsaw it; (c) reputation + hospital level → more patients paying higher prices.

---

## 4. Staffing meta

- **Hire cheap, train up.** A junior doctor with GP I + a good trait, trained in-house, beats an
  expensive consultant with a mish-mash of qualifications. All sources agree. At level start,
  hold out for: a doctor with **GP I**, a nurse with **Pharmacy Management** (or Diagnostics/
  Ward Management), a janitor with **Ghost Capture** (Mechanics a bonus), an assistant with
  **Customer Service I**.
- **Traits matter**: prioritize *Will work for peanuts* (Cheap), *Positive* (+10% happiness),
  *A natural mentor/Teacher* (+50% teaching), *Has Potential/Fast Learner* (+50% learning),
  *Motivated* (+20% speed), *Tireless*, *Charming*; the unicorn is *Has magic healing hands*
  (Healer — heals patients on contact; ~2–5% of candidates, hire on sight). Avoid *Grumpy*,
  *Lazy*, *Stupid* (−25% learning), *Expensive*, *Dirty/Litterer*, *Unhygienic*, *Evil*.
- **Training pipeline pattern**: unlocks at Flottering (level 3). Build **two small training
  rooms rather than one big one**; never train more than ~4 at a time; add another room once
  10+ staff are waiting for training. Stack training-speed items (Encyclopedia Bookcase II +4%,
  posters/skeletons +1% each) — community save-files show item-spammed rooms that train staff
  absurdly fast. Prefer an in-house teacher: a senior staffer with **Training Masterclass**
  beats paying guest trainers ($10,000 + $5,000–25,000 per trainee, 160% speed) — though guest
  trainers are worth it when pulling your GP off the floor would blow up queues. Use expensive
  legacy hires as teachers, then fire them.
- **Qualifications that matter most per role**:
  - Doctors: General Practice (bulk of doctors, to GP III; a few IV/V) > Treatment (to III+ for
    treatment-room doctors; +10%/level) > Diagnostics+Radiology or Genetics for machine rooms >
    Research (III→IV is the big jump — research speed roughly doubles) > Psychiatry track for
    psych doctors (+20% treat & diagnose per level from II).
  - Nurses: Diagnostics for General Diagnosis/Cardiology/Fluid Analysis; **Ward Management**
    (+20% ward diagnosis *and* treatment per level) for ward nurses; Treatment + Injection
    Administration / Pharmacy Management (+20% in-room) for the cure rooms.
  - Assistants: Customer Service (reception speed) and Marketing.
  - Janitors: Ghost Capture first, then Maintenance and **Mechanics** (stack to III+ on one or
    two janitors — an untrained janitor takes a month to upgrade one machine), plus Motivation/
    Stamina.
  - Everyone, when 90%+ staff-morale goals appear: **Emotional Intelligence** (+10% happiness)
    and Bedside Manner on patient-facing staff (GPs especially — happiness bubbles on every GP
    visit reduce rage-quits).
- **The "level III doctrine"**: qualification III is where cost/benefit peaks for almost every
  skill; IV–V mostly add speed and are for one-shot GPs, hard DNA/Surgery illnesses, and
  teachers.
- **Break policy**: the slider controls break length (10–30 days) and what fraction of each
  staff type can break simultaneously. Default is stingy; loosen it — staff returning from a
  *complete* break get the **Energised buff (+10% speed and +10% diagnosis/treatment/research
  skill)**, so don't recall staff early. Tired = −20% happiness, the biggest single morale hit.
- **Salary negotiation**: promotion pay-rise sliders have wiggle room — you can usually settle
  slightly *below* the default ask with no consequence, and happiness only jumps at certain
  thresholds. "Not Now" is safe; promote later from the staff panel once profits allow (an
  unpromoted, untrained staffer accrues a −5% "Wants Training" and eventually resignation
  threats on a 90-day timer — a small raise plus an ordered break almost always defuses it).
  Good Pay = +20% happiness, Overpaid = +30%: deliberately overpaying key staff is a cheap
  morale lever on staff-morale levels (Duckworth-upon-Bilge).
- **Manage room assignments** (clipboard icon on the staff list): lock specialists to their
  specialty rooms so your GP IV doctor never wanders into a Pans Lab. Color-code uniforms by
  qualification to spot misplacements at a glance. Enable "Staff Leave Rooms when Idle" so one
  treatment doctor can cover two low-traffic rooms.

---

## 5. Reputation & star-chasing

What actually moves reputation:

- Up: cures; emergency success (+10, perfect +15); VIP visits (+8 to +20); marketing (general
  campaigns); lower prices; awards.
- Down: deaths, rage-quits, failed emergencies, botched epidemics (−10), price hikes,
  Refuse-to-Pay events.
- Reputation (with hospital level) sets patient inflow and price tolerance. **Don't pump
  reputation before your GP/diagnosis chain can absorb the extra patients** — rep-driven
  patient snowball is the classic mid-game collapse (Steam guide + GameFAQs both warn).

Cure-rate management (recurring 85–95% cure-rate star goals):

- **The stat is a rolling window of the last 20 patients who left the hospital, in any
  fashion** — deaths *and* rage-quits count against it, not just failed treatments (GameFAQs).
  So cure rate is as much a happiness/queue metric as a medical one.
- Skill gates: get treatment staff to qualification III+, keep diagnosis certainty ≥90%, and
  **upgrade machines** — janitor upgrades cost $10k/$20k per tier and raise treatment power
  (TheGamer: +25%/+50%; GameFAQs quotes it as roughly +10% cure chance per tier and "fills the
  upgrade bar half/full" — sources disagree on the number, agree it's mandatory for 3-star cure
  rates). Upgrade existing machines *before* buying new rooms.
- Reduce rage-quits: amenities everywhere, temperature control, attractiveness, Bedside
  Manner GPs, prestige-5 rooms.
- Patient triage: manually front-queue sub-10% health patients who have a cure pending (a
  patient called into a room at 0% health still gets their cure attempt); send 90–100%
  diagnosed patients straight to treatment; send hopeless cases home.
- Marketing for easy illnesses: campaign for 0–20% difficulty illnesses (Grout 0%, Clamp 10%,
  Lightheadedness 20%…) to stack the last-20 window with easy cures (TheGamer + Steam guide's
  "lock in 90% of patients to something easy to treat").

Attractiveness & happiness goals: Yucca plants (good beauty-to-maintenance ratio; avoid
high-wilt Rosebush/Sunflower unless janitor-rich), trophy cases, skeletons/anatomy models,
fountains, Big Bins/Toxic-Waste bins, and **more janitors** — they're the real attractiveness
stat. Staff-morale goals: win every staff challenge (huge individual happiness boost), pay
above expectation, Emotional Intelligence for all, purge negative-trait staff, and as a
finisher send everyone on break at once for the recharge spike.

Hospital-value goals: see §3 — hard assets + steady rising profit + a justified price rise.

---

## 6. Advanced / cheese tactics (community-attributed)

All of these are community-discovered, not designed mechanics. Tradeoffs noted.

- **The Great Patient Purge** (GameFAQs, Steam forums, widely used): when queues won't drain,
  pause and mass-discharge patients — from a trim (~10–25%, lowest-health and still-in-reception
  first) up to a **full purge**. Cure rate craters to 0% (the last-20 window is all discharges),
  then rebounds fast because only easy, healthy patients remain; close reception during recovery
  for a cleaner rebound. Cost: **$100k–200k+ of lost fees in a big hospital** — it can
  bankrupt you; it also doesn't fix the underlying capacity problem. Late-game players report
  purging monthly to hold 95% cure rate.
- **Close reception / sell reception pods** to throttle intake when swamped; reopen after the
  backlog clears. Slower, safer version of the purge.
- **Pause-and-plant attractiveness sniping** (GameFAQs): if attractiveness is the last blocked
  objective, pause, carpet the hospital in décor, let the objective tick complete, then sell
  the items back for most of the money. Works because the check is instantaneous.
- **Gold Star Award prestige spam**: minimum-size rooms + walls of Gold Star Awards = Prestige 5
  everywhere (see §2). Tradeoff: none worth mentioning; this is the meta.
- **Training-room item spam + training loops**: bookcase-stacked training rooms plus a Teacher-
  trait mentor make qualification grinding near-instant; combined with hire-cheap this is the
  economy-defining loop. Tradeoff: staff pulled off the floor — stagger classes.
- **GP-only diagnosis builds**: an army of Senior Consultant GP V doctors one-shots most
  diagnoses, letting you nearly skip diagnosis rooms. GameFAQs' rebuttal: diagnosis rooms are
  profit centers and some illnesses still prefer specific rooms — pure-GP builds leave money on
  the table and stumble on high-difficulty illnesses. Viable, not optimal.
- **Mitton University research mule** (GameFAQs): research is account-wide, and Mitton pays
  $5,000 per completed training class and is an easy map. Players return there to grind
  research/training; the sneaky variant is researching a project to ~980/1000 at Mitton,
  pausing, then finishing the last points in the hospital that needs it so *that* researcher
  gets the XP — or running money-research at Mitton to bankroll a struggling save.
- **Save scumming (PC)**: back up save files before risky experiments on near-3-star hospitals
  (GameFAQs recommends it explicitly for cure-rate pushes).
- **Laxative (Swill) vending machines** (Pebberley Island DLC): drinking one restores ~10%
  patient health at the cost of wetting incidents — veterans line treatment corridors with them
  to keep near-death patients alive for the cure. Janitor load goes up.
- **Marketing spam**: back-to-back easy-illness campaigns keep the cure-rate window stuffed and
  income smooth. Tradeoff: each campaign surges a single room's queue — pre-build a second
  treatment room and hire a temp staffer before launching, or you'll convert the surge into
  rage-quits (GameFAQs' "double-edged sword" warning; Basically Average: too many simultaneous
  campaigns cause deaths).
- **Queue micromanagement**: manually reorder room queues (front-load dying patients), toggle
  hybrid rooms between diagnosis/treatment duty, and use half-speed to do it calmly. Some
  players close a room to force its queue to redistribute to a twin room. Tradeoff: pure APM
  tax; the game allows it freely while paused.

---

## 7. Emergencies, epidemics & VIP playbook

**Emergencies** (5–8 pre-diagnosed patients, one illness, usually 90 days — Surgery gets 150):

- Rewards: cure ≥ half → **+10 reputation, 10 Kudosh, ~$10,000**; cure *all* → +15 rep,
  15 Kudosh, roughly double cash. Failure dents reputation.
- Accept only if you have (or can instantly build) capacity. **Two rooms of the target type
  split the group automatically** and halve machine strain — machine breakdown mid-emergency is
  the usual cause of failure, so pre-repair/upgrade and park a janitor nearby.
- Use the pickup tool to drop your best-qualified staffer into the room before the helicopter
  lands; make sure that staffer is fresh (staff going on break mid-emergency is the other
  failure mode). Keep vending/toilets adjacent so patients don't wander to another building.
- Keep the relevant treatment room near the helipad on levels with recurring emergency types.

**Epidemics** (Abominable Curse — mummy walk; Jogger's Ripple — athletic jog; from the Tropical
region onward): you're asked to vaccinate all infected before the timer. Playbook: drop game
speed to half to spot the telltale animations (Jogger's Ripple is easy to confuse with the
cured-patient strut and happy-staff jog); trace new infections back to a common area; remember
**staff can be carriers** — if the infected count keeps ticking up for months, it's probably a
sedentary staffer (GP or nurse); open-and-close rooms to "shake" occupants out where you can see
them. If it escapes into a packed corridor, it's often unwinnable — **eating the −10 reputation
is a legitimate choice**; a healthy hospital recovers it quickly through cures.

**VIP visits**: rewards scale ~8–20 reputation plus Kudosh/cash for a good visit. Before
accepting: clean the hospital, empty bins, water plants, repair *everything*. Specific threats —
**Jumbo McNally** litters and will sabotage/destroy a machine if left alone with it (shadow him
with a janitor; pre-repair machines); **Agatha Sphere** hypnotizes patients into rage-quitting
and tempts staff to resign (discharge affected patients immediately); **Augustus Lavender**
vomits and poisons plants (janitor escort). Low-stakes visitors like Henry Jobsworth just want
an attractive, clean hospital.

---

## 8. Checklists

### First hour on any new map

1. **Pause. Don't build reception yet** — the hospital stays closed and nearly bill-free.
2. Survey the plot: mark where GP/diagnosis cluster will live (nearest entrance), where
   treatment/admin will drift later. Check the level's temperature (radiators/air-con from
   level 4 on) and its signature illnesses/emergency types.
3. Raise all prices +10% (Prices screen). Open Policy: enable Fast-Track, set diagnosis
   threshold (100% early; ~85–90% once staff are trained), enable auto-promote if you don't
   want to micromanage raises.
4. Build minimum-size (or template) rooms: Reception, 2 GP's Offices, General Diagnosis,
   Pharmacy, Toilets (4x4), small Staff Room; vending machines + bins + one arcade near
   reception; a few benches.
5. Shop the hire list *before* opening: doctor with GP I (good trait), nurse with
   Pharmacy/Diagnostics, assistant with Customer Service, janitor with Ghost Capture. Reject
   duds to refresh the pool. Only then let patients in.
6. Add rooms reactively: Ward and Psychiatry early (dual-duty), Cardiology at queue pressure,
   treatment rooms on the 3-strikes rule. Training room the moment it's available; Marketing
   room from Flemington on. Keep 1:1 GP:diagnosis.
7. Start research (or money-research) immediately if the level has a Research room.
8. Watch the monthly budget line; expand only on stable $10–20k profit.

### Stuck at 2 stars — troubleshooting

- **Cure rate too low?** It's a last-20-leavers stat: cut deaths *and* rage-quits. Upgrade
  machines (before new rooms), train treatment staff to III, hold diagnosis ≥90%, add
  amenities/prestige to stop rage-quits, market easy illnesses, purge hopeless patients
  (<30% health), and consider a reception close or full purge as a last resort.
- **GP queues over 6?** More GP's Offices + GP III training + Fast-Track + matching diagnosis
  rooms. Re-audit layout at every +50 patients; second reception at ~175–200.
- **Money bleeding?** Wages first: fire expensive mish-mash staff (after using them as
  teachers), replace with cheap trainees; check research is running for cash; take the loan;
  raise prices 10%; delay promotions; downsize oversized rooms instead of buying plots.
- **Hospital value goal?** Stabilize monthly profit (steady > spiky), buy hard assets, then a
  10–20% price rise backed by reputation.
- **Staff morale goal?** Pay above ask, win staff challenges, Emotional Intelligence for all,
  loosen break policy (full breaks = Energised buff), prestige-5 staff rooms, fire grumps,
  mass-break as a finisher.
- **Attractiveness goal?** Janitors + Yuccas + trophy cases + fountains; pause-and-plant snipe
  if you're within a few points.
- **Reputation goal?** 3–4 month general marketing campaign, accept every emergency and VIP you
  can service, drop prices a notch if you've over-raised.

---

## Sources

1. **GameFAQs — "Two Point Hospital Strategy Guide (PC)" by CityBuilderAK47**, v1.9 (Apr 2023),
   FAQ of the Month Oct 2018 — sections used: 11 Tips for Hospital Success; The 9 General Rules
   of Hospital Layout; Important Game Concepts; GP Queues; Hospital Level Snowballing; Expansion
   Strategy; Examples in Efficiency; Room Prestige; Patient Happiness; The Great Patient Purge;
   Training Tips; Doctor/Nurse Skills; Staff Traits; Staff Happiness & Staff Threats; Money
   Troubles; You want HOW Much in Hospital Value?; Attractiveness Rating; Bump that Cure Rate
   Up!; Staff Morale; Chance of Cure; Epidemics; Emergencies; VIP Visits; Room Templates;
   Marketing. (gamefaqs.gamespot.com/pc/230622-two-point-hospital/faqs/76595, via Wayback
   Machine snapshots, 2023.)
2. **Two Point Hospital Fandom Wiki** — pages: Diagnosis (room costs/fees, diagnosis-modifier
   math, rank-based routing, policy thresholds), Treatment (skill tiers, room/illness mapping),
   Prices, Marketing (campaign costs/durations, patient-volume cap), Epidemics.
   (two-point-hospital.fandom.com, via MediaWiki API.)
3. **Steam Community — "Two Point Hospital – Beginner's Guide"** (sharedfiles id 1632044281):
   8-GP-per-250-patients rule, nurse-over-doctor diagnosis economics, X-Ray skepticism, +10%
   price rule, "wages are the enemy", medicine-cabinet stacking, ward staffing, marketing
   lock-in, VIP-specific handling.
4. **TheGamer — "Two Point Hospital: How To Increase Your Cure Rate"**: machine upgrade costs
   ($10k/$20k) and power (+25%/+50%), 100% threshold policy, easy-illness difficulty list,
   send-home doctrine, room-clustering.
5. **Basically Average — "Two Point Hospital Tips"**: minimum-size + Gold Star Award prestige
   meta, policy settings (Fast-Track, idle-staff, queue warning length 1, 85% threshold),
   vending/staff-room-per-building doctrine, surgery economics, burst marketing.
6. **Steam Community forum threads** (via search): "MEGA scan and XRAY – too overused?" (X-Ray
   value debate, GP V ~50% ceiling on hard illnesses), cure-rate threads (monthly purge for 95%,
   90% cure-rate 3-star requirements), money threads (marketing vs. price-hike rep arithmetic).
7. **myPotatoGames — "Two Point Hospital Advanced Tips and Tricks"** and **Neoseeker
   walkthrough — "Raising Cure Rate Percentage"** (corroboration: gold-star spam, purge
   thresholds ~30%/50% health, 90% cure-rate star goal).
