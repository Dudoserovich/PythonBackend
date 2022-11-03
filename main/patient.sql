create table patient
(
    id        SERIAL
        primary key,
    full_name CHAR(50) not null,
    address   CHAR(50) not null,
    sex       BOOL     not null,
    birthday  DATE     not null,
    check (birthday between 1980 - 01 - 01 and 2023 - 01 - 01),
    check (id <= 9999)
);

