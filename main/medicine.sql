create table medicine
(
    id      SERIAL
        primary key,
    name    char(30)  not null,
    usage   char(100) not null,
    actions char(80)  not null,
    effects char(80),
    check (id <= 99999)
);

