#!/usr/bin/env python3
"""
check_patterns.py - mechanical checks for the medical-scientific-writing skill.

Counts the things a language model counts badly: words per sentence, em
dashes, repeated openers, rationed connectives, hedge stacks, candidate
AI-pattern phrases, and numbers or citations added or lost relative to the
original. Standard library only. Always exits 0.

The report lists CANDIDATES to read in context. A hit is not a violation:
"comprehensive geriatric assessment" and "robust standard errors" are
legitimate. The script gives no score.

Usage:
    python3 check_patterns.py revised.txt
    python3 check_patterns.py revised.txt --original original.txt
    python3 check_patterns.py < combined.txt

A single stream can carry both texts with marker lines:
    ===ORIGINAL===
    (original text)
    ===REVISED===
    (revised text)
"""

import argparse
import io
import re
import statistics
import sys

ORIGINAL_MARK = "===ORIGINAL==="
REVISED_MARK = "===REVISED==="

ABBREVIATIONS = {
    "e.g", "i.e", "et al", "vs", "cf", "fig", "figs", "eq", "eqs", "ref", "refs",
    "no", "nos", "dr", "prof", "mr", "mrs", "ms", "st", "approx", "ca", "resp",
    "inc", "ltd", "co", "jr", "sr", "vol", "pp", "p", "al", "etc", "viz", "suppl",
    "min", "max", "mo", "yr", "yrs", "wk", "wks", "hr", "hrs", "u.s", "jan", "feb",
    "mar", "apr", "jun", "jul", "aug", "sep", "sept", "oct", "nov", "dec",
}

