#!/usr/bin/env python3

import psycopg2


def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")

    # Open a cursor to perform database operations
    cur = conn.cursor()

def connect(news):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(news))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        # THEN perhaps exit the program
        sys.exit(1) # The easier method
        # OR perhaps throw an error
        raise e
        # If you choose to raise an exception,
        # It will need to be caught by the whoever called this function

    # Question 1
    sql_popular_articles = """
      select title,count(*) as views from articles, log where log.path ~  articles.slug group by title order by views desc limit 3;
    """
    cur.execute(sql_popular_articles)
    print("Most popular articles:")
    for (title, view) in cur.fetchall():
        print("    {} - {} views".format(title, view))
    print("-" * 70)

    # Question 2
    sql_popular_authors = """
    select name,view from authors,q2 where authors.id=q2.author
    """
    cur.execute(sql_popular_authors)
    print("Most popular authors:")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 70)

    # Question 3
    sql_more_than_one_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    cur.execute(sql_more_than_one_percent_errors)
    print("Days with more than 1% errors:")
    for (date, percentage) in cur.fetchall():
        print("    {} - {}% errors".format(date, percentage))
    print("-" * 70)

    # Close communication with the database
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()

