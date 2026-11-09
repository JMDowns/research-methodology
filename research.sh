#!/bin/bash
# research.sh — Start a new Claude research session
#
# Usage:
#   ./research.sh "topic description"
#   ./research.sh "How do hash maps handle collisions"
#   ./research.sh --for ~/dev/my-project "LLM prompt caching for long pipelines"
#
# --for <repo>: the study gathers domain knowledge for that project. It sets
# `feeds:` in the frontmatter and writes candidate intent items that
# /intent-and-understanding-init (run in the repo) can import.
#
# This creates a topic folder and launches an interactive Claude session
# with the research methodology pre-loaded.

set -euo pipefail

FOR_REPO=""
if [ "${1:-}" = "--for" ]; then
    if [ $# -lt 3 ]; then
        echo "Usage: ./research.sh --for <repo path> \"<topic description>\""
        exit 1
    fi
    FOR_REPO="$(cd "$2" && pwd)"
    shift 2
fi

if [ $# -eq 0 ]; then
    echo "Usage: ./research.sh \"<topic description>\""
    echo ""
    echo "Examples:"
    echo "  ./research.sh \"How do hash maps handle collisions\""
    echo "  ./research.sh \"Best practices for Python async patterns\""
    echo "  ./research.sh --for ~/dev/my-project \"LLM prompt caching for long pipelines\""
    echo ""
    echo "Current studies:"
    ls -d */ 2>/dev/null | sed 's/\/$/  /' || echo "  (none yet)"
    exit 1
fi

TOPIC_DESC="$*"
RESEARCH_DIR="$(cd "$(dirname "$0")" && pwd)"

# Generate a slug from the topic description
SLUG=$(echo "$TOPIC_DESC" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')

# Truncate slug if too long
if [ ${#SLUG} -gt 60 ]; then
    SLUG="${SLUG:0:60}"
    SLUG="${SLUG%-}"  # Remove trailing hyphen if any
fi

# Create the topic folder
mkdir -p "$RESEARCH_DIR/$SLUG/sources"

echo "Research topic: $TOPIC_DESC"
echo "Folder: $RESEARCH_DIR/$SLUG/"
[ -n "$FOR_REPO" ] && echo "Feeds project: $FOR_REPO"
echo "Starting Claude session..."
echo ""

FEEDS_NOTE=""
if [ -n "$FOR_REPO" ]; then
    FEEDS_NOTE="
This study feeds the project at $FOR_REPO. Follow the \"Studies that feed a project\" section of CLAUDE.md:
- Add feeds: [\"$FOR_REPO\"] to the frontmatter.
- If $FOR_REPO/docs/INTENT.md exists, read it first. Note which items (I1, P2, ...) this study bears on, and don't contradict a confirmed item without saying so plainly.
- End ai-instructions.md with a \"## Candidate intent for $(basename "$FOR_REPO")\" section.
- End README.md with a \"## Self-check\" section.
- Tell me at the end to run /intent-and-understanding-init in $FOR_REPO to import the candidates.
"
fi

# Launch Claude with the research context
cd "$RESEARCH_DIR"
claude "New research task: \"$TOPIC_DESC\"

The research folder for this study is: $SLUG/

Instructions:
1. Read CLAUDE.md for the full research methodology (it contains the tested search strategy)
2. Copy templates/STUDY_TEMPLATE.md to $SLUG/README.md and fill in the metadata
3. Classify the question complexity (Tier 1/2/3) per CLAUDE.md
4. Execute the search strategy for that tier — follow the Critical Rules exactly
5. Store raw sources in $SLUG/sources/
6. Write synthesized findings in $SLUG/README.md — only state facts from fetched sources
7. Run the quality checklist before finalizing
8. If findings are actionable, create $SLUG/ai-instructions.md
9. Update INDEX.md when done

CRITICAL: Never fill knowledge gaps from training data. If you cannot verify a claim from a fetched source, mark it '(unverified)' or fetch another source. Cross-reference across 2+ source domains.

$FEEDS_NOTE
Begin by reading CLAUDE.md, then start the research."
