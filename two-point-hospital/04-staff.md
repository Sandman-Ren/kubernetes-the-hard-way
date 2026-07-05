# Two Point Hospital — Staff Reference

Complete reference for the staff system in Two Point Hospital (2018, Two Point Studios): staff types, skills and qualifications, traits, training, and staff management. Data verified against the Two Point Hospital Fandom wiki (MediaWiki API) and the GameFAQs strategy guide by CityBuilderAK47 (v1.9, 2023). Uncertain or conflicting data is marked explicitly.

---

## 1. Staff Types

There are four hirable staff types, plus the Robo-Janitor (Close Encounters DLC). Every room and task in the hospital is serviced by exactly one staff type.

### Doctor
Diagnoses and treats patients; the only type that can research. Works in (Job Assignment list):

- **Diagnosis:** GP's Office (doctors only — the backbone of the patient flow), X-Ray, M.E.G.A Scan (needs Radiology), Psychiatry (needs Psychiatry qualification, also treats there)
- **Treatment:** Surgery (needs Surgery qualification; works alongside a nurse), Psychiatry, DNA Lab (needs Genetics; diagnosis + treatment), De-Lux Clinic, Pans Lab, Shock Clinic, Resolution Lab, Recurvery Room, Reanimation, Correcting Pool, Personification, Tech Support, Danger Zone, War Room, Cloud Computing, Wax Works, Powder Room, and other doctor treatment rooms
- **Other:** Research Room (needs Research qualification), Head Office (A Stitch in Time DLC), ambulances (Speedy Recovery DLC, needs Driving or Flying)

### Nurse
Treatment- and ward-focused; shares Diagnostics/Treatment training with doctors. Works in:

- **Diagnosis:** General Diagnosis, Cardiology, Fluid Analysis, Ward (diagnosis + treatment)
- **Treatment:** Pharmacy, Injection Room, Fracture Ward, Ward, Surgery (assists the doctor), Clown Clinic, Chromatherapy, Pest Control, Cryptology, Doghouse, Urban Mythology, Indentification, Escape Room, Self-Assembly, Toad Hall, Woodwork, Herb Garden, Farmacology, Wash Pit, and other nurse treatment rooms
- **Other:** ambulances (Speedy Recovery DLC, needs Driving or Flying)

### Assistant
Front-of-house and commerce. Works in: Reception desk / Reception Room, Café, Gift Shop, Newsagent, kiosks (Kiosk Hut, Cosy Kiosk, Cake Sale, Carnival Kiosk, Hotdog Kiosk), Marketing Room (needs Marketing qualification), Speed Dating (A Stitch in Time DLC, needs Yesterization). Assistants and janitors do not directly generate treatment income, but receptions and shops are essential to patient flow and profit.

### Janitor
Facilities and machines. Roles: repair/maintain machines, upgrade machines (needs Mechanics), restock vending machines, sweep litter, empty bins, unblock toilets, water plants, extinguish fires, repair air-con, capture ghosts (needs Ghost Capture), service/upgrade ambulances (Speedy Recovery DLC, needs Vehicular Mechanics). A machine below 50% maintenance sparks and radiates heat; at 0% it catches fire and can explode — only janitors use fire extinguishers. Ghosts spawn when patients die and scare people until a Ghost Capture janitor vacuums them up (an Ectovat can convert captured ghosts into staff energy).

### Robo-Janitor (Close Encounters DLC)
Unlocked at Star Level 3 of Chasm 24; afterwards a **Robo-Kit** ($25,000, placed in a corridor) can spawn one of each model per hospital. Robo-Janitors take **no salary**, have fixed happiness, and recharge at a **Charging Point** ($1,500 per charge, placed in staff rooms/corridors; they fall back to the Staff Room if none exists). All models can repair machines; each specialises narrowly but outperforms humans in its specialty:

| Model | Specialty | Effect | Cost |
|---|---|---|---|
| Audrey Fixsimmons | Maintain machinery | +150% Maintenance Skill | $10,000 |
| Coggerly Douse | Upgrade machines, extinguish fires | +120% Upgrade Skill | $15,000 |
| Sweepy Leroux | Litter and bins | +70% Speed | $6,000 |
| Phillup Plunge | Restock vending, service toilets | +100% Maintenance Skill | $5,000 |
| Sprinkle Spectre | Water plants, capture ghosts | +50% Speed | $11,000 |

---

## 2. Ability, Experience, and Qualification Slots

