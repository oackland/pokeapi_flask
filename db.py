from sqlalchemy import create_engine

# Create an engine to connect to the database
engine = create_engine('postgres://xdlygoah:Jzo4soGLFMBtJNSHGp6OpGaXareKF5LR@bubble.db.elephantsql.com/xdlygoah')

# Open a connection to the database
with engine.connect() as connection:
	# Execute a SQL query
	result = connection.execute('SELECT * FROM User')

	# Process the query result
	for row in result:
		print(row)
