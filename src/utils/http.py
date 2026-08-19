import requests
import logging
from urllib.parse import urlparse, urlunparse

logger = logging.getLogger(__name__)

def fetch_json(url, headers=None, params=None, timeout=15):
    try:
        r = requests.get(url, headers=headers, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logger.debug("fetch_json failed for %s: %s", url, e)
        return None

def normalize_url(url: str) -> str:
    if not url:
        return url
    try:
        parsed = urlparse(url.strip())
        scheme = parsed.scheme or "https"
        netloc = parsed.netloc.lower()
        path = parsed.path or "/"
        query = parsed.query
        normalized = urlunparse((scheme, netloc, path.rstrip("/"), "", query, ""))
        return normalized
    except Exception as e:
        logger.debug("normalize_url error for %s: %s", url, e)
        return url
