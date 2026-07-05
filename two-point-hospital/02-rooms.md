# Two Point Hospital — Complete Room Catalog (Base Game + All DLC)

Every buildable room in Two Point Hospital (2018, Two Point Studios), grouped into
**Diagnosis**, **Treatment** and **Facility** rooms. Data is taken from the Two Point
Hospital Fandom wiki (room infoboxes and body text, fetched via the MediaWiki API) and
cross-checked against the gamepressure.com room guide and Steam community guides.
Prices are base placement cost in in-game dollars ($) and exclude optional extra items.
Sizes are minimum footprints (width x depth in tiles). "Research 1,000" means the room
must be unlocked through a Research Room project of that approximate point cost.

General mechanics that apply to every room:

- **Prestige.** Each room has a prestige level (1–5) driven by its size and the items
  placed inside. Higher prestige keeps patients and staff happier (and a high-prestige
  Staff Room restores staff energy faster). Rugs, lamps, posters, certificates, trophy
  cases, bookcases and plants all raise prestige; the cheap "gold star" route is to
  oversize the room slightly and line the walls with posters and windows.
- **Machine upgrades.** Most rooms are built around one machine. Almost every machine
  has **two upgrades** (Level I → II → III). Upgrades must first be researched (roughly
  2,000 points for Level II and 3,000 for Level III per the community guides), cost about
  $10,000 (II, ~+25% stat) and $20,000 (III, ~+50% stat) to install, and are fitted by a
  Janitor with the Mechanics qualification. Upgrades raise the room's diagnosis or
  treatment power and are the main lever for curing late-game illnesses.
- **Boost items.** Diagnosis/Treatment Bookcases (+2% power), Wall Monitors (+1%
  diagnosis and +1% treatment), Medicine Cabinets (+1%/+1%) and similar items add small
  but stacking power bonuses in clinical rooms; Air Conditioners/radiators manage
  temperature, and bins + hand sanitiser manage litter and hygiene.

---

## 1. Diagnosis rooms

Patients ping-pong between the GP's Office and the diagnosis rooms below until their
diagnosis percentage passes the threshold set in Policy. Later rooms have higher
diagnosis power: General Diagnosis and Cardiology are the workhorse mid-tier, while
M.E.G.A Scan and the DNA Lab are the top tier. Ward, Psychiatry and DNA Lab are
hybrids that also cure illnesses (their cure lists are given below).

| Room | Type | Cost | Min. size | Staff | Unlock |
|---|---|---|---|---|---|
| GP's Office | Diagnosis | $5,800 | 3x3 | Doctor | Hogsport (tutorial) |
| General Diagnosis | Diagnosis | $7,100 | 3x3 | Nurse | Hogsport (tutorial) |
| Cardiology | Diagnosis | $7,600 | 3x3 | Nurse | Lower Bullocks (Star Level 1) |
| Fluid Analysis | Diagnosis | $20,100 | 3x3 | Nurse | Mitton University — research 1,000 |
| X-Ray | Diagnosis | $31,100 | 4x4 | Doctor | Mitton University — research 2,000 |
| M.E.G.A Scan | Diagnosis | $60,100 | 4x4 | Doctor + Radiology | after X-Ray — research 2,000 |
| DNA Lab | Diagnosis + Treatment | $50,100 | 3x4 | Doctor + Genetics | Melt Downs — research 1,000 |
| Ward | Diagnosis + Treatment | $7,600 | 3x4 | Nurse | Hogsport (tutorial) |
| Psychiatry | Diagnosis + Treatment | $6,100 | 3x3 | Doctor + Psychiatry | Lower Bullocks |

### GP's Office
- **Type:** Diagnosis (mandatory hub). "Diagnosis, consultation and basic human interaction."
- **Role:** First stop for every new patient; the GP attempts diagnosis and routes the
  patient onward. Patients return to a GP's Office after every diagnosis attempt until
  diagnosis is complete, so this is the game's biggest bottleneck.
- **Cost / size:** $5,800 / 3x3 minimum. 3x3 is perfectly serviceable — build *many*
  small offices rather than a few big ones; add another once queues hit ~6 patients.
- **Staff:** Doctor (no required qualification). **General Practice** qualifications
  give the biggest boost here.
- **Machine:** none — required items are Office Desk + Filing Cabinet (no upgrades).
- **Unlock:** Hogsport tutorial (base game).
- **Boost items:** Medicine Cabinet (+1% diagnosis/+1% treatment), bookcases, Anatomy
  Model/Display Skeleton; decorate for prestige since every patient visits repeatedly.

### General Diagnosis
- **Type:** Diagnosis.
- **Role:** Basic follow-up examination after the GP; cheap, always useful, first
  diagnosis room beyond the GP's Office.