# (regex, pattern id, short label). Case-insensitive.
CANDIDATES = [
    # W1 AI vocabulary
    (r"\bdelv(?:e|es|ed|ing)\b", "W1", "delve"),
    (r"\btapestr(?:y|ies)\b", "W1", "tapestry"),
    (r"\blandscape\b", "W1", "landscape"),
    (r"\brealm\b", "W1", "realm"),
    (r"\bpivotal\b", "W1", "pivotal"),
    (r"\bcrucial(?:ly)?\b", "W1", "crucial"),
    (r"\bparamount\b", "W1", "paramount"),
    (r"\bintrica(?:te|cies|cy)\b", "W1", "intricate"),
    (r"\bmultifaceted\b", "W1", "multifaceted"),
    (r"\binterplay\b", "W1", "interplay"),
    (r"\bnuanced?\b", "W1", "nuanced"),
    (r"\bholistic\b", "W1", "holistic"),
    (r"\bfoster(?:s|ed|ing)?\b", "W1", "foster"),
    (r"\bgarner(?:s|ed|ing)?\b", "W1", "garner"),
    (r"\bshowcas(?:e|es|ed|ing)\b", "W1", "showcase"),
    (r"\bunderscor(?:e|es|ed|ing)\b", "W1", "underscore"),
    (r"\bhighlight(?:s|ed|ing)?\b", "W1", "highlight (verb?)"),
    (r"\btestament\b", "W1", "testament"),
    (r"\bleverag(?:e|es|ed|ing)\b", "W1", "leverage"),
    (r"\butiliz(?:e|es|ed|ing|ation)\b", "W1", "utilize"),
    (r"\brobust(?:ly|ness)?\b", "W1", "robust (vague?)"),
    (r"\bcomprehensive(?:ly)?\b", "W1", "comprehensive (vague?)"),
    (r"\bseamless(?:ly)?\b", "W1", "seamless"),
    (r"\bmeticulous(?:ly)?\b", "W1", "meticulous"),
    (r"\bmyriad\b", "W1", "myriad"),
    (r"\bembark(?:s|ed|ing)?\b", "W1", "embark"),
    (r"\bharness(?:es|ed|ing)?\b", "W1", "harness"),
    (r"\belucidat(?:e|es|ed|ing)\b", "W1", "elucidate"),
    (r"\bshed(?:s|ding)? light\b", "W1", "shed light"),
    (r"\bdeeper understanding\b", "W1", "deeper understanding"),
    (r"\bnavigat(?:e|es|ed|ing) the\b", "W1", "navigate (figurative?)"),
    (r"\bunlock(?:s|ed|ing)?\b", "W1", "unlock"),
    (r"\bbolster(?:s|ed|ing)?\b", "W1", "bolster"),
    (r"\benduring\b", "W1", "enduring"),
    (r"\benhanc(?:e|es|ed|ing)\b", "W1", "enhance"),
    (r"\balign(?:s|ed)? with\b", "W1", "align with"),
    (r"\bdeep dive\b", "W1", "deep dive"),
    (r"\bquietly\b", "W1", "quietly"),
    # W2 inflation and evaluation
    (r"\bgroundbreaking\b", "W2", "groundbreaking"),
    (r"\bremarkabl[ey]\b", "W2", "remarkable"),
    (r"\bstriking(?:ly)?\b", "W2", "striking"),
    (r"\bimpressive(?:ly)?\b", "W2", "impressive"),
    (r"\bexcellent\b", "W2", "excellent"),
    (r"\boutstanding\b", "W2", "outstanding"),
    (r"\bexceptional(?:ly)?\b", "W2", "exceptional"),
    (r"\bunprecedented\b", "W2", "unprecedented"),
    (r"\btransformative\b", "W2", "transformative"),
    (r"\brevolutioni[sz](?:e|es|ed|ing)\b", "W2", "revolutionize"),
    (r"\bpromising\b", "W2", "promising"),
    (r"\bexciting\b", "W2", "exciting"),
    (r"\bnear-perfect\b", "W2", "near-perfect"),
    (r"\bgame[- ]changer\b", "W2", "game-changer"),
    (r"\bnovel\b", "W2", "novel (supported?)"),
    (r"\bcornerstone\b", "W2", "cornerstone"),
    (r"\bvaluable\b", "W2", "valuable"),
    # W3 ornamental adverbs
    (r"\b(?:markedly|dramatically|profoundly|critically|fundamentally|vastly|deeply|increasingly)\b", "W3", "ornamental adverb"),
    (r"\bsignificantly\b", "W3", "significantly (test reported?)"),
    (r"\bsubstantially\b", "W3", "substantially (number given?)"),
    (r"\bclearly\b", "W3", "clearly"),
    # W4 filler
    (r"\bin order to\b", "W4", "in order to"),
    (r"\bdue to the fact that\b", "W4", "due to the fact that"),
    (r"\bit is (?:important|worth|interesting) to note\b", "W4", "it is important to note"),
    (r"\bit (?:should|must) be (?:noted|emphasized)\b", "W4", "it should be noted"),
    (r"\bhas the (?:ability|potential) to\b", "W4", "has the ability/potential to"),
    (r"\bin terms of\b", "W4", "in terms of"),
    (r"\ba (?:large )?number of\b", "W4", "a number of"),
    (r"\bat the present time\b", "W4", "at the present time"),
    (r"\bprior to\b", "W4", "prior to"),
    # W7 AI-favored word choices
    (r"\blinked to\b", "W7", "linked to (associated with?)"),
    (r"\bvia\b", "W7", "via"),
    (r"\byield(?:s|ed|ing)?\b", "W7", "yield"),
    (r"(?:^|[.!?]\s+)Beyond\b", "W7", "Beyond as transition"),
    (r",\s+where\b", "W7", ", where (non-locative?)"),
    # W8 chatbot residue
    (r"\b(?:certainly|great question|i hope this helps|feel free to|as an ai|knowledge cutoff)\b", "W8", "chatbot residue"),
    # W9 buzzword compounds
    (r"\b(?:cutting-edge|state-of-the-art|data-driven|next-generation|best-in-class|world-class)\b", "W9", "buzzword compound"),
    # S1 -ing tails
    (r",\s+(?:thereby\s+|thus\s+)?(?:highlighting|underscoring|emphasizing|reflecting|symbolizing|showcasing|illustrating|demonstrating|suggesting|indicating|ensuring|contributing|paving|reinforcing|signaling|offering)\b", "S1", "-ing tail"),
    # S2 copula avoidance
    (r"\b(?:serves?|served|serving|stands?|stood|standing|functions?|acts?) as\b", "S2", "copula avoidance"),
    (r"\brepresents? (?:a|an|the)\b", "S2", "represents a"),
    # S3 negative parallelism
    (r"\bnot (?:only|merely|just|simply)\b", "S3", "negative parallelism"),
    (r"\bit(?:'s| is) not (?:about|just)\b", "S3", "it's not about"),
    (r"\b(?:does|do|did) not (?:mean|imply|suggest) that[^.]{0,120}\.\s+(?:It|This|Rather, it) (?:means|implies|suggests)\b", "S3", "split negative parallel"),
    # S7 clause chaining
    (r",\s+and (?:this|it|these|that)\b", "S7", ", and this/it"),
    # S11 signposting
    (r"\b(?:in this (?:section|paper|study), we (?:will )?(?:discuss|describe|present|explore))\b", "S11", "signposting"),
    (r"\b(?:as mentioned (?:above|earlier|previously)|as previously (?:discussed|mentioned|noted))\b", "S11", "as mentioned above"),
    (r"\b(?:let us|let's) (?:now )?(?:turn|consider|explore|examine|dive)\b", "S11", "let us turn"),
    (r"\b(?:in other words|put differently|that is to say|simply put|essentially),", "D9", "paraphrastic restatement"),
    # S14 staging and aphorism
    (r"\b(?:the (?:key|central|critical|real|crucial|fundamental) (?:question|issue|point|insight) (?:is|was|remains))\b", "S14", "staged run-up"),
    (r"\b(?:at its core|what really matters|here's the thing|the thing is|the hard part is|the part that matters)\b", "S14", "staged run-up"),
    (r"\b(?:is|are) the (?:new )?(?:currency|language|lifeblood|backbone|cornerstone|bedrock) of\b", "S14", "aphorism"),
    # S15 arguing with no one
    (r"\b(?:this is not to (?:say|suggest)|to be clear|one might (?:argue|be tempted)|it (?:may|might) be tempting to|a naive approach would be|we do not (?:suggest|claim|argue) that)\b", "S15", "arguing with no one"),
    # W8 gap-filling guesses
    (r"\b(?:not (?:documented|reported|available|recorded)),? (?:suggesting|indicating|implying)\b", "W8", "gap-filling guess"),
    (r"\b(?:it is believed that|(?:he|she|they|the patient) (?:likely|probably) (?:had|was|were|did|grew))\b", "W8", "gap-filling guess"),
    # S11 document self-description
    (r"\b(?:the (?:table|figure) below (?:shows|compares|summari[sz]es)|this (?:paper|article|section) is organi[sz]ed)\b", "S11", "self-description"),
    # D9 closing verdicts
    (r"(?:^|[.!?]\s+)(?:Overall|Ultimately|In essence),", "D9", "closing verdict (restates?)"),
    (r"(?:^|[.!?]\s+)This (?:illustrates|demonstrates|shows|highlights) (?:the|how|that)\b", "D9", "closer naming what a finding showed"),
    # S12 false range
    (r"\b(?:ranging|range|spans?|spanning) from [^.]{3,60}? to\b", "S12", "from X to Y (meaningful scale?)"),
    # D1 stated moral
    (r"\b(?:highlights?|underscores?|emphasi[sz]es?|illustrates?|reinforces?) the (?:importance|need|critical|crucial|vital|significance|value|role)\b", "D1", "stated moral"),
    (r"\bthis case (?:highlights|illustrates|underscores|demonstrates|emphasi[sz]es|reminds|serves|shows)\b", "D1", "this case highlights"),
    (r"\bserves? as an? (?:important |valuable |timely |stark )?(?:reminder|testament|example)\b", "D1", "serves as a reminder"),
    (r"\bhigh index of suspicion\b", "D1", "high index of suspicion (specific action?)"),
    (r"\bclinicians (?:should|must) (?:be aware|remain vigilant|maintain|consider)\b", "D1", "clinicians should be aware"),
    # D2 vague allusion (checked separately for citation presence too)
    (r"\b(?:a )?growing body of (?:evidence|literature|research)\b", "D2", "growing body of evidence"),
    (r"\b(?:experts|researchers|clinicians) (?:argue|suggest|believe|agree|recommend)\b", "D2", "unnamed experts"),
    (r"\bit is (?:well|widely) (?:known|established|accepted|recognized)\b", "D2", "it is well known"),
    # D4 study-as-hero / first claims
    (r"\b(?:fills?|filling|address(?:es|ing)?) (?:this|an important|a critical|a crucial|the) (?:critical |important |crucial |significant )?gap\b", "D4", "fills the gap"),
    (r"\bto (?:the best of )?our knowledge\b", "D4", "to our knowledge (search stated?)"),
    (r"\bfirst (?:to|study|report|reported|case|description)\b", "D4", "first claim (search stated?)"),
    (r"\b(?:definitive(?:ly)?|conclusively|unequivocally)\b", "D4", "definitive claim"),
    (r"\bprove[sd]?\b", "D4", "prove"),
    # D5 coda
    (r"\b(?:further|more|additional|future) (?:research|studies|investigation|work|trials)(?: is| are)? (?:needed|warranted|required|necessary)\b", "D5", "more research is needed"),
    (r"\bpav(?:e|es|ed|ing) the way\b", "D5", "pave the way"),
    (r"\bpromising (?:avenue|approach|tool|strategy|option|target)\b", "D5", "promising avenue"),
    (r"\bholds? (?:great |significant |considerable )?(?:promise|potential)\b", "D5", "holds promise"),
    (r"\bfuture (?:looks|is) bright\b", "D5", "future looks bright"),
    (r"\bhas the potential to (?:transform|revolutioni[sz]e|change)\b", "D5", "potential to transform"),
    # D6 generic preamble
    (r"\bin recent years\b", "D6", "in recent years"),
    (r"\b(?:remains?|is) a (?:major|significant|leading|growing) (?:cause|public health|global|health)\b", "D6", "generic burden opener"),
    (r"\bgained (?:increasing|growing|considerable) (?:attention|interest)\b", "D6", "gained increasing attention"),
    # D8 advocacy
    (r"\b(?:minor|small) limitation\b", "D8", "minor limitation (rebuttal?)"),
    (r"\bdoes not detract\b", "D8", "does not detract"),
    (r"\bunlikely to (?:affect|have affected|influence|alter)\b", "D8", "unlikely to affect (rebuttal?)"),
    (r"\bwe (?:believe|are confident|are excited)\b", "D8", "stance language"),
    (r"\bonly slightly (?:lower|worse|reduced)\b", "D8", "only slightly lower"),
    # D11 template scaffolding
    (r"\bchallenges and (?:future )?(?:directions|prospects|opportunities)\b", "D11", "challenges and future directions"),
    # Statistical spin
    (r"\btrend(?:ed|ing|s)? (?:toward|towards) (?:statistical )?significance\b", "STAT", "trend toward significance"),
    (r"\b(?:marginally|borderline|nearly) (?:statistically )?significant\b", "STAT", "marginally significant"),
    (r"\bapproach(?:ed|ing|es)? (?:statistical )?significance\b", "STAT", "approached significance"),
    (r"\bnumerically (?:superior|better)\b", "STAT", "numerically superior"),
]