- Every staff member has an **Ability** rating of 1–5 stars. Each star grants **one qualification (training) slot** — so a 5-star staff member can hold up to 5 qualifications.
- Staff earn **experience** by working. XP needed per rank: Rank 2 = 100 XP, Rank 3 = 200 XP, Rank 4 = 300 XP, Rank 5 = 400 XP.
- When the XP circle fills, the staff member requests a **promotion**. Promoting them raises their base skills, opens a new empty training slot, and comes with a small mandatory pay increase (you can add more to boost Pay Satisfaction). **The new slot must be filled by training before they can be promoted again.** Delaying a requested promotion reduces their happiness. Promotions are optional and can be deferred.

### Rank titles and base skills per star

| Stars | Doctor | Nurse | Assistant | Janitor |
|---|---|---|---|---|
| 1 | Intern Doctor | Student Nurse | Intern Assistant | Intern Janitor |
| 2 | Junior Doctor | Junior Nurse | Junior Assistant | Junior Janitor |
| 3 | Doctor | Nurse | Assistant | Janitor |
| 4 | Consultant | Senior Nurse | Senior Assistant | Senior Janitor |
| 5 | Senior Consultant | Chief Nurse | Head Assistant | Head Janitor |

Base skill values by star (before qualifications and mood modifiers):

| Skill (staff type) | 1★ | 2★ | 3★ | 4★ | 5★ |
|---|---|---|---|---|---|
| Diagnosis (Doctor & Nurse) | 80% | 90% | 100% | 110% | 120% |
| Treatment (Doctor & Nurse) | 10% | 20% | 30% | 40% | 50% |
| Customer Service (Assistant) | 100% | 150% | 200% | 250% | 300% |
| Marketing (Assistant) | 100% | 120% | 140% | 160% | 180% |
| Maintenance (Janitor) | 100% | 120% | 140% | 160% | 180% |
| Upgrade (Janitor) | 100% | 110% | 120% | 130% | 140% |
| Movement Speed (all) | 100% | 115% | 130% | 145% | 160% |

Note: the wiki reports movement-speed increases as bugged — only one speed modifier registers at a time, and star-based speed upgrades may not show on the Stats tab.

---

## 3. Training Mechanics

- The **Training Room** (3×3 minimum, $7,000 base, unlocked in Flottering; retroactively usable in earlier levels) requires a Door, a **Lectern** (trainer) and at least one **Trainee Desk** — one trainee per desk. Start a course from the lectern, by dropping a staff member into the room, from the Staff Inspector, or from a staff training-request letter.
- **Trainer options:**
  - **Your own staff member** who holds the qualification can teach it — **for free** — including across professions (e.g. a nurse with Diagnostics can train doctors).
  - A **Guest Trainer** costs **$10,000 flat + $5,000–$25,000 per trainee** (per-trainee fee scales with qualification rank: $5,000 at rank I up to $25,000 at rank V). Guest trainers teach at 160% training speed (Sophie Smiles, the common-skills trainer, teaches at 180%) — per GameFAQs.
  - Trainees put their normal work on hold for the whole course — do not train all your janitors (or all your GPs) at once.
- **Duration — Training Units (TU):** each course has a Required TU value (1 TU ≈ 1 second at 100% speed; a 240 TU course ≈ 4 minutes real time at base speed). Most courses run 240 TU at rank I, rising to 480 TU at rank V. Actual duration = TU modified by:
  - **Trainer's teaching speed** (base 100%; +50% from the Teacher trait; +50% from Training Masterclass; guest trainers 160–180%; GameFAQs also reports a small bonus per trainer ability star)
  - **Each trainee's learning speed** (base 100%; +50% Fast Learner trait; +50% Training Masterclass; −25% Stupid trait; the Brain Chair item also boosts learning)
  - **Training-boost items in the room** (stackable): Skeleton/Anatomy Poster/Anatomy Model/Brain Anatomy Poster/Cubism Anatomy Poster +1% each, Encyclopedia Bookcase I +2%, Encyclopedia Bookcase II +4%, Knight's Armour +2%, Wizardry Cauldron +5% (last two are Two Point Campus crossover items). Item spam makes training extremely fast.
- Some qualifications must be unlocked first: **Research II–V must each be researched** as research projects before anyone can be trained in them; some others unlock via level progression.
- Mitton University (level 4) pays a $5,000 bonus per completed training course; staff cannot move between hospitals.

