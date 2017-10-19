

For Query 2 add following view - 
create view q2 as select articles.author, count(path) as view from log,articles where articles.slug=substring(path,10) group by   	                    articles.author


For Query 3 add following view -

CREATE VIEW error_rate AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;

CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);

CREATE VIEW total_view AS
SELECT date(time), COUNT(*) AS views
FROM log 
GROUP BY date(time)
ORDER BY date(time);




