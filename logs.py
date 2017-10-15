import psycopg2

DBNAME = "news"

def query1():
	db = psycopg2.connect(database="news")
	c = db.cursor()
	c.execute("select title,count(*) as views from articles, log where log.path ~  articles.slug group by title order by views desc limit 3")
	rows = c.fetchall()
	print("\nTop 3")
	for row in rows[:3]:
 	     print("\nArticle: {:} \nViews: {:}" .format(row[0], row[1]))
	db.commit()
	db.close()
	query1()

def query2():
	db = psycopg2.connect(database="news")
	c = db.cursor()
	c.execute("create view q2 as select articles.author, count(path) as view from log, 		articles where articles.slug=substring(path,10) group by articles.author")
	c.execute("select name,view from authors,q2 where authors.id=q2.author")
	rows = c.fetchall()
	print("\nTop authors")
	for row in rows[:4]:
 	     print("\nAuthors: {:} \nViews: {:}" .format(row[0], row[1]))
	db.commit()
	db.close()

if __name__ == '__main__':
 	query1()
	query2()
	

