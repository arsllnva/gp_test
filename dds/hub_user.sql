create table dds.hub_user (
    user_hk bigserial primary key,
    user_id integer unique not null,
    load_dt timestamp default current_timestamp,
    record_source text
)