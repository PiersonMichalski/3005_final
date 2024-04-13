INSERT INTO Members (first_name, last_name, email, member_password)
VALUES 
('Hunter', 'Read', 'hr@gmail.com', '1234'),
('emily', 'ketcheson', 'ek@gmail.com', 'password'),
('julianna', 'hawekens', 'jh@gmail.com', '1234');

INSERT INTO Admins (first_name, last_name, email, admin_password)
VALUES
('pierson', 'michlaski', 'pm@gmail.com', '1234');

INSERT INTO Trainers (first_name, last_name, email, trainer_password)
VALUES
('zach', 'thomas', 'zt@gmail.com', '1234');

INSERT INTO Bills (amount, date_issued, member_id)
VALUES
(50, '2024-03-20', 3);

INSERT INTO Heart_rates (heart_rate, date_recorded, member_id)
VALUES
(72, '2024-03-20', 1);

INSERT INTO Weights (weight, date_recorded, member_id)
VALUES
(180, '2024-03-20', 1);

INSERT INTO Goals (goal, member_id)
VALUES
('bench 2 plates', 1);

INSERT INTO Routines (routine_description, member_id)
VALUES
('10 sets of 8 reps of 135 on bench', 1);

INSERT INTO Machines (machine_name, machine_status)
VALUES
('rowing machine', 'broken'),
('tredmill', 'perfect');

INSERT INTO Rooms (room_name)
VALUES
('general room 1'),
('general room 2'),
('general room 3');

INSERT INTO Classes (class_name, class_date, class_time, trainer_id, room_id)
VALUES
('pilates', '2024-03-22', '10:30:00', 1, 1);

INSERT INTO Events (event_name, event_date, event_time, room_id)
VALUES
('birthday', '2024-03-22', '10:30:00', 2);

INSERT INTO Trainer_work_schedule (block_date, block_time, trainer_id)
VALUES
('2024-03-22', '10:00:00', 1);
