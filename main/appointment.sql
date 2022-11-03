create table appointment
(
    visit_id    INTEGER
        references visit
            on update cascade on delete cascade,
    medicine_id INTEGER
        references medicine
            on update cascade on delete cascade,
    amount      INTEGER not null,
    primary key (visit_id, medicine_id),
    check (amount between 1 and 99),
    check (visit_id between 1 and 99999),
    check (visit_id between 1 and 99999)
);

