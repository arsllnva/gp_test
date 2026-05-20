create table dds.link_user_post (
    link_hk bigserial primary key,
	user_hk bigint references dds.hub_user(user_hk),
    post_hk bigint references dds.hub_post(post_hk),
    load_dt timestamp default current_timestamp,
    record_source text
)