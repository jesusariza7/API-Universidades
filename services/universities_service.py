from clients.universities_client import fetch_universities


def get_universities_by_country(country: str):
    data = fetch_universities(country)

    if not data:
        return {
            "country": country,
            "total": 0,
            "universities": []
        }

    universities = []
    for u in data:
        universities.append({
            "name": u.get("name"),
            "website": u.get("web_pages", [None])[0],
            "domains": u.get("domains")
        })

    return {
        "country": country,
        "total": len(universities),
        "universities": universities
    }
