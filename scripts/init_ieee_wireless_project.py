#!/usr/bin/env python3
"""Create an IEEE wireless manuscript workspace."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


SECTION_FILES = [
    ("01_introduction.tex", "Introduction"),
    ("02_related_work.tex", "Related Work"),
    ("03_system_model.tex", "System Model and Problem Formulation"),
    ("04_method.tex", "Proposed Method"),
    ("05_experiments.tex", "Numerical Results"),
    ("06_conclusion.tex", "Conclusion"),
]


def clean_tex(text: str) -> str:
    return (
        text.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
    )


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", help="Workspace directory to create")
    parser.add_argument("--title", default="Working Title for IEEE Wireless Submission")
    parser.add_argument("--venue", default="generic", help="generic, twc, tvt, wcl, jsac, tcom, iotj, iwcm, conference")
    parser.add_argument(
        "--area",
        default="csi",
        help="Primary area, e.g. csi, isac, ris, channel-estimation, ai-wireless, foundation-models, wireless-datasets",
    )
    parser.add_argument("--author", default="Author Name")
    parser.add_argument("--sim-lang", choices=["python", "matlab", "none"], default="python")
    args = parser.parse_args()

    root = Path(args.output_dir).resolve()
    paper = root / "paper"
    sections = paper / "sections"

    for directory in [
        sections,
        paper / "figures",
        paper / "tables",
        root / "notes",
        root / "experiments",
    ]:
        directory.mkdir(parents=True, exist_ok=True)

    for filename, heading in SECTION_FILES:
        write(
            sections / filename,
            f"""
            \\section{{{heading}}}
            % TODO: Draft this section with claim-evidence alignment.
            """,
        )

    includes = "\n".join(f"\\input{{sections/{filename}}}" for filename, _ in SECTION_FILES)
    write(
        paper / "main.tex",
        f"""
        \\documentclass[journal]{{IEEEtran}}
        \\usepackage{{amsmath,amssymb,amsfonts}}
        \\usepackage{{algorithmic}}
        \\usepackage{{graphicx}}
        \\usepackage{{cite}}
        \\usepackage{{booktabs}}

        \\title{{{clean_tex(args.title)}}}
        \\author{{{clean_tex(args.author)}}}

        \\begin{{document}}
        \\maketitle

        \\begin{{abstract}}
        TODO: State the wireless setting, prior gap, proposed method, key evidence, and boundary.
        \\end{{abstract}}

        \\begin{{IEEEkeywords}}
        {clean_tex(args.area)}, wireless communications, IEEE
        \\end{{IEEEkeywords}}

        {includes}

        \\bibliographystyle{{IEEEtran}}
        \\bibliography{{references}}
        \\end{{document}}
        """,
    )

    write(
        paper / "references.bib",
        """
        % Add verified BibTeX entries here. Do not add placeholder citations to final drafts.
        """,
    )

    write(
        root / "notes" / "claim_evidence_matrix.md",
        """
        # Claim-Evidence Matrix

        | Claim | Evidence location | Boundary | Citation role | Action |
        | --- | --- | --- | --- | --- |
        |  |  |  |  |  |
        """,
    )
    write(
        root / "notes" / "literature_matrix.md",
        """
        # Literature Matrix

        | Paper | Venue/year | Setting | Assumptions | Method | Evidence | Baselines | Limitation | Replication target |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  |  |  |  |  |  |  |  |  |
        """,
    )
    write(
        root / "notes" / "experiment_plan.md",
        f"""
        # Experiment Plan

        Target venue: {args.venue}
        Primary area: {args.area}

        | Claim | Figure/table | Baselines | Metrics | Channel/data setting | Missing evidence |
        | --- | --- | --- | --- | --- | --- |
        |  |  |  |  |  |  |
        """,
    )
    write(
        root / "notes" / "terminology_ledger.md",
        """
        # Terminology Ledger

        | Term/symbol | Definition | First-use location | Notes |
        | --- | --- | --- | --- |
        | CSI | channel state information | abstract/body | Define in both if needed |
        """,
    )
    write(
        root / "notes" / "reviewer_response_tracker.md",
        """
        # Reviewer Response Tracker

        | ID | Comment summary | Action | Manuscript location | Status |
        | --- | --- | --- | --- | --- |
        |  |  |  |  |  |
        """,
    )

    if args.sim_lang == "python":
        write(
            root / "experiments" / "main_experiment.py",
            """
            \"\"\"Starter experiment file. Replace with reproducible wireless simulations.\"\"\"

            def main():
                print("TODO: implement baselines, metrics, and channel settings")


            if __name__ == "__main__":
                main()
            """,
        )
    elif args.sim_lang == "matlab":
        write(
            root / "experiments" / "main_simulation.m",
            """
            % Starter simulation file. Replace with reproducible wireless simulations.
            disp('TODO: implement baselines, metrics, and channel settings');
            """,
        )

    print(f"Created IEEE wireless workspace: {root}")
    print(f"Paper entry point: {paper / 'main.tex'}")


if __name__ == "__main__":
    main()
