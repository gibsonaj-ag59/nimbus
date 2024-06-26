CREATE DATABASE nimbus;
\c nimbus;
CREATE USER nimbus WITH PASSWORD '$(VTRVS_PASSWORD)';
GRANT ALL PRIVILEGES ON DATABASE nimbus TO nimbus;
CREATE SCHEMA lookup;
GRANT USAGE, CREATE ON SCHEMA lookup TO nimbus;
ALTER DEFAULT PRIVILEGES IN SCHEMA lookup GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLES TO nimbus;
ALTER DEFAULT PRIVILEGES IN SCHEMA lookup GRANT USAGE, SELECT ON SEQUENCES TO nimbus;
ALTER SCHEMA lookup OWNER TO nimbus;
GRANT CREATE ON DATABASE nimbus TO nimbus;