- **Cost / size:** $7,100 / 3x3.
- **Staff:** Nurse; **Diagnostics** qualifications recommended.
- **Machine:** EZ-Scan (plus Examination Table) — upgradeable, two upgrades (Levels I–III).
- **Unlock:** Hogsport tutorial (base game).
- **Tips:** Remains useful all game as cheap queue relief for the mid-tier rooms.

### Cardiology
- **Type:** Diagnosis.
- **Role:** Treadmill stress test; mid-tier diagnosis power.
- **Cost / size:** $7,600 / 3x3.
- **Staff:** Nurse; Diagnostics qualifications recommended.
- **Machine:** Heart Racer — two upgrades.
- **Unlock:** Lower Bullocks, Star Level 1 (base game).
- **Tips:** Popular room; watch queues and duplicate as needed.

### Fluid Analysis
- **Type:** Diagnosis.
- **Role:** Spittoon-based fluid testing; solid mid/high-tier diagnosis power.
- **Cost / size:** $20,100 / 3x3 (gamepressure lists it as wanting 4x4 comfortably).
- **Staff:** Nurse; Diagnostics qualifications recommended.
- **Machine:** Fluid Accelerator — two upgrades (research required).
- **Unlock:** Research project (1,000) available as soon as you get the Research Room
  in Mitton University (base game).
- **Tips:** Extremely popular with the diagnosis AI — build more than one in big hospitals.

### X-Ray
- **Type:** Diagnosis.
- **Role:** High-power imaging; the step before M.E.G.A Scan.
- **Cost / size:** $31,100 / 4x4.
- **Staff:** Doctor (no required qualification). The **Radiology** qualification gives a
  **+20% diagnostic boost in this room**; Diagnostics qualifications stack after that.
- **Machine:** X-ray Machine (plus X-ray Terminal) — two upgrades (research required).
- **Unlock:** Research project (2,000) at Mitton University (base game).
- **Tips:** Sees heavy use until the M.E.G.A Scan takes over.

### M.E.G.A Scan
- **Type:** Diagnosis (top-tier).
- **Role:** The game's best pure diagnosis machine ("Machine Enabled Genome Analysis").
- **Cost / size:** $60,100 / 4x4.
- **Staff:** Doctor **with the Radiology qualification (required)**; further
  Diagnostics qualifications recommended.
- **Machine:** M.E.G.A Scanner — two upgrades (research required).
- **Unlock:** Research project (2,000), available once the first X-Ray research
  project is complete (base game).
- **Tips:** Very popular in late-game hospitals — expect to need several, each with a
  Radiology doctor. Expensive but the fastest way to hit high diagnosis certainty.

### DNA Lab
- **Type:** Diagnosis **and** Treatment (hybrid).
- **Role:** Top-tier diagnosis room that also cures all genetic illnesses from World 3
  onwards.
- **Cures:** Denim Genes, Flumps, Jumbo DNA, Leopard Skin, Touch of Midas, Evergreen,
  Half Pipe, Shin Blintz, Tartan Telomeres, Buccanear, False Tan, Jet Leg, Lemon Soul,
  Gorm Deficiency, Grunt, Hyperrealty, Isotrope, Telemutation, Avocado Hands, Bioweasel,
  Carbon Footprint, Stumblebum, Blooper, Cross-Frayed, Extrasensory, Metrognomic,
  Fossil Eyes, Time Warts, Woolly Man-Mouth (list spans base game + DLC illnesses).
- **Cost / size:** $50,100 / 3x4.
- **Staff:** Doctor **with the Genetics qualification (required)**; Diagnostics and/or
  Treatment qualifications on top.
- **Machine:** Healixir — two upgrades (research required).
- **Unlock:** Research project (1,000) at the outset of Melt Downs (base game).
- **Tips:** A "required room" from World 3 on; because it pulls double duty, one lab
  can bottleneck — separate labs for diagnosis and treatment help in large hospitals.

### Ward
- **Type:** Diagnosis **and** Treatment (hybrid).
- **Role:** Bed-based observation for diagnosis, plus the cure room for a large set of
  illnesses. Patients diagnosed in the Ward who also need Ward treatment leave and
  re-queue.
- **Cures:** Bed Face, Jazz Hand, Lazy Bones, Monobrow, Mucky Feet, Portishead,
  Anomalitis, Aurora Snorealis, Sore Judgement, Tongue Splinters, Crispy Skin,
  Hermitism, Logic Problem, Shadow Boxer, Vested Insects, Deeply Ill-Suited,
  H. G. Swells, Highly Ill-Suited, Science Friction, Zodiac Arrest, Bodily Druids,
  Chocolate Shorts, Pothead, Tenderbox, Concertoes, Inbagneato, Minty Condition,
  Motion Sickness, Shifting Perspective, Loopy, Mites of the Realm, Pneumatic Tubes,
  Predestinitis, Slackbladder, Busy Body, Peaky, Traffic Jam (base + DLC).
