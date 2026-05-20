create table dds.hub_post (
    post_hk bigserial primary key,
    id integer unique not null,
    load_dt timestamp default current_timestamp,
    record_source text
)