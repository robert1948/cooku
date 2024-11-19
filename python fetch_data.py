import psycopg2
from psycopg2.extras import RealDictCursor

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d69p3as4nk00l5",
        "USER": "u1ramlq01hqjf5",
        "PASSWORD": "pc09bb6b83a6714525921f9e59758d5e236c8a1134167134f964fdd23bbc1c2f5",
        "HOST": "c5p86clmevrg5s.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}

def get_data_from_db():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=DATABASES["default"]["NAME"],
            user=DATABASES["default"]["USER"],
            password=DATABASES["default"]["PASSWORD"],
            host=DATABASES["default"]["HOST"],
            port=DATABASES["default"]["PORT"],
        )

        # Create a cursor object
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            # Replace 'your_table_name' with your actual table name
            query = "SELECT * FROM events_venue;"
            cursor.execute(query)
            
            # Fetch all rows
            rows = cursor.fetchall()
            
            # Print the results
            for row in rows:
                print(row)
        
        # Close the connection
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_data_from_db()