---

## 4. Qualifications (full list)

Ranks are named I Increased, II Enhanced, III Advanced, IV Elite, V World Class. "TU" = Required Training Units per rank (I/II/III/IV/V). Guest-trainer cost is always $10,000 + ($5,000 × rank) per trainee unless noted.

### Doctor

| Qualification | Ranks | Effect | TU |
|---|---|---|---|
| General Practice | I–V | +15% GP's Office diagnosis skill per rank | 240/300/360/420/480 |
| Diagnostics | I–V | +10% Diagnosis skill (all diagnosis rooms) per rank | 240/300/360/420/480 |
| Treatment | I–V | +10% Treatment skill per rank | 240/300/360/420/480 |
| Psychiatry | I–V | I: unlocks working in Psychiatry; II–V: +20% diagnosis & treatment in Psychiatry per rank | 240/300/360/420/480 |
| Surgery | I–V | I: unlocks working in Surgery; II–V: +20% treatment per rank | 240/300/360/420/480 |
| Research | I–V | I: unlocks working in Research; II–V: +50% Research skill per rank (ranks II–V must be researched before trainable) | 240/300/360/420/480 |
| Radiology | single | Unlocks the M.E.G.A Scan and +20% X-Ray diagnosis skill | 240 (trainer fee $10,000 + $10,000/trainee) |
| Genetics | single | Unlocks working in the DNA Lab | 240 (trainer fee $10,000 + $10,000/trainee) |
| Driving (Speedy Recovery DLC) | I–V | I: can drive road ambulances; II–V: better driving | 240/300/360/420/480 |
| Flying (Speedy Recovery DLC) | I–V | I: can fly air ambulances; II–V: better flying | 240/300/360/420/480 |

### Nurse

| Qualification | Ranks | Effect | TU |
|---|---|---|---|
| Ward Management | I–V | +20% diagnosis skill in Ward and treatment skill in Ward & Fracture Ward per rank | 240 at every rank |
| Diagnostics | I–V | +10% Diagnosis skill per rank (shared with doctors) | 240/300/360/420/480 |
| Treatment | I–V | +10% Treatment skill per rank (shared with doctors) | 240/300/360/420/480 |
| Injection Administration | single | +20% treatment (injection) skill in the Injection Room | 240 |
| Pharmacy Management | single (see note) | +20% treatment skill in the Pharmacy | 240 |
| Driving / Flying (Speedy Recovery DLC) | I–V | Ambulance operation, as for doctors | 240/300/360/420/480 |

Note: the Fandom wiki lists Pharmacy Management as a single-level qualification, while the GameFAQs guide lists guest-trainer prices for Pharmacy Management I–V. Unresolved discrepancy — possibly changed by a patch; treat rank count as uncertain.

### Assistant

| Qualification | Ranks | Effect | TU |
|---|---|---|---|
| Customer Service | I–V | +50% Customer Service skill per rank (Reception and shops) | 240/300/360/420/480 |
| Marketing | I–V | I: unlocks working in the Marketing Room; II–V: +20% Marketing skill per rank | 240/300/360/420/480 |
| Yesterization (A Stitch in Time DLC) | I–V | I: unlocks working in Speed Dating; II–V: faster Yesteriser configuration | 240/300/360/420/480 |

### Janitor

| Qualification | Ranks | Effect | TU |
|---|---|---|---|
| Maintenance | I–V | +30% Repair & Maintenance skill per rank | 240/300/360/360/360 |
| Mechanics | I–V | I: unlocks upgrading machines; II–V: +50% Upgrade skill per rank | 240/300/360/420/480 |
| Ghost Capture | single | Can detect and capture ghosts | 240 |
| Vehicular Mechanics (Speedy Recovery DLC) | I–V | I: can service/upgrade ambulances; II–V: +50% Upgrade skill per rank (no guest trainer; taught by Gretchen Gearbox) | 240/300/360/420/480 |

### Personal-development qualifications (all staff types unless noted)

| Qualification | Ranks | Effect | TU |
|---|---|---|---|
| Bedside Manner (Doctor & Nurse only) | single | Increases patient happiness when dealing with them | 240 |
| Emotional Intelligence | single | +10% staff happiness | 240 |
| Motivation | single | +10% speed & efficiency | 240 |
| Stamina Training | single | Energy drains at a reduced rate (work longer between breaks) | 240 |
| Training Masterclass | single | +50% teaching speed and +50% learning speed | 240 |