ADDITIVE_OPENERS = {"additionally", "furthermore", "moreover", "notably", "importantly",
                    "interestingly", "crucially", "significantly", "overall"}

HEDGES = [r"\bmay\b", r"\bmight\b", r"\bcould\b", r"\bpossibl[ey]\b", r"\bpotential(?:ly)?\b",
          r"\bperhaps\b", r"\bsuggests?\b", r"\bappears?\b", r"\bseems?\b", r"\blikely\b",
          r"\bputative(?:ly)?\b", r"\bplausibl[ey]\b", r"\bto some extent\b", r"\bin part\b"]

VAGUE_ATTRIBUTION = re.compile(
    r"\b(?:studies|research|evidence|literature|reports|data|investigators) "
    r"(?:have|has)? ?(?:shown|demonstrated|suggested|reported|indicated|found|suggests|shows|indicates)\b",
    re.I)

CITATION = re.compile(
    r"\[\s*\d+(?:\s*[-–,]\s*\d+)*\s*\]"          # [3], [3-5], [1, 4]
    r"|\(\s*refs?\.?\s*[\d,\s–-]*\)"              # (ref), (refs 3-5)
    r"|\([A-Z][A-Za-z'\-]+(?: et al\.?| and [A-Z][A-Za-z'\-]+)?,? (?:19|20)\d{2}[a-z]?(?:[;,][^)]*)?\)"  # (Smith et al., 2020)
    r"|[A-Z][A-Za-z'\-]+ et al\.? \(?(?:19|20)\d{2}"  # Smith et al. (2020)
    r"|\^\(?\d"                                   # ^3 superscript-ish
    r"|\[CITATION NEEDED[^\]]*\]",
    re.I)

