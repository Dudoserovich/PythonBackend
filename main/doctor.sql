create table doctor
(
    id              SERIAL
        primary key,
    spec_id         INTEGER  not null
        references specialization
            on update cascade on delete cascade,
    full_name       CHAR(50) not null,
    sex             BOOL     not null,
    address         CHAR(40) not null,
    phone           CHAR(15) not null,
    work_experience INTEGER  not null,
    check (id <= 9999),
    check (spec_id between 1 and 9999),
    check (work_experience between 1 and 99)
);

