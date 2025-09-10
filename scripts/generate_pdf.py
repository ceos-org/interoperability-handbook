#!/usr/bin/env python3

import os
import click
import pypandoc

DEFAULT_MD_FILES = [
    "Introduction.md",
    "Framework.md",
    "Vocabulary.md",
    "Architecture.md",
    "Interface.md",
    "Quality.md",
    "Policy.md",
    "Conclusion.md",
]


@click.command()
@click.option(
    "--output",
    default="interoperability-handbook.pdf",
    show_default=True,
    help="Output PDF filename",
)
@click.option(
    "--version",
    default="Version 2.0 DRAFT",
    show_default=True,
    help="Version string for cover page",
)
def main(output, version):
    """
    Generate PDF from markdown files.
    Combines multiple markdown files into a single PDF with a cover page and table of contents.
    Requires pandoc and a LaTeX engine (e.g., xelatex) to be installed.
    The script uses pypandoc to handle the conversion.
    The generated PDF will be saved to the specified output file.

    Args:
        output (str): Output PDF filename.
        version (str): Version string for the cover page.

    Returns:
        None
    """
    # Compose cover page
    cover_page = f"""---
geometry: margin=2cm
fontsize: 12pt
header-includes:
    - \\usepackage{{graphicx}}
    - \\usepackage{{array}}
    - \\usepackage{{xcolor}}
    - \\usepackage{{uarial}}
    - \\renewcommand{{\\familydefault}}{{\\sfdefault}}
    - \\definecolor{{ceosblue}}{{RGB}}{{0,51,102}}
    - \\newcolumntype{{L}}{{>{{\\raggedright\\arraybackslash}}p{{0.1\\linewidth}}}}
    - \\setlength{{\\tabcolsep}}{{12pt}}
---

\\thispagestyle{{empty}}
\\pagecolor{{ceosblue}}
\\begin{{center}}
\\vspace*{{3cm}}
\\color{{white}}
\\includegraphics[width=0.4\\textwidth]{{{"images/ceos-logo-notext.png"}}} \\\\[1.5cm]
{{\\Huge \\textbf{{Interoperability Handbook}}}} \\\\[1.5cm]
{{\\large Version: {version}}} \\\\[0.5cm]
{{\\large \\today}}
\\end{{center}}
\\newpage
"""

    # Table of contents page
    cover_page += """
\\pagecolor{white}
\\setcounter{tocdepth}{1}
\\tableofcontents
\\newpage
"""

    # Combine markdown files
    combined_md = cover_page
    for fname in DEFAULT_MD_FILES:
        if not os.path.exists(fname):
            print(f"Warning: {fname} not found.")
            continue
        with open(fname, "r", encoding="utf-8") as f:
            combined_md += f.read() + "\n\n"

    # Remove unwanted lines
    combined_md = "\n".join(
        [line for line in combined_md.split("\n") if not line.startswith("[Previous]")]
    )
    # Add page break before each top-level header
    combined_md = combined_md.replace("\n# ", "\n\\newpage\n# ")

    # Add a final footnote with CC-BY license
    combined_md += "\n\n---\n\n"
    combined_md += (
        "This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)."
    )

    # Write to temp file
    with open("combined.md", "w", encoding="utf-8") as f:
        f.write(combined_md)

    extra_args = [
        "--pdf-engine=xelatex",
    ]

    pypandoc.convert_file(
        "combined.md", "pdf", outputfile=output, extra_args=extra_args
    )
    print(f"PDF created: {output}")


if __name__ == "__main__":
    main()
