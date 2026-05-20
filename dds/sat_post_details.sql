create table dds.sat_post_details (
    sat_hk bigserial primary key,
    post_hk bigint references dds.hub_post(post_hk),
	title text,
	body text,
    load_dt timestamp default current_timestamp,
    record_source text
)