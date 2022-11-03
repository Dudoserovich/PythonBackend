create table place
(
    id   SERIAL
        primary key,
    name CHAR(20) not null,
    check (id <= 9999)
);

