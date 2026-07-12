class SocialContentBuzzOutlineClient:
    def get_outline(self, keyword: str) -> dict:
        return {"outline": [f"Hook: {keyword}", "Context: trend change"]}