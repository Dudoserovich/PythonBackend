create table specialization
(
    id   SERIAL
        primary key,
    name CHAR(50) not null,
    check (id <= 9999)
);

