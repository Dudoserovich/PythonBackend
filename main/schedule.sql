create table schedule
(
    id       SERIAL
        primary key,
    day_week CHAR(2) not null,
    start    time    not null,
    ending   time    not null,
    check (id <= 9999)
);