- **Cost / size:** $7,600 / 3x4 minimum — but bigger is much better: more beds and
  screens = more simultaneous patients, and the room inspector lets you assign up to
  four additional nurses.
- **Staff:** Nurse; **Ward Management** qualifications recommended (up to 5 nurses).
- **Machine:** none — Ward Door, Nurse Station, Screen, Beds (standard/Jasmine/Pod).
  No machine upgrades; capacity scales with beds instead.
- **Unlock:** Hogsport tutorial (base game).
- **Tips:** One giant ward usually beats several small ones; add beds as demand grows.

### Psychiatry
- **Type:** Diagnosis + Treatment (hybrid — classified as a diagnosis room in-game,
  but it is the cure room for all mental illnesses).
- **Cures:** Boggled Mind, Emperor Complex, Freudian Lips, Inflated Ego, Mime Crisis,
  Mock Star, Night Fever, Bard Flu, Bloaty Dread, Brain Freeze, Knightmares,
  Paranoyance, Beach Wail, Football Crazy, Nerological Imbalance, Trumidity, Bowhine,
  Confidentures, Horrorscope, Space Caged, Eco-Worrier, Harebrained, Perforated
  Thoughts, Retrogaze, Culture Shock, Fourthwall Problem, Protagony, Writer's Block,
  Artificial Intelligence, Fomo Sapiens, Forefraught, Historical Laughter, Reptile
  Dysfunction, Rock Star, Alarmed, Mean Feet (base + DLC).
- **Cost / size:** $6,100 / 3x3.
- **Staff:** Doctor **with the Psychiatry qualification (required)**; higher Psychiatry
  levels improve both roles.
- **Machine:** none — Psychiatrist's Armchair + Psychiatric Couch (no upgrades; power
  comes almost entirely from the doctor's Psychiatry level).
- **Unlock:** Lower Bullocks (base game).
- **Tips:** Cheap to duplicate; a Psychiatry V doctor in a high-prestige office cures
  even late-game mental illnesses reliably.

---

## 2. Treatment rooms

Single-illness clinics plus four multi-illness workhorses (Pharmacy, Injection Room,
Surgery, Fracture Ward — and Herb Garden in Off The Grid). Treatment rooms are marked
with their DLC where applicable. All machine rooms follow the same pattern: the machine
has two researchable upgrades (Levels I–III) that raise treatment power, and the
operating staff member's Treatment qualification level adds on top.

### Base game

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Pharmacy | $7,600 | 3x3 | Nurse | many (potions) | Hogsport (tutorial) |
| Injection Room | $15,100 | 3x3 | Nurse | many (jabs) | Mitton Univ. — research 1,000 |
| Surgery | $26,000 | 3x4 | Doctor + Surgery, & Nurse | many (operations) | Smogley |
| Fracture Ward | $13,600 | 3x4 | Nurse | fractures | Tumble |
| De-Lux Clinic | $21,100 | 3x3 | Doctor | Lightheadedness (+variants) | Hogsport (tutorial) |
| Pans Lab | $20,100 | 4x4 | Doctor | Pandemic | Lower Bullocks |
| Clown Clinic | $20,100 | 4x4 | Nurse | Jest Infection / Jester Infection | Flottering |
| Chromatherapy | $21,100 | 3x4 | Nurse | Grey Anatomy | Mitton Univ. — research 1,000 |
| Pest Control | $20,100 | 4x4 | Nurse | Animal Magnetism | Flemington — research 1,000 |
| Shock Clinic | $30,100 | 4x4 | Doctor | Shock Horror | Melt Downs — research 1,000 |
| Cryptology | $30,100 | 3x4 | Nurse | Premature Mummification | Sweaty Palms — research 1,000 |
| Head Office | $30,100 | 4x4 | Doctor | Turtle Head | Smogley — research 1,000 |
| Resolution Lab | $30,100 | 4x4 | Doctor | 8-bitten | Duckworth-upon-Bilge — research 1,000 |
| Recurvery Room | $35,100 | 3x5 | Doctor | Cubism, Futurism | Grockle Bay — research 1,000 |

#### Pharmacy
- **Cures (multi-illness):** Bogwarts, Clamp, Grout, Lycanthropy, Misery Guts, Potty
  Mouth, Verbal Diarrhoea, Cold Shoulder, Face Plant, Skull Chutney, Sweet Teeth,
  Budgie Struggler, Heat Wave, Loose Jowels, Sandy Crack, Tooth Mutiny, Fanatick,
  Flack Hole, Hero Complex, Home Sick, Meteormites, Diluted Pupils, Mulch, Roadstool,
  Ramshackled, Spellbound, Art Sick, Blue Blood, Director's Gut, Misdewiener, Snot
  Twist, Square Eyes, Chewed a Rose, Cod Piece, Hologlands, Parapox, Tarred Pits,
  Hazardous Waist, Sticky, Wet Behind The Ears (base + DLC).