---

## 5. Traits

Staff have **1–3 permanent traits** (never gained or lost) drawn at hire time; conflicting pairs (e.g. Lazy/Tireless) can't coexist. Traits show on the hire screen as "Employment Reference" phrases. There are also 300+ pure **flavour traits** with no gameplay effect (e.g. "Owns a crossbow").

### Positive traits

| Trait | Hire-screen phrase | Effect |
|---|---|---|
| Charming | "Charming." | +10 patient/staff happiness when processing or chatting on breaks |
| Cheap | "Will work for peanuts." | −10% salary. Conflicts with Expensive |
| Entertainer | "Entertains people with their sweet dance moves." | −100 patient boredom when processing; −80 when dancing with them on breaks. Conflicts with Boring |
| Fast Learner | "Has potential." | +50% XP gain and training speed (stacks with Training Masterclass and Brain Chair). Conflicts with Stupid |
| Funny | "Funny." | −40 patient boredom when talking on breaks |
| Green Fingers | "Green fingers." | Waters plants when idle |
| Healer | "Has magic healing hands." | +5 patient health when processing. Rare; doctors/nurses only. Conflicts with Evil |
| Heart-Throb | "The boy/girl next door." | May give "Has a Crush" buff (+15% move speed briefly) |
| Hygienic | "Hygienic." | Passively higher hygiene. Conflicts with Dirty/Unhygienic |
| Inspiring | "Inspiring." | +5 patient/staff happiness when talking on breaks |
| Motivated | "Motivated." | +20% movement speed. Conflicts with Unmotivated |
| Positive | "Positive." | +10% happiness; happiness rises passively. Conflicts with Grumpy |
| Romantic | "Thinks their life is a romcom." | Break-time chats may give both parties +30 happiness and "In Love" (+15% speed) |
| Teacher | "A natural mentor." | +50% teaching speed (stacks with Training Masterclass) |
| Tireless | "High energy." | Slower energy drain (~33 extra days of work; ~99 with Stamina Training). Conflicts with Lazy |

### Negative traits

| Trait | Hire-screen phrase | Effect |
|---|---|---|
| Argumentative | "Likes to argue." | −5% happiness to both when chatting with other argumentative staff |
| Boring | "Terribly dull." | +80 patient boredom when processing/talking. Conflicts with Entertainer |
| Dirty | "Dirty habits." | May not wash hands after the toilet |
| Evil | "Has a dark side." | −5 patient health when processing. Conflicts with Healer |
| Expensive | "Wants more money." | +10% salary. Conflicts with Cheap |
| Gross | "Nausea inducing." | People nearby more likely to vomit |
| Grumpy | "Grumpy." | −10% happiness; happiness decays faster. Conflicts with Positive |
| Hangry | "Hangry." | When very hungry: happiness drains, −5%/−10% happiness to people they process/chat with, "Annoyed" outbursts |
| Lazy | "Tires easily." | Faster energy drain (~22 fewer work days). Conflicts with Tireless |
| Litterer | "Litterer." | Regularly drops litter when idle / on breaks |
| Nasty | "Nasty." | Reduces patient happiness when processing (worse the unhappier the staff member is); outbursts annoy people nearby |
| Short Temper | "Short temper." | When happiness < 40%: −5–12% patient happiness when processing; outbursts |
| Sleepy | "Suffers from spontaneous bouts of snoozing." | Randomly falls asleep when idle / on breaks |
| Stupid | "Cheese for brains." | −25% XP gain and training speed. Conflicts with Fast Learner |
| Toilet Rage | "Gets toilet rage." | When desperate for the toilet: happiness drains, −5% patient happiness when processing, outbursts |
| Unhygienic | "Unhygienic." | Loses hygiene faster, never washes hands (can catch the Sniffles, causing vomiting — per GameFAQs) |
| Unmotivated | "Unmotivated." | −20% movement speed. Conflicts with Motivated |
| Weak Bladder | "Weak bladder." | Toilet need drains 5× as fast |

Movement-speed traits are affected by the same "only one speed modifier applies" bug noted above.

### Hiring heuristics from traits

