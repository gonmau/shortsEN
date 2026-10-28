"""영어 채널 소재 분류 (Food / Etiquette / Language / Traditions / Tech / School & Work / Daily Life / Travel).
- 새 소재는 generate_topics 가 theme 을 직접 받고, 없거나 목록 밖이면 여기 키워드로 보정합니다.
- yt_report 는 theme 이 비어 있는 예전 소재를 이 함수로 즉석 분류합니다(DB는 건드리지 않음)."""
import re

THEMES = ["Food & Dining", "Etiquette & Manners", "Language & Names", "Holidays & Traditions",
          "Tech & Innovation", "School & Work", "Daily Life", "Travel & Places"]

_RULES = [
    ("Language & Names", r"\b(honorific|slang|greeting|word|phrase|hangul|dialect|nickname|saying|expression|ssi|name|language|texting|emoji)\b|뭐해|‑ssi"),
    ("Etiquette & Manners", r"\b(etiquette|manners?|respect\w*|elders?|bow\w*|both hands|pour\w*|polite|tipping|shoes|gift|quiet|silent|noise)\b"),
    ("Holidays & Traditions", r"\b(holiday|festival|tradition\w*|dol|baek.?il|birthday|wedding|chuseok|seollal|lunar|pepero|celebrat\w*|ritual|ceremony|hanbok|snow)\b|1000.day|pepero|black day"),
    ("Food & Dining", r"\b(food|eat\w*|meal\w*|lunch|dinner|restaurant|cafe|café|coffee|tea|chicken|kimchi|banchan|rice|soju|bingsu|dessert|snack|grill|bbq|noodle|ramen|street food|menu)\b"),
    ("Tech & Innovation", r"\b(app|qr|kiosk|robot|ai|smart|digital|vending|machine|fingerprint|locker|solar|livestream|online|mobile|wifi|5g|high.tech|tech\w*|sensor|streetlights?|apps?)\b"),
    ("School & Work", r"\b(school|student\w*|exam\w*|hagwon|university|office|company|work\w*|boss|colleague|commut\w*|uniform|library|career|job)\b"),
    ("Travel & Places", r"\b(subway|train|ktx|bus|airport|han river|seoul|jeju|busan|tourist\w*|travel\w*|station|bike|park|mall|underground|tour\w*)\b"),
]


def _hit(t):
    for name, pat in _RULES:
        if re.search(pat, t, re.I):
            return name
    return None


def classify(label, topic="", *rest):
    """제목(label)을 먼저 보고, 안 걸리면 한 줄 요약(topic)까지 봄"""
    return _hit(str(label or "").lower()) or _hit(" ".join(str(x or "") for x in (label, topic) + rest).lower()) or "Daily Life"


def normalize(theme, *texts):
    """모델이 준 theme 이 목록에 있으면 그대로, 아니면 키워드로 분류"""
    t = str(theme or "").strip()
    for x in THEMES:
        if t.lower() == x.lower():
            return x
    return classify(*texts)
