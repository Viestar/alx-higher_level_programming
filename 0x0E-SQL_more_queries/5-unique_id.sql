-- creates the table unique_id if not exists, set unique to default 1 and add attribute name.
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));