- **Cost / size / staff:** $7,600 / 3x3 / Nurse (Treatment qualifications recommended).
- **Machine:** Drug Mixer — two upgrades. **Unlock:** Hogsport tutorial (2nd room built).
- **Tips:** Critical from the first hospital to the last; keep one near the GP cluster.

#### Injection Room
- **Cures (multi-illness):** Decision Rash, Litter Bug, Mood Poisoning, Pudding Blood,
  Rock Bottom, Spontaneous Combustion, Curdled Blood, Eye Candy, Rantlers, Thin
  Skinned, Cauliflower Ears, Fool's Mould, Oozmosis, Placid Reflux, Wild Spore,
  Aller-Gs, Anty Matter, Asterrhoids, Cosmoss, Foot-in-Mouth, Root Snoot, Sproutrage,
  Weeping Iris, Banging Headache, Dramatic Paws, Listless, Monopolies, Sinewment,
  Bloat of Arms, Dino Sores, Hacking Cough, Cyclonic Irritation, Frosted Tips (base + DLC).
- **Cost / size / staff:** $15,100 / 3x3 / Nurse — no qualification required, but
  **Injection Administration** and Treatment qualifications raise her effectiveness.
- **Machine:** Jab Master — two upgrades.
- **Unlock:** Research project (1,000) once the Research Room arrives in Mitton
  University (base game).
- **Tips:** Steady moderate demand in nearly every hospital from World 2 onwards.

#### Surgery
- **Cures (multi-illness, operations):** Floppy Discs, Gurning Loins, Heart Throb,
  Pipe Organs, Spinal Bap, Blaggis, Cheese Bored, Displaced Glands, Goobris, Brain
  Farts, Desserted, Jellied Feels, Painapple, Astroknot, Extraterrestical, Planetary
  Ring, Situational Gravity, Warped, Burning Desire, Craft Ailment, Crystal Balls,
  Heavyhandedness, Canapains, Flash Back, Foxtrodden, Guest Cist, Limelit, Bionic
  Plague, Bone Head, Rolling Stones, Pelvic Crust, Shaken Kidneys, Weathered Veins
  (base + DLC).
- **Cost / size:** $26,000 / 3x4.
- **Staff:** Doctor **with the Surgery qualification (required)** *plus* a Nurse. Only
  the doctor's Surgery level affects success; the nurse's stats don't factor in.
- **Machine:** Operating Table (+ Medical Sink, Screen) — no machine upgrades; invest
  in the surgeon's training instead.
- **Unlock:** Smogley (base game).
- **Tips:** Called "the most profitable room in the game" — treats many illnesses at
  high prices. Operation Monitor adds +2% treatment power.

#### Fracture Ward
- **Cures:** Broken Face, Cross Bones, Humerus Injury, Hurty Leg, Shattered, Boneless
  Thighs, Dead Arm, Inverted 1080, Menace Elbow, Camel Toe, Knobbly Knee, Limb
  Empathy, Limpette, Continuthumb, Neutrainers, Sputneck, Star Struck, Flappy Hamper,
  Nasty Trip, Pine Dented, Broken Leg, Corrupt Footage, Stage Hand, Wardrobe
  Malfunction, Clockjaw, Fractured Timeline, Glass Dome, Missing Link, Hairline
  Fracture, Scrambled Legs, Piste Off (base + DLC).
- **Cost / size:** $13,600 / 3x4 minimum; like the Ward, it scales with size — the
  Traction Beds are large, so go big.
- **Staff:** Nurse; **Ward Management** qualifications recommended; up to four extra
  nurses assignable via the room inspector.
- **Machine:** Plaster Caster + Traction Beds (Ward Door, Nurse Station required) —
  no machine upgrades listed.
- **Unlock:** Tumble (base game).

#### De-Lux Clinic
- **Cures:** Lightheadedness — plus themed variants added later: Headcrabedness
  (Half-Life crossover), Beheadedness, Hotheadedness, Byteheadedness, and
  Frightheadedness (Spooky Mode).
- **Cost / size / staff:** $21,100 / 3x3 / Doctor (Treatment quals recommended).
- **Machine:** De-Lux O-Luxe (+ Console) — two upgrades. Screws a fresh bulb onto the
  patient's lightbulb head.
- **Unlock:** Hogsport tutorial (base game). One of your first treatment rooms.

#### Pans Lab
- **Cures:** Pandemic (pan stuck on head).
- **Cost / size / staff:** $20,100 / 4x4 / Doctor.
- **Machine:** Extract-a-Pan (giant magnet) — two upgrades.
- **Unlock:** Lower Bullocks initial objectives (base game).