PLACEHOLDER = re.compile(r"\[(?:DATA NEEDED|CITATION NEEDED|AUTHORS?|PLACEHOLDER|UNVERIFIED|VERIFY)[^\]]*\]", re.I)

NUMBER = re.compile(r"(?<![A-Za-z])\d+(?:[.,]\d+)*")


def read_text(path):
    with io.open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def split_stream(text):
    if ORIGINAL_MARK in text and REVISED_MARK in text:
        _, rest = text.split(ORIGINAL_MARK, 1)
        original, revised = rest.split(REVISED_MARK, 1)
        return original.strip(), revised.strip()
    return None, text


def paragraphs(text):
    """Prose paragraphs, skipping headings, fences, tables, and blank blocks."""
    paras, block, fenced = [], [], False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        if not stripped:
            if block:
                paras.append(" ".join(block))
                block = []
            continue
        if stripped.startswith("#") or stripped.startswith("|"):
            if block:
                paras.append(" ".join(block))
                block = []
            continue
        stripped = re.sub(r"^>\s?", "", stripped)
        block.append(stripped)
    if block:
        paras.append(" ".join(block))
    return [p for p in paras if re.search(r"[A-Za-z]", p)]


def sentences(paragraph):
    result, start = [], 0
    for match in re.finditer(r"[.!?](?:[\"')\]]*)\s+(?=[A-Z0-9\[(\"'])", paragraph):
        end = match.start()
        preceding = paragraph[start:end + 1]
        token = re.search(r"([A-Za-z.]+)\.$", preceding)
        if token and token.group(1).lower().rstrip(".") in ABBREVIATIONS:
            continue
        # single capital initial ("J. Smith")
        if re.search(r"\b[A-Z]\.$", preceding):
            continue
        result.append(paragraph[start:match.end()].strip())
        start = match.end()
    tail = paragraph[start:].strip()
    if tail:
        result.append(tail)
    return [s for s in result if s]


