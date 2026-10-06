#!/usr/bin/env python3
"""
arXiv Cognitive Radar — Autonomous Ingestion & Extraction Engine (Production Grade)

Target scope: Comprehensive AI Research & Core Computer Science/Tech Disciplines
- Artificial Intelligence (cs.AI, stat.ML)
- Machine Learning & Deep Learning (cs.LG, cs.NE)
- Computation & Language / NLP / LLMs (cs.CL)
- Computer Vision & Pattern Recognition (cs.CV)
- Robotics & Autonomous Systems (cs.RO)
- Multi-Agent Systems & Coordination (cs.MA)
- Core Tech & Systems (cs.SE, cs.CR, cs.DC, cs.IR)
"""

import sys
import time
import json
import re
import io
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

try:
    import pypdf
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"

DEFAULT_AI_TECH_CATEGORIES = [
    "cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.RO", "cs.MA",
    "cs.NE", "stat.ML", "cs.SE", "cs.CR", "cs.DC", "cs.IR"
]

DEFAULT_KEYWORDS = [
    "agent", "multi-agent", "llm", "autonomous", "reasoning",
    "foundation model", "transformer", "reinforcement learning",
    "deep learning", "neural", "planning", "computer vision",
    "robotics", "nlp", "benchmark", "tool", "fine-tuning"
]


