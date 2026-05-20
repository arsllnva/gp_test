create table stg.posts (
	user_id integer not null,
	id integer not null,
	title text,
	body text, 
	load_dt timestamp default current_timestamp
)