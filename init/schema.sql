CREATE TABLE IF NOT EXISTS request_logs (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    http_method VARCHAR(10) NOT NULL,
    request_method VARCHAR(10) NOT NULL,
    headers JSONB NOT NULL,
    service VARCHAR(100) NOT NULL,
    endpoint VARCHAR(100) NOT NULL,
    request_body JSONB NULL,
    response_body JSONB NULL,
    response_time_ms INT NOT NULL,
    status_code INT NOT NULL,
    user_id UUID NULL,
    request_id UUID NOT NULL,
    client_ip VARCHAR(45) NULL,
    error_message JSONB NULL
);