- **Grab on sight:** Healer (rarest trait in the game, ~2–5% of applicants per GameFAQs), Fast Learner, Teacher (earmark them as your in-house trainer), Cheap, Tireless, Positive, Motivated.
- **Front-line people (GPs, receptionists, ward nurses):** prefer Charming/Funny/Inspiring/Entertainer — their happiness/boredom effects reduce patient rage-quits and lift your cure rate. Avoid Nasty, Boring, Short Temper, Grumpy in patient-facing roles.
- **Generally avoid:** Stupid (training tax on every course), Expensive, Lazy, Litterer (extra janitor load), Unhygienic/Dirty (hurts hospital hygiene score), Weak Bladder.
- A bad trait can be tolerable on back-office staff (researchers, marketing assistants) who rarely meet patients.

---

## 6. Staff Management

### Salary and pay rises
- Applicants show a base annual salary; you pay a one-off **recruitment fee** up front when hiring.
- **Pay Satisfaction** has five levels (Very Happy / Happy / Satisfied / Unhappy / Very Unhappy) and feeds directly into happiness. Adjust salary from the Staff Inspector or the **Pay Review** tab of the Staff List; a slider proposes a raise, with a face showing the resulting satisfaction. The **"Satisfy Pay Requests"** button raises everyone below Satisfied up to Satisfied in one click and shows the total cost.
- Every **promotion carries a small mandatory pay increase**; you can top it up for extra satisfaction. Staff also ask for pay rises on their own over time. Cheap/Expensive traits move salary ±10%.

### Happiness / morale
Contributing factors (all visible on the Staff Overview screen and per-staff Mood tab):
- **Pay satisfaction**
- **Needs:** hunger, thirst, toilet — mostly satisfied on breaks; unmet needs accelerate happiness loss. Hot rooms make staff thirsty faster.
- **Environment:** hospital attractiveness, temperature (aim mid-bar — neither hot nor cold), hygiene, and **room prestige** (staff complain about low-prestige rooms; high-prestige rooms please them)
- **Breaks and energy** (below), **delayed promotions**, training when requested, and trait/feeling modifiers (e.g. Emotional Intelligence +10%)
- Unhappy staff perform worse; if happiness drops too low they send a **resignation-threat letter giving you 90 days to get them back to at least 20% happiness**, otherwise they quit.

### Energy and breaks
- Energy drains as staff work; at low energy they go on break **if the break policy allows**. They recover in the **Staff Room** — higher room prestige = faster energy regain. Returning to work with ≥80% energy grants the **Energised** buff.
- **Break Policy** (Overview → Staff): per-staff-type sliders for (a) how many of that type may be on break simultaneously (from none to all) and (b) break duration, **10 to 30 in-game days**.
- Stamina Training (qualification) and Tireless (trait) slow the drain; Lazy speeds it. An **Ectovat** converts captured ghosts into an energy refill for a staff member.
- You can manually force a break ("Take a Break"/drop into Staff Room) or force a return to work.

