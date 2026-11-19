# Source notes

What this skill was built from, what each source contributed, and how disagreements between them were resolved. Read this when a rule seems arbitrary, or when deciding whether to relax one for a specific author or journal.

## 1. The detection study

**Russell J, Rajendhran R, Pham CM, Iyyer M, Wieting J. StoryScope: Investigating idiosyncrasies in AI fiction. arXiv:2604.03136 (v6).** University of Maryland and Google DeepMind. CC0.

What it did: 10,272 human stories from Books3 (mean about 6,400 words); for each, a writing prompt was reverse-engineered and five LLMs (Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5) wrote a "mirror" story, for 61,608 stories. An LLM pipeline extracted 304 discourse-level narrative features (adapted from the NarraBench taxonomy); 47 style-linked features were removed to leave a 257-feature "narrative" set. XGBoost classifiers with SHAP analysis.

Key findings:
- Narrative features alone separated human from AI at 93.2% macro-F1 (style features alone: 85.8%; combined: 96.0%; raw-text classifiers such as ModernBERT reached 99.9%; zero-shot Binoculars only 55.9% on long fiction).
- Results held on length-matched subsets and after memorization filtering; no topic confound.
- Six-way attribution (human plus five models) from narrative features: 68.4% macro-F1 (chance 16.7%).
- **Removing surface artifacts did not remove the signal**: after LAMP editing (which rewrites cliché and purple prose) on 278 Gemini stories, narrative detection moved only from 95.5% to 93.9%.
- AI stories cluster: the five models occupy a tight region of narrative space (human-to-AI centroid distance 1.6 times the AI-to-AI distance); human stories are more dispersed and rarer (rarity percentile 0.71 vs 0.49, d = 0.83).

Core human-vs-AI differences (AI vs human): explicit statement of theme 77% vs 52%; dialogue used for philosophical debate 59% vs 34%; vague allusions 72% vs 50% (specific named works 24% vs 47%); protagonist-driven resolutions 69% vs 46%; no subplots 79% vs 57%; endings of internal acceptance 47% vs 27%; morally ambivalent protagonists 38% vs 59%; emotion conveyed through bodily sensation 81% vs 38% (explicit emotion labels 8% vs 29%); smell imagery 82% vs 57%; fourth-wall breaks 39% vs 67%; direct reader address 7% vs 28%. Humans used more time jumps, flashbacks, and nonlinear structure.

Model fingerprints: Claude, flat escalation, the most uniform voice, reverent continuation of conventions, frequent epilogues; GPT, rumor as plot device, retrospective framing, subverted expectations; Gemini, tidiest endings, extended denouements, bleak settings; DeepSeek, front-loads crucial context; Kimi, the generic center of the AI distribution.

Surface style: the paper deliberately does not quantify word-level features. It cites prior work that AI overuses em dashes and words such as "delve" and "tapestry", notes that newer models reduced em-dash use, and argues that style-based detection is brittle to paraphrase and light editing, whereas narrative choices require structural rewrites to change.

**How this skill uses it.** The study is about fiction, so its features do not transfer one to one. The transferable lesson is the hierarchy: discourse-level choices (what is said, what is left out, how the argument resolves) carry the AI signature, and vocabulary edits alone leave it intact. This skill therefore fixes structure first. The specific translations (labelled [StoryScope] in the pattern catalog) are adaptations by this skill's author:

| StoryScope finding | Scientific-writing pattern |
|---|---|
| Explicit theme statement | D1, the stated moral ("This case highlights the importance of...") |
| Vague allusion vs named works | D2, unnamed "studies have shown" vs named, cited, quantified evidence |
| Tight causality, few subplots | D3, the tidy story that drops nulls, weak subgroups, diagnostic detours |
| Protagonist-driven resolution | D4, the study as hero that fills the gap and neutralizes every limitation |
| Acceptance endings, epilogues, extended denouements | D5, reassuring or promotional coda, "further research is needed" |
| Front-loaded context | D6, generic preamble |
| Uniform voice, co-occurring profile | D7, uniform paragraph architecture and certainty |
| Homogeneity, low rarity | The swap test: generic sentences fit any paper |

