from sqlalchemy import create_engine, text

def get_engine():
    user = "postgres"
    password = "postgres123"
    host = "localhost"
    port = "5432"
    database = "sports_betting_analytics"

    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url)
    return engine

if __name__ == "__main__":
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Connection successful!'"))
        print(result.fetchone())
