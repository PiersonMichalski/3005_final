create table Members
	(member_id		serial,
    height          int,
    gender          varchar(255),
    first_name      varchar(255),
    last_name       varchar(255),
    email           varchar(255) unique not null,
    member_password        varchar(255) not null,
	primary key (member_id)
	);

create table Bills
    (bill_id        serial,
    amount         int,
    date_issued     date DEFAULT current_timestamp,
    member_id       int not null,
    paid            boolean DEFAULT FALSE,
    primary key (bill_id),
    foreign key (member_id) references Members
        on delete cascade
    );

create table Heart_rates
    (heart_rate     int,
    date_recorded   date DEFAULT current_timestamp,
    member_id       int not null,
    foreign key (member_id) references Members
        on delete cascade
    );

create table Weights
    (weight         int,
    date_recorded   date DEFAULT current_timestamp,
    member_id       int not null,
    foreign key (member_id) references Members
        on delete cascade
    );

create table Goals
    (goal_id        serial,
    goal            varchar(255),
    member_id       int not null,
    completed       boolean DEFAULT FALSE,
    primary key (goal_id),
    foreign key (member_id) references Members
        on delete cascade
    );

create table Routines
    (routine_id     serial,
    routine_description         varchar(255),
    member_id       int not null,
    primary key (routine_id),
    foreign key (member_id) references Members
        on delete cascade
    );

create table Machines
    (machine_id     serial,
    machine_name    varchar(255),
    machine_status  varchar(255),
    primary key (machine_id)
    );

create table Admins
    (admin_id       serial,
    email           varchar(255) not null,
    admin_password  varchar(255) not null,
    first_name      varchar(255),
    last_name       varchar(255),
    primary key (admin_id)
    );

create table Trainers
    (trainer_id     serial,
    email           varchar(255) not null,
    trainer_password   varchar(255) not null,
    first_name      varchar(255),
    last_name       varchar(255),
    primary key (trainer_id)
    );

create table Rooms
    (room_id        serial,
    room_name       varchar(255),
    primary key (room_id)
    );

create table Classes
    (class_id       serial,
    class_name     varchar(255),
    class_date      date,
    class_time      time,
    trainer_id      int,
    room_id         int,
    primary key (class_id),
    foreign key (room_id) references Rooms
        on delete set null,
    foreign key (trainer_id) references Trainers
        on delete set null
    );

create table Events
    (event_name     varchar(255),
    event_date      date,
    event_time      time,
    room_id         int,
    foreign key (room_id) references Rooms
        on delete set null
    );

create table Trainer_work_schedule
    (block_date      date,
    block_time      time,
    free            boolean DEFAULT TRUE,
    trainer_id      int not null,
    foreign key (trainer_id) references Trainers
        on delete cascade
    );

create table regestered
    (class_id   int,
    member_id   int,
    foreign key (class_id) references Classes
        on delete cascade,
    foreign key (member_id) references Members
        on delete cascade
    );