Features with no scientific analogue (embodied emotion, smell imagery, fourth-wall breaks, dialogue function) were not used. Nonlinear structure was not imported either: IMRaD is linear by design, and faking nonlinearity would harm clarity.

## 2. The six source skills

### eniktab/scientific-paper-writer (MIT)

Structure: one large SKILL.md (about 1,000 lines) in numbered parts (absolute rules, workflow phases, AI-voice audit, storytelling, journal profile, grants, reviewer response, cover letter, field conventions, checklists, rejection causes), plus a companion `journal-intelligence` skill that fetches live author guidelines, AI policies, and LaTeX templates into a `journal_profile.yaml`.

Contributed: integrity rules (verified citations only, `[UNVERIFIED]` and `[PLACEHOLDER]` tags, no p-hacking language, no HARKing); two-stage outline-then-prose writing; prose only in IMRaD sections; IMRaD tense and voice table; four-move Introduction funnel; five-move Discussion; "lead with the finding, not the test"; statistical reporting by test type; reporting-guideline table; 25 AI patterns with a self-audit checklist (significance inflation, notability name-dropping, -ing analyses, promotional language, vague attribution, challenge-and-triumph arcs, AI vocabulary, copula avoidance, negative parallelism, rule of three, synonym cycling, false ranges, em dash and boldface overuse, inline-header lists, sentence-initial filler transitions, hyphenated-compound buzzwords, chatbot artifacts, sycophancy, filler, hedge stacks, generic conclusions, epistemic uniformity, structural predictability); "soul factor" (intellectual commitment, field precision, rhythm, analytical specificity, negative space); perplexity and burstiness framing; central-claim test; grant, cover letter, and reviewer-response templates; "journal instructions win".

Not adopted as-is: its ban on "importantly", "notably", "interestingly" in all cases (softened to rationing, see conflicts); "maximum one Furthermore per manuscript" (softened to per-paragraph rationing); Nature-specific defaults (prose abstract, "Here we show") presented as universal.

### matsuikentaro1/humanizer_academic (MIT; based on blader/humanizer and Wikipedia's "Signs of AI writing")

Structure: SKILL.md of about 900 lines with 35 numbered patterns, each with words-to-watch, problem, and before/after pairs drawn from EMPA-REG OUTCOME publications; `references/reader-clarity.md` with eight diagnostic examples; `scripts/humanizer_check.py` (sentence lengths per paragraph, em dashes, curly quotes, repeated openers, ", and" chains, numbers added vs the original, candidate words). Two-pass draft and self-audit process with mandatory final checks and a fixed output format.

Contributed: reader clarity before compression; the strict fidelity rule (never insert facts; `[DATA NEEDED]` placeholders; recalled candidates listed separately); subject-verb compatibility (non-human subjects should not "determine" or "acknowledge"); preserve legitimate academic phrases and logical connectives; calibrated hedging (one layer, sized to design); medical-specific word choices ("linked to" vs "associated with", "via", "beyond", "yield", loose "where"); ornamental vs functional -ly adverbs; connective-preserving edits (never bare-delete a transition; choppy prose is a tell); paragraph cohesion through old-to-new flow; paraphrastic repetition; content-free evaluation sentences; the burstiness criterion (no paragraph of 3+ sentences with all lengths within a 5-word range; humans 10 to 55 words, SD 10 to 15; AI SD under 5); keep short claim sentences; clause chaining with ", and this/it", stacked predicates, nested lists; em-dash elimination; the checker script design.

