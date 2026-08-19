from bs4 import BeautifulSoup
import re
import logging

logger = logging.getLogger(__name__)

def clean_html(html_text: str) -> str:
    if not html_text:
        return ""
    try:
        soup = BeautifulSoup(html_text, "lxml")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text(separator=" ", strip=True)
        text = re.sub(r"\s+", " ", text)
        return text
    except Exception as e:
        logger.debug("clean_html error: %s", e)
        return html_text.strip()
