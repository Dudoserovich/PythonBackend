create table doctor_schedule
(
    id          SERIAL
        primary key,
    doctor_id   INTEGER
        references doctor
            on update cascade on delete cascade,
    schedule_id INTEGER
        references schedule
            on update cascade on delete cascade,
    patient_id  INTEGER
        references patient
            on update cascade on delete cascade,
    place_id    INTEGER
        references place
            on update cascade on delete cascade,
    check (doctor_id <= 9999),
    check (id <= 9999),
    check (patient_id <= 9999),
    check (place_id <= 9999),
    check (schedule_id <= 9999)
);