Not adopted: the author-specific voice profile (one researcher's sentence lengths and connective repertoire). The principle is kept: when the user provides their own prior writing, calibrate to it.

### HeartWise-AI/ai-writing-skills (MIT)

Structure: several skills for medical AI research (protocol writing, manuscript writing, TRIPOD+AI manuscript writing, manuscript review, CIHR grant writing and format compliance), each a SKILL.md with section-by-section structure, success checklists, pseudo-code verification logic, templates, and QC scripts (typography, length budgets).

Contributed: the advocacy gate (G2), with ten signals of authors writing as advocates and an evidence-matched verb table by design; symmetric reporting; limitations without rebuttal; "do not overcorrect"; the clinical-meaning gate (who uses it, where, at which step, against which guideline comparator, counts per 1,000, what is still unproven); the length and information-density gate with measured overshoot of AI-assisted drafts (2 to 11 times author targets); "compress by deleting the explaining, not the facts"; negative-space deletion with the test "would this be equally true of a paper whose authors never considered the issue?"; routing detail to the Supplement with a citation at the point of removal; abbreviation expansion including dataset names; Results rules (every estimate self-contained, overlapping CIs are not differences); six-question Discussion; "finish with an anti-slop pass, but manuscript invariants win on tone".

Not adopted as defaults: house-style rules (no "vs.", no "e.g.", "to" in CI ranges, two decimals everywhere, strengths before limitations, ethics as first Methods subsection, AUROC-only metrics). These are reasonable for that group's journals and are left to the journal or author.

### noora-noureldin2000/Skills-for-MedicalResearch-writing (license per file; MIT where stated)

Structure: a collection. Relevant parts: `.agents/skills/academic-writing` (IMRaD formatting per Gastel and Day, ICMJE, AMA), `skills/sciwrite` (five-pass audit after Sainani), `skills/humanizer_general.md` (general humanizer with an academic section), `skills/proofreading.md` (LaTeX and content proofreading), plus statistics, reference validation, and document-automation skills.

Contributed: tense architecture table; gap formula and gap types; purpose-statement formula with strong verbs; MEAL paragraph plan; Introduction three-move funnel with proportions; Methods six subsections and the five required statistical elements; Results no-redundancy rule; Discussion five moves with limitations as state, impact, mitigation; title and abstract rules; MeSH keywords; number formatting; AMA citation style; bias-free, person-first language; ICMJE authorship and required statements, including AI disclosure wording; CARE case-report structure and cautious language; cover letter and reviewer response structure; sciwrite's five passes (clutter, voice and verbs, sentence architecture, keyword consistency, numbers and citations) with severity levels and the "telephone game" citation audit; proofreading's overclaiming checks ("significantly" without tests, "outperform" without full support) and "figure captions describe, they do not conclude".

Not adopted: humanizer_general's "personality and soul" advice (opinions, humor, "let some mess in"), its instruction to remove transitions such as "therefore" and "in conclusion" wholesale, its removal of hyphens from compound modifiers, and its framing of driving detector scores "close to 0%". These conflict with manuscript conventions, with the other sources, or with the integrity rules.

### quanghuy0497/Writing-in-the-Sciences (course notes; Stanford/Coursera, Kristin Sainani)

Structure: eight unit READMEs of course notes with worked examples: principles and clutter; verbs; sentences, punctuation, and paragraphs; the writing process; the original manuscript; publishing and peer review; reviews, grants, letters; communicating with broader audiences.

Contributed: the core principles (cut clutter, active voice, strong verbs, no nominalizations, don't bury the verb); clutter categories and tricks (eliminate negatives, "there is/are", needless prepositions); "we" as responsibility; punctuation hierarchy; parallelism; paragraph rules (one idea, point early, logic over transition words, outline-and-rewrite editing); repetition of keywords is fine; acronym austerity; the 70/10/20 writing process; order of writing a manuscript; Results summarize rather than read tables, report negative and control results, reserve "significant"; Methods may use passive and jargon; Introduction known, unknown, question in two to five paragraphs; Discussion answers the question first, stays close to the data, focuses on limitations that matter; review-article thesis and organization; lay writing (take-home first, avoid jargon including scientist-speak, unpack, filter detail by layers, get there faster, tell a story); final consistency and reference checks.

Where it conflicts with the AI-pattern sources: Sainani endorses the em dash for emphasis and the rule of three as a rhetorical device. Both are now strong AI markers when used by habit; see conflicts below.

### ashryaagr/karpathy-output-style (MIT)

Structure: four short skills (clear writing, explain-diagram, explain-webpage, explainer videos). Only `clear-writing` and its `references/asd-ste100.md` are relevant.

Contributed: the STE-inspired plain-English mode: main idea first, common words, concrete subjects, active verbs, one name per concept, 25 words per descriptive sentence and 20 per instruction, one instruction per sentence, condition before action, unstack noun groups, preserve facts and uncertainty; and the honesty boundary that "STE-inspired" is a style, not a compliance claim.

## 3. Conflicts and how they were resolved

| Question | Positions in sources | Resolution in this skill | Why |
|---|---|---|---|
| Em dashes | Banned (HeartWise, Matsui, noora proofreading); max one per section (eniktab); a legitimate emphasis tool (Sainani) | Replace all in manuscript prose by default; at most one per section if the journal or author uses them | Strongest consensus among medical sources; high reader salience as an AI marker; colons and parentheses do the same work |
| "Notably", "Importantly", "Interestingly" | Banned as persuasion (eniktab, HeartWise G2); legitimate academic transitions (Matsui) | Rationed: at most one per paragraph, only before a concrete datum, never only for favorable results | Both sides are right about different uses; the asymmetry test catches the advocacy use |
| Additive connectives (Furthermore, Moreover, Additionally) | Max one per manuscript as paragraph opener (eniktab); remove entirely (humanizer_general); keep, never bare-delete (Matsui) | At most one per paragraph, not as consecutive paragraph openers; when removed, restore the link | Removing all of them produces choppy, machine-cleaned prose |
| Logical connectives (thus, therefore, however) | Remove (humanizer_general); keep (Matsui, Sainani, academic-writing) | Keep where the relation is real | They carry the argument |
| Active vs passive | Active throughout, Nature preference (eniktab, Sainani); passive conventional in Methods (all medical sources); preserve author voice (Matsui) | Active where the actor matters; passive acceptable in Methods; no mechanical flipping | Accountability where it matters, convention where it doesn't |
| Rule of three | Pattern to eliminate (eniktab, Matsui, humanizer); classic device (Sainani) | Flag reflexive triads; keep genuine lists of any length | The problem is habit, not the number three |
| Hedging | One hedge, calibrated (all); add a cushion for observational causal implications (Matsui) | Calibration table by design | Both stacking and overclaiming are miscalibration |
| "Add voice" | Opinions, humor, mess (humanizer_general); intellectual commitment (eniktab); neutral, evidence-matched tone (HeartWise) | Intellectual commitment calibrated to evidence; no manufactured personality | Manuscripts are not essays; editors read affect as bias |
| Hyphenated compounds | Remove hyphens from common pairs (humanizer_general); flag buzzword compounds (eniktab) | Flag buzzwords; keep correct hyphenation of compound modifiers | Removing hyphens is a grammar error under AMA style |
| Length | Hard budgets for medical AI papers (HeartWise); journal limits (all) | Journal limit first; budget table as defaults; measure before polishing | Budgets vary by field and journal |
| Burstiness target | Strict criterion (Matsui); "8 words, then 31, then 14" (eniktab); short punchy sentences (humanizer_general) | Matsui's 5-word-range criterion, achieved through clarity edits, never staccato | Rhythm variation that serves meaning reads as human; theatrical rhythm does not |
| Goal framing | "Reduce AI detection close to 0%" (humanizer_general); "no AI-detectable patterns" (eniktab) | Better writing; no detector promises; disclosure remains the author's duty | Detector-evasion is not a quality goal, and AI-use disclosure is required by ICMJE and most journals |
| Abstract format | Prose "Here we show" (eniktab, Nature); structured (HeartWise, academic-writing) | Follow the journal | Varies by journal and article type |

## 4. Attribution

Patterns and principles are adapted, rewritten, and reorganized; examples in this skill are newly written unless marked. Upstream sources: Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup); blader/humanizer (MIT); matsuikentaro1/humanizer_academic (MIT, K. Matsui); eniktab/scientific-paper-writer (MIT); HeartWise-AI/ai-writing-skills (MIT); noora-noureldin2000/Skills-for-MedicalResearch-writing; quanghuy0497/Writing-in-the-Sciences (notes on K. Sainani's Stanford course); ashryaagr/karpathy-output-style (MIT); ASD-STE100 Issue 9 (ASD/STEMG); Russell et al., StoryScope, arXiv:2604.03136 (CC0).
