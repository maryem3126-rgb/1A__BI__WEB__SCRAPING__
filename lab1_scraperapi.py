import json
from datetime import datetime
from google_play_scraper import search, app, reviews, Sort
def search_apps(query, n_apps=15, lang="en", country="us"):
    """Recherche des apps sur le Play Store et renvoie la liste des résultats."""
    print(f"Recherche d'applications pour : '{query}'...")
    results = search(query, lang=lang, country=country, n_hits=n_apps)
    print(f"  -> {len(results)} applications trouvees.")
    return results

def get_app_details(app_id, lang="en", country="us"):
    """Recupere les details complets d'une application via son ID."""
    details = app(app_id, lang=lang, country=country)
    return {
        "appId": details.get("appId"),
        "title": details.get("title"),
        "developer": details.get("developer"),
        "genre": details.get("genre"),
        "score": details.get("score"),
        "ratings": details.get("ratings"),
        "reviews_count": details.get("reviews"),
        "installs": details.get("installs"),
        "realInstalls": details.get("realInstalls"),
        "free": details.get("free"),
        "price": details.get("price"),
        "containsAds": details.get("containsAds"),
        "description": details.get("description"),
        "released": details.get("released"),
    }


def get_app_reviews(app_id, count=50, lang="en", country="us"):
    """Recupere jusqu'a `count` avis pour une application donnee."""
    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=count,
        filter_score_with=None,
    )
    cleaned = []
    for r in result:
        cleaned.append({
            "userName": r.get("userName"),
            "score": r.get("score"),
            "content": r.get("content"),
            "thumbsUp": r.get("thumbsUpCount"),
            "date": str(r.get("at")),
        })
    return cleaned


def json_serializer(obj):
    """Convertit les objets non serialisables (dates) en chaine de caracteres."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)


def main():
    SEARCH_TERM = "mental health wellness ai"
    N_APPS = 15
    REVIEWS_PER_APP = 50

    found = search_apps(SEARCH_TERM, n_apps=N_APPS)

    dataset = []
    for i, item in enumerate(found, start=1):
        app_id = item["appId"]
        print(f"[{i}/{len(found)}] Traitement de {app_id}...")
        try:
            details = get_app_details(app_id)
            details["user_reviews"] = get_app_reviews(app_id, count=REVIEWS_PER_APP)
            dataset.append(details)
        except Exception as e:
            print(f"  /!\\ Echec pour {app_id} : {e}")

    output_file = "wellness_apps_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            dataset,
            f,
            ensure_ascii=False,
            indent=2,
            default=json_serializer,
        )

    print(f"\nTermine ! {len(dataset)} applications enregistrees dans '{output_file}'.")
    total_reviews = sum(len(a["user_reviews"]) for a in dataset)
    print(f"Total d'avis collectes : {total_reviews}")


if __name__ == "__main__":
    main()