#### Clown Clinic
- **Cures:** Jest Infection (and the medieval variant Jester Infection).
- **Cost / size / staff:** $20,100 / 4x4 / Nurse.
- **Machine:** Dehumorfier — two upgrades. De-clowns the patient.
- **Unlock:** Flottering initial objectives (base game).

#### Chromatherapy
- **Cures:** Grey Anatomy (patient rendered greyscale).
- **Cost / size / staff:** $21,100 / 3x4 / Nurse.
- **Machine:** Colourizer (+ Console) — two upgrades (research required).
- **Unlock:** Research project (1,000), available with the Research Room in Mitton
  University (base game).

#### Pest Control
- **Cures:** Animal Magnetism (animals clamped to the patient).
- **Cost / size / staff:** $20,100 / 4x4 / Nurse.
- **Machine:** Ultrasonic Cannon — two upgrades (research required).
- **Unlock:** Research project (1,000) from the outset of Flemington (base game).

#### Shock Clinic
- **Cures:** Shock Horror.
- **Cost / size / staff:** $30,100 / 4x4 / Doctor.
- **Machine:** Discharger — two upgrades (research required).
- **Unlock:** Research project (1,000) at the outset of Melt Downs (base game).
- **Tips:** Mostly needed in and around Melt Downs.

#### Cryptology
- **Cures:** Premature Mummification.
- **Cost / size / staff:** $30,100 / 3x4 / Nurse.
- **Machine:** Decrypter — two upgrades (research required).
- **Unlock:** Research project (1,000) from the outset of Sweaty Palms (base game).

#### Head Office
- **Cures:** Turtle Head.
- **Cost / size / staff:** $30,100 / 4x4 / Doctor.
- **Machine:** Turbo-Plunger — two upgrades (research required).
- **Unlock:** Research project (1,000); infobox lists Smogley as the first hospital
  (the wiki body text says Melt Downs — sources disagree).

#### Resolution Lab
- **Cures:** 8-bitten (pixelated patients).
- **Cost / size / staff:** $30,100 / 4x4 / Doctor.
- **Machine:** Debugger — two upgrades (research required).
- **Unlock:** Research project (1,000); first hospital Duckworth-upon-Bilge (base game).
- **Tips:** Fairly common, profitable illness in late-game maps.

#### Recurvery Room
- **Cures:** Cubism — plus Futurism (illness added with A Stitch In Time).
- **Cost / size / staff:** $35,100 / 3x5 / Doctor.
- **Machine:** Recurvery Unit (claw crane that reassembles cubed patients) — two
  upgrades (research required).
- **Unlock:** Research project (1,000); first hospital Grockle Bay (base game).

### Pebberley Island DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Indentification | $25,100 | 3x4 | Nurse | Blank Look | Pebberley Reef |
| Escape Room | $30,100 | 5x9 | Nurse | Wanderust | Overgrowth — research 1,000 |
| Correcting Pool | $36,100 | 3x4 | Doctor | Screwball | Topless Mountain (Wave 4) — research 1,000 |

#### Indentification *(Pebberley Island DLC)*
- **Cures:** Blank Look (featureless face). Machine: **Face Stamp** — two upgrades
  (research required). $25,100, 3x4, Nurse. Unlocked in Pebberley Reef's initial
  objectives.

#### Escape Room *(Pebberley Island DLC)*
- **Cures:** Wanderust. Machine: **Counterfeat** obstacle course — two upgrades
  (research required). $30,100, and by far the largest treatment footprint in the game
  at **5x9** — reserve a big block for it. Nurse-run. Unlocked by research (1,000) from
  the start of Overgrowth.

#### Correcting Pool *(Pebberley Island DLC)*
- **Cures:** Screwball (head replaced by a beach ball). Machine: **Autocue** (+
  Console) — two upgrades (research required). $36,100, 3x4, Doctor. Unlocked at Wave 4
  of the Topless Mountain horde-challenge hospital, via research (1,000).

### Bigfoot DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Doghouse | $20,100 | 4x4 | Nurse | Barking Mad | Underlook Hotel |
| Urban Mythology | $25,100 | 5x6 | Nurse | Metropolism | Swelbard — research 1,000 |
| Reanimation | $30,100 | 4x4 | Doctor | Monster Mishmash | Roquefort Castle |