def word_count(sentence):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-.,%]*", sentence))


def first_word(sentence):
    m = re.match(r"[\W_]*([A-Za-z]+)", sentence)
    return m.group(1).lower() if m else ""


def snippet(text, width=90):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= width else text[: width - 3] + "..."


def normalize_number(token):
    token = token.rstrip(".,")
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", token):
        token = token.replace(",", "")
    return token


def numbers(text):
    found = []
    for m in NUMBER.finditer(text):
        tok = normalize_number(m.group(0))
        # split "1,4" style citation lists that are not thousands
        if "," in tok:
            found.extend(t for t in tok.split(",") if t)
        else:
            found.append(tok)
    return found


def citations(text):
    return [re.sub(r"\s+", " ", m.group(0)).strip() for m in CITATION.finditer(text)
            if not m.group(0).upper().startswith("[CITATION NEEDED")]


def multiset_diff(a, b):
    """Items in a that are not covered by b (respecting counts)."""
    pool = {}
    for item in b:
        pool[item] = pool.get(item, 0) + 1
    missing = []
    for item in a:
        if pool.get(item, 0) > 0:
            pool[item] -= 1
        else:
            missing.append(item)
    return missing


def strip_placeholders(text):
    """Remove [DATA NEEDED: ...]-style placeholders so they don't count as prose."""
    return re.sub(r"\s*" + PLACEHOLDER.pattern, "", text, flags=re.I)