### Job assignment (room restriction)
- The Jobs screen (Staff List → Jobs) is a grid of toggles: each staff member × each room/task they could work. **New hires default to ALL available assignments** — un-tick aggressively so specialists stay put (e.g. restrict a GP-trained doctor to the GP's Office only, Ward Management nurses to Ward/Fracture Ward). Doctors/Nurses screens have "Diagnosis"/"Treatment" filters.
- Rooms that need a qualification (Psychiatry, Surgery, Research, M.E.G.A Scan, DNA Lab, Marketing, machine upgrades, ambulances, Speed Dating…) only appear as valid assignments for qualified staff.

### Firing and rival competition
- Fire from the Staff Inspector footer; the employee will attempt a guilt trip but there is no other penalty. There is no direct "poach a rival's named staff" mechanic — instead, **rival hospitals compete for the same applicant pool**, so desirable applicants disappear from the hire screen if you dally.

---

## 7. Hiring

- The Hire screen lists applicants per staff type with their ability stars, current qualifications (one circle per star; a dark empty circle = "Ready for Training"), traits (Employment Reference), base salary, and recruitment fee.
- **Applicant slots:** you get 1 application slot per staff type per 5 Hospital Levels, to a maximum of **8 slots per type**. A new applicant appears **every 15 days** per empty slot. Rejecting an applicant frees the slot.
- **Hospital reputation** (specifically the Staff component — staff happiness and team size — plus overall reputation) influences how quickly new applicants apply. Higher-level hospitals see more and better applicants; higher-star applicants come pre-loaded with more qualifications and cost more.
- **Recruitment Marketing** (Marketing Room, from Flemington; requires an assistant with the Marketing qualification): per-type campaigns ($7,000 for 3 months up to $25,000 for 12 months, at $2,000/extra month) that increase the rate at which recruits of that type appear, or the likelihood recruits carry a desired qualification. Longer campaigns are more cost-efficient.
- Hiring staff raises your Hospital Level (doctors/nurses more than janitors/assistants).

---

## 8. Strategy

**Cheap-and-train beats expensive jack-of-all-trades.** Multi-skill senior consultants from the hire pool are usually overpriced; a cheap 1–2 star hire with good traits, trained in exactly the skill you need, outperforms them per dollar (GameFAQs: a well-trained student "will run laps around" a random senior). Hire for **traits first, stars second** — traits are permanent, qualifications are trainable.

Recommended builds (fill slots as they promote):

- **GP doctor:** General Practice III as the workhorse standard (GP IV/V only for a few flagship doctors — diminishing returns above III), then soft skills: Bedside Manner, Stamina Training or Emotional Intelligence. A GP IV + Training Masterclass doctor makes an excellent in-house GP trainer. GPs interact with every patient, so pick people-pleasing traits here.
- **Diagnostics doctor/nurse:** Diagnostics III(+) for X-Ray/M.E.G.A/General Diagnosis/Cardiology staff; add Radiology on the doctor who runs the M.E.G.A Scan.
- **Psychiatry specialist:** Psychiatry I to unlock, then stack to III–V (Psychiatry both diagnoses and treats, and several illnesses are psychiatry-only). Restrict them to Psychiatry.
- **Surgeon:** Surgery I then stack — surgery has low base cure chances and benefits heavily from rank II–V's +20% treatment per rank. Pair with a high-Treatment/Ward nurse.
- **Research doctor:** Research I–V + Fast Learner traits; park them permanently in the Research Room (they earn no ward income, so keep the team small and dedicated).
- **Ward nurse:** Ward Management I–V (uniquely cheap: 240 TU at every rank, +20% per rank) — the single most efficient stacked qualification in the game. Restrict to Ward/Fracture Ward.
- **Treatment nurse:** Treatment III(+); add Injection Administration and/or Pharmacy Management for those rooms.
- **Assistant:** Customer Service III–V for reception (front-desk speed and patient happiness); train one or two with Marketing I(+) and restrict them to the Marketing Room.
- **Janitor:** split the team — most on Maintenance III(+) (repairs, restocking, toilets), a couple of dedicated **mechanics** with Mechanics I–V restricted to Upgrade Machines (upgrade times drop sharply with rank: level II upgrades take ~37 days base, level III ~112 days), one with Ghost Capture per hospital.
- **Every senior staff member's spare slot:** Training Masterclass on your designated teachers; Stamina Training/Motivation as filler.

**Training operations:** build two smaller training rooms rather than one large (≤4 trainees per class is the practical maximum); add another room when 10+ staff are waiting to train. Cram training rooms with boost items. Use your own skilled staff as free trainers; the guest trainer's $10k + per-head fee is only worth it when pulling a teacher off the floor would cause queues, or when nobody has the skill yet. A conniving alternative: hire an expensive consultant who already has the skill, use them to teach your cheap staff, then fire them.

**Temporary staffing:** hire disposable extra janitors for cleanup-heavy level starts (e.g. Melt Downs), or extra doctors/nurses ahead of a big illness-marketing campaign, then let them go.

**Keep spares:** always maintain slight over-staffing so breaks and training never leave rooms empty — an empty GP's Office is the fastest way to queue collapse.

---

## Sources

- Two Point Hospital Fandom wiki, via MediaWiki API (`two-point-hospital.fandom.com/api.php`): pages "Staff", "Staff Training", "Staff Skills", "Traits", "Doctor", "Nurse", "Assistant", "Janitor", "Robo-Janitor", "Training (Room)", "Staff Room", "Overview", "Marketing" (retrieved 2026-07-05).
- CityBuilderAK47, *Two Point Hospital Strategy Guide* v1.9 (updated 2023-04-10), GameFAQs — sections "Staff Traits", "Before You Build: Staffing", "Training Tips" (retrieved via Wayback Machine).
- gamepressure.com Two Point Hospital staff guide (general staff management corroboration).

Known uncertainties: Pharmacy Management rank count (wiki: single level; GameFAQs: I–V); exact numeric happiness weights for individual morale factors (not published — dashes above where unknown); movement-speed modifiers reportedly bugged (only one applies at a time); Healer trait rarity is an anecdotal ~2–5% estimate.
