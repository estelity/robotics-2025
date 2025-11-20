#!/usr/bin/env zsh
set -e

# This script converts text files into one HTML file.

# List of files to convert (supports recursive glob with **)
FILES=(
  ./README.md
  ./src/**/*.py
)

# Extension override map
EXT_OVERRIDES=(
  "hpp:cpp"
  "sh:bash"
  "h:c"
)

typeset -A FILE_OVERRIDES

# Output file
OUTPUT="index.html"

# Header
cat <<EOF > "$OUTPUT"
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My Project</title>

  <!-- PrismJS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-coy.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css" />

  <style>
    body { font-family: sans-serif; margin: 0; padding: 8px; font-size: 0.75rem; }
    pre { margin: 0; }
    code { font-family: monospace; }
    h1 { margin-top: 1rem; margin-bottom: 0.25rem; }
    p { margin-top: 0.25rem; margin-bottom: 0.25rem; }
    pre[class*="language-"], code[class*="language-"] { max-height: inherit !important; overflow: hidden !important; box-shadow: none !important; border-left: none !important; }
    code[class*="language"] { overflow: hidden !important; font-size: 0.75rem; }
  </style>
</head>
<body>
EOF

# Expand files safely
EXPANDED_FILES=()
for FILE in $FILES; do
    [[ -f "$FILE" ]] && EXPANDED_FILES+=("$FILE")
done

# Process each real file
for FILE in $EXPANDED_FILES; do
    FILE_EXT="${FILE##*.}"

    # Markdown to HTML
    if [[ "$FILE_EXT" == "md" ]]; then
        FILE_EXT="html"
        pandoc -f markdown -t html "$FILE" >> "$OUTPUT"
        echo "<hr>" >> "$OUTPUT"
        continue
    fi

    # Apply extension overrides
    for OVERRIDE in $EXT_OVERRIDES; do
        EXT="${OVERRIDE%%:*}"
        NEW_EXT="${OVERRIDE##*:}"
        [[ "$FILE_EXT" == "$EXT" ]] && FILE_EXT="$NEW_EXT"
    done

    # Append file title
    echo "<h1>$FILE</h1>" >> "$OUTPUT"

    # Git commit info (ignore errors if not tracked)
    LAST_COMMIT=$(git log -1 --pretty=format:"%s (%ad)" --date=short "$FILE" 2>/dev/null || echo "No git info")
    echo "<p><strong>Last commit:</strong> $LAST_COMMIT</p>" >> "$OUTPUT"

    # Append file contents
    if [[ -z "${FILE_OVERRIDES[$FILE]}" ]]; then
        echo -n "<pre class=\"line-numbers language-$FILE_EXT\" style=\"white-space: pre-wrap;\"><code>" >> "$OUTPUT"
        sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g' "$FILE" >> "$OUTPUT"
        echo -n "</code></pre>" >> "$OUTPUT"
    else
        echo "${FILE_OVERRIDES[$FILE]}" >> "$OUTPUT"
    fi
done

# Footer
cat <<EOF >> "$OUTPUT"
<!-- PrismJS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
</body>
</html>
EOF