#### Doghouse *(Bigfoot DLC)*
- **Cures:** Barking Mad (patients who think they're dogs). Machine: **K9-Away** — two
  upgrades (research required). $20,100, 4x4, Nurse. Unlocked in Underlook Hotel's
  initial objectives.

#### Urban Mythology *(Bigfoot DLC)*
- **Cures:** Metropolism. Machine: **Inner-City-Simulator** (a slice of city life for
  yeti-fied patients) — two upgrades (research required). $25,100, large 5x6 footprint,
  Nurse. Unlocked by research (1,000) from the outset of Swelbard.

#### Reanimation *(Bigfoot DLC)*
- **Cures:** Monster Mishmash. Machine: **Cryomatic** — two upgrades (research
  required). $30,100, 4x4, Doctor. Available from the outset of Roquefort Castle.

### Close Encounters DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Personification | $35,100 | 6x6 | Doctor | Lack of Humanity | Chasm 24 — research 1,000 |
| Self-Assembly | $25,100 | 4x5 | Nurse | Flat-Packed | Goldpan — research 1,000 |
| Toad Hall | $30,100 | 4x7 | Nurse | Frogborne | Camouflage Falls (Wave 7) |

#### Personification *(Close Encounters DLC)*
- **Cures:** Lack of Humanity (aliens in disguise). Machine: **Spin-Doctor** (+
  Console) — two upgrades (research required). $35,100 and a hefty 6x6 minimum,
  Doctor-run. Unlocked by research (1,000) from the start of Chasm 24.

#### Self-Assembly *(Close Encounters DLC)*
- **Cures:** Flat-Packed (patients folded into flat-pack furniture). Machine:
  **Character Creator** — two upgrades (research required). $25,100, 4x5, Nurse.
  Unlocked by research (1,000) from the start of Goldpan.

#### Toad Hall *(Close Encounters DLC)*
- **Cures:** Frogborne. Machine: **Poly-Cog** — two upgrades (research required).
  $30,100, 4x7, Nurse. Unlocked at Wave 7 of the Camouflage Falls challenge hospital.

### Culture Shock DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Danger Zone | $25,100 | 3x7 | Doctor | Stunt Trouble | Plywood Studios |
| War Room | $25,100 | 4x4 | Doctor | Private Parts | Fitzpocket Academy — research 750 |
| Wash Pit | $30,100 | 5x5 | Nurse | Soiled Self | Mudbury Festival (Wave 4) |

#### Danger Zone *(Culture Shock DLC)*
- **Cures:** Stunt Trouble. Machine: **Crash Course** stunt track (+ Console) — two
  upgrades (research required). $25,100, long 3x7 footprint, Doctor. Unlocked in
  Plywood Studios' initial objectives.

#### War Room *(Culture Shock DLC)*
- **Cures:** Private Parts (toy-soldier patients). Machine: **Meltn' Mould** — two
  upgrades (research required). $25,100, 4x4, Doctor. Unlocked by research (750) from
  the start of Fitzpocket Academy.

#### Wash Pit *(Culture Shock DLC)*
- **Cures:** Soiled Self. Machine: **Rub-O-Dub Tub** — two upgrades (research
  required). $30,100, 5x5, Nurse. Unlocked at Wave 4 of the Mudbury Festival challenge
  hospital.

### Off The Grid DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Farmacology | $25,100 | 3x6 | Nurse | Distrawed | Old Newpoint |
| Herb Garden | $7,100 | 3x4 | Nurse | 4 green illnesses | Old Newpoint |
| Woodwork | $25,100 | 4x4 | Nurse | Woodworms | Wanderoff — research 500 |
| Tech Support | $25,100 | 4x6 | Doctor | Glitchy Patch | Windsock — research 1,000 |

#### Farmacology *(Off The Grid DLC)*
- **Cures:** Distrawed (scarecrow patients). Machine: **Crop-Out** (+ Console) — two
  upgrades (research required). $25,100, 3x6, Nurse. Unlocked in Old Newpoint's initial
  objectives.

#### Herb Garden *(Off The Grid DLC)*
- **Cures (multi-illness):** Green Fingers, Incensed, Mage Fright, Pesticitis.
- **Cost / size / staff:** $7,100 / 3x4 / Nurse (ward-style room; Ward Door + Nurse
  Station required).
- **Machine:** Flower Bed (**one** upgrade, research required) + Vine Yard (no
  upgrade).
- **Unlock:** One comes pre-built at the outset of Old Newpoint; no research needed to
  build more.

#### Woodwork *(Off The Grid DLC)*
- **Cures:** Woodworms (wooden patients). Machine: **De-FIB** — two upgrades (research
  required). $25,100, 4x4, Nurse. Unlocked by research (500) from the start of
  Wanderoff.

#### Tech Support *(Off The Grid DLC)*
- **Cures:** Glitchy Patch. Machine: **Next-Generator** — two upgrades (research
  required). $25,100, 4x6, Doctor. Unlocked by research (1,000) from the start of
  Windsock.

### Speedy Recovery DLC

| Room | Cost | Min. size | Staff | Cures | Unlock |
|---|---|---|---|---|---|
| Wax Works | $19,100 | 4x4 | Doctor | Hive Mind | Betts Shore |
| Cloud Computing | $20,100 | 4x4 | Doctor | Under The Weather | Ailing |
| Powder Room | $22,600 | 4x4 | Doctor | Snow Problem | Pointy Pass — research 500 |

#### Wax Works *(Speedy Recovery DLC)*
- **Cures:** Hive Mind (beehive heads). Machine: **Honey Trap** — two upgrades
  (research required). $19,100, 4x4, Doctor. Available from the start of Betts Shore.

#### Cloud Computing *(Speedy Recovery DLC)*
- **Cures:** Under The Weather (personal storm cloud). Machine: **Storm Drain** — two
  upgrades (research required). $20,100, 4x4, Doctor. Unlocked in Ailing's initial
  objectives.

#### Powder Room *(Speedy Recovery DLC)*
- **Cures:** Snow Problem (snowman patients). Machine: **Flake Cannon** — two upgrades
  (research required). $22,600, 4x4, Doctor. Unlocked by research (500) from the start
  of Pointy Pass.

---

## 3. Facility rooms

Non-clinical rooms that keep the hospital running. None of these cure or diagnose
(except indirectly); most have no machine upgrades. Staff shown as "any" means the
room is used by staff rather than operated by one.

| Room | Cost | Min. size | Staff | Purpose | Unlock |
|---|---|---|---|---|---|
| Reception (Room) | $1,600 | 2x3 | Assistant(s) | patient check-in | Flottering (Star Level 1) |
| Toilets | $5,600 | 2x3 | — (all use it) | bathroom need | Hogsport (tutorial) |
| Staff Room | $5,100 | 2x3 | — (staff only) | energy/break recovery | Hogsport (tutorial) |
| Café (Room) | $7,600 | 4x5 | Assistant(s) | hunger + thirst, income | Flemington (Star Level 1) |
| Training (Room) | $7,000 | 3x3 | — (all staff train) | qualifications | Flottering |
| Research (Room) | $35,100 | 3x4 | Doctor + Research | unlock rooms/upgrades, income | Mitton University (challenge) |
| Marketing (Room) | $7,100 | 3x4 | Assistant + Marketing | campaigns | Flemington |
| Speed Dating | $35,100 | 4x5 | Assistant + Yesterization | returns time-travel patients | Clockwise-above-Thyme *(A Stitch In Time DLC)* |
| Corridor | — | — | — | connects everything | Hogsport (always available) |

### Reception (Room)
- A walled, multi-desk replacement for the freestanding Reception Desk: each
  **Reception Pod** inside needs its own Assistant, so one room can check in several
  patients at once. $1,600, 2x3 minimum (one pod); bigger rooms fit more pods.
- **Staff:** Assistant; **Customer Service** qualifications speed up check-in.
- **Unlock:** Star Level 1 in Flottering (base game). Place it directly inside the
  main entrance with clear corridor flow to the GP cluster.

### Toilets
- Drains the bathroom need of patients and staff. $5,600, 2x3 minimum. Required items:
  toilet cubicles (standard, Golden Toilet or Water Closet) — add Sinks and Hand
  Dryers for hygiene. No operating staff (Janitors clean them).
- **Unlock:** Hogsport tutorial (4th room). The Golden Bathroom Suite (Golden Toilet /
  Sink / Hand Dryer) comes free with the Hospital Pass newsletter sign-up.
- **Tips:** Several small blocks spread around the hospital beat one big one; more
  cubicles per room = shorter queues.

### Staff Room
- Where staff recover energy on breaks; seating, food/drink machines, TVs, arcade
  cabinets and pool tables speed recovery. $5,100, 2x3 minimum, no required items
  beyond the door.
- **The higher the room's prestige, the faster staff regain energy** — this is the one
  room where over-decorating pays direct dividends. Keep one within a short walk of
  every wing so breaks don't eat working time.
- **Unlock:** Hogsport tutorial (3rd room).

### Café (Room)
- Full-service café: an Assistant runs the Café Counter like a shop; customers pay
  ~$40 for a tray and sit at Café Tables (4 seats each). Handles hunger *and* thirst
  and earns steady income. $7,600, 4x5 minimum.
- **Staff:** Assistant per counter; Customer Service qualifications help.
- **Unlock:** Star Level 1 in Flemington (base game).
- **Tips:** Make it large and evenly laid out so crowds don't jam between the counter
  and the tables; roughly one café per two buildings.

### Training (Room)
- Teaches qualifications to any staff type. A staff member (or a paid Guest Trainer)
  lectures from the Lectern; each Trainee Desk seats one student, so a bigger room
  trains more staff per course. $7,000, 3x3 minimum.
- **Unlock:** Flottering initial objectives (base game).
- **Boost items:** Encyclopedia Bookcase I/II (+2%/+4% training speed), Anatomy
  Models, Anatomy Posters — these stack and meaningfully shorten courses.
- **Tips:** Several mid-size rooms (6–9 desks) running in parallel beat one giant one.

### Research (Room)
- Generates research points to unlock new rooms (the "research N" unlocks throughout
  this document), machine upgrades and cash projects. Each Research Pod is worked by
  one qualified doctor. $35,100, 3x4 minimum — make it spacious and multi-pod.
- **Staff:** Doctor **with the Research qualification (required)**; higher Research
  levels = faster progress.
- **Unlock:** Mitton University, after completing the challenge "Get Hospital Level to
  3" + "Upgrade a Machine" (base game). Research then carries across your whole
  career via the project list.

### Marketing (Room)
- Launches marketing campaigns from the Marketing Table: **General** campaigns raise
  hospital attractiveness/reputation, and targeted campaigns attract patients with a
  specific illness (profitable ones, ideally) or applicants for a staff role.
  $7,100, 3x4 minimum.
- **Staff:** Assistant **with the Marketing qualification (required)**; more levels =
  better campaigns.
- **Unlock:** Flemington initial objectives (base game).
- **Tips:** Build it early on new maps to bootstrap patient flow.

### Speed Dating *(A Stitch In Time DLC)*
- Despite the name, a facility room: patients who arrived through a Time Portal report
  here after being cured, and the **Yesterizer** machine sends them back to their own
  time period. $35,100, 4x5.
- **Staff:** Assistant **with the Yesterization qualification (required)**.
- **Unlock:** Available from the outset of Clockwise-above-Thyme (A Stitch In Time DLC).

### Corridor
- Not a buildable "room" but the connective tissue: every room's door must connect to
  corridor space with a clear path to every other room and the plot entrances. No
  cost, no size, no staff.
- Corridors host the freestanding service items — Reception Desks, vending machines,
  seating/benches, magazine racks, arcade machines, plants, bins, hygiene stations —
  which keep queueing patients fed, watered, entertained and non-mutinous. Wide,
  straight corridors with seating outside busy rooms (GP's Offices especially) are one
  of the strongest layout habits in the game.

---

## Quick reference: DLC room ownership

- **Base game:** all Section 1 rooms; Pharmacy, Injection Room, Surgery, Fracture
  Ward, De-Lux Clinic, Pans Lab, Clown Clinic, Chromatherapy, Pest Control, Shock
  Clinic, Cryptology, Head Office, Resolution Lab, Recurvery Room; all facilities
  except Speed Dating.
- **Pebberley Island:** Indentification, Escape Room, Correcting Pool.
- **Bigfoot:** Doghouse, Urban Mythology, Reanimation.
- **Close Encounters:** Personification, Self-Assembly, Toad Hall.
- **Culture Shock:** Danger Zone, War Room, Wash Pit.
- **Off The Grid:** Farmacology, Herb Garden, Woodwork, Tech Support.
- **Speedy Recovery:** Wax Works, Cloud Computing, Powder Room.
- **A Stitch In Time:** Speed Dating (plus new illnesses routed to existing rooms,
  e.g. Futurism → Recurvery Room, Jester Infection → Clown Clinic, Beheadedness →
  De-Lux Clinic).

## Sources

- Two Point Hospital Wiki (Fandom) — individual room pages fetched via the MediaWiki
  API (`two-point-hospital.fandom.com/api.php`), July 2026: GP's Office, General
  Diagnosis, Cardiology, Fluid Analysis, X-Ray, M.E.G.A Scan, DNA Lab, Ward,
  Psychiatry, Pharmacy, Injection Room, Surgery, Fracture Ward, De-Lux Clinic, Pans
  Lab, Clown Clinic, Shock Clinic, Recurvery Room, Head Office, Chromatherapy,
  Cryptology, Pest Control, Correcting Pool, Danger Zone, Escape Room, Farmacology,
  Herb Garden, Doghouse, Indentification, Personification, Resolution Lab,
  Self-Assembly, Speed Dating, Tech Support, Toad Hall, Urban Mythology, War Room,
  Wash Pit, Wax Works, Woodwork, Cloud Computing, Reanimation, Powder Room, Reception
  (Room), Toilets, Staff Room, Café (Room), Training (Room), Research (Room),
  Marketing (Room), Corridor. Primary source for costs, sizes, staff, machines,
  unlocks and cure lists.
- gamepressure.com — "Two Point Hospital: Hospital Rooms" guide
  (https://www.gamepressure.com/two-point-hospital/hospital-rooms/zbb405). Used to
  cross-check base-game costs/sizes and for demand/queue tips. (Where it disagreed
  with the wiki — Ward $7,500 vs $7,600, Training $17,000 vs $7,000 — the wiki
  infobox value was used.)
- Steam Community — "Two Point Hospital Guide [RETIRED]"
  (https://steamcommunity.com/sharedfiles/filedetails/?id=1498319124). Source for
  machine-upgrade costs/percentages, research point costs, and item boost values
  (bookcases, wall monitors, encyclopedias).
