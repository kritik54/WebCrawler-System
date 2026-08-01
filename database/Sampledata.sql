INSERT INTO Users (username, password_hash, full_name, email, role)
VALUES
('admin', 'hashed_password', 'System Administrator', 'admin@example.com', 'Administrator');

INSERT INTO SeedURLs (user_id, url, priority, status)
VALUES
(1, 'https://example.com/jobs', 1, 'Active');