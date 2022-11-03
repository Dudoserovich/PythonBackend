create table visit
(
    id              SERIAL
        primary key,
    registration_id INTEGER   not null
        references doctor_schedule
            on update cascade on delete cascade,
    visit_date      DATE      not null,
    place           char(30)  not null,
    symptoms        char(100) not null,
    diagnosis       char(100) not null,
    check (id <= 99999),
    check (registration_id between 1 and 9999),
    check (visit_date between 1980 - 01 - 01 and 2023 - 01 - 01)
);