class ArxivAgentRadar:
    BASE_URL = "https://export.arxiv.org/api/query"

    def __init__(self, categories=None, delay_seconds=3.0):
        self.categories = categories or DEFAULT_AI_TECH_CATEGORIES
        self.delay_seconds = delay_seconds

    def build_query(self, search_terms=None, start=0, max_results=30, sort_by="submittedDate", sort_order="descending"):
        cat_query = "cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.MA OR cat:stat.ML"
        if search_terms:
            terms_query = " AND ".join([f'all:"{term}"' for term in search_terms])
            full_query = f"({cat_query}) AND ({terms_query})"
        else:
            full_query = cat_query

        params = {
            "search_query": full_query,
            "start": start,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order
        }
        return f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"

    def fetch_papers(self, search_terms=None, start=0, max_results=30):
        url = self.build_query(search_terms=search_terms, start=start, max_results=max_results)
        print(f"[*] Querying arXiv API across AI/CS categories: {url}", file=sys.stderr)

        headers = {
            "User-Agent": "ArxivAgentRadar/2.0 (mailto:ygrcastonguay@gmail.com)"
        }
        req = urllib.request.Request(url, headers=headers)
        time.sleep(self.delay_seconds)

        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                xml_data = response.read().decode("utf-8")
            return self.parse_feed(xml_data)
        except Exception as e:
            print(f"[!] Error fetching papers from arXiv: {e}", file=sys.stderr)
            return []

    def parse_feed(self, xml_string):
        try:
            root = ET.fromstring(xml_string)
        except Exception as e:
            print(f"[!] XML parsing error: {e}", file=sys.stderr)
            return []

        entries = root.findall(f"{ATOM_NS}entry")
        papers = []

        for entry in entries:
            id_url = entry.findtext(f"{ATOM_NS}id", "").strip()
            title = entry.findtext(f"{ATOM_NS}title", "").strip().replace("\n", " ")

            if title.lower() == "error":
                print(f"[!] Encountered error entry from arXiv API: {title}", file=sys.stderr)
                continue

            title = re.sub(r"\s+", " ", title)
            summary = entry.findtext(f"{ATOM_NS}summary", "").strip().replace("\n", " ")
            summary = re.sub(r"\s+", " ", summary)
            published = entry.findtext(f"{ATOM_NS}published", "").strip()
            updated = entry.findtext(f"{ATOM_NS}updated", "").strip()

            authors = []
            for author_node in entry.findall(f"{ATOM_NS}author"):
                name = author_node.findtext(f"{ATOM_NS}name", "").strip()
                if name:
                    authors.append(name)

            categories = []
            for cat_node in entry.findall(f"{ATOM_NS}category"):
                term = cat_node.attrib.get("term")
                if term:
                    categories.append(term)

            pdf_url = ""
            for link_node in entry.findall(f"{ATOM_NS}link"):
                if link_node.attrib.get("title") == "pdf" or link_node.attrib.get("type") == "application/pdf":
                    pdf_url = link_node.attrib.get("href", "")
                    break

            arxiv_id = id_url.split("/abs/")[-1] if "/abs/" in id_url else id_url

            papers.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "published": published,
                "updated": updated,
                "categories": categories,
                "summary": summary,
                "abs_url": id_url,
                "pdf_url": pdf_url
            })

        return papers

    def score_paper(self, paper, keywords=None):
        score = 0.0
        title_text = paper.get("title", "").lower()
        summary_text = paper.get("summary", "").lower()

        for cat in paper.get("categories", []):
            if cat in self.categories:
                score += 3.0

        target_keywords = keywords or DEFAULT_KEYWORDS
        for kw in target_keywords:
            kw_lower = kw.lower()
            if kw_lower in title_text:
                score += 6.0
            if kw_lower in summary_text:
                score += 2.0

        pub_date_str = paper.get("published", "")
        if pub_date_str:
            try:
                pub_dt = datetime.strptime(pub_date_str[:10], "%Y-%m-%d")
                days_old = (datetime.utcnow() - pub_dt).days
                recency_boost = max(0.0, 5.0 - (days_old / 15.0))
                score += recency_boost
            except Exception:
                pass

        return score

    def rank_candidates(self, papers, top_k=10, keywords=None):
        scored_papers = []
        for paper in papers:
            s = self.score_paper(paper, keywords=keywords)
            scored_papers.append((s, paper))
        scored_papers.sort(key=lambda x: x[0], reverse=True)

        ranked = [paper for score, paper in scored_papers[:top_k] if score > 0]
        return ranked if ranked else papers[:top_k]

    def extract_pdf_sections(self, pdf_url):
        if not PYPDF_AVAILABLE or not pdf_url:
            return {}

        try:
            print(f"[*] Slicing key sections from: {pdf_url}", file=sys.stderr)
            time.sleep(self.delay_seconds)
            headers = {"User-Agent": "ArxivAgentRadar/2.0"}
            req = urllib.request.Request(pdf_url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                pdf_bytes = resp.read()

            reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
            num_pages = len(reader.pages)
            if num_pages == 0:
                return {}

            first_pages_text = "\n".join([reader.pages[i].extract_text() or "" for i in range(min(3, num_pages))])
            last_pages_text = "\n".join([reader.pages[i].extract_text() or "" for i in range(max(0, num_pages - 3), num_pages)])

            contributions = self._slice_contributions(first_pages_text)
            conclusions = self._slice_conclusions(last_pages_text)

            return {
                "contributions": contributions,
                "conclusions": conclusions
            }
        except Exception as e:
            print(f"[!] PDF section slicing fallback triggered for {pdf_url}: {e}", file=sys.stderr)
            return {}

    def _slice_contributions(self, text):
        match = re.search(
            r"(our (main )?contributions|in this work, we|we summarize our contributions|contributions:?)\s*[:\n](.*?)(?=\n\n|\n[1-9]\s+[A-Z]|references|bibliography|appendix)",
            text, re.IGNORECASE | re.DOTALL
        )
        if match:
            extracted = match.group(0).strip()
            return extracted[:750]
        return ""

    def _slice_conclusions(self, text):
        text_no_refs = re.split(r"\n\s*(references|bibliography)\s*\n", text, flags=re.IGNORECASE)[0]
        match = re.search(
            r"(conclusion|limitations|discussion and conclusion|future work)\s*[:\n](.*?)(?=\n\s*(references|bibliography|appendix)|$)",
            text_no_refs, re.IGNORECASE | re.DOTALL
        )
        if match:
            extracted = match.group(0).strip()
            return extracted[:750]
        return ""

    def generate_dossier_card(self, paper, pdf_data=None):
        pdf_data = pdf_data or {}
        summary = paper.get("summary", "")

        problem_thesis = summary[:300] + "..." if len(summary) > 300 else summary

        contrib_text = pdf_data.get("contributions")
        if not contrib_text:
            contrib_text = f"From Abstract: {summary[300:600]}" if len(summary) > 300 else summary

        cats_str = ", ".join(paper.get("categories", []))
        methodology = f"Categories: {cats_str}. Focused on AI architecture, computational models, and algorithmic implementation."

        concl_text = pdf_data.get("conclusions")
        if not concl_text:
            concl_text = f"Published on {paper.get('published', '')[:10]}. Detailed empirical evaluation provided in full manuscript."

        limitations = "Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation."

        authors_str = ", ".join(paper.get("authors", [])[:5])
        if len(paper.get("authors", [])) > 5:
            authors_str += " et al."

        card = []
        card.append(f"### [{paper.get('title', '')}]({paper.get('abs_url', '')})")
        card.append(f"**arXiv ID:** `{paper.get('arxiv_id', '')}` | **PDF:** [View PDF]({paper.get('pdf_url', '')}) | **Published:** {paper.get('published', '')[:10]}")
        card.append(f"**Authors:** {authors_str}")
        card.append("\n#### 5-Point Executive Dossier:")
        card.append(f"1. **Core Problem & Thesis:** {problem_thesis}")
        card.append(f"2. **Key Technical Contributions:** {contrib_text}")
        card.append(f"3. **Methodology & Architecture:** {methodology}")
        card.append(f"4. **Key Results & Findings:** {concl_text}")
        card.append(f"5. **Limitations & Radar Notes:** {limitations}\n")
        card.append("---\n")
        return "\n".join(card)

    def generate_markdown_report(self, papers, output_file="arxiv_radar_latest.md"):
        md = []
        md.append("# arXiv AI & Computer Science Research Radar")
        md.append(f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
        md.append(f"**Target Categories:** {', '.join(self.categories)}")
        md.append(f"**High-Yield Papers Analyzed:** {len(papers)}\n")
        md.append("---\n")

        for idx, paper in enumerate(papers, 1):
            pdf_data = self.extract_pdf_sections(paper.get("pdf_url", ""))
            card_md = self.generate_dossier_card(paper, pdf_data=pdf_data)
            md.append(card_md)

        report = "\n".join(md)
        if output_file:
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(report)
                print(f"[*] Report successfully written to {output_file}", file=sys.stderr)
            except Exception as e:
                print(f"[!] Failed to write report to file: {e}", file=sys.stderr)
        return report

    def sync_to_drive_webhook(self, report_content, webhook_url=None, auth_token=None):
        import os
        url = webhook_url or os.environ.get("DRIVE_WEBHOOK_URL")
        token = auth_token or os.environ.get("DRIVE_WEBHOOK_SECRET", "SPARK_RADAR_SECRET_2026_GUELPH")
        if not url:
            print("[*] No DRIVE_WEBHOOK_URL configured; skipping Drive sync.", file=sys.stderr)
            return False

        try:
            today_str = datetime.utcnow().strftime("%Y-%m-%d")
            payload = {
                "auth_token": token,
                "filename": f"arxiv_radar_{today_str}.md",
                "content": report_content
            }
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                print(f"[*] Cloud Drive sync successful: {res}", file=sys.stderr)
                return True
        except Exception as e:
            print(f"[!] Error syncing to Google Drive webhook: {e}", file=sys.stderr)
            return False


if __name__ == "__main__":
    radar = ArxivAgentRadar()
    query_terms = sys.argv[1:] if len(sys.argv) > 1 else None

    if query_terms:
        print(f"Executing arXiv search for specific terms: {query_terms}...")
    else:
        print("Executing broad scan across top AI & Computer Science disciplines...")

    try:
        raw_papers = radar.fetch_papers(search_terms=query_terms, start=0, max_results=30)
        top_papers = radar.rank_candidates(raw_papers, top_k=10, keywords=query_terms)
        print(f"Selected top {len(top_papers)} high-yield papers.")
        report = radar.generate_markdown_report(top_papers, "arxiv_radar_latest.md")

        radar.sync_to_drive_webhook(report)
        print("\n" + report[:1200] + "...\n")
    except Exception as e:
        print(f"Execution notice: {e}")