def check(revised, original=None):
    out = []
    full_text = revised
    paras = paragraphs(strip_placeholders(revised))
    all_sents = [s for p in paras for s in sentences(p)]
    total_words = sum(word_count(s) for s in all_sents)

    out.append("CHECK_PATTERNS REPORT (candidates to read in context, not violations)")
    out.append("=" * 70)
    line = f"Paragraphs: {len(paras)}  Sentences: {len(all_sents)}  Words: {total_words}"
    if all_sents:
        line += f"  Mean sentence length: {total_words / len(all_sents):.1f}"
    bare_words = total_words
    line += "  (placeholders excluded from counts)"
    if original is not None:
        orig_words = sum(word_count(s) for p in paragraphs(original) for s in sentences(p))
        line += f"  (original: {orig_words} words)"
        if bare_words > orig_words * 1.1:
            line += "\n  LENGTH: revision is more than 10% longer than the original; justify (restored content) or cut"
    out.append(line)

    # Marks
    out.append("\n[W6] Marks")
    em = revised.count("—")
    spaced_en = len(re.findall(r"\s–\s", revised))
    double_hyphen = len(re.findall(r"\s--\s", revised))
    curly = len(re.findall("[“”‘’]", revised))
    out.append(f"  em dashes: {em}   spaced en dashes used as dashes: {spaced_en}   ' -- ': {double_hyphen}   curly quotes/apostrophes: {curly}")
    if em:
        for p in paras:
            if "—" in p:
                out.append(f"    - {snippet(p[max(0, p.index(chr(0x2014)) - 50):p.index(chr(0x2014)) + 40])}")

    # Rhythm
    out.append("\n[S8] Rhythm: paragraphs of 3+ sentences with all lengths within a 5-word range")
    flagged = 0
    for i, p in enumerate(paras, 1):
        sents = sentences(p)
        if len(sents) < 3:
            continue
        counts = [word_count(s) for s in sents]
        sd = statistics.pstdev(counts)
        if max(counts) - min(counts) <= 5:
            flagged += 1
            out.append(f"  P{i}: UNIFORM lengths {counts} (SD {sd:.1f}) | {snippet(p, 60)}")
        elif sd < 5:
            out.append(f"  P{i}: low variation {counts} (SD {sd:.1f}), consider one structural change")
    if not flagged:
        out.append("  none uniform")

    # Openers and connectives
    out.append("\n[S8/W5] Openers and rationed connectives")
    opener_hits = 0
    prev_para_opener = None
    for i, p in enumerate(paras, 1):
        sents = sentences(p)
        firsts = [first_word(s) for s in sents]
        for j in range(len(firsts) - 2):
            if firsts[j] and firsts[j] == firsts[j + 1] == firsts[j + 2]:
                out.append(f"  P{i}: three consecutive sentences start with '{firsts[j]}'")
                opener_hits += 1
                break
        additive = [f for f in firsts if f in ADDITIVE_OPENERS]
        if len(additive) > 1:
            out.append(f"  P{i}: {len(additive)} additive/attention openers ({', '.join(additive)})")
            opener_hits += 1
        this_opener = firsts[0] if firsts else None
        if this_opener in ADDITIVE_OPENERS and prev_para_opener in ADDITIVE_OPENERS:
            out.append(f"  P{i}: consecutive paragraphs open with additive connectives ('{prev_para_opener}', '{this_opener}')")
            opener_hits += 1
        prev_para_opener = this_opener
    if not opener_hits:
        out.append("  none")

    # Hedge stacks
    out.append("\n[S6] Hedge stacks (3+ hedge tokens, or modal + potentially/possibly, in one sentence)")
    hedge_hits = 0
    for s in all_sents:
        n = sum(len(re.findall(h, s, re.I)) for h in HEDGES)
        modal_combo = re.search(r"\b(?:may|might|could)\b[^.]{0,40}\b(?:potentially|possibly|perhaps)\b", s, re.I)
        if n >= 3 or modal_combo:
            hedge_hits += 1
            out.append(f"  ({n}) {snippet(s)}")
    if not hedge_hits:
        out.append("  none")

    # Vague attribution without citation
    out.append("\n[D2] Attribution phrases in sentences with no citation marker")
    vague_hits = 0
    full_sents = [s for p in paragraphs(full_text) for s in sentences(p)]
    for s in full_sents:
        if VAGUE_ATTRIBUTION.search(s) and not CITATION.search(s) and not PLACEHOLDER.search(s):
            vague_hits += 1
            out.append(f"  {snippet(s)}")
    if not vague_hits:
        out.append("  none")

    # Candidate phrases
    out.append("\n[Candidates] Pattern phrases (read each in context)")
    by_id = {}
    for regex, pid, label in CANDIDATES:
        for m in re.finditer(regex, revised, re.I | re.M):
            ctx = revised[max(0, m.start() - 45): m.end() + 35]
            by_id.setdefault(pid, []).append((label, snippet(ctx, 95)))
    order = ["STAT", "D1", "D2", "D4", "D5", "D6", "D8", "D9", "D11",
             "S1", "S2", "S3", "S7", "S11", "S12", "S14", "S15", "W1", "W2", "W3", "W4", "W7", "W8", "W9"]
    if not by_id:
        out.append("  none")
    for pid in order:
        hits = by_id.get(pid)
        if not hits:
            continue
        out.append(f"  {pid}: {len(hits)}")
        for label, ctx in hits[:12]:
            out.append(f"    - {label}: ...{ctx}...")
        if len(hits) > 12:
            out.append(f"    ... {len(hits) - 12} more")

    # Placeholders
    ph = PLACEHOLDER.findall(full_text)
    out.append(f"\n[Placeholders] {len(ph)}")
    for item in ph:
        out.append(f"  {item}")

    # Fidelity
    if original is not None:
        out.append("\n[Fidelity] Numbers and citations versus the original")
        orig_nums, rev_nums = numbers(original), numbers(strip_placeholders(revised))
        added = sorted(set(rev_nums) - set(orig_nums))
        lost = sorted(set(orig_nums) - set(rev_nums))
        out.append(f"  numbers in revision not in original: {sorted(set(added)) if added else 'none'}")
        out.append(f"  numbers in original missing from revision: {sorted(set(lost)) if lost else 'none'}")
        if added:
            out.append("    -> check each added number; a number the original spelled out as a word is fine")
        if lost:
            out.append("    -> check each lost number; deleting a reported result is a fidelity failure (D3)")
        orig_c, rev_c = citations(original), citations(revised)
        lost_c = multiset_diff(orig_c, rev_c)
        added_c = multiset_diff(rev_c, orig_c)
        out.append(f"  citation markers lost: {lost_c if lost_c else 'none'}")
        out.append(f"  citation markers added: {added_c if added_c else 'none'}")
        if added_c:
            out.append("    -> an added citation must come from the user's material or a verified source")
    else:
        out.append("\n[Fidelity] no original supplied; run with --original to compare numbers and citations")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("revised", nargs="?", help="revised text file (default: stdin)")
    parser.add_argument("--original", help="original text file, for fidelity checks")
    args = parser.parse_args()

    if args.revised:
        text = read_text(args.revised)
    else:
        text = sys.stdin.read()
    original, revised = split_stream(text)
    if args.original:
        original = read_text(args.original)
    print(check(revised, original))
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # never block the workflow
        print(f"check_patterns.py error: {exc}")
    sys.exit(0)
